import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.pyplot import title

my_dataset=pd.read_csv('avgIQpercountry.csv')

my_dataset['Population - 2023']=my_dataset['Population - 2023'].str.replace(',','').astype(float)


fig=px.choropleth(my_dataset,locations="Country",locationmode="country names",hover_data=["Literacy Rate", "Nobel Prices"],
                    color="Continent", projection="natural earth" , title="Average IQ by Country",  color_continuous_scale="agsunset")

fig.show()