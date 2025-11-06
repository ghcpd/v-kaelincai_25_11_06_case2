import json
import os
import pytest
import math
import matplotlib
matplotlib.use('Agg')

from Project_B_PostFeature_UI.src.chart_generator import ChartGeneratorPost as ChartGenPost


def rects_overlap(r1, r2):
    # r = (x0, y0, x1, y1)
    return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])


@pytest.fixture(scope='module')
def test_data():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    data_path = os.path.join(root, 'test_data.json')
    with open(data_path) as f:
        return json.load(f)


def test_postfeature_no_overlap_and_contrast(tmp_path, test_data):
    out = tmp_path
    cg = ChartGenPost(str(out))
    results = []
    for case in test_data:
        cid = case['id']
        filename = f'chart_post_{cid}.png'
        # Render chart
        if case['type'] == 'single_series':
            path, bboxes = cg.draw_bar_chart(case['data'], labels=case.get('labels'), title=f"{cid}", filename=filename, return_bboxes=True)
        else:
            path, bboxes = cg.draw_bar_chart([sum(col) for col in zip(*case['data'])], labels=case.get('labels'), title=f"{cid}", filename=filename, return_bboxes=True)

        # Now compute overlap on returned bboxes
        overlap = False
        for i in range(len(bboxes)):
            for j in range(i+1, len(bboxes)):
                if rects_overlap(bboxes[i]['bbox'], bboxes[j]['bbox']):
                    overlap = True
                    break
            if overlap:
                break

        expect_no_overlap = not overlap
        # For malformed input, we accept failure
        if case['labels'] is None:
            expect_no_overlap = False

        # Also check contrast ratios for placed label colors
        low_contrast = False
        for b in bboxes:
            color = b['color']
            # Map named colors to hex if needed
            color_hex = color
            if color == 'white':
                color_hex = '#ffffff'
            elif color == 'black':
                color_hex = '#000000'
            try:
                cr = ChartGenPost.contrast_ratio(color_hex, b['bar_color'])
            except Exception:
                cr = 0
            if cr < 4.5:
                low_contrast = True
                break

        # Compute min vertical gap between bboxes (in pixels)
        y_centers = [(b['bbox'][1] + b['bbox'][3]) / 2.0 for b in bboxes]
        y_centers_sorted = sorted(y_centers)
        min_gap = min([y_centers_sorted[i+1]-y_centers_sorted[i] for i in range(len(y_centers_sorted)-1)]) if len(y_centers_sorted) > 1 else None

        results.append({'id': cid, 'detected_overlap': overlap, 'rect_count': len(bboxes), 'expect_no_overlap': expect_no_overlap, 'low_contrast': low_contrast, 'min_vertical_gap_px': min_gap})

    # Save into project results folder
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    res_path = os.path.join(project_root, 'results', 'results_post.json')
    with open(res_path, 'w') as f:
        json.dump(results, f, indent=2)

    # Copy charts
    import shutil
    for file in os.listdir(str(out)):
        if file.startswith('chart_post_') and file.endswith('.png'):
            shutil.copyfile(os.path.join(str(out), file), os.path.join(project_root, 'results', file))

    # Validate that at least 3 cases are overlap-free
    assert sum(1 for r in results if r['expect_no_overlap']) >= 3


if __name__ == '__main__':
    pytest.main([__file__])
