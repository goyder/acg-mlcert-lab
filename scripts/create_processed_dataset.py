import pandas as pd
import geopandas as gpd
import os
from os.path import join

# Set our input filepaths
# Should we so desire, we could break this out into an input variable
root_dir = os.path.abspath("..")
data_dir = join(root_dir, "data")
raw_data_dir = join(data_dir, "raw")
processed_data_dir = join(data_dir, "processed")
input_dataset = join(raw_data_dir, "ufo_fullset.csv")
os.makedirs(processed_data_dir, exist_ok=True)

df_ufo = pd.read_csv(input_dataset)

# We now apply our transformations.

# Filter by research outcome
df_ufo = (df_ufo
          .query("researchOutcome in ['probable', 'unexplained']"))

# Map to country and limit to USA
gdf_ufo = gpd.GeoDataFrame(df_ufo,
                           geometry=gpd.points_from_xy(
                               df_ufo.longitude,
                               df_ufo.latitude,
                               crs="EPSG:4326"
                           ))
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries = world[['geometry', 'name']]
gdf_ufo = gpd.sjoin(gdf_ufo, countries, how='inner', op='intersects')
gdf_ufo = (gdf_ufo
           .query("name == 'United States of America'"))

# Remove columns
relevant_columns = ["latitude", "longitude"]
gdf_ufo = gdf_ufo.loc[:, relevant_columns]

# Write to file as .csv
filename = "ufo_locations.csv"
gdf_ufo.to_csv(join(processed_data_dir, filename))
