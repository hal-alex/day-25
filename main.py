
# data = open("weather_data.csv", "r")
# print(data.readlines())

# data_list = []
#
# with open("weather_data.csv", "r") as data:
#     for weather in data:
#         weather.strip()
#         data_list.append(weather)

# import csv

# with open("weather_data.csv") as data_file:
#     data = iter(csv.reader(data_file))
#     temperatures = []
#     next(data)
#     for row in data:
#         inter_row = int(row[1])
#         temperatures.append(inter_row)
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])