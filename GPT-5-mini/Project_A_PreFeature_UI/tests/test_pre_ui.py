import json
from pathlib import Path
import importlib.util

def load_app_module():
    path = Path(__file__).resolve().parents[2] / 'Project_A_PreFeature_UI' / 'src' / 'app.py'
    spec = importlib.util.spec_from_file_location('app_pre', str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

app = load_app_module()

def load_case(case):
    return case['data']

def boxes_overlap(a, b):
    # a and b are [x0,y0,x1,y1]
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])

def test_cases():
    root = Path(__file__).resolve().parents[2]
    cases = json.loads(root.joinpath('test_data.json').read_text())
    results = []
    out_dir = root.joinpath('Project_A_PreFeature_UI','results')
    out_dir.mkdir(parents=True, exist_ok=True)
    for c in cases:
        cid = c['id']
        in_file = root.joinpath('Project_A_PreFeature_UI','data', f'{cid}.json')
        in_file.parent.mkdir(parents=True, exist_ok=True)
        in_file.write_text(json.dumps(c['data']))
        try:
            bboxes = app.render(c['data'], out_dir.joinpath(f'{cid}.png'))
            # check overlaps
            overlap_found = False
            for i in range(len(bboxes)):
                for j in range(i+1, len(bboxes)):
                    if boxes_overlap(bboxes[i], bboxes[j]):
                        overlap_found = True
            results.append({'id': cid, 'overlap': overlap_found})
        except Exception as e:
            results.append({'id': cid, 'error': str(e)})
    out_dir.joinpath('results_pre.json').write_text(json.dumps(results, indent=2))
    # Basic assert: at least one case shows overlap (the bug)
    assert any(r.get('overlap') for r in results if 'overlap' in r)

if __name__ == '__main__':
    test_cases()
