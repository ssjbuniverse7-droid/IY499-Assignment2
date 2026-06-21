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
        try:
            if user.lower() == "done":
                break

            else:
                data.append(float(user))
        except ValueError:
            print("Invalid Input. Please enter numerical data or 'done' to finish.")

    # Step 2: Create A Pandas DataFrame With Appropriate Column Name
    df = pd.DataFrame(data, columns=[colName])

    # Step 3: Save The DataFrame To A CSV File
    df.to_csv("raw_data.csv", index=False)

    # Check if list is empty
    if len(data) == 0:
        print("\nNo data entered.")
    else:
        print("\nData saved to 'raw_data.csv'.")

    return data

def read_data():
    # Step 1: Read The CSV File To A Pandas DataFrame
    try:
        df = pd.read_csv("raw_data.csv")
    except FileNotFoundError:
        print("raw_data.csv was not found. Try entering data first.")
        return None
    except Exception as e:
        print("Error:", e)
        print("Something went wrong. Maybe 'raw_data.csv' is empty?")
        return None

    # Step 2: Display The Data To Verify
    print("Data From CSV File: ")
    print(df)

    # Step 3: Perform Operations On The Numercial Data (Optional)
    print("\nData Statistics: ")
    print(df.describe()) # Provides Descriptive Statistics For Numerical Columns

    return df.iloc[:, 0].tolist()  # Return the column as a list

def group_data(data, class_width):
    if len(data) == 0:
        print("No data available.")
        return None, None, None
    
    min_val, max_val = min(data), max(data)

    bins = np.arange(min_val, max_val + class_width, class_width)
    if bins[-1] < max_val:
        bins = np.append(bins, bins[-1] + class_width)

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

def draw_histogram(grouped_df, class_width):
    plt.bar(
        grouped_df['Midpoint'], 
        grouped_df['Frequency'], 
        width = class_width,  # Increase width to reduce gaps
        color = 'green',  # Change color to green
        edgecolor = 'black', 
        alpha = 0.6
    )
    plt.xlabel("Class Interval")
    plt.ylabel("Frequency")
    plt.title("Histogram of Continuous Numerical Data")
    plt.show()

def compute_statistics(data, grouped_df, frequency, midpoints):
    # Statistics from the original data
    mean = np.mean(data)
    median = np.median(data)
    mode = statistics.multimode(data)
    variance = np.var(data, ddof=1)
    std_dev = np.std(data, ddof=1)
    grouped_mean = np.sum(frequency * np.array(midpoints)) / np.sum(frequency)

    grouped_df["Cumulative Frequency"] = grouped_df["Frequency"].cumsum()

    stats_df = pd.DataFrame({
        "Statistic": [
            "Mean",
            "Grouped Mean",
            "Median",
            "Mode",
            "Variance",
            "Standard Deviation"
        ],
        "Value": [
            mean,
            grouped_mean,
            median,
            ", ".join(map(str, mode)),
            variance,
            std_dev
        ]
    })

    return stats_df

# Main Method
def Main():
    data = None
    grouped_df = None
    stats_df = None
    frequency = None
    midpoints = None

    print("\n***** Data Science Program *****")

    while True:
        print("-----------------------------------------")
        print("Welcome To The Main Menu!")
        print("-----------------------------------------")
        print("1 - Enter Data")
        print("2 - Load Previously Entered Data")
        print("3 - Draw A Histogram")
        print("4 - Calculate Statistics")
        print("5 - Save Results To CSV File")
        print("0 - Exit Program")
        print("-----------------------------------------")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            print("-----------------------------------------")
            data = get_data()

        elif choice == "2":
            print("-----------------------------------------")
            data = read_data()
            if data is not None:
                print("\nData Loaded Successfully.")

        elif choice == "3":
            print("-----------------------------------------")
            if data is None or len(data) == 0:
                print("No data available. Please enter or load data first.")
                continue
            
            else:
                try:
                    class_width = float(input("Enter Class Width: "))

                    if class_width <= 0:
                        print("\nClass Width Must Be Greater Than 0.")
                    else:
                        print("\nGrouping data...\nData grouped.")
                        grouped_df, frequency, midpoints = group_data(data, class_width)
                        print("\nGrouped Frequency Distribution")
                        print(grouped_df)

                        draw_histogram(grouped_df, class_width)

                except ValueError:
                    print("\nInvalid Class Width. PLease enter a valid number.")

        elif choice == "4":
            print("-----------------------------------------")
            if grouped_df is None:
                print("No Grouped Data Available, Please Create A Histogram First.")
                continue
            
            else:
                stats_df = compute_statistics(data, grouped_df, frequency, midpoints)
                print("\nGrouped Data Table:")
                print(grouped_df)
                print("\nStatistics Table:")
                print(stats_df)

        elif choice == "5":
            print("-----------------------------------------")
            if grouped_df is not None:
                canSaveG = True
            else:
                canSaveG = False
            if stats_df is not None:
                canSaveS = True
            else:
                canSaveS = False

            choice = input("What would you like to save?\n1 - Grouped data\n2 - Statistics\n3 - Both\n0 - Cancel\n--> ")
            if choice == "1":
                if canSaveG:
                    grouped_df.to_csv("grouped_data.csv", index= False)
                    print("\nGrouped Data Saved To 'grouped_data.csv'")
                else:
                    print("\nNo data found. Please draw a histogram first.")

            elif choice == "2":
                if canSaveS:
                    stats_df.to_csv("statistics.csv", index= False)
                    print("\nStatistics Saved To 'statistics.csv'")
                else:
                    print("\nNo statistics found. Please calculate statistics first.")

            elif choice == "3":
                if canSaveG and canSaveS:
                    grouped_df.to_csv("grouped_data.csv", index= False)
                    stats_df.to_csv("statistics.csv", index= False)
                    print("\nGrouped data and statistics saved to 'grouped_data.csv' and 'statistics.csv'")
                if canSaveG and not canSaveS:
                    grouped_df.to_csv("grouped_data.csv", index= False)
                    print("\nGrouped Data Saved To 'grouped_data.csv'")
                    print("\nBut no statistics found. Please calculate statistics first.")

            else:
                print("\nSave cancelled.")

        elif choice == "0":
            print("-----------------------------------------")
            print("Have A Good Day!\n")
            break

        else:
            print("-----------------------------------------")
            print("Invalid input. Please choose from the menu.")

# Run Main Method
Main()