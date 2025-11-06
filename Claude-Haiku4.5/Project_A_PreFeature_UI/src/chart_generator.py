"""
Data Visualization Platform - Pre-Enhancement Version
This version has overlapping value labels and static positioning issues.
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
import json
from pathlib import Path


class ChartGeneratorPreEnhancement:
    """
    Basic chart generator with static label positioning.
    KNOWN ISSUES:
    - Value labels overlap with bars/lines
    - No dynamic adjustment of label positions
    - Fixed font size regardless of chart density
    - Poor contrast in some scenarios
    """
    
    def __init__(self):
        self.default_font_size = 12  # Static font size
        self.label_offset = 2  # Fixed offset for all labels
        
    def generate_bar_chart(self, data, output_path):
        """Generate a bar chart with static label positioning (causes overlaps)"""
        categories = data['categories']
        values = data['values']
        title = data['title']
        
        # Filter out None/empty categories
        valid_data = [(cat if cat else f"Item_{i}", val) 
                      for i, (cat, val) in enumerate(zip(categories, values))]
        categories, values = zip(*valid_data) if valid_data else ([], [])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(categories, values, color='steelblue', alpha=0.7)
        
        # PROBLEM: Static label positioning - all labels at same offset
        # This causes overlaps when bars are close together
        for i, (bar, value) in enumerate(zip(bars, values)):
            # Fixed vertical offset - doesn't consider bar height or proximity to other labels
            label_y = bar.get_height() + self.label_offset
            
            # Static font size - doesn't adjust for chart density
            ax.text(bar.get_x() + bar.get_width()/2, label_y, 
                   f'{value}',
                   ha='center', va='bottom',
                   fontsize=self.default_font_size,  # Always same size
                   color='black')  # Fixed color, no contrast consideration
        
        ax.set_title(title, fontsize=14, pad=20)
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=12)
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=12)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Rotate labels if many categories, but may still overlap
        if len(categories) > 10:
            plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return output_path
    
    def generate_line_chart(self, data, output_path):
        """Generate a line chart with static label positioning (causes overlaps)"""
        categories = data['categories']
        values = data['values']
        title = data['title']
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(categories, values, marker='o', linewidth=2, 
                markersize=8, color='steelblue')
        
        # PROBLEM: Labels placed at fixed offset above each point
        # When values are similar, labels overlap severely
        for i, (cat, value) in enumerate(zip(categories, values)):
            # No collision detection - all labels at same offset
            ax.text(i, value + self.label_offset, 
                   f'{value}',
                   ha='center', va='bottom',
                   fontsize=self.default_font_size,
                   color='black')
        
        ax.set_title(title, fontsize=14, pad=20)
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=12)
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=12)
        ax.grid(True, alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return output_path
    
    def generate_multi_bar_chart(self, data, output_path):
        """Generate a multi-series bar chart with overlapping labels"""
        categories = data['categories']
        series_data = data['series']
        title = data['title']
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        num_series = len(series_data)
        bar_width = 0.25
        x = np.arange(len(categories))
        
        # Plot each series
        for idx, series in enumerate(series_data):
            offset = (idx - num_series/2) * bar_width + bar_width/2
            bars = ax.bar(x + offset, series['values'], bar_width, 
                         label=series['name'], alpha=0.7)
            
            # PROBLEM: All labels at fixed offset regardless of density
            # In multi-series charts, this causes severe overlaps
            for bar, value in zip(bars, series['values']):
                ax.text(bar.get_x() + bar.get_width()/2, 
                       bar.get_height() + self.label_offset,
                       f'{value}',
                       ha='center', va='bottom',
                       fontsize=self.default_font_size,  # No size adjustment
                       color='black')
        
        ax.set_title(title, fontsize=14, pad=20)
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=12)
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return output_path
    
    def generate_chart(self, test_case, output_dir):
        """Generate chart based on test case data"""
        chart_type = test_case['chart_type']
        data = test_case['data']
        test_id = test_case['test_id']
        
        output_path = Path(output_dir) / f"{test_id}_chart.png"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if chart_type == 'bar':
            return self.generate_bar_chart(data, str(output_path))
        elif chart_type == 'line':
            return self.generate_line_chart(data, str(output_path))
        elif chart_type == 'multi_bar':
            return self.generate_multi_bar_chart(data, str(output_path))
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")


def main():
    """Test the chart generator"""
    generator = ChartGeneratorPreEnhancement()
    
    # Load test data
    with open('../../test_data.json', 'r') as f:
        test_data = json.load(f)
    
    output_dir = '../results/charts'
    
    for test_case in test_data['test_cases']:
        print(f"Generating chart for {test_case['test_id']}...")
        try:
            output_path = generator.generate_chart(test_case, output_dir)
            print(f"  Saved to: {output_path}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == '__main__':
    main()
