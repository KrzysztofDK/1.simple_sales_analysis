import pandas as pd

def agumentation_with_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to agument DataFrame with new columns in simple_sales_analysis project.
    """
    df = df.copy()
    df['YEAR'] = df['ORDERDATE'].dt.year
    df['MONTH'] = df['ORDERDATE'].dt.month
    return df