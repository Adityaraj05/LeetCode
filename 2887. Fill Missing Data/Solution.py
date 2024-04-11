import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # selects the "quantity" column from the DataFrame products. This isolates the column containing quantity values for each product..fillna(0) is a method used to address missing values (represented by NaN in pandas) within the selected column. In this case, it replaces any missing values in the "quantity" column with the number 0.
    products["quantity"] = products["quantity"].fillna(0)
    return products
    
