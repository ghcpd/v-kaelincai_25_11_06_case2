import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import os


class ChartGeneratorPost:
    """Improved chart generator with dynamic label placement and contrast optimization."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    @staticmethod
    def _relative_luminance(hexcolor):
        hexcolor = hexcolor.lstrip('#')
        r = int(hexcolor[0:2], 16) / 255.0
        g = int(hexcolor[2:4], 16) / 255.0
        b = int(hexcolor[4:6], 16) / 255.0
        def _c(c):
            return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
        return 0.2126 * _c(r) + 0.7152 * _c(g) + 0.0722 * _c(b)

    @staticmethod
    def contrast_ratio(hex1, hex2):
        l1 = ChartGeneratorPost._relative_luminance(hex1)
        l2 = ChartGeneratorPost._relative_luminance(hex2)
        L1, L2 = max(l1, l2), min(l1, l2)
        return (L1 + 0.05) / (L2 + 0.05)

    def draw_bar_chart(self, values, labels=None, title='Bar Chart (Post-Feature)', filename='chart_post.png', return_bboxes=False):
        fig, ax = plt.subplots(figsize=(10, 5))
        x = np.arange(len(values))
        bars = ax.bar(x, values, color='#2b6ea3')
        ax.set_xticks(x)
        ax.set_xticklabels(labels if labels else [str(i) for i in range(len(values))])
        ax.set_title(title)

        # Use dynamic label placement: shift labels upward if they overlap
        placed_rects = []
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        for bar, val in zip(bars, values):
            # Initial position
            x_pos = bar.get_x() + bar.get_width() / 2
            y_pos = val
            txt = ax.text(x_pos, y_pos, f'{val}', ha='center', va='bottom', fontsize=11, color='white')
            fig.canvas.draw()
            bbox = txt.get_window_extent(renderer=renderer)
            # If text overlaps any existing label, move it up
            shift_px = 4
            attempts = 0
            while any((bbox.x0 < r[2] and bbox.x1 > r[0] and bbox.y0 < r[3] and bbox.y1 > r[1]) for r in placed_rects) and attempts < 10:
                y_pos += (bbox.height / fig.dpi) + 0.02  # shift by height in inches + a margin
                txt.set_y(y_pos)
                fig.canvas.draw()
                bbox = txt.get_window_extent(renderer=renderer)
                attempts += 1
            # Compute color contrast: make label white on dark bars, black otherwise
            bar_color = bar.get_facecolor()
            # Map RGBA to hex
            rgb = tuple(int(255*c) for c in bar_color[:3])
            hexcolor = '#%02x%02x%02x' % rgb
            c_white = '#ffffff'
            c_black = '#000000'
            if self.contrast_ratio(hexcolor, c_white) >= 4.5:
                txt.set_color(c_white)
            else:
                txt.set_color(c_black)
            # Save bbox in pixels
            bbox = txt.get_window_extent(renderer=renderer)
            placed_rects.append({'bbox': (bbox.x0, bbox.y0, bbox.x1, bbox.y1), 'color': txt.get_color(), 'bar_color': hexcolor})

        path = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        fig.savefig(path)
        if return_bboxes:
            return path, placed_rects
        plt.close(fig)
        return path
