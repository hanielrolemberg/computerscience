# Employee Extras Management System

This project provides a system to manage and track the extras completed and pending for employees. The system loads employee data and their respective extras from CSV files, processes the data, and allows users to query specific employees based on their ID or name.

## Features

- Load employee and extras data from CSV files.
- Merge employee data with their respective extras.
- Identify completed and pending extras for each employee.
- Calculate the quantity of completed and pending extras.
- Display detailed information for a specific employee based on their ID or name.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/employee-extras-management.git
    cd employee-extras-management
    ```

2. Install the required library:
    ```bash
    pip install pandas
    ```

## Usage

1. Prepare your CSV files:
    - `employees.csv` should have the columns: `ID`, `Employee`, `Completed Extras`
    - `extras.csv` should have the columns: `ID`, `Employee`, `All Extras`

    Example `employees.csv`:
    ```csv
    ID,Employee,Completed Extras
    1,John,Extra1,Extra2
    2,Peter,Extra1,Extra3
    3,Mary,Extra2
    ```

    Example `extras.csv`:
    ```csv
    ID,Employee,All Extras
    1,John,Extra1,Extra2,Extra3
    2,Peter,Extra1,Extra2,Extra3
    3,Mary,Extra1,Extra2,Extra3
    ```

2. Run the script:
    ```bash
    python main.py
    ```

3. Follow the prompts to search for an employee by ID or name.

## Example

Here is an example of how to run the script and search for an employee:

```bash
$ python main.py
Structure of employees_df:
   ID Employee Completed Extras
0   1     John     Extra1,Extra2
1   2    Peter     Extra1,Extra3
2   3     Mary            Extra2

Structure of extras_df:
   ID Employee        All Extras
0   1     John  Extra1,Extra2,Extra3
1   2    Peter  Extra1,Extra2,Extra3
2   3     Mary  Extra1,Extra2,Extra3

Search by ID or name (type 'ID' or 'Employee'): ID
Enter the ID: 1
ID: 1
Employee: John

Completed Extras:
Extra1, Extra2
Quantity of Completed Extras: 2

Pending Extras to receive:
Extra3
Quantity of Pending Extras to receive: 1
--------------------------------------------------

```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
