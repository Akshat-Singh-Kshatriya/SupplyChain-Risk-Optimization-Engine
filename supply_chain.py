import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

# 1. Load Data & Engineer Features
df = pd.read_csv('ai4i2020.csv')
df['Temp_Diff'] = df['Process temperature [K]'] - df['Air temperature [K]']

features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Temp_Diff']
X = df[features]
y = df['Machine failure'] 

# 2. Initialize the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 3. Setup Stratified K-Fold Cross Validation
# We use Stratified to ensure the rare machine failures are evenly distributed across all 5 folds
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 4. Execute Cross-Validation
# We use 'f1' scoring instead of 'accuracy'. Accuracy is misleading if failures are rare!
cv_scores = cross_val_score(model, X, y, cv=skf, scoring='f1')

print("=== Cross-Validation Results ===")
print(f"F1 Scores for each fold: {np.round(cv_scores, 4)}")
print(f"Average F1 Score: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores) * 2:.4f})")

# 5. Train Final Model on ALL data to generate the SQL export
model.fit(X, y)
future_data = X.copy()
future_data['Predicted_Failure'] = model.predict(X)
future_data['Failure_Probability'] = model.predict_proba(X)[:, 1]

# Export for PostgreSQL
future_data.to_csv('machine_health_predictions.csv', index=False)
