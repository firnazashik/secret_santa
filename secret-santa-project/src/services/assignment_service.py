import random
from models.assignment import Assignment

class AssignmentService:
    def __init__(self, employees, prev_assignments):
        self.employees = employees
        self.prev_assignments = prev_assignments

    def generate_assignments(self):
        givers = self.employees[:]
        receivers = self.employees[:]
        random.shuffle(receivers)

        # Retry until a valid combination found
        for _ in range(1000):
            valid = True
            random.shuffle(receivers)
            pairs = []
            for giver, receiver in zip(givers, receivers):
                if giver == receiver:
                    valid = False
                    break
                if self.prev_assignments.get(giver.email) == receiver.email:
                    valid = False
                    break
                pairs.append(Assignment(giver, receiver))
            if valid:
                return pairs
        raise Exception("Unable to generate valid Secret Santa assignments after many attempts.")
