import os
import pandas as pd


folder_path = "C:/Users/ponsekha.kg/Desktop/data processing/"



# Check if the folder exists
if not os.path.exists("C:/Users/ponsekha.kg/Desktop/data processing/"):
    print("Folder not found.")
else:
    
    # Get a list of files in the folder
    files = os.listdir("C:/Users/ponsekha.kg/Desktop/data processing/")
    
    # Check if any CSV files are present
    csv_files = [file for file in files if file.endswith('.csv')]
    if not csv_files:
        print("No CSV files found.")
    else:
        for file in csv_files:

            # Read the CSV file
            csv_path = os.path.join(r'C:/Users/ponsekha.kg/Desktop/data processing/', "employee_details.csv")
            df = pd.read_csv(csv_path)

            # Get salary of employeeId=101
            salary_101 = df[df['employeId'] == 101]['salary'].values
            print(f"Salary of employeId=101: {salary_101[0] if len(salary_101) > 0 else 'Not found'}")
            
            # Get number of employees in each department
            employees_per_department = df['department'].value_counts()
            print("Number of employees in each department:")
            print(employees_per_department)
            
            # Get average salary for each department
            avg_salary_per_department = df.groupby('department')['salary'].mean()
            print("Average salary for each department:")
            print(avg_salary_per_department)
            
            # Add a new column based on age condition
            df['new_column'] = df['age'].apply(lambda x: 0 if x >= 30 else 1)
            
            # Write the modified DataFrame to a new CSV file
            new_csv_path = os.path.join(folder_path, f"modified_{file}")
            df.to_csv(new_csv_path, index=False)
            print(f"Modified DataFrame saved to: {new_csv_path}")
           
            # Convert the DataFrame to JSON and display it
            json_data = df.to_json(orient='records')
            print("DataFrame in JSON format:")
            print(json_data)
