import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # pivot() is a method provided by Pandas DataFrame objects for reshaping data. It takes several arguments:index='month': This specifies that the 'month' column of the DataFrame will be used as the index of the pivoted DataFrame.
  # Each unique value in the 'month' column will become a row in the resulting DataFrame.columns='city': This specifies that the 'city' column of the DataFrame will be used to create new columns in the pivoted DataFrame. 
  # Each unique value in the 'city' column will become a column in the resulting DataFrame.values='temperature': This specifies that the values to populate the pivoted DataFrame will be taken from the 'temperature' column of the original DataFrame.
  # The result of this operation is a new DataFrame where each row represents a month, each column represents a city, and the cells contain the corresponding temperature values.
    return weather.pivot(index='month', columns='city', values='temperature')
    
