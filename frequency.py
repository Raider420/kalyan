import collections
import pandas as pd
def sorting_frequency(x):
    frequency = dict(collections.Counter(x))
    df = pd.DataFrame({" Numbers": frequency.keys(),
                       "Frequency": frequency.values()})
    df_sorted = df.sort_values('Frequency', ascending=False)
    df_sorted.to_csv('ALL TRIO SATURDAY MORNING NUMBERS .csv')
    return df_sorted