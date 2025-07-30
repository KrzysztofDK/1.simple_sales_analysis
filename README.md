# 📊 Simple Sales Analysis

## 🧠 About the Project
This is simple starting project to demonstrate data reading, cleaning, aggregation, EDA and visualization using Python.

## 📁 Dataset
Dataset taken from Kaggle -> https://www.kaggle.com/datasets/kyanyoga/sample-sales-data?resource=download

Sales data for replica toys, cars, ships, trains, etc.

Contains: Order Number, Quantity, Price, Sales, Dates, Status, Customer Info, Address etc.

Originally Written by María Carina Roldán, Pentaho Community Member, BI consultant (Assert Solutions), Argentina. This work is licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License. Modified by Gus Segura June 2014.

## ⚙️ Technologies Used
- Python 3.10
- Jupyter Notebook
- VS Code
- Pandas
- Matplotlib
- Seaborn
- Chardet
- dill

## 🔧 Installation:
pip install -r requirements.txt
## 🔧 Run by:
python main.py

All visualizations will be saved in 'images' folder.

## 🧪 Steps Performed
1. **Data Cleaning**
   - Removed duplicates,
   - Filled Nans,
   - Fixed columns data types (date),
   - Changed columns names,
   - Checked for zero intigers/floats,
   - Removed unnecessary columns.
2. **Feature Engineering**
   - Extracted month and year.
3. **Exploratory Data Analysis**
   - Basic understanding of dataset,
   - Charts were created like histogram, scatter plot, boxplot, correlation heatmap,
   - The questions asked in the analysis were answered.

## 📈 Questions asked in the analysis:
1. Which month had the highest sales?
2. Which productlines sold the best?
3. Which country generated the most revenue?
4. Which customer generates the largest orders and how are they related to the number of products ordered?
5. Is there seasonality in sales?

### Step-by-step analysis with notes and summaries is available in 'notebook/data_analysis.ipynb'.

🧑‍💼 Author: Krzysztof Kopytowski
📎 LinkedIn: https://www.linkedin.com/in/krzysztof-kopytowski-74964516a/
📎 GitHub: https://github.com/KrzysztofDK