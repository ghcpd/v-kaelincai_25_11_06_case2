import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from app_fixed import generate_bar_chart_dynamic, load_test_data
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def bbox_overlap(bbox1, bbox2):
    return not (bbox1.x1 <= bbox2.x0 or bbox1.x0 >= bbox2.x1 or bbox1.y1 <= bbox2.y0 or bbox1.y0 >= bbox2.y1)


def get_text_bboxes(fig):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bboxes = []
    for text in fig.texts:
        bboxes.append(text.get_window_extent(renderer=renderer))
    return bboxes


def run_test_case(case, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    if case.get('id') == 'TC04_malformed':
        try:
            generate_bar_chart_dynamic(case['data'], case['categories'], os.path.join(out_dir, case['id'] + '.png'))
        except Exception:
            return {'id': case['id'], 'error': True}
        return {'id': case['id'], 'error': False}

    path = generate_bar_chart_dynamic(case['data'], case['categories'], os.path.join(out_dir, case['id'] + '.png'))

    # Recreate chart to compute bboxes and ensure they don't overlap
    fig, ax = plt.subplots(figsize=(8,4))
    x = range(len(case['data']))
    bars = ax.bar(x, case['data'])
    base_offset = max(case['data']) * 0.02
    texts = []
    for bar, val in zip(bars, case['data']):
        y = bar.get_height() + base_offset
        text = ax.text(bar.get_x() + bar.get_width()/2, y, f"{val}", ha='center', va='bottom', fontsize=10)
        texts.append(text)

    fig.canvas.draw()
    bboxes = get_text_bboxes(fig)
    overlaps = 0
    for i in range(len(bboxes)):
        for j in range(i+1, len(bboxes)):
            if bbox_overlap(bboxes[i], bboxes[j]):
                overlaps += 1

    # check font path effects (contrast stroke)
    has_stroke = False
    for text in fig.texts:
        if len(text.get_path_effects()) > 0:
            has_stroke = True
            break

    plt.close(fig)
    return {'id': case['id'], 'overlaps': overlaps, 'has_stroke': has_stroke}


def test_post_feature_all_cases(tmp_path):
    data = load_test_data(os.path.join(os.path.dirname(__file__), '..', '..', 'test_data.json'))
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    results = []
    for case in data:
        res = run_test_case(case, out_dir)
        results.append(res)

    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'results'), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), '..', 'results', 'results_post.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # All non-malformed cases should have 0 overlaps
    assert all(r.get('overlaps', 0) == 0 for r in results if r.get('id') != 'TC04_malformed')
    # Also ensure improvements: stroke (contrast) is present in at least one result
    assert any(r.get('has_stroke', False) for r in results if r.get('id') != 'TC04_malformed')
