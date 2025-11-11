class Employee:
    def __init__(self, name: str, email: str):
        self.name = name.strip()
        self.email = email.strip()

    def __repr__(self):
        return f"Employee({self.name}, {self.email})"

    def __eq__(self, other):
        return self.email.lower() == other.email.lower()

    def __hash__(self):
        return hash(self.email.lower())
