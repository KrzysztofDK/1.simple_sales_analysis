"""Modul to transform data."""

import sys
import os
from dataclasses import dataclass

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.exception import CustomException
from src.logger import logging


def check_duplicates(df: pd.DataFrame, column_name: str, max_rows: int = 20) -> None:
    """
    Check for duplicated values in a specific column and in the whole DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        column_name (str): The column in which to check for duplicates.
        max_rows (int): Default = 20. Number of top duplicate rows to display.

    Returns:
        None
    """

    logging.info("Function to check duplicates has started.")

    try:
        if column_name not in df.columns:
            raise ValueError(
                f"Column '{column_name}' not found in DataFrame. Function has stopped."
            )
        else:
            column_duplicates = df[df.duplicated(subset=[column_name], keep=False)]
            total_duplicates = df.duplicated(keep="first").sum()

            if total_duplicates == 0:
                print("There are no duplicated rows.")

            else:
                print(f"Total duplicated rows in the DataFrame: {total_duplicates}")

            if column_duplicates.empty:
                print(f"There are no duplicates by column '{column_name}'.")

            elif max_rows > 0:
                column_duplicates = column_duplicates.sort_values(by=column_name)
                print(f"Top {max_rows} duplicates by column '{column_name}':")
                print(column_duplicates.head(max_rows))

    except Exception as e:
        logging.info("Function to check duplicates has encountered a problem.")
        raise CustomException(e, sys) from e


def handling_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Function to fill and visualize nulls in simple_sales_analysis project.

    Args:
        df (pd.DataFrame): DataFrame to check and fill nulls.

    Returns:
        pd.DataFrame: Fixed DataFrame.
    """

    logging.info("Function to check and fill nulls has started.")

    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    plt.title("Nulls in dataframe")
    plt.savefig(os.path.join("images", "isnull.png"), dpi=300, bbox_inches="tight")
    plt.close()

    try:
        df.fillna(value="Unknown", inplace=True)

        plt.figure(figsize=(12, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
        plt.title("Fixed nulls in dataframe")
        plt.savefig(
            os.path.join("images", "isnull_fixed.png"), dpi=300, bbox_inches="tight"
        )
        plt.close()

        return df

    except Exception as e:
        logging.info("Function to check and fill nulls has encountered a problem.")
        raise CustomException(e, sys) from e


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Function to clean data in simple_sales_analysis project.

    Args:
        df (pd.DataFrame): DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """

    logging.info("Function to clean data has started.")

    df = df.copy()

    check_duplicates(df, "ORDERNUMBER", max_rows=20)

    df = handling_nulls(df)

    try:
        df["ORDERDATE"] = pd.to_datetime(
            df["ORDERDATE"], errors="coerce", format="%m/%d/%Y %H:%M"
        )
        invalid_dates = df["ORDERDATE"].isna().sum()
        print(f"Unparsable ORDERDATE entries: {invalid_dates}")

        df.rename(
            columns={
                "MSRP": "RECOMMENDEDPRICE",
                "CUSTOMERNAME": "COMPANYNAME",
                "CONTACTLASTNAME": "LASTNAME",
                "CONTACTFIRSTNAME": "FIRSTNAME",
            },
            inplace=True,
        )

        df.drop(
            [
                "ORDERLINENUMBER",
                "STATUS",
                "QTR_ID",
                "PHONE",
                "ADDRESSLINE1",
                "ADDRESSLINE2",
                "STATE",
                "POSTALCODE",
                "TERRITORY",
                "LASTNAME",
                "FIRSTNAME",
            ],
            axis=1,
            inplace=True,
            errors="raise",
        )

        return df

    except Exception as e:
        logging.info("Function to clean data has encountered a problem.")
        raise CustomException(e, sys) from e


def agumentation_with_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Function to agument DataFrame with new columns in simple_sales_analysis project.

    Args:
        df (pd.DataFrame): DataFrame to agument with columns in 1.simple_sales_analysis project.

    Returns:
        pd.DataFrame: DataFrame with agumented columns.
    """

    df = df.copy()
    df["YEAR"] = df["ORDERDATE"].dt.year
    df["MONTH"] = df["ORDERDATE"].dt.month
    return df


@dataclass
class DataTransformationConfig:
    """Config class with paths to files."""

    transformed_data_file_path = os.path.join("artifacts", "transformed_data.csv")


class DataTransformation:
    """Class to data transformation."""

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def data_transformation_and_save_as_csv(self, df: pd.DataFrame) -> pd.DataFrame:
        """Function to initiate data transformation and save as csv.

        Returns:
            pd.DataFrame: Returns trasnformed DataFrame.
        """

        logging.info("Data transformation started.")

        df = clean_data(df)

        df = agumentation_with_columns(df)

        try:
            df.to_csv(
                self.data_transformation_config.transformed_data_file_path, index=False
            )
        except Exception as e:
            logging.info("During DataFrame saving program encountered a problem.")
            raise CustomException(e, sys) from e

        return df
