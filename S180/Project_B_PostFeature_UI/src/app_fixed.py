import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Improved chart: label positions dynamically adjusted to avoid overlaps.

def draw_bar_chart(data, labels, outfile):
    fig, ax = plt.subplots(figsize=(8,4))
    x = np.arange(len(data))
    bars = ax.bar(x, data, color='navy')

    # compute candidate positions above and below bar
    used_boxes = []
    for i, bar in enumerate(bars):
        height = bar.get_height()
        # try top position first
        txt = ax.text(bar.get_x() + bar.get_width()/2, height + 0.01*max(data),
                      f"{data[i]}", ha='center', va='bottom', color='white', fontsize=11, fontweight='bold', bbox=dict(facecolor='black', alpha=0.6, pad=2))
        fig.canvas.draw()
        bbox = txt.get_window_extent(renderer=fig.canvas.get_renderer())
        # check overlap with existing labels
        overlap = False
        for b in used_boxes:
            if b.intersects(bbox):
                overlap = True
                break
        if overlap:
            # shift below the bar
            txt.set_y(height - 0.02*max(data))
            txt.set_va('top')
            fig.canvas.draw()
            bbox = txt.get_window_extent(renderer=fig.canvas.get_renderer())
        used_boxes.append(bbox)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, max(data)*1.4)
    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)

if __name__ == '__main__':
    sample_data = [10, 11, 10, 11, 10, 11, 10, 11]
    sample_labels = [f"P{i}" for i in range(len(sample_data))]
    draw_bar_chart(sample_data, sample_labels, 'results/post_fix.png')
