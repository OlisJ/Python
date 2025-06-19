import pandas as pd

products=["Apples","Bananas","Oranges","Grapes","Pineapples"]
sales=[150,200,180,90,60]

sales_per_products=pd.Series(sales,index=products)
print(sales_per_products)

#grape sales
print(sales_per_products["Grapes"])

best_seller=sales_per_products.idxmax()
print(best_seller)

