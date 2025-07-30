"""Module to generate plots specyfic for 1.simple_analysis_project."""

import os
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from src.exception import CustomException
from src.logger import logging


def run_all_visualizations(df: pd.DataFrame) -> None:
    """Function to visualize data in 1.simple_sales_analysis project.

    Args:
        df (pd.DataFrame): Data to visualize.
    """

    logging.info("Function to run all visualizations has started.")

    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(df["SALES"], bins=50)
        plt.savefig(
            os.path.join("images", "sales_count_histplot.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="QUANTITYORDERED", y="SALES", data=df)
        plt.savefig(
            os.path.join("images", "quanttityordered_scatterplot.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        plt.figure(figsize=(10, 6))
        sns.boxplot(x="DEALSIZE", y="SALES", data=df)
        plt.savefig(
            os.path.join("images", "dealsize_sale_boxplot.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.savefig(
            os.path.join("images", "corr_heatmap.png"), dpi=300, bbox_inches="tight"
        )
        plt.close()

        monthly_sales = df.groupby(["YEAR", "MONTH"])["SALES"].sum().reset_index()
        temp_df = df.drop(["ORDERDATE"], axis=1)
        temp_df = temp_df[temp_df["YEAR_ID"] != "2005"]
        sales_df = temp_df.groupby("MONTH_ID")["SALES"].sum()
        months = range(1, 13)
        formatter = FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))
        plt.figure(figsize=(10, 6))
        plt.bar(months, sales_df)
        plt.xticks(months)
        plt.ylabel("Sales")
        plt.xlabel("Month")
        plt.title("Sales by Month")
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.savefig(
            os.path.join("images", "month_sales_bar.png"), dpi=300, bbox_inches="tight"
        )
        plt.close()

        temp_df = df.drop(["ORDERDATE"], axis=1)
        product_sales_df = temp_df.groupby("PRODUCTLINE")["SALES"].sum()
        product = [prod for prod, df in df.groupby("PRODUCTLINE")]
        formatter = FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))
        plt.figure(figsize=(10, 6))
        plt.bar(product, product_sales_df)
        plt.xticks(product, size=9)
        plt.ylabel("Sales")
        plt.xlabel("Product")
        plt.title("Sales by Productline")
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.savefig(
            os.path.join("images", "productline_sales_bar.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        temp_df = df.drop(["ORDERDATE"], axis=1)
        country_sales_df = (
            temp_df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)
        )
        formatter = FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))
        plt.figure(figsize=(10, 6))
        plt.bar(country_sales_df.index, country_sales_df.values)
        plt.xticks(rotation="vertical")
        plt.ylabel("Sales")
        plt.xlabel("Country")
        plt.title("Sales by Country")
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.savefig(
            os.path.join("images", "country_sales_bar.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        temp_df = df.drop(["ORDERDATE"], axis=1)
        customer_quantity_sales_df = (
            temp_df.groupby("COMPANYNAME")[["SALES", "QUANTITYORDERED"]]
            .sum()
            .sort_values(by="SALES", ascending=False)
        )
        customer_quantity_sales_df = customer_quantity_sales_df.iloc[:15]
        _, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(
            customer_quantity_sales_df.index,
            customer_quantity_sales_df["SALES"],
            color="g",
        )
        ax1.set_xlabel("Customer")
        ax1.set_ylabel("Sales", color="g")
        ax1.tick_params(axis="y", labelcolor="g")
        ax1.tick_params(axis="x", rotation=90)
        ax2 = ax1.twinx()
        ax2.plot(
            customer_quantity_sales_df.index,
            customer_quantity_sales_df["QUANTITYORDERED"],
            "b-o",
        )
        ax2.set_ylabel("Quantity ordered", color="b")
        ax2.tick_params(axis="y", labelcolor="b")
        plt.title("Top 15 Customers: Sales vs Quantity Ordered")
        plt.tight_layout()
        plt.savefig(
            os.path.join("images", "customer_sales_quantity_bar.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

        monthly_sales = df.groupby(["YEAR", "MONTH"])["SALES"].sum().reset_index()
        pivot_df = monthly_sales.pivot(
            index="MONTH", columns="YEAR", values="SALES"
        ).sort_index()
        plt.figure(figsize=(12, 6))
        for year in pivot_df.columns:
            plt.plot(pivot_df.index, pivot_df[year], marker="o", label=str(year))
        plt.title("Sales by Month for Each Year")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.legend(title="Year")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(
            os.path.join("images", "sales_by_month_per_year_plot.png"),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    except Exception as e:
        logging.info("Function to run all visualizations has encountered a problem.")
        raise CustomException(e, sys) from e
