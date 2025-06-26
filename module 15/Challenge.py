import pandas as pd
import matplotlib.pyplot as plt

#getting data from file
my_dataset=pd.read_csv('weather_tokyo_data.csv')
print(my_dataset)
my_dataset["temperature"]=pd.to_numeric(my_dataset["temperature"],errors='coerce')
tempavg=my_dataset.groupby('temperature').mean()
print(tempavg)