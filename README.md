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


The team has selected the Bike Sharing dataset by UC Irvine. Our analysis will look at weather factors and time of year to see how these variables affect the types of riders, registered vs. casual. 
1. How do the percentages of casual vs registered depending on the day of week, i.e. workweek vs weekend?
2. do holidays, low windspeed, high temperature increase casual ridership?
3. Given a certain type of weather, how does time of the year or season affect ridership levels? 
4. Does the rate of weather change affect ridership? 
5. What time of the day on weekends vs weekdays, do we see the greatest increase in casual vs. registered ridership?
6. Is there a variance in ridership levels that is caused by outliers? (Are there any errors in data collection from the machine that is tracking the data?) Checking any high spikes, and seeing what possible causes there could be for that spike. 
7. What time of the day on weekends vs weekdays, do we see the greatest increase in casual vs. registered ridership?

We sourced our raw dataset by downloading them from the links below: 
    - https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

## Stakeholders
    - Public Health
    - City Staff
    - Bike Sharing Staff

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
    - Data exploring: (ADD IN REGRESSION HERE) 
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

## Visualizations

## Conclusion
