# Secret Santa Assignment System


Automates Secret Santa assignments while enforcing constraints:
- No self-assignment.
- No repeat assignment from last year (if provided).
- Each participant gives and receives exactly one gift.


## Tech
- Python 3.9+
- pytest (for tests)


## Setup
1. Clone the repo.
2. Create a virtualenv: `python -m venv .venv` and activate it.
3. Install dependencies:


```bash
pip install -r requirements.txt

Place your input CSVs in data/ (use provided samples as guide).

Run the program:

python -m src.main --employees data/employees_sample.csv --prev data/last_year_assignments_sample.csv --output output/secret_santa_output.csv

Run tests:
pytest -q