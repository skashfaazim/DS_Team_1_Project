import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# =============================
# LOAD DATA
# =============================
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# =============================
# FEATURE ENGINEERING
# =============================
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
hour_df['season_label'] = hour_df['season'].map(season_map)
day_df['season_label'] = day_df['season'].map(season_map)

weekday_map = {0: 'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
hour_df['weekday_label'] = hour_df['weekday'].map(weekday_map)

weather_map = {
    1: 'Clear / Few Clouds / Partly Cloudy',
    2: 'Mist / Cloudy / Broken Clouds',
    3: 'Light Snow / Light Rain / Thunderstorm',
    4: 'Heavy Rain / Ice Pellets / Snow / Fog'
}
hour_df['weather_label'] = hour_df['weathersit'].map(weather_map)

def classify_day(row):
    if row['holiday'] == 1:
        return 'Holiday'
    elif row['workingday'] == 1:
        return 'Working Day'
    else:
        return 'Weekend'
hour_df['day_category'] = hour_df.apply(classify_day, axis=1)

def peak_flag(hr):
    return 'Peak' if hr in [7,8,9,16,17,18,19] else 'Off-Peak'
hour_df['peak_offpeak'] = hour_df['hr'].apply(peak_flag)

def temp_bin(temp):
    if temp < 0.33:
        return 'Low Temp (<13°C)'
    elif temp < 0.66:
        return 'Moderate Temp (13–27°C)'
    else:
        return 'High Temp (>27°C)'
hour_df['temp_bin'] = hour_df['temp'].apply(temp_bin)
hour_df['hour_label'] = hour_df['hr'].apply(lambda x: f"{x:02d}:00")

weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
hour_order = [f"{h:02d}:00" for h in range(24)]

# =============================
# CREATE FIGURES
# =============================

# Average hourly demand
hourly_all = hour_df.groupby('hr')[['casual','registered']].mean().reset_index()
hourly_all['hour_label'] = hourly_all['hr'].apply(lambda x: f"{x:02d}:00")
hourly_all_melt = hourly_all.melt(id_vars=['hour_label'], value_vars=['casual','registered'],
                                  var_name='user_type', value_name='avg_count')
fig_avg_hour = px.bar(hourly_all_melt, x='hour_label', y='avg_count', color='user_type',
                      barmode='group',
                      color_discrete_sequence=px.colors.qualitative.Set2,
                      title='Average Hourly Demand (Casual vs Registered)')
fig_avg_hour.update_layout(xaxis_tickangle=45)

# Hourly usage by day category
hourly_group_cat = hour_df.groupby(['hr','day_category'])[['casual','registered']].mean().reset_index()
hourly_melt_cat = hourly_group_cat.melt(id_vars=['hr','day_category'],
                                        value_vars=['casual','registered'],
                                        var_name='user_type', value_name='count')
fig_hourly_combined = px.line(hourly_melt_cat, x='hr', y='count', color='day_category',
                              facet_col='user_type', markers=True,
                              title='Hourly Usage by Day Category (Casual & Registered)',
                              labels={'hr':'Hour of Day','count':'Average Count'})

# Seasonal usage
melt_season = day_df.melt(id_vars=['season_label'], value_vars=['casual','registered'],
                          var_name='user_type', value_name='count')
fig_season = px.box(melt_season, x='season_label', y='count', color='user_type',
                    title='Seasonal Usage Variation: Casual vs Registered')

# Temperature bin usage
melt_temp_daycat = hour_df.melt(id_vars=['temp_bin','day_category'],
                                value_vars=['casual','registered'],
                                var_name='user_type', value_name='count')
fig_temp_daycat = px.box(melt_temp_daycat, x='temp_bin', y='count', color='day_category',
                         facet_col='user_type',
                         title='Usage by Temperature Bin and Day Category (Casual & Registered)')
fig_temp_daycat.update_xaxes(tickangle=20)

# Weather impact
weather_group = hour_df.groupby(['weather_label','peak_offpeak'])[['casual','registered']].mean().reset_index()
weather_melt = weather_group.melt(id_vars=['weather_label','peak_offpeak'],
                                  value_vars=['casual','registered'],
                                  var_name='user_type', value_name='count')
fig_weather = px.bar(weather_melt, x='peak_offpeak', y='count', color='weather_label',
                     pattern_shape='user_type', barmode='group',
                     title='Weather Impact on Usage (Peak vs Off-Peak, Pattern=User Type)')

# Heatmaps
heatmap_casual = hour_df.groupby(['weekday_label','hour_label'])['casual'].mean().reset_index()
fig_heat_casual = px.density_heatmap(heatmap_casual, x='hour_label', y='weekday_label', z='casual',
                                     color_continuous_scale='Plasma',
                                     title='Casual Demand (Hour vs Day of Week)',
                                     category_orders={'hour_label': hour_order, 'weekday_label': weekday_order})

heatmap_registered = hour_df.groupby(['weekday_label','hour_label'])['registered'].mean().reset_index()
fig_heat_registered = px.density_heatmap(heatmap_registered, x='hour_label', y='weekday_label', z='registered',
                                         color_continuous_scale='Plasma',
                                         title='Registered Demand (Hour vs Day of Week)',
                                         category_orders={'hour_label': hour_order, 'weekday_label': weekday_order})

# Faceted boxplots
melt_facet = hour_df.melt(id_vars=['season_label','temp_bin','day_category'],
                          value_vars=['casual','registered'],
                          var_name='user_type', value_name='count')
fig_facet = px.box(melt_facet, x='temp_bin', y='count', color='day_category',
                   facet_col='season_label', facet_row='user_type',
                   title='Usage Faceted by Season, Day Category, and User Type')
fig_facet.update_xaxes(tickangle=25)



# =============================
# DASH APP LAYOUT
# =============================
app = Dash(__name__)

app.layout = html.Div([

    html.H3("Average Hourly Demand"),
    dcc.Graph(figure=fig_avg_hour),

    html.H1("Bike Sharing Usage Dashboard", style={'textAlign':'center'}),
    html.Hr(),

    html.H3("Hourly Usage by Day Category"),
    dcc.Graph(figure=fig_hourly_combined),

    html.H3("Seasonal Usage Variation"),
    dcc.Graph(figure=fig_season),

    html.H3("Usage by Temperature Bin and Day Category"),
    dcc.Graph(figure=fig_temp_daycat),

    html.H3("Weather Impact on Usage"),
    dcc.Graph(figure=fig_weather),

    html.H3("Casual Demand (Hour vs Day of Week)"),
    dcc.Graph(figure=fig_heat_casual),

    html.H3("Registered Demand (Hour vs Day of Week)"),
    dcc.Graph(figure=fig_heat_registered),

    html.H3("Usage Faceted by Season, Day Category, and User Type"),
    dcc.Graph(figure=fig_facet)
   
])

# =============================
# RUN SERVER
# =============================
if __name__ == "__main__":
    app.run(debug=True)