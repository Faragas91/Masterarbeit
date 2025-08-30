import pandas as pd

wanted_columns = [
    'name_file',
    'zscore',
    'z-score calculated from 7. 8. and 9.',
    'File'
]

df1 = pd.read_csv('D:/Masterarbeit/2.Versuch/Result/Native_Results/ECSFinder/structure_input_sense.csv')
df2 = pd.read_excel('D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_Excel_TEST/native.xlsx')

df2['File'] = df2['File'].str.replace('.txt', '', regex=False)

merge_df = pd.merge(df1, df2, left_on='name_file', right_on='File', how='inner')

print(merge_df.head(10))

filter_data = merge_df[wanted_columns]

filter_data.rename(columns={
    'name_file': 'Martin File',
    'zscore': 'Martin Z-Score ',
    'z-score calculated from 7. 8. and 9.': 'Tanja Z-Score',
    'File': 'Tanja File'}
    , inplace=True
)

filter_data.to_excel("D:/Masterarbeit/2.Versuch/Result/Native_Results/compare_martin_tanja.xlsx", index=False)

print(filter_data.head(10))