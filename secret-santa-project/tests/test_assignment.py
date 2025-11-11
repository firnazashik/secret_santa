import unittest
from models.employee import Employee
from services.assignment_service import AssignmentService

class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com")
        ]
        self.prev = {"alice@example.com": "bob@example.com"}

    def test_no_self_assignment(self):
        service = AssignmentService(self.employees, self.prev)
        assignments = service.generate_assignments()
        for a in assignments:
            self.assertNotEqual(a.giver.email, a.receiver.email)

if __name__ == "__main__":
    unittest.main()