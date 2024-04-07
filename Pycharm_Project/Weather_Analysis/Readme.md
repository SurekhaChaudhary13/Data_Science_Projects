# Weather Data Analysis using Decision Tree Classification

This project aims to analyze weather data using decision tree classification to predict high humidity conditions.

## Overview

In this project, we utilize a decision tree classifier to predict whether there will be high humidity at 3pm based on morning weather conditions. The dataset used for this analysis is provided in the `data_weather.csv` file.


## Dataset

The dataset used for this analysis contains the following columns:

- `air_pressure_9am`: Air pressure at 9am
- `air_temp_9am`: Air temperature at 9am
- `avg_wind_direction_9am`: Average wind direction at 9am
- `avg_wind_speed_9am`: Average wind speed at 9am
- `max_wind_direction_9am`: Maximum wind direction at 9am
- `max_wind_speed_9am`: Maximum wind speed at 9am
- `rain_accumulation_9am`: Rain accumulation at 9am
- `rain_duration_9am`: Rain duration at 9am
- `relative_humidity_9am`: Relative humidity at 9am
- `relative_humidity_3pm`: Relative humidity at 3pm

## Data Cleaning

- Removed the unnecessary `number` column.
- Dropped rows with missing values.
## Model Training

- Used a decision tree classifier with a maximum of 10 leaf nodes.
- Trained the classifier using a portion of the data.

## Evaluation

The accuracy of the model on the test set is measured using the `accuracy_score` metric. The achieved accuracy is printed to the console.

## Conclusion

This project demonstrates how decision tree classification can be utilized for weather data analysis to predict high humidity conditions.
![]()
