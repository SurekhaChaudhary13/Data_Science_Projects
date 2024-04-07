# Weather Data Analysis using Decision Tree Classification
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data from CSV file
data = pd.read_csv('C:/Surekha/data_weather.csv')

# Data Cleaning
del data['number']  # Remove unnecessary column
data = data.dropna()  # Drop rows with missing values

# Binarize the relative_humidity_3pm column
data['high_humidity_label'] = (data['relative_humidity_3pm'] > 24.99) * 1

# Define features and target variable
features = ['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
            'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
            'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am']

X = data[features].copy()
y = data['high_humidity_label'].copy()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)

# Train a Decision Tree Classifier
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
humidity_classifier.fit(X_train, y_train)

# Predict on the test set
predictions = humidity_classifier.predict(X_test)

# Measure accuracy
accuracy = accuracy_score(y_true=y_test, y_pred=predictions)
print("Accuracy:", accuracy)
