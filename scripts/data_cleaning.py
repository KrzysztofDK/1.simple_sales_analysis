import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def check_duplicates(df: pd.DataFrame, column_name: str, max_rows: int = 20) -> pd.DataFrame:
    """
    Check for duplicated values in a specific column and in the whole DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to check.
    - column_name (str): The column in which to check for duplicates.
    - max_rows (int): Number of top duplicate rows to display.

    Returns:
    - pd.DataFrame: DataFrame with duplicated rows based on the given column.
    """
    if column_name not in df.columns:
        raise ValueError(f'Column "{column_name}" not found in DataFrame.')
    
    try:
        column_duplicates = df[df.duplicated(subset=[column_name], keep=False)]
        column_duplicates = column_duplicates.sort_values(by=column_name)
        print(f'Top {max_rows} duplicates by column "{column_name}":')
        if max_rows > 0:
            print(column_duplicates.head(max_rows))

        total_duplicates = df.duplicated(keep='first').sum()
        print(f'Total duplicated rows in the DataFrame: {total_duplicates}')
        
        return column_duplicates
    
    except Exception as e:
        print(f'An error occured while checking duplicates: {e}')
        raise

def handling_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to fill and visualize nulls in simple_sales_analysis project.
    """
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Nulls in dataframe')
    plt.savefig(os.path.join('images', 'isnull.png'), dpi=300, bbox_inches='tight')
    plt.close()
  
    df.fillna(value='Unknown', inplace=True)
    
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Fixed nulls in dataframe')
    plt.savefig(os.path.join('images', 'isnull_fixed.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to clean data in simple_sales_analysis project.
    """
    df = df.copy()
    
    df_duplicated = check_duplicates(df, 'ORDERNUMBER', 0)
    
    df = handling_nulls(df)
    
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce', format='%m/%d/%Y %H:%M')
    invalid_dates = df['ORDERDATE'].isna().sum()
    print(f"[INFO] Unparsable ORDERDATE entries: {invalid_dates}")

    df.rename(columns={
        'MSRP': 'RECOMMENDEDPRICE',
        'CUSTOMERNAME': 'COMPANYNAME',
        'CONTACTLASTNAME': 'LASTNAME',
        'CONTACTFIRSTNAME': 'FIRSTNAME'
    }, inplace=True)

    df.drop(['ORDERLINENUMBER', 'STATUS', 'QTR_ID', 'PHONE', 'ADDRESSLINE1',
             'ADDRESSLINE2', 'STATE', 'POSTALCODE', 'TERRITORY', 'LASTNAME', 'FIRSTNAME'],
             axis=1, inplace=True, errors='raise')

    return df