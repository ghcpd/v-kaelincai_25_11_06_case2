import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from app import generate_bar_chart, load_test_data
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def bbox_overlap(bbox1, bbox2, tol=1e-6):
    # bbox = (x0, y0, x1, y1)
    return not (bbox1[2] <= bbox2[0] or bbox1[0] >= bbox2[2] or bbox1[3] <= bbox2[1] or bbox1[1] >= bbox2[3])


def get_text_bboxes(fig):
    fig.canvas.draw()
    bboxes = []
    for text in fig.texts:
        bbox = text.get_window_extent(renderer=fig.canvas.get_renderer()).extents
        bboxes.append(tuple(bbox))
    return bboxes


def run_test_case(case, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    if case.get('id') == 'TC04_malformed':
        try:
            generate_bar_chart(case['data'], case['categories'], os.path.join(out_dir, case['id'] + '.png'))
        except Exception:
            return {'id': case['id'], 'error': True}
        return {'id': case['id'], 'error': False}

    path = generate_bar_chart(case['data'], case['categories'], os.path.join(out_dir, case['id'] + '.png'))

    # load figure for reading positions - recreate chart in memory
    fig, ax = plt.subplots(figsize=(8,4))
    x = range(len(case['data']))
    bars = ax.bar(x, case['data'])
    for bar, val in zip(bars, case['data']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(case['data'])*0.02,
                f"{val}", ha='center', va='bottom', fontsize=9)

    bboxes = get_text_bboxes(fig)

    overlaps = 0
    for i in range(len(bboxes)):
        for j in range(i+1, len(bboxes)):
            if bbox_overlap(bboxes[i], bboxes[j]):
                overlaps += 1

    total_pairs = max(1, len(bboxes)*(len(bboxes)-1)//2)
    readability = 1.0 - overlaps/total_pairs

    plt.close(fig)
    return {'id': case['id'], 'overlaps': overlaps, 'readability': readability}


def test_pre_feature_all_cases(tmp_path, capsys):
    data = load_test_data(os.path.join(os.path.dirname(__file__), '..', '..', 'test_data.json'))
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    results = []
    for case in data:
        res = run_test_case(case, out_dir)
        results.append(res)

    # Save results
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'results'), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), '..', 'results', 'results_pre.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # Assert at least one test shows overlaps
    assert any(r.get('overlaps', 0) > 0 for r in results if r.get('id') != 'TC04_malformed')
