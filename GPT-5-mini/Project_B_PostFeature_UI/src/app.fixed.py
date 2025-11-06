"""
Improved rendering with label collision avoidance and better contrast
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def place_labels(ax, bars, values, renderer, min_gap=2):
    texts = []
    # Start with labels above each bar at different heights based on value to reduce collisions
    heights = [b.get_height() for b in bars]
    sorted_idx = sorted(range(len(bars)), key=lambda i: heights[i], reverse=True)
    placed = []
    for i in sorted_idx:
        b = bars[i]
        x = b.get_x() + b.get_width()/2
        y = b.get_height()
        # candidate y positions: offset increments
        for offset in [0.02, 0.05, 0.08, 0.12, 0.18]:
            cand_y = y + (max(heights) * offset)
            t = ax.text(x, cand_y, str(values[i]), ha='center', va='bottom', fontsize=11, color='#000000')
            fig = ax.get_figure()
            fig.canvas.draw()
            bbox = t.get_window_extent(renderer)
            conflict = False
            for p in placed:
                # simple overlap check in pixel coords
                if not (bbox.x1 + min_gap <= p[0] or bbox.x0 - min_gap >= p[2] or bbox.y1 + min_gap <= p[1] or bbox.y0 - min_gap >= p[3]):
                    conflict = True
                    break
            if not conflict:
                placed.append([bbox.x0, bbox.y0, bbox.x1, bbox.y1])
                texts.append(t)
                break
            else:
                t.remove()
        else:
            # fallback: place inside bar
            t = ax.text(x, y/2, str(values[i]), ha='center', va='center', fontsize=10, color='white')
            texts.append(t)
    return texts

def render(data, out_path):
    labels = [str(x['label']) for x in data]
    values = [x['value'] for x in data]
    fig, ax = plt.subplots(figsize=(8,4))
    bars = ax.bar(range(len(values)), values, color='#1f77b4')
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    plt.tight_layout()
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    texts = place_labels(ax, bars, values, renderer)
    fig.savefig(out_path, dpi=150)
    # compute bboxes
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bboxes = [t.get_window_extent(renderer).extents.tolist() for t in texts]
    plt.close(fig)
    return bboxes

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    data = json.loads(Path(in_file).read_text())
    render(data, Path(out_file))
