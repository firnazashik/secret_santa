from services.csv_service import CSVService
from services.assignment_service import AssignmentService
from services.validation_service import ValidationService

def main():
    employees = CSVService.read_employees("data/employees_list.csv")
    prev = CSVService.read_previous_assignments("data/last_year_assignments.csv")

    ValidationService.validate_employees(employees)

    service = AssignmentService(employees, prev)
    assignments = service.generate_assignments()

    CSVService.write_assignments(assignments, "output/secret_santa_2025.csv")
    print("✅ Secret Santa assignments generated successfully!")

if __name__ == "__main__":
    main()