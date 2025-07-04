import os
from scripts import load_csv_with_detected_encoding
from scripts import clean_data
from scripts import agumentation_with_columns
from scripts import run_all_visualizations

def main():
    BASE_DIR = os.path.dirname(__file__)
    data_path = os.path.join(BASE_DIR, "data", "sales_data.csv")

    df = load_csv_with_detected_encoding('data/sales_data.csv')

    df = clean_data(df)

    df = agumentation_with_columns(df)
    
    run_all_visualizations(df)

if __name__ == '__main__':
    main()
