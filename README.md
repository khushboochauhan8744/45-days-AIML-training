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

---

## Author

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
```

---
#Author 
*khushbu*

 Day 7 - 45 Days AIML Training Tasks

Python practice tasks completed on Day 7 of 45-Days AIML Training.

## Task List

### Task 1: Student Profile Card using F-Strings and Type Hints
Creates a formatted student profile card using f-strings and type hints.  
**File:** `student_profile.py`  
**Key Concepts:** f-strings, type hints, dictionaries

### Task 2: Class with Useful Method
Defines a `Learner` class with `__init__` and `get_info()` method.  
**File:** `task2_learner_class.py`  
**Key Concepts:** OOP, classes, methods, f-strings

### Task 3: Filter Columns and Rows from DataFrame
Loads `students.csv`, filters rows where `Department == "AIML"` and `Score > 80`, displays selected columns.  
**File:** `task3_filter_dataframe.py`  
**Key Concepts:** `pd.read_csv()`, boolean indexing, column selection

### Task 4: Clean Missing Values and Inspect Dataset
Creates sample data with missing values, checks `isnull().sum()`, applies `fillna("Unknown")` and `dropna()`.  
**File:** `task4_handle_missing.py`  
**Key Concepts:** `isnull()`, `fillna()`, `dropna()`, data cleaning

### Task 5: JSON Parsing with List Comprehension
Parses JSON string using `json.loads()`, converts skills to uppercase using list comprehension.  
**File:** `task5_json_skills.py`  
**Key Concepts:** `json.loads()`, list comprehension, string methods

### Task 6: Quick Insights with describe() and value_counts()
Loads `students.csv`, uses `describe()` for statistics, `value_counts()` for department frequency, calculates average score.  
**File:** `task6_describe_insights.py`  
**Key Concepts:** `describe()`, `value_counts()`, `mean()`

### Task 7: Build and Inspect NumPy Arrays
Creates arrays using `array()`, `arange()`, `zeros()`, `linspace()`. Inspects `shape`, `dtype`, `ndim`, uses negative indexing and slicing.  
**File:** `task7_numpy_arrays.py`  
**Key Concepts:** NumPy array creation, array properties, slicing

### Task 8: Masking, Broadcasting, and Cosine Similarity
Demonstrates NumPy masking `arr > 10`, broadcasting `arr * 2`, and implements cosine similarity using `np.dot()` and `np.linalg.norm()`.  
**File:** `task8_masking_broadcasting.py`  
**Key Concepts:** Masking, broadcasting, cosine similarity

## Dataset
`students.csv` - Contains student data with columns: `Name`, `Department`, `Score`

## Requirements
```bash
pip install pandas numpy
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7
