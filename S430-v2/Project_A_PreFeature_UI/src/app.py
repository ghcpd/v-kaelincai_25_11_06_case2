import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def generate_bar_chart(data, categories, output_path, title='Chart', static_labels=True):
    """
    Generate a bar chart and save to output_path.
    static_labels: if True, add labels at a fixed offset (this is the bug)
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig, ax = plt.subplots(figsize=(8,4))
    x = np.arange(len(data))
    # Support multi-series input
    if isinstance(data, dict) and 'series' in data:
        series = data['series']
        categories = data.get('categories', categories)
        n_series = len(series)
        width = 0.8 / n_series
        for i, s in enumerate(series):
            vals = s['values']
            xs = [xi + (i - n_series/2 + 0.5)*width for xi in x]
            bars = ax.bar(xs, vals, width=width, label=s.get('name', f"series_{i}"))
            if static_labels:
                offset = max(vals) * 0.02
                for bar, val in zip(bars, vals):
                    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + offset,
                            f"{val}", ha='center', va='bottom', fontsize=9, color='black')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
    else:
        bars = ax.bar(x, data, color='#3B82F6')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.set_title(title)

        # Static label placement (bug): constant offset above bar top
        if static_labels:
            offset = max(data) * 0.02
            for bar, val in zip(bars, data):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + offset,
                        f"{val}", ha='center', va='bottom', fontsize=9, color='black')
        else:
            # No labels
            pass

    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return output_path


def load_test_data(path):
    with open(path, 'r') as f:
        return json.load(f)
