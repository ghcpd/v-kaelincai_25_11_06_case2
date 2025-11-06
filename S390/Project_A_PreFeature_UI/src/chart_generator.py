import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import os


class ChartGeneratorPre:
    """Basic (buggy) chart generator: places labels directly above bar centers without collision detection."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def draw_bar_chart(self, values, labels=None, title='Bar Chart (Pre-Feature)', filename='chart_pre.png', return_fig=False):
        fig, ax = plt.subplots(figsize=(8, 4))
        x = np.arange(len(values))
        bars = ax.bar(x, values, color='#4c72b0')
        ax.set_xticks(x)
        ax.set_xticklabels(labels if labels else [str(i) for i in range(len(values))])
        ax.set_title(title)

        # Buggy label placement: fixed position centered on bar top, without collision avoidance
        for bar, val in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                val,
                f'{val}',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black',
            )

        path = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        fig.savefig(path)
        if return_fig:
            return fig, path
        plt.close(fig)
        return path
