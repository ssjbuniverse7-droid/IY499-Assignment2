import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

def get_user_data():
    hi = 0

def read_data():
    hi = 0

def compute_statistics(data, grouped_df, frequency, midpoints):
    hi = 0

def draw_histogram(grouped_df):
    hi = 0

def group_data(data, class_width):
    hi = 0

# Main Method
def Main():
    get_user_data()
    data = read_data()

    class_width = float(input("Enter Class Width: "))
    grouped_df, frequency, midpoints = group_data(data, class_width)
    print("\nGrouped Data Table")
    print(grouped_df)
    grouped_df.to_csv('grouped_data.csv', index = False)
    print("Grouped Data Saved To 'grouped_data.csv'")

    statistics_df = compute_statistics(data, grouped_df, frequency, midpoints)
    print("\nStatistics Table: ")
    print(statistics_df)
    statistics_df.to_csv('statistics.csv', index = False)
    print("Statistics Saved To 'statistics.csv'")

    draw_histogram(grouped_df)

# Run Main Method
if __name__ == "__Main__":
    Main()
