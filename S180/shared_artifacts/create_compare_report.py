import json, os
p='shared_artifacts'
pre=json.load(open(os.path.join(p,'results_pre.json')))
post=json.load(open(os.path.join(p,'results_post.json')))
open(os.path.join(p,'compare_report.json'),'w').write(json.dumps({'pre':pre,'post':post},indent=2))
print('Wrote compare_report.json')
