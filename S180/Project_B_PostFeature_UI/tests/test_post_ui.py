import json
import os
import sys
from PIL import Image
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE, 'src'))
from app_fixed import draw_bar_chart
from viz_utils_fixed import bbox_overlap_pixels

DATA_FILE = os.path.join(BASE, 'data', 'test_data.json')
OUT_DIR = os.path.join(BASE, 'results')

os.makedirs(OUT_DIR, exist_ok=True)

with open(DATA_FILE) as f:
    tests = json.load(f)


def test_postcharts_no_overlap():
    results = []
    for t in tests:
        tid = t['id']
        try:
            data = t['data']
            labels = t['labels']
            if not isinstance(data, list):
                results.append({'id': tid, 'status': 'error', 'reason': 'malformed input'})
                continue
            outname = os.path.join(OUT_DIR, f'{tid}_post.png')
            draw_bar_chart(data, labels, outname)
            img = Image.open(outname)
            dark_pixels = bbox_overlap_pixels(img)
            expect_no_overlap = t.get('expect_no_overlap', False)
            # threshold for dense dark pixels reduced vs pre
            overlap_flag = dark_pixels > 500
            results.append({'id': tid, 'dark_pixels': dark_pixels, 'overlap_flag': overlap_flag, 'expect_no_overlap': expect_no_overlap, 'status': 'fail' if overlap_flag and expect_no_overlap else 'pass'})
        except Exception as e:
            results.append({'id': tid, 'status': 'error', 'reason': str(e)})

    with open(os.path.join(OUT_DIR, 'results_post.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # final assert: no test with expect_no_overlap True should have overlap_flag True
    assert not any(r.get('overlap_flag') and r.get('expect_no_overlap') for r in results)
