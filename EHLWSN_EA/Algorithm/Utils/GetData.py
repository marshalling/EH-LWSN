import pandas as pd
import os

'''
Get the renewable energy data set and get the actual energy values received
'''


def multiply_solar(dataset, mul_solar):
    # Create a new array of the same size as the input array
    result = [[0 for _ in range(len(dataset[0]))] for _ in range(len(dataset))]

    # Loop through each element of the input array and multiply by the given multiplier
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            result[i][j] = dataset[i][j] * mul_solar

    return result


def multiply_wind(dataset, mul_wind):
    # Create a new array of the same size as the input array
    result = [[0 for _ in range(len(dataset[0]))] for _ in range(len(dataset))]

    # Loop through each element of the input array and multiply by the given multiplier
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            result[i][j] = dataset[i][j] * dataset[i][j] * dataset[i][j] * mul_wind

    return result


def getData(energy):
    raw_data = []
    raw_dataset = []
    # Get the directory where the current script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Build the relative path of a.xlsx file
    excel_file_path = os.path.join(current_directory, '..\..\Dataset', energy)
    for i in range(6):
        excel_data = pd.read_excel(excel_file_path, sheet_name=(i + 1))
        # Select data in the specified range
        selected_data = excel_data.iloc[:, 2:3].values.flatten()  # 2:3 -> first device
        raw_data.append(selected_data)
    for i in range(6):
        raw_dataset.append(raw_data[i].tolist())
    return raw_dataset


def getData_solar():
    # solar
    multiplier_solar = 0.2 * 0.2
    solar_dataset = multiply_solar(getData("solar_energy.xlsx"), multiplier_solar)
    return solar_dataset


def getData_wind():
    # wind
    multiplier_wind =  1 / 2 * 1.225 * 0.01 * 60
    wind_dataset = multiply_solar(getData("solar_energy.xlsx"), multiplier_wind)
    return wind_dataset
