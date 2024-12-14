import os
import re
import csv

def process_solver_log(file_path):
    """
    Processes a solver log file to determine satisfiability and solving time.
    :param file_path: Path to the solver log file.
    :return: A dictionary with file name, satisfiability, and solving time.
    """
    satisfiable = None
    solving_time = None

    with open(file_path, 'r') as f:
        for line in f:
            # Look for satisfiability result
            if line.startswith('s '):
                if 'UNSATISFIABLE' in line:
                    satisfiable = "UNSATISFIABLE"
                elif 'SATISFIABLE' in line:
                    satisfiable = "SATISFIABLE"
                else:
                    satisfiable = "UNKNOWN"
            
            # Look for solving time
            if 'process-time' in line or 'total' in line:
                time_match = re.search(r'(\d+\.\d+)\s+seconds', line)
                if time_match:
                    solving_time = float(time_match.group(1))

    return {
        "File": os.path.basename(file_path),
        "Satisfiable": satisfiable,
        "Time (s)": solving_time
    }

def process_all_logs_in_directory(directory, output_csv):
    """
    Processes all files in a directory and saves results to a CSV file.
    :param directory: Directory containing solver log files.
    :param output_csv: Path to the output CSV file.
    """
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing {file_path}...")
            result = process_solver_log(file_path)
            results.append(result)

    # Save results to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ["File", "Satisfiable", "Time (s)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_csv}")

# Example usage
if __name__ == "__main__":
    subdirectory = ["output_standard", "i13", "i14", "i15", "i16", "i17"]
    for i in subdirectory:
        input_directory = "/home/song/ENEE759U/data_preprocess/" + i
        output_csv = "/home/song/ENEE759U/data_preprocess/solver_results_csv/" + i + ".csv"
        process_all_logs_in_directory(input_directory, output_csv)
