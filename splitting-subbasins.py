#Watch the video for this script here:
#https://www.youtube.com/watch?v=Dnp-27qmjmY

import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
shapefile_path = 'Subcuencas_CRP_50k_UTM_SAM56.shp'
gdf = gpd.read_file(shapefile_path)

# Print the columns to find the correct one
print(gdf.columns)
#Index(['Subcuenca', 'CODIGO', 'Area_ha', 'geometry'], dtype='object')
# Display the unique attributes to identify subbasins

# Get the unique subbasins
subcuencas = gdf['Subcuenca'].unique()
print(subcuencas)
# Filter the subbasins based on a certain attribute
# Replace 'your_attribute_column' and 'value' accordingly
# Loop through each unique subbasin and create a mask
for subcuenca in subcuencas:
    # Create mask for the current subbasin
    mask = gdf[gdf['Subcuenca'] == subcuenca]
    # Save the mask to a new shapefile
    output_filename = f'subbasin_mask_{subcuenca}.shp'
    mask.to_file(output_filename)
    # Optional: Plot the results
    ax = gdf.plot(color='lightgrey', edgecolor='black', figsize=(10, 10))
    mask.plot(ax=ax, color='red', alpha=0.5)
    plt.title(f'Mask for Subcuenca: {subcuenca}')
    # Save the plot as a PNG file
    plot_filename = f'subbasin_plot_{subcuenca}.png'
    plt.savefig(plot_filename)
    plt.close()  # Close the plot to avoid displaying it multiple times

print("Masks and plots saved for all subbasins.")
