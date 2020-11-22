import pandas as pd

def plot_mean_bar(dataframe,x_col_list,y_col):
    if len(x_col_list) > 1:
        ax = (dataframe
             .groupby(x_col_list)[y_col]
             .mean()
             .unstack()
             .plot(kind = 'barh'))
        _= ax.legend(loc = "best",bbox_to_anchor=(1, 1))
    else:
        ax = (dataframe
             .groupby(x_col_list)[y_col]
             .mean()
             .plot(kind = 'barh'))
    return ax



