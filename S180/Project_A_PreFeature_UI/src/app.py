import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Basic chart which places labels statically centered on bars leading to potential overlap

def draw_bar_chart(data, labels, outfile):
    fig, ax = plt.subplots(figsize=(8,4))
    x = np.arange(len(data))
    bars = ax.bar(x, data, color='skyblue')

    for i, bar in enumerate(bars):
        height = bar.get_height()
        # static label placement at top center (bug: can overlap if bars close)
        ax.text(bar.get_x() + bar.get_width()/2, height - 0.02*max(data),
                f"{data[i]}", ha='center', va='top', color='black', fontsize=10)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, max(data)*1.2)
    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)

if __name__ == '__main__':
    sample_data = [10, 12, 11, 10, 12, 11, 11, 12]
    sample_labels = [f"P{i}" for i in range(len(sample_data))]
    draw_bar_chart(sample_data, sample_labels, 'results/pre_bug.png')
