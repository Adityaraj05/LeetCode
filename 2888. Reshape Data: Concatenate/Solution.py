import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # for addding vertically we make the axis  = 0 and if need concatenate horizontially make axis = 1
    return pd.concat([df1, df2], axis = 0)
