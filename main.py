import csv
import pandas as pd
from pandas import DataFrame


def consolidation():
    df = pd.read_csv('mbti.csv',
                     skiprows=1,
                     names=['Types', 'Posts'],)

    # filter from the Dataframe only the rows that contain the 'wanted_string'
    wanted_string = input("Enter an query attribute  ==> ")
    filter_ = df['Posts'].str.contains(wanted_string)
    df1 = df[filter_]  # filtered Dataframe

    df1.to_csv(r"C:\Users\AndrenLuiz\PycharmProjects\20240619_VlookUp\output.csv",
               index=False)


if __name__ == '__main__':
    consolidation()
# call the script using 'python main.py & python vlookup.py output.csv' in the command
# line from the project folder to export the outcome into a csv file
