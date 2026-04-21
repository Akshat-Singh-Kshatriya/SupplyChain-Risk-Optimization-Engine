import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, RandomizedSearchCV

df = pd.read_csv('ai4i2020.csv')

df['Power'] = df['Torque [Nm]'] * df['Rotational speed [rpm]'] 
df['Temp_Diff'] = df['Process temperature [K]'] - df['Air temperature [K]']
df['Torque_Wear_Interaction'] = df['Torque [Nm]'] * df['Tool wear [min]']

features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 
            'Torque [Nm]', 'Tool wear [min]', 'Temp_Diff', 'Power', 'Torque_Wear_Interaction']

X = df[features]
y = df['Machine failure'] 

# 2. Hyperparameter Optimization & Imbalance Handling.
param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced', 'balanced_subsample'] # Penalizes misclassifying failures
}

# 3. Randomized Search for Efficient Tuning

rf = RandomForestClassifier(random_state=42)
random_search = RandomizedSearchCV(rf, param_distributions=param_dist, n_iter=10, 
                                   cv=5, scoring='f1', random_state=42, n_jobs=-1)
random_search.fit(X, y)

best_model = random_search.best_estimator_

# 4. Execute Robust Stratified Cross-Validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(best_model, X, y, cv=skf, scoring='f1')

print(f"Optimized F1 Scores: {np.round(cv_scores, 4)}")
print(f"Average F1 Score: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores) * 2:.4f})")
print(f"Best Parameters: {random_search.best_params_}")

# 5. Final Training and Export for SQL Ingestion
best_model.fit(X, y)
future_data = X.copy()
future_data['Predicted_Failure'] = best_model.predict(X)
future_data['Failure_Probability'] = best_model.predict_proba(X)[:, 1]

# Exporting optimized results for the Power BI dashboard [cite: 41, 52]
future_data.to_csv('machine_health_predictions_v2.csv', index=False)
