import pandas as pd
df1 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='2019')
df2 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='1st Quarter')
df3 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='2nd Quarter')
df4 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='3rd Quarter')
df5 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='4th Quarter')
df6 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name = 'Weekdays')
df7 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name ='Weekends')
df8 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name = 'Past 3yrs')
df9 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name = 'Next 3yrs')
df10 = pd.read_excel(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\AbdulJaleel AbdulSamad-Input.xlsx', sheet_name = 'Status')
df1.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\2019.csv')
df2.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\1st Quarter.csv')
df3.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\2nd Quarter.csv')
df4.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\3rd Quarter.csv')
df5.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\4th Quarter.csv')
df6.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\Weekdays.csv')
df7.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\Weekends.csv')
df8.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\Past 3yrs.csv')
df9.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\Next 3yrs.csv')
df10.to_csv(r'C:\Users\Dept of Accounting\Desktop\AAA\.ipynb_checkpoints\Status.csv')