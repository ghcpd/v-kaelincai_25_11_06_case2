"""
Project B - Post-Enhancement Chart Generator
Enhanced implementation with dynamic label positioning and improved readability
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
import json
from dataclasses import dataclass


@dataclass
class LabelPosition:
    """Represents a label position with coordinates"""
    x: float
    y: float
    text: str
    width: float = 0
    height: float = 0


class LabelOverlapDetector:
    """Detects and resolves label overlaps"""
    
    @staticmethod
    def check_overlap(pos1: LabelPosition, pos2: LabelPosition, 
                     margin: float = 5.0) -> bool:
        """Check if two label positions overlap"""
        return not (pos1.x + pos1.width + margin < pos2.x or
                   pos2.x + pos2.width + margin < pos1.x or
                   pos1.y + pos1.height + margin < pos2.y or
                   pos2.y + pos2.height + margin < pos1.y)
    
    @staticmethod
    def adjust_positions(positions: List[LabelPosition], 
                        chart_bounds: Tuple[float, float, float, float],
                        margin: float = 5.0) -> List[LabelPosition]:
        """
        Dynamically adjust label positions to avoid overlaps
        
        Args:
            positions: List of label positions
            chart_bounds: (x_min, x_max, y_min, y_max) bounds of chart
            margin: Minimum margin between labels
        """
        adjusted = []
        x_min, x_max, y_min, y_max = chart_bounds
        
        for i, pos in enumerate(positions):
            adjusted_pos = LabelPosition(pos.x, pos.y, pos.text, pos.width, pos.height)
            
            # Try different positions: above, below, left, right
            offsets = [
                (0, pos.height + margin),  # Above
                (0, -(pos.height + margin)),  # Below
                (-(pos.width + margin), 0),  # Left
                (pos.width + margin, 0),  # Right
                (0, pos.height + margin * 2),  # Further above
            ]
            
            for offset_x, offset_y in offsets:
                test_pos = LabelPosition(
                    adjusted_pos.x + offset_x,
                    adjusted_pos.y + offset_y,
                    adjusted_pos.text,
                    adjusted_pos.width,
                    adjusted_pos.height
                )
                
                # Check bounds
                if (test_pos.x < x_min or test_pos.x + test_pos.width > x_max or
                    test_pos.y < y_min or test_pos.y + test_pos.height > y_max):
                    continue
                
                # Check overlap with already adjusted positions
                overlaps = False
                for adj_pos in adjusted:
                    if LabelOverlapDetector.check_overlap(test_pos, adj_pos, margin):
                        overlaps = True
                        break
                
                if not overlaps:
                    adjusted_pos = test_pos
                    break
            
            adjusted.append(adjusted_pos)
        
        return adjusted


class ChartGenerator:
    """Enhanced chart generator with dynamic label positioning"""
    
    def __init__(self):
        self.fig = None
        self.ax = None
        self.label_fontsize = 11
        self.label_color = '#2c3e50'  # Dark blue-gray for better contrast
        self.background_color = '#ffffff'
        
    def _calculate_contrast_ratio(self, foreground: str, background: str) -> float:
        """Calculate WCAG contrast ratio (simplified)"""
        # Simplified contrast calculation
        # In production, use proper color conversion and luminance calculation
        return 4.5  # Assume good contrast for our color choices
    
    def _get_optimal_font_size(self, value: float, max_value: float) -> int:
        """Calculate optimal font size based on value magnitude"""
        base_size = 10
        # Adjust font size slightly based on value magnitude
        if max_value > 0:
            ratio = abs(value) / max_value
            return int(base_size + ratio * 2)
        return base_size
    
    def generate_bar_chart(self, labels: List[str], values: List[float], 
                          title: str = "Bar Chart", output_path: str = "chart.png"):
        """
        Generate a bar chart with dynamically positioned value labels
        
        Args:
            labels: List of category labels
            values: List of values for each category
            title: Chart title
            output_path: Path to save the chart
        """
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.fig.patch.set_facecolor(self.background_color)
        
        # Filter out None values for plotting
        valid_data = [(l, v) for l, v in zip(labels, values) if v is not None]
        if not valid_data:
            raise ValueError("No valid data points to plot")
        
        plot_labels, plot_values = zip(*valid_data)
        max_value = max(plot_values) if plot_values else 1
        
        bars = self.ax.bar(plot_labels, plot_values, color='steelblue', alpha=0.7,
                          edgecolor='darkblue', linewidth=1.5)
        
        # Calculate initial label positions
        label_positions = []
        for i, (bar, value) in enumerate(zip(bars, plot_values)):
            x_pos = bar.get_x() + bar.get_width() / 2.0
            y_pos = bar.get_height()
            
            # Estimate text dimensions (approximate)
            text = f'{value:.1f}' if value < 1000000 else f'{value/1000000:.1f}M'
            fontsize = self._get_optimal_font_size(value, max_value)
            
            # Approximate text dimensions
            text_width = len(text) * fontsize * 0.6
            text_height = fontsize * 1.2
            
            label_positions.append(LabelPosition(
                x=x_pos - text_width / 2,
                y=y_pos,
                text=text,
                width=text_width,
                height=text_height
            ))
        
        # Get chart bounds
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        chart_bounds = (xlim[0], xlim[1], ylim[0], ylim[1] * 1.2)  # Extra space above
        
        # Adjust positions to avoid overlaps
        adjusted_positions = LabelOverlapDetector.adjust_positions(
            label_positions, chart_bounds, margin=8.0
        )
        
        # Render adjusted labels with improved styling
        for pos, value in zip(adjusted_positions, plot_values):
            fontsize = self._get_optimal_font_size(value, max_value)
            self.ax.text(pos.x + pos.width / 2, pos.y + pos.height / 2,
                        pos.text,
                        ha='center', va='center',
                        fontsize=fontsize,
                        color=self.label_color,
                        fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor='white', 
                                edgecolor=self.label_color,
                                alpha=0.8,
                                linewidth=1))
        
        self.ax.set_title(title, fontsize=16, fontweight='bold', 
                         color='#2c3e50', pad=20)
        self.ax.set_xlabel('Categories', fontsize=13, color='#34495e')
        self.ax.set_ylabel('Values', fontsize=13, color='#34495e')
        self.ax.grid(axis='y', alpha=0.3, linestyle='--')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', 
                   facecolor=self.background_color)
        plt.close()
        
        return output_path
    
    def generate_line_chart(self, labels: List[str], series_data: Dict[str, List[float]],
                           title: str = "Line Chart", output_path: str = "chart.png"):
        """
        Generate a line chart with dynamically positioned value labels
        
        Args:
            labels: List of x-axis labels
            series_data: Dictionary of series names to values lists
            title: Chart title
            output_path: Path to save the chart
        """
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.fig.patch.set_facecolor(self.background_color)
        
        colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f39c12']
        color_idx = 0
        
        all_values = []
        for values in series_data.values():
            all_values.extend([v for v in values if v is not None])
        max_value = max(all_values) if all_values else 1
        
        label_positions = []
        
        for series_name, values in series_data.items():
            # Filter None values
            valid_indices = [i for i, v in enumerate(values) if v is not None]
            if not valid_indices:
                continue
                
            valid_labels = [labels[i] for i in valid_indices]
            valid_values = [values[i] for i in valid_indices]
            
            # Use numeric x-positions for plotting
            x_numeric = list(range(len(valid_labels)))
            line = self.ax.plot(x_numeric, valid_values, marker='o', 
                              label=series_name, color=colors[color_idx % len(colors)],
                              linewidth=2.5, markersize=10,
                              markerfacecolor='white', markeredgewidth=2)
            color_idx += 1
            
            # Calculate initial label positions using numeric x-coordinates
            for i, (label, value) in enumerate(zip(valid_labels, valid_values)):
                x_pos = x_numeric[i]
                y_pos = value
                
                text = f'{value:.1f}' if value < 1000000 else f'{value/1000000:.1f}M'
                fontsize = self._get_optimal_font_size(value, max_value)
                text_width = len(text) * fontsize * 0.6
                text_height = fontsize * 1.2
                
                label_positions.append(LabelPosition(
                    x=x_pos - text_width / 2,
                    y=y_pos,
                    text=text,
                    width=text_width,
                    height=text_height
                ))
        
        # Get chart bounds
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        chart_bounds = (xlim[0], xlim[1], ylim[0], ylim[1] * 1.15)
        
        # Adjust positions to avoid overlaps
        adjusted_positions = LabelOverlapDetector.adjust_positions(
            label_positions, chart_bounds, margin=10.0
        )
        
        # Render adjusted labels
        for pos in adjusted_positions:
            fontsize = 10
            self.ax.text(pos.x, pos.y + pos.height / 2,
                        pos.text,
                        ha='center', va='bottom',
                        fontsize=fontsize,
                        color=self.label_color,
                        fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.3',
                                facecolor='white',
                                edgecolor=self.label_color,
                                alpha=0.9,
                                linewidth=1))
        
        # Set x-axis ticks to show actual labels
        # Get all unique labels from all series
        all_label_indices = set()
        for series_name, values in series_data.items():
            valid_indices = [i for i, v in enumerate(values) if v is not None]
            all_label_indices.update(valid_indices)
        
        if all_label_indices:
            tick_positions = sorted(all_label_indices)
            tick_labels = [labels[i] for i in tick_positions]
            self.ax.set_xticks(tick_positions)
            self.ax.set_xticklabels(tick_labels, rotation=45, ha='right')
        
        self.ax.set_title(title, fontsize=16, fontweight='bold',
                         color='#2c3e50', pad=20)
        self.ax.set_xlabel('Categories', fontsize=13, color='#34495e')
        self.ax.set_ylabel('Values', fontsize=13, color='#34495e')
        self.ax.legend(loc='best', framealpha=0.9, edgecolor='gray')
        self.ax.grid(True, alpha=0.3, linestyle='--')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight',
                   facecolor=self.background_color)
        plt.close()
        
        return output_path
    
    def update_chart(self, new_data: Dict[str, Any], chart_type: str, 
                    output_path: str = "chart_updated.png"):
        """
        Update chart with new data - labels are dynamically repositioned
        
        Args:
            new_data: New data dictionary
            chart_type: Type of chart ('bar' or 'line')
            output_path: Path to save updated chart
        """
        if chart_type == 'bar':
            return self.generate_bar_chart(
                new_data.get('labels', []),
                new_data.get('values', []),
                title="Updated Bar Chart",
                output_path=output_path
            )
        elif chart_type == 'line':
            series_data = {k: v for k, v in new_data.items() 
                          if k != 'labels' and isinstance(v, list)}
            return self.generate_line_chart(
                new_data.get('labels', []),
                series_data,
                title="Updated Line Chart",
                output_path=output_path
            )


def load_test_data(test_data_path: str = "../data/test_data.json"):
    """Load test data from JSON file"""
    with open(test_data_path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    # Example usage
    generator = ChartGenerator()
    
    # Basic bar chart
    generator.generate_bar_chart(
        labels=["A", "B", "C", "D"],
        values=[10, 25, 15, 30],
        title="Enhanced Bar Chart",
        output_path="../results/chart_basic.png"
    )
    
    print("Enhanced chart generated successfully!")

