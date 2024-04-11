import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # To convert any list into dataframe we have a function in pandas called DataFrame
    df = pd.DataFrame(student_data, columns = ['student_id', 'age'])
    return df
