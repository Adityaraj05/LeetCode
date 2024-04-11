import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    #  This line uses the .loc indexer of the DataFrame students to select rows where the value in the 'student_id' column is equal to 101.
    return students.loc[students['student_id'] == 101][['name', 'age']]
