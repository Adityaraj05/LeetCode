import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # animals['weight'] > 100: This condition filters the rows of the DataFrame animals to select only those where the value in the 'weight' column is greater than 100. This creates a boolean mask indicating which rows meet this condition.
# animals[...]: This notation is used to filter the DataFrame animals based on the boolean mask created in the previous step. It selects only the rows where the condition animals['weight'] > 100 is True.
# .sort_values('weight', ascending=False): This sorts the filtered DataFrame based on the 'weight' column in descending order (ascending=False). This means that rows with higher weights will appear first.
# [['name']]: This selects only the 'name' column from the sorted DataFrame. The double square brackets [['name']] are used to indicate that we're selecting a column (or columns), and it returns a DataFrame with just that column.
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
    
