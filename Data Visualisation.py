import pandas as pd
import seaborn as sns
df1 = pd.read_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\gapminder-FiveYearData.csv')
df2 = df1.pivot_table('lifeExp','continent','year')
print(df2)
sns.heatmap(df2).get_figure().savefig('Seaborn_heatmap.png')
