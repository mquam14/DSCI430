import pandas as pd
from toolz import first
from dfply import *

    
parcel_com_cols = pd.read_csv("./data/parcel_common_columns_2004_2014.csv")
common_columns = parcel_com_cols["0"].to_list()

dtypes_dict = {'centroid_lat': str,
               'centroid_long': str}

new_xref = pd.read_csv("./data/new_xref.csv", dtype=dtypes_dict)

lat_long_code_dict = {(lat, long):code for lat, long, code in zip(new_xref.centroid_lat, new_xref.centroid_long, new_xref.Monit_MAP_CODE1)}

lat_long_name_dict = {(lat, long):name for lat, long, name in zip(new_xref.centroid_lat, new_xref.centroid_long, new_xref.lake_name)}

lat_long_dist= {(lat, long):dist for lat, long, dist in zip(new_xref.centroid_lat, new_xref.centroid_long, new_xref.Distance_Parcel_Monitoring_Site_meters)}


ll_set = set((lat, long) for lat, long in zip(new_xref.centroid_lat, new_xref.centroid_long))

     
     
     
     
     
     
     
     