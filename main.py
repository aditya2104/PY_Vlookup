import pandas as pd
import numpy as np
import configparser as cp

config = cp.ConfigParser()
config.read("Config.ini")
on = config.get("vlookup","on")
how = config.get("vlookup","how")
file_name = config.get("excel","file_name")
sheet1_name = config.get("excel","sheet1_name")
sheet2_name = config.get("excel","sheet2_name")
                         
df1 = pd.read_excel(file_name,sheet_name= sheet1_name)
df2 = pd.read_excel("student_data.xlsx",sheet_name= sheet2_name)
df_result = pd.merge(df1,
                     df2,
                     on = on,
                     how = how
)
# print(df1)
# print(df2)
print(df_result)