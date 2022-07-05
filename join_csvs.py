# importing pandas
import pandas as pd

# merging two csv files
df = pd.concat(
    map(pd.read_csv, ['chunk1_selected.csv', 'chunk2_selected.csv','chunk3_selected.csv','chunk4_selected.csv',
                      'chunk5_selected.csv','chunk6_selected.csv']), ignore_index=True)

df.to_csv('final_dataset_drugs.csv')