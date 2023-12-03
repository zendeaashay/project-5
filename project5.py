import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Assuming merged_df.geojson is the GeoJSON file path
geojson_path = "merged_df.geojson"

# Load GeoJSON data using GeoPandas
gdf = gpd.read_file(geojson_path)

def plot_geographical_heatmap(gdf, column, title):
    # Plot the geographical heat map with neighborhood names for the specified column
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Get the minimum and maximum values for the specified column
    vmin, vmax = gdf[column].min(), gdf[column].max()
    
    gdf.plot(column=column, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, vmin=vmin, vmax=vmax)

    # Annotate each neighborhood with its name
    for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['neighborhood']):
        ax.text(x, y, label, fontsize=6, ha='center', va='center', color='black')

    # Customize the plot
    ax.set_title(f'Boston Neighborhoods: {title}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Show the plot
    st.pyplot(fig)

# List of columns to be plotted
columns_to_plot = [
    'FY2021.AV_mean', 'DiffAV2021_mean', 'PercChangeAV2021_mean', 
    'RecoveryDiffAV_mean', 'RecoveryPercChangeAV_mean', 'GROSS_AREA_mean', 
    'RES_FLOOR_mean', 'LIVING_AREA_mean', 'LAND_VALUE_mean', 
    'BLDG_VALUE_mean', 'TOTAL_VALUE_mean', 'FY2000.AV_mean', 
    'GrowthPercChangeAV_mean', 'CrashPercChangeAV_mean', 'NUM_BLDGS_mean', 
    'LAND_SF_mean', 'YR_BUILT_mean', 'GROSS_TAX_mean', 'Observation_Count'
]

# Dropdown widget
selected_column = st.selectbox('Select Column', columns_to_plot)

# Function to update the plot based on the selected column
plot_geographical_heatmap(gdf, selected_column, selected_column.replace("_mean", "").replace("_", " "))