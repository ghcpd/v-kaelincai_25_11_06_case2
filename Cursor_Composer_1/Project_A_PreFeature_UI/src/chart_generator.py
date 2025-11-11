"""
Project A - Pre-Enhancement Chart Generator
Basic implementation with overlapping value labels
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from typing import Dict, List, Optional, Any
import json


class ChartGenerator:
    """Basic chart generator with static label positioning"""
    
    def __init__(self):
        self.fig = None
        self.ax = None
        
    def generate_bar_chart(self, labels: List[str], values: List[float], 
                          title: str = "Bar Chart", output_path: str = "chart.png"):
        """
        Generate a bar chart with value labels that may overlap
        
        Args:
            labels: List of category labels
            values: List of values for each category
            title: Chart title
            output_path: Path to save the chart
        """
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        
        # Filter out None values for plotting
        valid_data = [(l, v) for l, v in zip(labels, values) if v is not None]
        if not valid_data:
            raise ValueError("No valid data points to plot")
        
        plot_labels, plot_values = zip(*valid_data)
        
        bars = self.ax.bar(plot_labels, plot_values, color='steelblue', alpha=0.7)
        
        # Static label placement - always above bars, may overlap
        for bar in bars:
            height = bar.get_height()
            # Static positioning - no overlap detection
            self.ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f}',
                        ha='center', va='bottom', fontsize=10, color='black')
        
        self.ax.set_title(title, fontsize=14, fontweight='bold')
        self.ax.set_xlabel('Categories', fontsize=12)
        self.ax.set_ylabel('Values', fontsize=12)
        self.ax.grid(axis='y', alpha=0.3)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        return output_path
    
    def generate_line_chart(self, labels: List[str], series_data: Dict[str, List[float]],
                           title: str = "Line Chart", output_path: str = "chart.png"):
        """
        Generate a line chart with value labels that may overlap
        
        Args:
            labels: List of x-axis labels
            series_data: Dictionary of series names to values lists
            title: Chart title
            output_path: Path to save the chart
        """
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        
        colors = ['steelblue', 'coral', 'green', 'purple', 'orange']
        color_idx = 0
        
        for series_name, values in series_data.items():
            # Filter None values
            valid_indices = [i for i, v in enumerate(values) if v is not None]
            if not valid_indices:
                continue
                
            valid_labels = [labels[i] for i in valid_indices]
            valid_values = [values[i] for i in valid_indices]
            
            line = self.ax.plot(valid_labels, valid_values, marker='o', 
                              label=series_name, color=colors[color_idx % len(colors)],
                              linewidth=2, markersize=8)
            color_idx += 1
            
            # Static label placement - always above points, may overlap
            for label, value in zip(valid_labels, valid_values):
                self.ax.text(label, value, f'{value:.1f}',
                           ha='center', va='bottom', fontsize=9, color='black')
        
        self.ax.set_title(title, fontsize=14, fontweight='bold')
        self.ax.set_xlabel('Categories', fontsize=12)
        self.ax.set_ylabel('Values', fontsize=12)
        self.ax.legend(loc='best')
        self.ax.grid(True, alpha=0.3)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        return output_path
    
    def update_chart(self, new_data: Dict[str, Any], chart_type: str, 
                    output_path: str = "chart_updated.png"):
        """
        Update chart with new data - labels remain in static positions
        
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
        title="Basic Bar Chart",
        output_path="../results/chart_basic.png"
    )
    
    print("Chart generated successfully!")

