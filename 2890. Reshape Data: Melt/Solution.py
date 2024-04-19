import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # pd.melt: This is calling the melt function from the Pandas library. The melt function is used to reshape or transform data from wide to long format.report:
  # This is likely a DataFrame in Pandas that contains the data you want to reshape.id_vars=['product']: This parameter specifies which columns should remain as identifier variables (columns that you want to keep as they are) during the melting process.
  # In this case, it's stating that the 'product' column should remain unchanged.var_name='quarter': This parameter sets the name of the new column that will contain the variable names.
  # In this case, it's setting the name of the column that will store the original column names (except for the 'product' column) before they were melted.value_name='sales': 
  # This parameter sets the name of the new column that will contain the values from the columns that are being melted. In this case, it's setting the name of the column that will store the sales data.
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    
