<!-- ...existing code... -->
# Student Portal Processor Assessment 🎓

A small TDD-focused project to practice Python fundamentals and problem solving. You will implement student-related logic and write tests that prove the implementation works.

## Project layout

```
assessment_1/
├── student_portal.py          # Implement the functions (Q1–Q4)
├── tests/
│   └── test_student_portal.py # Write tests for those functions (Q5)
└── README.md                  # This file
```

## Where to start

1. Open `student_portal.py` and read the TODO comments for Questions 1–4.
2. Open `tests/test_student_portal.py` and add / uncomment tests for Question 5.
3. Implement code and tests incrementally using TDD.

## Tasks (high level)

- Q1–Q4: Implement functions in `student_portal.py`.
- Q5: Add unit tests in `tests/test_student_portal.py` to validate the behaviors.

## Running tests

Recommended: use pytest.

1. Install pytest (one-time):
```bash
pip install pytest
```

2. Run all tests:
```bash
pytest
```

Alternative (built-in unittest):
```bash
python3 -m unittest tests/test_student_portal.py
```
(If `python3` is not available, try `python`.)

## TDD workflow (fast)

1. RED — write a failing test in `tests/test_student_portal.py`.
2. GREEN — implement the minimal code in `student_portal.py` to pass the test.
3. REFACTOR — clean up code and tests.
4. Repeat for the next requirement.

## Tips

- Run pytest frequently to get clear, readable failures.
- Keep each test focused on one behavior.
- Commit often with small changes.

"It does not matter how slowly you go as long as you do not stop." Take it one function at a time. Good luck, Deevine!