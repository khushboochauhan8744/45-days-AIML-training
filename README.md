# AI/ML Crash Course Practice Repository

This repository contains Python practice tasks completed during the AI/ML Crash Course.

---

# Day 3 Tasks

### intro.py

Basic Python introduction program.

Run:

```bash
python intro.py
```

### calculator.py

Performs basic arithmetic operations.

Run:

```bash
python calculator.py
```

### even_odd.py

Checks whether a number is even or odd.

Run:

```bash
python even_odd.py
```

### grade_classifier.py

Classifies grades based on marks.

Run:

```bash
python grade_classifier.py
```

### word_frequency.py

Counts the frequency of words in a text.

Run:

```bash
python word_frequency.py
```

### skills_counter.py

Performs counting and analysis on skills data.

Run:

```bash
python skills_counter.py
```

### tip_calculator.py

Calculates tip amount and total bill.

Run:

```bash
python tip_calculator.py
```

---
#Author 
*khushbu*
# Day 7 - 45 Days AIML Training Tasks

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