# Linear Regression Project Report

## Dataset

California Housing Dataset

## Task 1: Baseline Model

A Linear Regression model was trained to predict median house values.

Metrics:
- MSE
- RMSE
- MAE
- R²

Actual and predicted values were compared using a visualization.

---

## Task 2: Model Comparison

Two models were created:

Model A:
- Single Feature

Model B:
- Multiple Features

The multi-feature model achieved better performance on all evaluation metrics.

---

## Task 3: Train/Test Split Analysis

The model was evaluated using:

- 80/20 Split
- 70/30 Split
- 60/40 Split

The results showed consistent performance across splits, indicating good model stability.

---

## Task 4: Metric Verification

Metrics were calculated manually and compared with Scikit-Learn outputs.

The values matched exactly.

Additional Metric:
- Median Absolute Error

---

## Large Error Experiment

Three artificial prediction errors were introduced.

Observations:

- MSE increased significantly.
- RMSE increased significantly.
- MAE increased moderately.

Conclusion:

MSE is the most sensitive metric to large prediction errors because it squares the error values.

---

## Final Conclusion

Linear Regression performed effectively on the California Housing Dataset.

The multi-feature model consistently outperformed the single-feature model.

Metric verification confirmed the correctness of evaluation calculations.

MSE was identified as the most sensitive metric for detecting large prediction errors.