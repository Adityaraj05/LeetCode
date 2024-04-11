import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # head function in Python displays the first five rows of the dataframe by default , but we want we can adjust according to our needs.
    return employees.head(3)
