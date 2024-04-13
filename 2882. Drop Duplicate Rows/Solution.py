import pandas as pd
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # drop_duplicates(): This is a method provided by Pandas DataFrame objects. It's used to remove duplicate rows from the DataFrame.
    # subset='email': This argument instructs the drop_duplicates() method to identify and remove duplicate rows based on the 'email' column within the customers DataFrame. In simpler terms, it will only keep rows where the email address is unique.
    return customers.drop_duplicates(subset=['email'])
    
