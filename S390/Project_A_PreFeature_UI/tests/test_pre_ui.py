import json
import os
import pytest
from PIL import Image
import matplotlib
matplotlib.use('Agg')

from Project_A_PreFeature_UI.src.chart_generator import ChartGeneratorPre as ChartGenPre

# Helper functions to compute rectangle overlaps based on saved figure

def rects_overlap(r1, r2):
    # r = (x0, y0, x1, y1)
    return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])


def compute_text_bboxes_from_figure(fig):
    fig.canvas.draw()  # need to draw to compute renderer
    renderer = fig.canvas.get_renderer()
    rects = []
    for ax in fig.axes:
        for text in ax.texts:
            bbox = text.get_window_extent(renderer=renderer)
            rects.append((bbox.x0, bbox.y0, bbox.x1, bbox.y1))
    return rects


@pytest.fixture(scope='module')
def test_data():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    data_path = os.path.join(root, 'test_data.json')
    with open(data_path) as f:
        return json.load(f)


def test_prefeature_charts_write_and_overlap(tmp_path, test_data):
    out = tmp_path
    cg = ChartGenPre(str(out))
    results = []
    for case in test_data:
        cid = case['id']
        filename = f'chart_pre_{cid}.png'
        # Render chart and return fig to compute text bboxes
        if case['type'] == 'single_series':
            fig, path = cg.draw_bar_chart(case['data'], labels=case.get('labels'), title=f"{cid}", filename=filename, return_fig=True)
        else:
            fig, path = cg.draw_bar_chart([sum(col) for col in zip(*case['data'])], labels=case.get('labels'), title=f"{cid}", filename=filename, return_fig=True)

        # Use the renderer to compute text bounding boxes
        rects = compute_text_bboxes_from_figure(fig)

        # Detect overlap between any pair
        overlap = False
        for i in range(len(rects)):
            for j in range(i+1, len(rects)):
                if rects_overlap(rects[i], rects[j]):
                    overlap = True
                    break
            if overlap:
                break
        # Compute min vertical gap between label centers
        if len(rects)>1:
            y_centers = [ (r[1]+r[3]) / 2.0 for r in rects]
            y_centers_sorted = sorted(y_centers)
            min_gap = min([y_centers_sorted[i+1]-y_centers_sorted[i] for i in range(len(y_centers_sorted)-1)])
        else:
            min_gap = None

        results.append({'id': cid, 'detected_overlap': overlap, 'rect_count': len(rects), 'min_vertical_gap_px': min_gap})
        try:
            import matplotlib.pyplot as plt
            plt.close(fig)
        except Exception:
            pass


    # Save results file
    # Save into project results folder
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    res_path = os.path.join(project_root, 'results', 'results_pre.json')

    with open(res_path, 'w') as f:
        json.dump(results, f, indent=2)

    # Also copy generated charts to results folder
    import shutil
    for file in os.listdir(str(out)):
        if file.startswith('chart_pre_') and file.endswith('.png'):
            shutil.copyfile(os.path.join(str(out), file), os.path.join(project_root, 'results', file))


    # Assertions: Project A is buggy and should show overlap for some cases
    assert any(r['detected_overlap'] for r in results)


if __name__ == '__main__':
    pytest.main([__file__])
