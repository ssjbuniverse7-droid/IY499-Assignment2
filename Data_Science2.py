'''
Practical
Name: Chinkhuslen Khishignemekh

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

def get_user_data():
    # Step 1: Numerical Data In A List
    data = []

    # Step 2: Create A Pandas DataFrame With Appropriate Column Names
    df = pd.DataFrame(data, columns=["ID", "Weight", "Age"])

    # Step 3: Save The DataFrame To A CSV File
    df.to_csv("Numerical_Output.csv", index= False)

def read_data():
    # Step 1: Read The CSV File To A Pandas DataFrame
    df = pd.read_csv("Numerical_Output.csv")

    # Step 2: Display The Data To Verify
    print("Data From CSV File: ")
    print(df)

    # Step 3: Perform Operations On The Numercial Data (Optional)
    print("\nData Statistics; ")
    print(df.describe()) # Provides Descriptive Statistics For Numerical Columns

def compute_statistics(data, grouped_df, frequency, midpoints):
    hi = 0

def draw_histogram(grouped_df):
    hi = 0

def group_data(data, class_width):
    hi = 0

# Main Method
def Main():
    data = []
    grouped_df = None
    stats_df = None

    while True:
        print("\nMenu")
        print("1 - Get User Data And Write To File")
        print("2 - Read Data From A File")
        print("3 - Draw Histogram By Getting Class Width")
        print("4 - Show Statistics")
        print("5 - Save")
        print("0 - Exit")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            get_user_data()

        elif choice == "2":
            data = read_data()
            print("Data Loaded From File")

        elif choice == "3":
            if not data:
                print("No Data Available. Pleas Load Data First.")
                continue

            class_width = float(input("Enter Class Width: "))
            grouped_df, frequency, midpoints = group_data(data, class_width)
            draw_histogram(grouped_df)

        elif choice == "4":
            if grouped_df is None:
                print("No Grouped Data Available, Please Create A Histogram First.")
                continue
        
            stats_df = compute_statistics(data, grouped_df, frequency, midpoints)
            print("\nGrouped Data Table:")
            print(grouped_df)
            print("\nStatistics Table:")
            print(stats_df)

        elif choice == "5":
            if grouped_df is not None:
                grouped_df.to_csv("Grouped_Data.csv", index= False)
                print("Grouped Data Saved To 'Grouped_Data.csv'")
            if stats_df is not None:
                stats_df.to_csv("Statistics.csv", index= False)
                print("Statistics Saved To 'Statistics.csv'")

        elif choice == "0":
            print("Have A Good Day!")
            break

        else:
            print("Invalid Input, Please Try Again")

# Run Main Method
if __name__ == "__Main__":
    Main()
