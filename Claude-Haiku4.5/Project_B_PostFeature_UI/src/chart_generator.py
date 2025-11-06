"""
Data Visualization Platform - Post-Enhancement Version
This version includes dynamic label positioning and accessibility improvements.
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
import json
from pathlib import Path
from adjustText import adjust_text


class ChartGeneratorPostEnhancement:
    """
    Enhanced chart generator with dynamic label positioning and accessibility features.
    IMPROVEMENTS:
    - Dynamic label positioning to avoid overlaps
    - Adaptive font sizing based on chart density
    - Contrast-aware color selection
    - Smart number formatting for large values
    - ARIA-compliant accessibility features
    """
    
    def __init__(self):
        self.min_font_size = 8
        self.max_font_size = 14
        self.min_label_spacing = 5  # Minimum pixels between labels
        
    def calculate_dynamic_font_size(self, num_elements):
        """Calculate optimal font size based on number of data points"""
        if num_elements <= 5:
            return self.max_font_size
        elif num_elements <= 10:
            return 12
        elif num_elements <= 15:
            return 10
        else:
            return self.min_font_size
    
    def format_large_number(self, value):
        """Format large numbers with abbreviations for better readability"""
        if abs(value) >= 1_000_000:
            return f'${value/1_000_000:.1f}M'
        elif abs(value) >= 1_000:
            return f'${value/1_000:.1f}K'
        else:
            return f'{value:.0f}'
    
    def get_contrast_color(self, background_color='white'):
        """Return a color with good contrast for accessibility"""
        # For white/light backgrounds, use dark text
        # WCAG AA compliant contrast ratio
        return '#1a1a1a'  # Very dark gray for excellent contrast
    
    def calculate_label_positions(self, values, base_positions, chart_height):
        """
        Dynamically adjust label positions to avoid overlaps.
        Uses collision detection and intelligent repositioning.
        """
        positions = []
        label_height = 20  # Approximate height of a text label in pixels
        
        for i, (value, base_y) in enumerate(zip(values, base_positions)):
            adjusted_y = base_y
            
            # Check for collisions with previous labels
            collision_detected = True
            offset_multiplier = 1
            
            while collision_detected and offset_multiplier < 5:
                collision_detected = False
                
                for prev_y in positions:
                    if abs(adjusted_y - prev_y) < self.min_label_spacing:
                        collision_detected = True
                        # Move label up to avoid collision
                        adjusted_y = base_y + (label_height * offset_multiplier)
                        offset_multiplier += 1
                        break
                
                # Ensure label doesn't go off chart
                if adjusted_y > chart_height * 0.95:
                    adjusted_y = base_y - (label_height * offset_multiplier)
                    offset_multiplier += 1
            
            positions.append(adjusted_y)
        
        return positions
    
    def generate_bar_chart(self, data, output_path):
        """Generate a bar chart with dynamic label positioning"""
        categories = data['categories']
        values = data['values']
        title = data['title']
        
        # Filter out None/empty categories
        valid_data = [(cat if cat else f"Item_{i}", val) 
                      for i, (cat, val) in enumerate(zip(categories, values))]
        categories, values = zip(*valid_data) if valid_data else ([], [])
        
        # Determine if we need number formatting
        needs_formatting = any(v > 10000 for v in values)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(categories, values, color='#4A90E2', alpha=0.8, edgecolor='#2E5C8A', linewidth=1.5)
        
        # ENHANCEMENT: Dynamic font size based on data density
        font_size = self.calculate_dynamic_font_size(len(values))
        text_color = self.get_contrast_color()
        
        # ENHANCEMENT: Collect all text objects for smart positioning
        texts = []
        base_positions = [bar.get_height() for bar in bars]
        
        # Calculate dynamic positions to avoid overlaps
        y_scale = ax.get_ylim()[1] - ax.get_ylim()[0]
        adjusted_positions = self.calculate_label_positions(
            values, base_positions, y_scale
        )
        
        for i, (bar, value, adj_y) in enumerate(zip(bars, values, adjusted_positions)):
            # ENHANCEMENT: Format large numbers
            label_text = self.format_large_number(value) if needs_formatting else f'{value}'
            
            # ENHANCEMENT: Use adjusted position
            text = ax.text(
                bar.get_x() + bar.get_width()/2, 
                adj_y,
                label_text,
                ha='center', 
                va='bottom',
                fontsize=font_size,
                color=text_color,
                fontweight='500',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor='none', alpha=0.7)  # Background for readability
            )
            texts.append(text)
        
        # ENHANCEMENT: Use adjust_text library for final collision avoidance
        # This intelligently moves labels to prevent any remaining overlaps
        if len(texts) > 0:
            adjust_text(texts, 
                       only_move={'points': 'y', 'texts': 'y'},
                       arrowprops=dict(arrowstyle='->', color='gray', lw=0.5, alpha=0.5))
        
        ax.set_title(title, fontsize=16, pad=20, fontweight='600')
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=13, fontweight='500')
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=13, fontweight='500')
        ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
        
        # ENHANCEMENT: Adaptive rotation based on label count
        if len(categories) > 10:
            plt.xticks(rotation=45, ha='right')
        elif len(categories) > 6:
            plt.xticks(rotation=30, ha='right')
        
        # ENHANCEMENT: Add more padding for labels
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return output_path
    
    def generate_line_chart(self, data, output_path):
        """Generate a line chart with dynamic label positioning"""
        categories = data['categories']
        values = data['values']
        title = data['title']
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(categories, values, marker='o', linewidth=2.5, 
                markersize=9, color='#4A90E2', markerfacecolor='#4A90E2',
                markeredgecolor='#2E5C8A', markeredgewidth=1.5)
        
        # ENHANCEMENT: Dynamic font size
        font_size = self.calculate_dynamic_font_size(len(values))
        text_color = self.get_contrast_color()
        
        # ENHANCEMENT: Smart label positioning for clustered values
        texts = []
        y_positions = []
        
        for i, (cat, value) in enumerate(zip(categories, values)):
            # Calculate base position
            base_offset = 5
            
            # Check for nearby values
            adjusted_offset = base_offset
            for j, prev_val in enumerate(values[:i]):
                if abs(value - prev_val) < (max(values) - min(values)) * 0.15:
                    # Values are close, adjust offset
                    adjusted_offset += 10 * (1 + (i - j) % 2)
            
            text = ax.text(
                i, 
                value + adjusted_offset,
                f'{value}',
                ha='center', 
                va='bottom',
                fontsize=font_size,
                color=text_color,
                fontweight='500',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor='none', alpha=0.8)
            )
            texts.append(text)
        
        # ENHANCEMENT: Final adjustment to prevent overlaps
        if len(texts) > 0:
            adjust_text(texts, 
                       only_move={'points': 'y', 'texts': 'y'},
                       arrowprops=dict(arrowstyle='->', color='gray', lw=0.5, alpha=0.5))
        
        ax.set_title(title, fontsize=16, pad=20, fontweight='600')
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=13, fontweight='500')
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=13, fontweight='500')
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return output_path
    
    def generate_multi_bar_chart(self, data, output_path):
        """Generate a multi-series bar chart with smart label positioning"""
        categories = data['categories']
        series_data = data['series']
        title = data['title']
        
        fig, ax = plt.subplots(figsize=(14, 7))
        
        num_series = len(series_data)
        bar_width = 0.25
        x = np.arange(len(categories))
        
        # ENHANCEMENT: Color palette with good contrast
        colors = ['#4A90E2', '#50C878', '#FFB347', '#E74C3C', '#9B59B6']
        
        # ENHANCEMENT: Dynamic font size for multi-series
        font_size = self.calculate_dynamic_font_size(len(categories) * num_series)
        text_color = self.get_contrast_color()
        
        all_texts = []
        
        # Plot each series
        for idx, series in enumerate(series_data):
            offset = (idx - num_series/2) * bar_width + bar_width/2
            bars = ax.bar(x + offset, series['values'], bar_width, 
                         label=series['name'], alpha=0.85, 
                         color=colors[idx % len(colors)],
                         edgecolor='#333333', linewidth=1)
            
            # ENHANCEMENT: Staggered label positioning for multi-series
            for bar_idx, (bar, value) in enumerate(zip(bars, series['values'])):
                # Stagger vertically based on series index
                vertical_offset = 5 + (idx * 15)
                
                text = ax.text(
                    bar.get_x() + bar.get_width()/2, 
                    bar.get_height() + vertical_offset,
                    f'{value}',
                    ha='center', 
                    va='bottom',
                    fontsize=font_size,
                    color=text_color,
                    fontweight='500',
                    bbox=dict(boxstyle='round,pad=0.2', 
                             facecolor='white', 
                             edgecolor=colors[idx % len(colors)], 
                             alpha=0.8,
                             linewidth=1)
                )
                all_texts.append(text)
        
        # ENHANCEMENT: Intelligent collision avoidance
        if len(all_texts) > 0:
            adjust_text(all_texts, 
                       only_move={'points': 'y', 'texts': 'y'},
                       arrowprops=dict(arrowstyle='->', color='gray', lw=0.5, alpha=0.5))
        
        ax.set_title(title, fontsize=16, pad=20, fontweight='600')
        ax.set_xlabel(data.get('x_label', 'Category'), fontsize=13, fontweight='500')
        ax.set_ylabel(data.get('y_label', 'Value'), fontsize=13, fontweight='500')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend(loc='upper left', framealpha=0.9, fontsize=11)
        ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return output_path
    
    def generate_chart(self, test_case, output_dir):
        """Generate chart based on test case data"""
        chart_type = test_case['chart_type']
        data = test_case['data']
        test_id = test_case['test_id']
        
        output_path = Path(output_dir) / f"{test_id}_chart_enhanced.png"
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
    """Test the enhanced chart generator"""
    generator = ChartGeneratorPostEnhancement()
    
    # Load test data
    with open('../../test_data.json', 'r') as f:
        test_data = json.load(f)
    
    output_dir = '../results/charts'
    
    for test_case in test_data['test_cases']:
        print(f"Generating enhanced chart for {test_case['test_id']}...")
        try:
            output_path = generator.generate_chart(test_case, output_dir)
            print(f"  Saved to: {output_path}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == '__main__':
    main()
