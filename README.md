# DS_Team_1_Project

# Bike Sharing Dataset

Data Science Institute - Cohort 6 - Team 1 Project

As part of the Data Sceince Certificate program at the University of Toronto's Data Science Institute, our capstone project was (INSERT 1 SENTENCE BUSINESS CASE HERE). We chose the "Bike Sharing" dataset to apply our analytical and technical skills to. To complete our final project, we summarized the data, performed exploratory analysis' such as (INSERT CHOSEN REGRESSION MODEL HERE), created visualizations to present actionable insights. This project demonstrated all the skills that we have learned through the certificate program. 


## Members


- Rachel Barber-Pin [rbarberpin](https://github.com/rbarberpin)
- Ana Dubcovsky [anadub](https://github.com/anadub)
- Jonah Chevrier [chevrie4](https://github.com/chevrie4)
- Muhammad Ammar Bin Che Mahzan [AmmarMahzan](https://github.com/AmmarMahzan)
- Syyeda Kashfa Azim [skashfaazim](https://github.com/skashfaazim) 

# Business case


Our team has selected the Bike Sharing dataset and will be investigating “Usage Patterns and Optimization.” By analyzing when and under what conditions demand rises or falls, stakeholders like bike‑sharing companies can improve fleet allocation, municipal governing bodies and planning staff can efficiently organize infrastructure and maintenance, and public health initiatives can be strengthened by encouraging more people to choose cycling as a safe, reliable mode of transport. Stakeholders should note that this dataset is geographically and temporally limited to Washington D.C. and to the years 2011-2012.

These are the research questions that we will be focussing on analysis upon for this project: 
1. How do casual vs. registered ridership patterns vary based on time of day, day of the week and type of day (i.e. weekday, weekend, holiday)?
2. How do weather conditions influence registered vs. casual ridership?

We sourced our raw dataset by downloading them from the links below: 
    - https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset



# Project overview  
  
    - Requirements
    - Exploratory Data Analysis
    - Understanding the Raw Data
    - Data Analysis on Pyton
        - Linear Regression
        - Clustering
    - Data Visualization
    - Conclusion
    - Team Videos


## Requirements


This project uses the following Python libraries
    - Data cleaning: pandas, numpy
    - Data exploring: pandas, scikitlearn
    - Visualization: matplotlib, seaborn, 

## Exploratory Data Analysis

The following libraries: pandas, numpy, matplotlib.pyplot, and seaborn were used to generate an overview of the dataset, revealing (ADD IN TOPICS THAT IT REVEALED HERE). We were also able to determine that there were 17,379 rows and 17 columns in the data, and that there were no missing values in the dataset. Seaborn and MatPlotlib was used to create visualizations such as (ASK ANA FOR TYPES OF GRAPHS) heatmaps, scatter plots, bargraphs, and histograms to highlight relationships and trends in the data.

To explore the dynamic features download the (INSERT FILE NAME) file in our repo. 

## Understanding the Raw Data
Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is publicly available in http://capitalbikeshare.com/system-data.
The original raw data was aggregated on two hourly and daily basis and then extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 


### Schema 

| Column     | Type       | Description                                                                                                                                                 |
|------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| instant    | Integer    | Record index                                                                                                                                                |
| dteday     | Date       | Date                                                                                                                                                        |
| season     | Categorical| 1: winter, 2: spring, 3: summer, 4: fall                                                                                                                     |
| yr         | Categorical| Year (0: 2011, 1: 2012)                                                                                                                                      |
| mnth       | Categorical| Month (1 to 12)                                                                                                                                              |
| hr         | Categorical| Hour (0 to 23)                                                                                                                                               |
| holiday    | Binary     | Whether the day is a holiday (from [DC holiday schedule](http://dchr.dc.gov/page/holiday-schedule))                                                        |
| weekday    | Categorical| Day of the week                                                                                                                                              |
| workingday | Binary     | 1 if the day is neither a weekend nor a holiday, 0 otherwise                                                                                                |
| weathersit | Categorical| 1: Clear, Few clouds, Partly cloudy, Partly cloudy                                                                                                           |
| temp       | Continuous | Normalized temperature in Celsius. Derived via (t - t_min)/(t_max - t_min), t_min = -8, t_max = +39 (only in hourly scale)                                 |
| atemp      | Continuous | Normalized feeling temperature in Celsius. Derived via (t - t_min)/(t_max - t_min), t_min = -16, t_max = +50 (only in hourly scale)                        |
| hum        | Continuous | Normalized humidity. Values are divided by 100 (max)                                                                                                        |
| windspeed  | Continuous | Normalized wind speed. Values are divided by 67 (max)                                                                                                       |
| casual     | Integer    | Count of casual users                                                                                                                                       |
| registered | Integer    | Count of registered users                                                                                                                                   |
| cnt        | Integer    | Count of total rental bikes including both casual and registered                                                                                            |

### Summarizations Found in the Dataset

The following table present key summarizations derived from the Bike Sharing dataset. These summarizations provide a foundational understanding of the dataset's scope, including the number of bikers (registered vs. casual), the time span covered, and the completeness of the data. 

| Question                                   | Analysis                                                  |
|--------------------------------------------|------------------------------------------------------------|
| How many years are in this data set?       | There are two years in this dataset                        |
| What is the time range of this dataset?    | The timeline range for this data is between 2011-01-01 to 2012-12-31 |
| What is the total number of instances in the dataset? | 17379                                          |
| What is the total number of columns?       | 13                                                         |
| How many values are missing?               | There are no missing values                                |


## Data Analysis (Linear Regression, Clustering)

## Model Selection

### Linear Regression with One-Hot Encoding

- **Simplicity and Interpretability:**  
  Linear regression provides clear insights into how each feature affects bike rentals. Using one-hot encoding ensures categorical variables like season and hour are properly represented.

- **Baseline Benchmark:**  
  Serves as a straightforward baseline to understand the main drivers of bike sharing usage.

- **Feature Effect Insights:**  
  Coefficients quantify the impact of each factor (e.g., temperature, working day) on rental counts, helping with business understanding.

### Random Forest Regressor

- **Captures Nonlinear Relationships and Interactions:**  
  Real-world factors often interact in complex ways. Random forests model these nonlinear patterns without manual feature engineering.

- **Improved Accuracy and Robustness:**  
  Ensemble learning reduces overfitting, generally improving prediction quality over linear models.

- **Feature Importance:**  
  Identifies the most influential features driving bike rentals, aiding further analysis.

### Summary

Using both models provides a balance between interpretability and predictive performance:

- The **linear regression model** helps explain *how* different factors influence ridership.
- The **random forest model** captures complex patterns for more accurate predictions.

This dual approach supports both exploratory analysis and practical forecasting needs.

# Summary of Insights from the Models

## 1. Linear Regression with One-Hot Encoding

### What We Did:
- Transformed categorical variables (`season`, `hr`, `workingday`) using one-hot encoding.
- Trained a Linear Regression model on numeric + encoded features.

### What It Tells Us:
- Linearly additive effects: Assumes each feature independently affects bike rentals in a linear way.
- Strong predictors:  
  - Higher temperatures lead to more rentals.  
  - Higher humidity leads to fewer rentals.
- Hourly pattern:  
  Rentals peak during morning and evening commute hours on weekdays.
- Working day effect:  
  Slightly higher rental counts on working days compared to weekends for registered users.
- Limitations:  
  Cannot capture nonlinear trends or interactions (e.g., "hour × weekend").

### Linear Regression: Actual vs Predicted Visualization

![Linear Regression model](Images/Linear_Regression.png)


## Overview

This scatter plot compares the actual bike rental counts (y_test) to the predicted counts (y_pred) from the Linear Regression model. The red dashed diagonal line represents perfect predictions where actual equals predicted. Points clustered closely along this line indicate accurate predictions.

## Insights:

The model captures general trends in rental counts but shows some spread, indicating prediction errors.

At higher rental counts, predictions tend to deviate more, suggesting the model struggles with extreme values.

Overall, this plot confirms that the Linear Regression provides a reasonable baseline but has limitations in capturing complex patterns.

--- 


## 2. Random Forest Regressor

### What We Did:
- Used the same one-hot encoded features.
- Trained a Random Forest model, which can automatically handle nonlinearities and feature interactions.

### What It Tells Us:
- Better predictive accuracy:  
  Higher R² score than the Linear Regression model.
- Captured nonlinear relationships and interactions:  
  For example, how hour effects vary depending on whether it is a working day.
- Important features:  
  - Hour of day (`hr_xx`) is the strongest predictor of rental volume.  
  - Temperature (`temp`, `atemp`) encourages more rentals when warmer.  
  - `workingday` and `season` explain weekly and seasonal patterns.
- Richer insights:  
  - Peak usage during weekday rush hours (registered users).  
  - Midday spikes on weekends (casual users).  
  - Sharp drops in rentals during cold or humid conditions.


### Random Forest: Actual vs Predicted Visualization

![Random Forest Model](Images/Random_Forest.png) 


### Overview

This scatter plot shows actual versus predicted rental counts from the Random Forest model, using green markers. Like the previous plot, the red dashed line represents perfect prediction.

### Insights:

The points are more tightly clustered along the diagonal compared to Linear Regression, indicating better prediction accuracy.

The model handles extreme rental counts more effectively, reducing large prediction errors.

This visualization supports that the Random Forest model captures nonlinear relationships and interactions, resulting in improved performance.

## Overall Insights
Both models provide valuable insights:

- The Linear Regression model helps us understand general trends and directional influences (e.g., temperature increase leads to more rentals).
- The Random Forest model offers a more accurate and nuanced understanding of bike rental behavior, capturing complex interactions between time, weather, and work schedules.

## Visualizations

## Conclusion
