
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

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# max_temp = data["temp"].max()
#
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp * 2 + 30
# print(monday_temp)

#creating dataframe from lists

# data_dict = {
#     "students": ["Amy", "Alex", "Angela"],
#     "scores": [76, 56, 65]
#
# }
#
# data_names = pandas.DataFrame(data_dict)
#
# data_names.to_csv("new_names.csv")

import pandas

task_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_s = len(task_data[task_data["Primary Fur Color"] == "Gray"])
red_s = len(task_data[task_data["Primary Fur Color"] == "Cinnamon"])
black_s = len(task_data[task_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_s, red_s, black_s]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")


