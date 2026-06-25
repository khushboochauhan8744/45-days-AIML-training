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

---

## Author

Khushbu 

Machine Learning & Data Analytics Project
