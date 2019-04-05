import pandas as pd
from toolz import first

    
parcel_com_cols = pd.read_csv("./parcel_common_columns_2004_2014.csv")
common_columns = parcel_com_cols["0"].to_list()


#Part 2
import pandas as pd
from dfply import *
#from more_pyspark import to_pandas
mces_lakes = (pd.read_csv('./MinneMUDAC_raw_files/mces_lakes_1999_2014_update.csv', header = 0, sep = ',', engine= 'python'))

mces_lakes.longitude = mces_lakes.longitude.astype('str')
mces_lakes.latitude = mces_lakes.latitude.astype('str')

lake_info = (mces_lakes
             >> select(X.DNR_ID_Site_Number, X.longitude, X.latitude)
             >> group_by(X.DNR_ID_Site_Number, X.longitude, X.latitude)
             >> filter_by(X.DNR_ID_Site_Number.isin(common_codes))
             >> summarise(cnt = n(X.DNR_ID_Site_Number))
             >> drop(X.cnt)
            )

lat_long_code_dict = {(lat, long):code for lat, long, code in zip(lake_info.latitude, lake_info.longitude, lake_info.DNR_ID_Site_Number)}


lat_long_name_dict = {key:code_name_dict[val] for key, val in lat_long_code_dict.items()}
     
lat_long_dist= {lat_long: code_dist_dict[code] for lat_long, code in lat_long_code_dict.items()}


     
     
     
     
     
     
     
     
     
     
     
     