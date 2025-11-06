import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects


def generate_bar_chart_dynamic(data, categories, output_path, title='Chart'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig, ax = plt.subplots(figsize=(8,4))
    x = np.arange(len(categories))

    # Support multi-series
    if isinstance(data, dict) and 'series' in data:
        series = data['series']
        n_series = len(series)
        width = 0.8 / n_series
        placed_bboxes = []
        renderer = fig.canvas.get_renderer()
        gap = 4
        for i, s in enumerate(series):
            vals = s['values']
            xs = [xi + (i - n_series/2 + 0.5)*width for xi in x]
            bars = ax.bar(xs, vals, width=width, color=['#1F2937', '#2563EB'][i % 2], label=s.get('name'))
            base_offset = max(vals) * 0.02
            for bar, val in zip(bars, vals):
                y = bar.get_height() + base_offset
                txt = ax.text(bar.get_x() + bar.get_width()/2, y, f"{val}", ha='center', va='bottom', fontsize=10, color='#ffffff')
                # Add stroke for contrast
                txt.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'), path_effects.Normal()])
                fig.canvas.draw()
                bbox = txt.get_window_extent(renderer=renderer).expanded(1.0, 1.0)
                overlap = True
                retries = 0
                while overlap and retries < 20:
                    overlap = False
                    for pb in placed_bboxes:
                        if not (bbox.x1 <= pb.x0 or bbox.x0 >= pb.x1 or bbox.y1 <= pb.y0 or bbox.y0 >= pb.y1):
                            label_height = bbox.height
                            y += (label_height + gap) * (ax.get_window_extent(renderer=renderer).height / ax.bbox.height) / fig.dpi
                            txt.set_y(y)
                            fig.canvas.draw()
                            bbox = txt.get_window_extent(renderer=renderer).expanded(1.0, 1.0)
                            overlap = True
                            retries += 1
                            break
                placed_bboxes.append(bbox)
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
    else:
        bars = ax.bar(x, data, color='#1F2937')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.set_title(title)

        # dynamic label placement: avoid overlap
        renderer = fig.canvas.get_renderer()
        placed_bboxes = []
        gap = 4  # pixels of separation to enforce
        base_offset = max(data) * 0.02
        for bar, val in zip(bars, data):
            y = bar.get_height() + base_offset
            txt = ax.text(bar.get_x() + bar.get_width()/2, y, f"{val}", ha='center', va='bottom', fontsize=10, color='#ffffff')
            # Add stroke for contrast
            txt.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'), path_effects.Normal()])
            fig.canvas.draw()
            bbox = txt.get_window_extent(renderer=renderer).expanded(1.0, 1.0)

            # push label up until it does not overlap previous labels
            overlap = True
            retries = 0
            while overlap and retries < 20:
                overlap = False
                for pb in placed_bboxes:
                    if not (bbox.x1 <= pb.x0 or bbox.x0 >= pb.x1 or bbox.y1 <= pb.y0 or bbox.y0 >= pb.y1):
                        # overlap - move label up by its height + gap
                        label_height = bbox.height
                        y += (label_height + gap) * (ax.get_window_extent(renderer=renderer).height / ax.bbox.height) / fig.dpi
                        txt.set_y(y)
                        fig.canvas.draw()
                        bbox = txt.get_window_extent(renderer=renderer).expanded(1.0, 1.0)
                        overlap = True
                        retries += 1
                        break

            placed_bboxes.append(bbox)

    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return output_path


def load_test_data(path):
    with open(path, 'r') as f:
        return json.load(f)
