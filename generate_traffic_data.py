import csv
import random

# Function to generate random traffic data
def generate_traffic_data(num_intervals):
    traffic_data = []
    for _ in range(num_intervals):
        vehicle_count = random.randint(0, 50)
        average_speed = random.uniform(10, 80)
        traffic_data.append([vehicle_count, average_speed])
    return traffic_data

# Function to save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Vehicle Count', 'Average Speed'])
        csvwriter.writerows(data)

if __name__ == "__main__":
    num_intervals = 100  # Number of time intervals to generate data for
    output_filename = 'traffic_data.csv'  # Name of the output CSV file

    simulated_data = generate_traffic_data(num_intervals)
    save_to_csv(simulated_data, output_filename)
    print(f"Simulated traffic data saved to {output_filename}")
