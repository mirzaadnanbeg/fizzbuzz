import pandas as pd
import csv
with open('trails.csv') as file:
    csvfile= csv.reader(file)
    for lines in csvfile:
        print(lines[9])