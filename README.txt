Description:
The first script of this project loads a data source CSV file, whose rows vinculate multiple Myers–Briggs types to their respective posts in the internet. The data tabe has 9000 row and 2 columns.Then, the script uses Pandas Dataframes to filter the types in the first row of the data source based on an input keyword typed in the command line.
The output is condensed CSV file containing in the first row only the types filtered by the query.
The second script loads the output CSV file from the previous script and applies the MapReduce technique to determine the frequency on how each type appears in the 'type' column.

The data source file was downloaded from 'Kaggle' web page.

How to run:
Call the script using 'python main.py & python vlookup.py output.csv' in the command line from the project folder.
Creat a .bat file and save it in the project folder.

Programing Language:
Python

IDE:
Pycharm Community Edition 2024.1.2

Operating System
Windows 10