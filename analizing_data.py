import pandas as pd

car_data = pd.read_csv("vehicles_us.csv")

min_year = car_data['model_year'].min()
max_year = car_data['model_year'].max()
print(min_year)
print(max_year)