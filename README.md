<<<<<<< HEAD
# Order Delay Intelligence System

## Project Overview

This project focuses on predicting delayed e-commerce orders using Machine Learning techniques. The objective is to help businesses identify orders that are likely to be delayed and take proactive actions to improve customer satisfaction and logistics efficiency.

The project utilizes the Olist E-commerce Dataset and implements an end-to-end machine learning workflow including data preprocessing, exploratory data analysis, feature engineering, model building, evaluation, hyperparameter tuning, and model explainability.

---

## Business Problem

Late deliveries negatively impact customer satisfaction, increase support costs, and reduce customer retention.

The goal of this project is to build a predictive model that can identify potentially delayed orders before delivery issues occur.

---

## Project Objectives

* Analyze e-commerce order delivery patterns.
* Identify factors influencing delivery delays.
* Build machine learning models to predict delayed orders.
* Compare model performance.
* Interpret model predictions using SHAP explainability.
* Generate actionable business recommendations.

---

## Dataset

**Dataset:** Olist Brazilian E-Commerce Public Dataset

The dataset contains information about:

* Orders
* Customers
* Products
* Payments
* Delivery dates
* Order status

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* SHAP

### Development Environment

* Jupyter Notebook
* VS Code

---

## Project Workflow

### 1. Data Loading

Multiple datasets were loaded and merged:

* Orders Dataset
* Customers Dataset
* Payments Dataset
* Order Items Dataset
* Products Dataset

---

### 2. Data Cleaning

Performed:

* Missing value handling
* Data type conversion
* Duplicate inspection

---

### 3. Exploratory Data Analysis (EDA)

Analyzed:

* Delivery performance
* Payment behavior
* Monthly order trends
* Delay distribution

Visualizations were created to understand delivery patterns and customer behavior.

---

### 4. Feature Engineering

Created new features including:

* Delivery Days
* Delay Days
* Purchase Month
* Delay Indicator (Target Variable)

Target Variable:

```python
is_delayed
```

* 1 = Delayed Order
* 0 = On-Time Order

---

### 5. Baseline Model

Implemented:

* Logistic Regression

Purpose:

* Establish baseline performance
* Compare with advanced models

---

### 6. Advanced Model

Implemented:

### XGBoost Classifier

Features:

* Pipeline-based workflow
* StandardScaler preprocessing
* Automated feature transformation

Benefits:

* Handles non-linear relationships
* High predictive performance
* Suitable for tabular business data

---

### 7. Cross Validation

Used:

* Stratified K-Fold Cross Validation

Purpose:

* Measure model stability
* Reduce overfitting risk

---

### 8. Hyperparameter Tuning

Used:

* GridSearchCV

Optimized:

* Number of estimators
* Learning rate
* Maximum tree depth

---

### 9. Model Comparison

Models Compared:

1. Logistic Regression
2. XGBoost Classifier

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

Result:

XGBoost outperformed the baseline model and was selected as the final model.

---

### 10. SHAP Explainability

Implemented SHAP (SHapley Additive Explanations) to:

* Interpret model predictions
* Identify important features
* Improve model transparency

Visualizations:

* SHAP Summary Plot
* SHAP Feature Importance Plot

---

## Key Findings

* Delivery-related features strongly influence delay prediction.
* Payment-related features contribute to model performance.
* XGBoost provides superior predictive capability.
* SHAP enables transparent and interpretable predictions.

---

## Business Recommendations

### Early Delay Detection

Use predictive analytics to identify high-risk orders before delays occur.

### Proactive Customer Communication

Notify customers in advance about possible delivery delays.

### Logistics Optimization

Prioritize orders with higher delay risk.

### Continuous Monitoring

Retrain the model regularly using updated order data.

### Operational Dashboard Integration

Deploy the model within business dashboards for real-time decision-making.

---

## Project Outcome

The project successfully developed an intelligent order delay prediction system capable of identifying delayed orders with strong predictive performance and explainable insights.

This solution can help businesses improve delivery efficiency, customer satisfaction, and logistics planning.
=======
<<<<<<< HEAD
# California Housing Price Prediction using Linear Regression

## Project Overview

This project applies Linear Regression to the California Housing Dataset to predict house prices.

The project covers:

- Baseline Linear Regression Model
- Single Feature vs Multi Feature Comparison
- Different Train/Test Split Analysis
- Metric Verification and Exploration

## Dataset

California Housing Dataset

Source:
https://www.kaggle.com/datasets/camnugent/california-housing-prices

## Project Structure
=======
<<<<<<< HEAD
# E-Commerce Sales Performance Analysis

## Project Overview
This project analyzes the Brazilian E-Commerce dataset (Olist) to identify sales trends, customer behavior, payment preferences, seller performance, and business opportunities.

## Objectives
- Analyze sales performance
- Identify top-selling product categories
- Study customer purchasing behavior
- Analyze payment methods
- Evaluate seller performance
- Generate business insights and recommendations

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

ecommerce_sales_eda_project/
│
├── data/
├── Ecommerce_EDA_Project.ipynb
├── images/
├── reports/
├── README.md
└── requirements.txt

## Key Insights
- Top product categories contribute most revenue.
- Customer purchasing patterns reveal business opportunities.
- Payment preferences influence purchasing behavior.
- Sales vary across different regions and time periods.

## Business Recommendations
- Focus on high-performing categories.
- Improve customer retention strategies.
- Support top-performing sellers.
- Use customer feedback to improve service quality.
=======
<<<<<<< HEAD
# AI/ML Crash Course Practice Repository

=======
# Advanced Pandas + Visualization + SQL Assignment

## Project Overview

This project demonstrates data analysis using Pandas, Data Visualization, and SQLite. The project includes data cleaning, grouping, merging, pivot tables, visualizations, SQL queries, and business insights.

---

## Files

### 1. create_dataset.py
Creates sample datasets:
- customers.csv
- products.csv
- orders.csv

### 2. data_audit.py
Performs:
- Shape
- Columns
- Data Types
- Missing Values
- Duplicate Values
- Unique Values

### 3. data_cleaning.py
Performs:
- Data Cleaning
- Remove Duplicates
- Handle Missing Values
- Standardize Column Names

### 4. groupby_analysis.py
Performs:
- Region Wise Sales
- Category Wise Sales
- Segment Wise Sales
- Multi-Level GroupBy

### 5. merge_analysis.py
Performs:
- Merge Tables
- Total Revenue
- Average Order Value
- Top Selling Products

### 6. pivot_table.py
Creates:
- Region vs Month
- Category vs Segment

### 7. visualization.py
Creates:
- Histogram
- Scatter Plot
- Bar Chart
- Line Chart
- Box Plot
- Heatmap

### 8. sqlite_queries.py
Performs:
- SELECT
- WHERE
- GROUP BY
- ORDER BY
- JOIN

### 9. business_insights.py
Generates business insights from the dataset.

### 10. pandas_vs_sql.py
Compares Pandas and SQL outputs.

---

## Libraries Used

- Pandas
- Matplotlib
- SQLite3

---

## Run Commands

```
python create_dataset.py
python data_audit.py
python data_cleaning.py
python groupby_analysis.py
python merge_analysis.py
python pivot_table.py
python visualization.py
python sqlite_queries.py
python business_insights.py
python pandas_vs_sql.py
```

---

## Skills Demonstrated

- Data Cleaning
- Data Analysis
- GroupBy
- Merge
- Pivot Table
- Data Visualization
- SQLite
- Business Insights
- Pandas vs SQL Comparison
>>>>>>> 52b21e434f5559f7c662e796b9117f608f2ac0c5

---

## Author

<<<<<<< HEAD
Khushbu 

Machine Learning & Data Analytics Project
=======
Khushbu
B.Tech Computer Science Student


# AI/ML Crash Course Practice Repository
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7
This repository contains Python practice tasks completed during the AI/ML Crash Course.

---

<<<<<<< HEAD
#Day 5 Tasks

## T1 - Student Report System

### student_report.py

Student report card system using OOP concepts.
=======
# Day 3 Tasks

### intro.py

Basic Python introduction program.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python student_report.py
```

---

## T2 - List Comprehension Drills

### comprehension_drills.py

Practice exercises using list comprehensions.
=======
python intro.py
```

### calculator.py

Performs basic arithmetic operations.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python comprehension_drills.py
```

---

## T3 - File Records

### file_records.py

Reads student records from CSV and generates results.

### students.csv

Sample student records dataset.

### results.csv

Generated results containing averages and grades.
=======
python calculator.py
```

### even_odd.py

Checks whether a number is even or odd.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python file_records.py
```

---

## T4 - Typed Calculator

### typed_calculator.py

Calculator with type hints and docstrings.
=======
python even_odd.py
```

### grade_classifier.py

Classifies grades based on marks.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python typed_calculator.py
```

---

## T5 - Library System

### library_system.py

Library management system using inheritance and method overriding.
=======
python grade_classifier.py
```

### word_frequency.py

Counts the frequency of words in a text.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python library_system.py
```

---

## T6 - JSON Config Manager

### config_manager.py

Save, load and update JSON configuration files.

### config.json

Generated configuration file.
=======
python word_frequency.py
```

### skills_counter.py

Performs counting and analysis on skills data.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python config_manager.py
```

---

## T7 - Pandas Dataset Exploration

### pandas_explore.py

Student dataset analysis using Pandas.
=======
python skills_counter.py
```

### tip_calculator.py

Calculates tip amount and total bill.
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7

Run:

```bash
<<<<<<< HEAD
python pandas_explore.py
```

---

## T8 - Fraction Class

### fraction_class.py

Custom Fraction class using dunder methods.

Run:

```bash
python fraction_class.py
```

---

## T9 - Inventory Management System

### inventory.py

Inventory management system with CSV persistence.

### inventory.csv

Generated inventory data file.

Run:

```bash
python inventory.py
```

---

# Technologies Used

* Python
* Pandas
* CSV Module
* JSON Module
* Object-Oriented Programming (OOP)
* File Handling
* Type Hints

---

# Author

**khushbu**
=======
python tip_calculator.py

AI/ML Training Practice Repository

=======

Project Overview

This repository contains 4 tasks completed during AI/ML training. It focuses on Python basics, data analysis, object-oriented programming, and exploratory data analysis using real-world datasets.

Task 1 - Python Basics

This task focuses on learning basic Python concepts.

Variables and data types
Loops (for, while)
Conditional statements (if-else)
Basic functions
Simple logic building programs
Task 2 - Pandas Data Analysis

This task focuses on data analysis using Pandas library.

DataFrame creation and loading datasets
Data filtering and selection
GroupBy operations
Aggregation functions (mean, sum, count)
Basic data exploration techniques
Task 3 - Object Oriented Programming (OOP)

This task focuses on Python OOP concepts.

Classes and objects
Constructors (init)
Methods and functions inside class
Real-world problem solving using OOP
Code reusability and structure improvement
Task 4 - California Housing EDA

This task focuses on exploratory data analysis using real dataset.

California housing dataset analysis (1990 census data)
Data loading using Pandas
Data cleaning and preprocessing
Statistical summary of dataset
Data visualization using Matplotlib and Seaborn
Analysis of income vs house price
Correlation and pattern identification
Key Learnings
Python programming fundamentals
Data analysis using Pandas
Data visualization techniques
Object-oriented programming concepts
Real-world dataset handling and insights
Author

Khushbu Chauhan
AI/ML Training Program


>>>>>>> d3dbbf77d8e670ebc1ae7dc4b7f82834dd702da8
>>>>>>> 598462c57906eaad3f6766177792b6c2d8b4aad4
>>>>>>> 52b21e434f5559f7c662e796b9117f608f2ac0c5
