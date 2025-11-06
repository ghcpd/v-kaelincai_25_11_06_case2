"""
Simple script to generate a bar chart with overlapping labels (pre-enhancement)
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def render(data, out_path):
    labels = [str(x['label']) for x in data]
    values = [x['value'] for x in data]
    fig, ax = plt.subplots(figsize=(8,4))
    bars = ax.bar(range(len(values)), values, color='skyblue')
    # Intentionally bad label placement: all labels at top with same y-offset causing overlap
    texts = []
    # Intentionally bad: place every label at the same center position to create overlap
    center_bar = bars[len(bars)//2]
    cx = center_bar.get_x() + center_bar.get_width()/2
    cy = max(values) * 0.95
    for i, b in enumerate(bars):
        t = ax.text(cx, cy, str(values[i]), ha='center', va='center', fontsize=10, color='black')
        texts.append(t)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Draw to compute renderer and text bboxes
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bboxes = []
    for t in texts:
        bbox = t.get_window_extent(renderer)
        bboxes.append([bbox.x0, bbox.y0, bbox.x1, bbox.y1])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return bboxes

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    data = json.loads(Path(in_file).read_text())
    render(data, Path(out_file))
