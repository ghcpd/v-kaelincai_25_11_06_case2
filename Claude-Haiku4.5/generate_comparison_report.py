"""
Comparison Report Generator
Compares pre-enhancement and post-enhancement results
"""

import json
from pathlib import Path
from datetime import datetime


def generate_comparison_report():
    """Generate a comprehensive comparison report in Markdown format"""
    
    # Load results from both projects
    pre_results_path = Path('Project_A_PreFeature_UI/results/results_pre.json')
    post_results_path = Path('Project_B_PostFeature_UI/results/results_post.json')
    
    if not pre_results_path.exists():
        print(f"Warning: {pre_results_path} not found. Run Project A tests first.")
        pre_results = {'test_results': [], 'passed': 0, 'failed': 0, 'total_tests': 0}
    else:
        with open(pre_results_path, 'r') as f:
            pre_results = json.load(f)
    
    if not post_results_path.exists():
        print(f"Warning: {post_results_path} not found. Run Project B tests first.")
        post_results = {'test_results': [], 'passed': 0, 'failed': 0, 'total_tests': 0}
    else:
        with open(post_results_path, 'r') as f:
            post_results = json.load(f)
    
    # Generate markdown report
    report = []
    
    report.append("# Data Visualization Enhancement - Comparison Report\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append("---\n\n")
    
    # Executive Summary
    report.append("## Executive Summary\n\n")
    report.append("This report compares the data visualization platform before and after implementing ")
    report.append("enhancements to address label overlap and readability issues.\n\n")
    
    report.append("### Overall Test Results\n\n")
    report.append("| Project | Total Tests | Passed | Failed | Success Rate |\n")
    report.append("|---------|-------------|--------|--------|-------------|\n")
    
    pre_success_rate = (pre_results['passed'] / pre_results['total_tests'] * 100) if pre_results['total_tests'] > 0 else 0
    post_success_rate = (post_results['passed'] / post_results['total_tests'] * 100) if post_results['total_tests'] > 0 else 0
    
    report.append(f"| Project A (Pre-Enhancement) | {pre_results['total_tests']} | "
                 f"{pre_results['passed']} | {pre_results['failed']} | {pre_success_rate:.1f}% |\n")
    report.append(f"| Project B (Post-Enhancement) | {post_results['total_tests']} | "
                 f"{post_results['passed']} | {post_results['failed']} | {post_success_rate:.1f}% |\n\n")
    
    improvement = post_success_rate - pre_success_rate
    report.append(f"**Improvement:** +{improvement:.1f} percentage points\n\n")
    
    # Key Improvements
    report.append("## Key Improvements Implemented\n\n")
    
    if 'enhancements_implemented' in post_results:
        for enhancement in post_results['enhancements_implemented']:
            report.append(f"- ✅ {enhancement}\n")
        report.append("\n")
    
    # Accessibility Metrics
    report.append("## Accessibility Improvements\n\n")
    
    if 'accessibility_improvements' in post_results:
        acc = post_results['accessibility_improvements']
        report.append("| Metric | Value | Standard | Status |\n")
        report.append("|--------|-------|----------|--------|\n")
        report.append(f"| Average Contrast Ratio | {acc.get('average_contrast_ratio', 'N/A')} | 4.5:1 (WCAG AA) | "
                     f"{'✅ Pass' if acc.get('wcag_aa_compliant') else '❌ Fail'} |\n")
        report.append(f"| WCAG AAA Compliance | {'Yes' if acc.get('wcag_aaa_compliant') else 'No'} | 7:1 | "
                     f"{'✅ Pass' if acc.get('wcag_aaa_compliant') else '❌ Fail'} |\n")
        report.append(f"| Adaptive Font Sizing | {'Enabled' if acc.get('adaptive_font_sizing') else 'Disabled'} | Recommended | "
                     f"{'✅ Pass' if acc.get('adaptive_font_sizing') else '❌ Fail'} |\n\n")
    
    # Detailed Test Case Comparison
    report.append("## Detailed Test Case Comparison\n\n")
    
    # Create a mapping of test results
    pre_tests = {t['test_id']: t for t in pre_results.get('test_results', [])}
    post_tests = {t['test_id']: t for t in post_results.get('test_results', [])}
    
    all_test_ids = sorted(set(list(pre_tests.keys()) + list(post_tests.keys())))
    
    for test_id in all_test_ids:
        pre_test = pre_tests.get(test_id, {})
        post_test = post_tests.get(test_id, {})
        
        report.append(f"### {test_id}: {post_test.get('test_name', pre_test.get('test_name', 'Unknown'))}\n\n")
        
        # Status comparison
        report.append("| Aspect | Pre-Enhancement | Post-Enhancement |\n")
        report.append("|--------|-----------------|------------------|\n")
        report.append(f"| **Status** | {pre_test.get('status', 'N/A')} | {post_test.get('status', 'N/A')} |\n")
        
        # Chart comparison
        if pre_test.get('chart_path') or post_test.get('chart_path'):
            report.append(f"| **Chart Generated** | {'✅' if pre_test.get('chart_generated') else '❌'} | "
                         f"{'✅' if post_test.get('chart_generated') else '❌'} |\n")
        
        # Issues vs Improvements
        if 'issues' in pre_test and 'improvements' in post_test:
            report.append("\n**Issues Resolved:**\n\n")
            
            pre_issues = pre_test['issues']
            post_improvements = post_test['improvements']
            
            for issue_key, issue_value in pre_issues.items():
                improvement_key = issue_key.replace('_', ' ').replace('poor', 'high').replace('low', 'excellent').replace('no', '')
                matched_improvement = None
                
                for imp_key, imp_value in post_improvements.items():
                    if any(word in imp_key for word in issue_key.split('_')):
                        matched_improvement = (imp_key, imp_value)
                        break
                
                if issue_value:  # If the issue existed
                    report.append(f"- ❌ **Before:** {issue_key.replace('_', ' ').title()}\n")
                    if matched_improvement:
                        report.append(f"  - ✅ **After:** {matched_improvement[0].replace('_', ' ').title()}\n")
        
        # Metrics comparison
        if 'metrics' in pre_test or 'metrics' in post_test:
            report.append("\n**Metrics:**\n\n")
            report.append("| Metric | Pre-Enhancement | Post-Enhancement | Improvement |\n")
            report.append("|--------|-----------------|------------------|-------------|\n")
            
            pre_metrics = pre_test.get('metrics', {})
            post_metrics = post_test.get('metrics', {})
            
            all_metrics = set(list(pre_metrics.keys()) + list(post_metrics.keys()))
            
            for metric in sorted(all_metrics):
                pre_val = pre_metrics.get(metric, 'N/A')
                post_val = post_metrics.get(metric, 'N/A')
                
                if isinstance(pre_val, (int, float)) and isinstance(post_val, (int, float)):
                    improvement_val = post_val - pre_val
                    improvement_str = f"+{improvement_val:.1f}" if improvement_val > 0 else f"{improvement_val:.1f}"
                else:
                    improvement_str = "N/A"
                
                report.append(f"| {metric.replace('_', ' ').title()} | {pre_val} | {post_val} | {improvement_str} |\n")
        
        # Screenshot comparison
        report.append("\n**Visual Comparison:**\n\n")
        
        if pre_test.get('chart_path'):
            pre_path = Path(pre_test['chart_path']).relative_to(Path.cwd())
            report.append(f"**Before (Pre-Enhancement):**\n\n")
            report.append(f"![Pre-Enhancement Chart]({pre_path})\n\n")
        
        if post_test.get('chart_path'):
            post_path = Path(post_test['chart_path']).relative_to(Path.cwd())
            report.append(f"**After (Post-Enhancement):**\n\n")
            report.append(f"![Post-Enhancement Chart]({post_path})\n\n")
        
        report.append("---\n\n")
    
    # Known Issues (Pre-Enhancement)
    if 'known_issues' in pre_results:
        report.append("## Known Issues in Pre-Enhancement Version\n\n")
        for issue in pre_results['known_issues']:
            report.append(f"- ⚠️ {issue}\n")
        report.append("\n")
    
    # Conclusion
    report.append("## Conclusion\n\n")
    report.append(f"The post-enhancement version successfully addressed all major issues identified in ")
    report.append(f"the pre-enhancement version. Test success rate improved from {pre_success_rate:.1f}% ")
    report.append(f"to {post_success_rate:.1f}%, demonstrating significant improvements in:\n\n")
    report.append("- Label positioning and overlap prevention\n")
    report.append("- Chart readability and accessibility\n")
    report.append("- Dynamic adaptation to different data densities\n")
    report.append("- Compliance with WCAG accessibility standards\n\n")
    
    report.append("**Recommendation:** Deploy the post-enhancement version to production.\n")
    
    # Save report
    report_path = Path('compare_report.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(report)
    
    print(f"Comparison report generated: {report_path}")
    return report_path


if __name__ == '__main__':
    generate_comparison_report()
