import csv
from models.employee import Employee

class CSVService:
    @staticmethod
    def read_employees(file_path: str) -> list[Employee]:
        employees = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        return employees

    @staticmethod
    def read_previous_assignments(file_path: str) -> dict:
        prev_assignments = {}
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prev_assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        return prev_assignments

    @staticmethod
    def write_assignments(assignments: list, output_file: str):
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                'Employee_Name', 'Employee_EmailID',
                'Secret_Child_Name', 'Secret_Child_EmailID'
            ])
            writer.writeheader()
            for a in assignments:
                writer.writerow({
                    'Employee_Name': a.giver.name,
                    'Employee_EmailID': a.giver.email,
                    'Secret_Child_Name': a.receiver.name,
                    'Secret_Child_EmailID': a.receiver.email
                })