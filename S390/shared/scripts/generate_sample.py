from Project_A_PreFeature_UI.src.chart_generator import ChartGeneratorPre
from Project_B_PostFeature_UI.src.chart_generator import ChartGeneratorPost

pre = ChartGeneratorPre('Project_A_PreFeature_UI/results')
post = ChartGeneratorPost('Project_B_PostFeature_UI/results')

sample = [5, 6, 7, 3, 9, 10, 8, 7, 11, 2, 9, 10]
pre.draw_bar_chart(sample, labels=[f'P{i}' for i in range(len(sample))], filename='chart_pre_sample.png')
post.draw_bar_chart(sample, labels=[f'P{i}' for i in range(len(sample))], filename='chart_post_sample.png')
print('Generated sample charts in results folders')