import os

from src.logger import logging
from src.components.data_loader import load_csv_with_detected_encoding
from src.components.data_transformation import DataTransformation
from src.plot_generator import run_all_visualizations


def main():
    logging.info("Main program started.")

    BASE_DIR = os.path.dirname(__file__)
    data_path = os.path.join(BASE_DIR, "notebook", "data", "sales_data.csv")

    df = load_csv_with_detected_encoding(data_path)

    transformer = DataTransformation()
    df = transformer.data_transformation_and_save_as_csv(df)

    run_all_visualizations(df)

    logging.info("Main program ended.")


if __name__ == "__main__":
    main()
