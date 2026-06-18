'''
Practical Programming Assignment
Name: Chinkhuslen Khishignemekh

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

def get_data():
    # Step 1: Collect Numerical Data In A List
    data = []
    colName = input("Enter Column Name For The Data. --> ")
    while True:

        user = input("Enter A Number Or 'Done' To Finish. --> ")


        if user.lower() == "done":
            break

        try:
            data.append(float(user))
        except ValueError:
            print("Invalid Input, Try Again.")

    # Step 2: Create A Pandas DataFrame With Appropriate Column Name
    df = pd.DataFrame(data, columns=[colName])

    # Step 3: Save The DataFrame To A CSV File
    df.to_csv("Numerical_Output.csv", index=False)

    if len(data) == 0:
        print("No data entered.")
    else:
        print("Data saved to 'Numerical_Output.csv'.")

def read_data():
    # Step 1: Read The CSV File To A Pandas DataFrame
    df = pd.read_csv("Numerical_Output.csv")

    # Step 2: Display The Data To Verify
    print("Data From CSV File: ")
    print(df)

    # Step 3: Perform Operations On The Numercial Data (Optional)
    print("\nData Statistics; ")
    print(df.describe()) # Provides Descriptive Statistics For Numerical Columns

    return df.iloc[:, 0].tolist()  # Return the first column as a list

def group_data(data, class_width):
    if len(data) == 0:
        print("No data available.")

    min_val, max_val = min(data), max(data)
    bins = np.arange(min_val, max_val + class_width + 1, class_width)
    frequency, bin_edges = np.histogram(data, bins=bins)
    
    midpoints = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges)-1)]
    freq_times_mid = [frequency[i] * midpoints[i] for i in range(len(frequency))]
    
    grouped_df = pd.DataFrame({
        'Classes': [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range(len(bin_edges)-1)],
        'Frequency': frequency,
        'Midpoint': midpoints,
        'Freq * Mid': freq_times_mid
    })
    
    return grouped_df, frequency, midpoints

def compute_statistics(data, grouped_df, frequency, midpoints):
    mean = np.mean(data)
    median = np.median(data)
    mode = statistics.multimode(data)
    variance = np.var(data)
    std_dev = np.std(data)

    stats_df = pd.DataFrame({
        'Statistic': ['Mean', 'Median', 'Mode', 'Variance', 'Standard Deviation'],
        'Value': [mean, median, mode, variance, std_dev]
    })

    return stats_df

def draw_histogram(grouped_df, class_width):
    plt.bar(
        grouped_df['Midpoint'], 
        grouped_df['Frequency'], 
        width= class_width,  # Increase width to reduce gaps
        color='green',  # Change color to green
        edgecolor='black', 
        alpha=0.6
    )
    plt.xlabel("Midpoint")
    plt.ylabel("Frequency")
    plt.title("Histogram of Grouped Data")
    plt.show()

# Main Method
def Main():
    data = []
    grouped_df = None
    stats_df = None

    print("\n***** Data Science Program *****")

    while True:
        print("\n-----------------------------------------")
        print("Welcome To The Main Menu!")
        print("-----------------------------------------")
        print("1 - Enter Data And Write To A File")
        print("2 - Read Data From A File")
        print("3 - Draw Histogram")
        print("4 - Show Statistics")
        print("5 - Save To CSV File")
        print("0 - Exit")
        print("-----------------------------------------")
        choice = input("Enter Your Choice: \n")

        if choice == "1":
            get_data()

        elif choice == "2":
            data = read_data()
            print("Data Loaded Successfully.")

        elif choice == "3":
            if not data:
                print("No Data Available. Pleas Load Data First.")
                continue

            class_width = float(input("Enter Class Width: "))
            grouped_df, frequency, midpoints = group_data(data, class_width)
            draw_histogram(grouped_df, class_width)

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
            print("Invalid Input, Please Try Again.")

# Run Main Method
Main()
