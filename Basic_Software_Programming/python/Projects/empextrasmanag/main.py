import pandas as pd

# Function to load data
def load_data(employees_file, extras_file):
    employees_df = pd.read_csv(employees_file)
    extras_df = pd.read_csv(extras_file)
    return employees_df, extras_df

# Function to process data
def process_extras(employees_df, extras_df):
    # Check if 'ID' and 'Employee' columns are present
    if 'ID' not in employees_df.columns or 'Employee' not in employees_df.columns:
        raise KeyError("Column 'ID' or 'Employee' not found in employees_df")
    if 'ID' not in extras_df.columns or 'Employee' not in extras_df.columns:
        raise KeyError("Column 'ID' or 'Employee' not found in extras_df")

    # Ensure columns are treated as strings
    employees_df['Employee'] = employees_df['Employee'].astype(str)
    employees_df['ID'] = employees_df['ID'].astype(str)
    extras_df['Employee'] = extras_df['Employee'].astype(str)
    extras_df['ID'] = extras_df['ID'].astype(str)
    
    # Merge dataframes by ID and name
    df = pd.merge(employees_df, extras_df, on=['Employee', 'ID'], how='left')
    
    # Check which extras have been completed (convert string to list)
    df['Completed Extras'] = df['Completed Extras'].apply(lambda x: x.split(',') if pd.notnull(x) else [])
    df['All Extras'] = df['All Extras'].apply(lambda x: x.split(',') if pd.notnull(x) else [])
    
    # Identify pending extras
    df['Pending Extras'] = df.apply(lambda row: list(set(row['All Extras']) - set(row['Completed Extras'])), axis=1)
    
    # Calculate quantity of pending and completed extras
    df['Quantity of Pending Extras'] = df['Pending Extras'].apply(len)
    df['Quantity of Completed Extras'] = df['Completed Extras'].apply(len)
    
    return df

# Function to display results of a specific employee
def display_results(df, key, value):
    employee_df = df[df[key] == value]
    if employee_df.empty:
        print(f"No employee found with {key} = {value}")
    else:
        for index, row in employee_df.iterrows():
            print(f"ID: {row['ID']}")
            print(f"Employee: {row['Employee']}")
            print("\nCompleted Extras:")
            print(f"{', '.join(row['Completed Extras'])}")
            print(f"Quantity of Completed Extras: {row['Quantity of Completed Extras']}")
            print("\nPending Extras to receive:")
            print(f"{', '.join(row['Pending Extras'])}")
            print(f"Quantity of Pending Extras to receive: {row['Quantity of Pending Extras']}")
            print('-' * 50)

# Paths to the CSV files
employees_file = 'employees.csv'
extras_file = 'extras.csv'

# Load the data
employees_df, extras_df = load_data(employees_file, extras_file)

# Check the structure of the loaded dataframes
print("Structure of employees_df:")
print(employees_df.head())
print("\nStructure of extras_df:")
print(extras_df.head())

# Process the data
processed_df = process_extras(employees_df, extras_df)

# Input ID or name to search for information
key = input("Search by ID or name (type 'ID' or 'Employee'): ").strip()
value = input(f"Enter the {key}: ").strip()

# Display results for the specific employee
display_results(processed_df, key, value)
