#Utilities Module

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

def get_target(dataframe,target_name):
    TARGET_MAP = {'Pass':'Pass','Fail':'Fail','Distinction':'Pass'}
    df = dataframe.copy()
    df[target_name] = df[target_name].map(TARGET_MAP)
    return df

def categorical_cardinality(dataframe):
    df = dataframe.copy()
    return {col:df[col].nunique() for col in df if df[col].dtype == 'object'}

def categorical_mean(dataframe,categorical,target):
    """Calcula a razao entre a media global do target e a media para cada valor possivel 
    da variavel categorica.
     ---------------------------------------------------------------------------
       Input: Dataframe,lista das variaveis categoricas
     ---------------------------------------------------------------------------
       Output: Um objeto Ipython Display contendo dataframes
    """
    df = dataframe.copy()
    global_mean = df[target].mean()
    for col in categorical:
        df_group = df.groupby(col)[target].agg(['mean'])
        df_group['rate'] = df_group['mean'] / global_mean
        df_group.sort_values("rate",inplace = True,ascending = False)
        display(df_group)
        
def numerical_mean(dataframe,numerical,n_quantiles,target):
    """Calcula a razao entre a media global do target e a media para cada quartil
    da variavel numerica.
     ---------------------------------------------------------------------------
       Input: Dataframe,lista das variaveis numericas
     ---------------------------------------------------------------------------
       Output: Um objeto Ipython Display contendo dataframes"""
    
    df = dataframe.copy()
    global_mean = df[target].mean()
    for col in numerical:
        df_group = df.groupby(pd.Series(pd.qcut(df[col],q = n_quantiles)))[target].agg(['mean'])
        df_group['rate'] = df_group['mean'] / global_mean
        df_group.sort_values("rate",inplace = True,ascending = False)
        display(df_group)


