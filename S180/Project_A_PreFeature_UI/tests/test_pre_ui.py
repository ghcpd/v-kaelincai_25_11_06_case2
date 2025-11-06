import json
import os
import sys
from PIL import Image
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE, 'src'))
from app import draw_bar_chart
from viz_utils import bbox_overlap

DATA_FILE = os.path.join(BASE, 'data', 'test_data.json')
OUT_DIR = os.path.join(BASE, 'results')

os.makedirs(OUT_DIR, exist_ok=True)

with open(DATA_FILE) as f:
    tests = json.load(f)


def test_precharts_overlap():
    results = []
    for t in tests:
        tid = t['id']
        try:
            data = t['data']
            labels = t['labels']
            if not isinstance(data, list):
                results.append({'id': tid, 'status': 'error', 'reason': 'malformed input'})
                continue
            outname = os.path.join(OUT_DIR, f'{tid}_pre.png')
            draw_bar_chart(data, labels, outname)
            img = Image.open(outname)
            # naive check: scan for many dense black pixels near top (indicative of overlapping labels)
            w,h = img.size
            top_region = img.crop((0,0,w,int(h*0.4))).convert('L')
            arr = top_region.load()
            # count dark pixels
            dark = 0
            for x in range(top_region.size[0]):
                for y in range(top_region.size[1]):
                    if top_region.getpixel((x,y))<50:
                        dark += 1
            overlap_flag = dark > 500
            expect_no_overlap = t.get('expect_no_overlap', False)
            results.append({'id': tid, 'overlap_flag': overlap_flag, 'expect_no_overlap': expect_no_overlap, 'status': 'fail' if overlap_flag and expect_no_overlap else 'pass'})
        except Exception as e:
            results.append({'id': tid, 'status': 'error', 'reason': str(e)})

    with open(os.path.join(OUT_DIR, 'results_pre.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # final assert: at least one case has overlap detection (replicates bug)
    assert any(r.get('overlap_flag') for r in results if r.get('status')=='pass' or r.get('status')=='fail')
