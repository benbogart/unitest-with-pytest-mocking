
def add_col(df, colname, coldata):
    
    coldata = pd.Series(coldata)
    # add a column to a DataFrame
    df[colname] = coldata
    return df