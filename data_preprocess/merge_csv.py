import os
import pandas as pd

def merge_csv_files(directory, output_file):
    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the directory.")
        return

    # Initialize an empty DataFrame
    merged_df = pd.DataFrame()

    for file in csv_files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        
        # Merge on the first column
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(
                merged_df, df, on=df.columns[0], how='outer', suffixes=(None, f'_{file.split('.')[0]}')
            )

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV file saved as {output_file}")

# Example usage
directory = "./solver_results_csv"  # Replace with your directory path
output_file = "merged_output.csv"  # Desired output file name
merge_csv_files(directory, output_file)
