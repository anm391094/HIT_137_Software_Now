import pandas as pd
import os

# Function to load and combine all the CSV files into a single dataframe
def load_temperature_data(folder_path):
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(file)
        data = pd.concat([data, df], ignore_index=True)
    return data

# Function to assign each month to a season (Dry/Wet for Darwin)
def assign_season(month):
    if month in ['November', 'December', 'January', 'February', 'March', 'April']:
        return 'Wet'  # Wet season from Nov-Apr
    elif month in ['May', 'June', 'July', 'August', 'September', 'October']:
        return 'Dry'  # Dry season from May-Oct

# Function to calculate average temperature for each season
def calculate_seasonal_avg(data):
    print("Calculating seasonal averages for Dry and Wet seasons...")  # Debug statement
    
    # List of months
    month_columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Create a new dataframe to hold seasonal averages across all years
    seasonal_data = []
    
    # Iterate over the month columns and assign each month to a season
    for month in month_columns:
        # Assign season based on the month
        seasonal_data.append({
            'Month': month,
            'Season': assign_season(month),
            'Average Temperature': data[month].mean()  # Calculate average for that month across all years
        })
    
    # Create a new dataframe for the seasonal averages
    seasonal_avg = pd.DataFrame(seasonal_data)
    print("Seasonal averages calculated.")  # Debug statement
    return seasonal_avg

# Function to find the station with the largest temperature range
def find_largest_temp_range(data):
    print("Finding station with the largest temperature range...")  # Debug statement
    month_columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Calculate the temperature range (max - min) for each station across all month columns
    data['Temperature Range'] = data[month_columns].max(axis=1) - data[month_columns].min(axis=1)
    
    # Find the station with the largest temperature range
    largest_range_station = data.loc[data['Temperature Range'].idxmax()]
    print(f"Largest temperature range found at station {largest_range_station['STN_ID']}")  # Debug statement
    return largest_range_station['STN_ID'], largest_range_station['Temperature Range']

# Function to find the warmest and coolest station
def find_warmest_and_coolest_station(data):
    print("Finding warmest and coolest stations...")  # Debug statement
    month_columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Calculate the average temperature for each station across all month columns
    data['Average Temperature'] = data[month_columns].mean(axis=1)
    
    # Find the warmest and coolest station
    warmest_station = data.loc[data['Average Temperature'].idxmax()]
    coolest_station = data.loc[data['Average Temperature'].idxmin()]
    
    print(f"Warmest station: {warmest_station['STN_ID']}, Coolest station: {coolest_station['STN_ID']}")  # Debug statement
    return warmest_station['STN_ID'], warmest_station['Average Temperature'], coolest_station['STN_ID'], coolest_station['Average Temperature']

# Main function to execute the tasks
def main():
    folder_path = '/Users/anmshahariyar/Desktop/Assignment_2_S1_2025/temperature_data'  # Adjust path if needed
    print(f"Using folder: {folder_path}")  # Debug statement
    
    # Load the temperature data from the CSV files
    data = load_temperature_data(folder_path)
    
    if data.empty:
        print("No data loaded. Exiting...")  # Debug statement
        return
    
    # Calculate the average temperature for each season (Dry and Wet)
    seasonal_avg = calculate_seasonal_avg(data)
    seasonal_avg.to_csv('average_temp.txt', index=False)
    print("Average temperature per season saved to 'average_temp.txt'.")
    
    # Find the station with the largest temperature range
    largest_range_station, range_data = find_largest_temp_range(data)
    with open('largest_temp_range_station.txt', 'w') as file:
        file.write(f"Station ID: {largest_range_station}\nTemperature Range: {range_data}")
    print("Largest temperature range station saved to 'largest_temp_range_station.txt'.")
    
    # Find the warmest and coolest station
    warmest_station, warmest_temp, coolest_station, coolest_temp = find_warmest_and_coolest_station(data)
    with open('warmest_and_coolest_station.txt', 'w') as file:
        file.write(f"Warmest Station: {warmest_station} with Avg Temp: {warmest_temp}\n")
        file.write(f"Coolest Station: {coolest_station} with Avg Temp: {coolest_temp}")
    print("Warmest and coolest stations saved to 'warmest_and_coolest_station.txt'.")

if __name__ == "__main__":
    main()
