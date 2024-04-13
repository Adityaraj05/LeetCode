import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # drop_duplicates(): This is a method provided by Pandas DataFrame objects. It's used to remove duplicate rows from the DataFrame.
    # subset='email': This argument instructs the drop_duplicates() method to identify and remove duplicate rows based on the 'email' column within the customers DataFrame. In simpler terms, it will only keep rows where the email address is unique.
    # inplace=True: This argument is optional but crucial in this context. By setting inplace=True, the drop_duplicates() method modifies the original customers DataFrame directly, removing the duplicate rows. Without inplace=True, the method would return a new DataFrame containing only the unique rows, but wouldn't alter the original customers variable.
    customers.drop_duplicates(subset = 'email', inplace = True)
    return customers
    
