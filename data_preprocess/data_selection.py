import pandas as pd

# Load the Excel file
file_path = './merged_output.csv'
df = pd.read_csv(file_path)

# Ensure necessary columns exist
satisfiable_columns = [col for col in df.columns if 'satisfiable' in col.lower()]
time_columns = [col for col in df.columns if 'time' in col.lower()]

def mark_selection(row):
    # Check if all satisfiable columns are 'unknown'
    if all(str(row[col]).lower() == 'unknown' for col in satisfiable_columns if pd.notnull(row[col])):
        return 'Not Selected'
    # Check if all time columns are less than 10 seconds
    if all(float(row[col]) < 10 for col in time_columns if pd.notnull(row[col])):
        return 'Not Selected'
    return 'Selected'

# Apply the marking function
df['Selection'] = df.apply(mark_selection, axis=1)

# Save the updated DataFrame to a new CSV
output_file_path = './marked_output.csv'
df.to_csv(output_file_path, index=False)

print(f"Processed file saved to {output_file_path}")
