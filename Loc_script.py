#!/usr/bin/env python


import pandas as pd

def max_value_in_each_row(input_file, sheet_name):
    # Read the specific sheet from the Excel file
    df = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

    # Use apply to find the column index with the maximum value for each row
    max_column_indices = df.apply(lambda row: row.idxmax(), axis=1)

    # Extract the corresponding values from the header row
    header_values = df.iloc[0, max_column_indices]

    return header_values

if __name__ == "__main__":
    # Replace 'input_file.xlsx' and 'Sheet1' with your actual file name and sheet name
    input_file = ''
    sheet_name = ''

    result = max_value_in_each_row(input_file, sheet_name)

    # Create a DataFrame with a single row using to_frame() and transpose
    result_df = result.to_frame().T

    # Replace 'output_file.xlsx' with your desired output file name
    output_file = ''

    # Save the result DataFrame to a new Excel file
    result_df.to_excel(output_file, index=False)
