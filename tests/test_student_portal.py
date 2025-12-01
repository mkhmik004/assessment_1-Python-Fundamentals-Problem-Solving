import unittest

from student_portal import check_student_progress

class TestStudentProgress(unittest.TestCase):

    # ==========================================
    # CATEGORY 1: Basic Failures & Zero
    # ==========================================
    def test_standard_fail(self):
        """Example: A standard failing mark."""
        self.assertEqual(check_student_progress(40), 'Fail')

    # TODO 1: Add a test case for a score of exactly 0. 
    # It should return 'No Submission'.
    
    # TODO 2: Add a test case for a score of 49 (Boundary check).
    # It should still return 'Fail'.


    # ==========================================
    # CATEGORY 2: Passing Logic (Even vs Odd)
    # ==========================================
    def test_pass_even_number(self):
        """Example: A passing mark that is an even number."""
        self.assertEqual(check_student_progress(82), 'Pass - Good')

    # TODO 3: Add a test case for a passing mark that is ODD (e.g. 75).
    # It should return 'Pass - Review Needed'.

    # TODO 4: Add a test case for the number 100 specifically.
    # It should return 'Perfect' (Not 'Pass - Good').


    # ==========================================
    # CATEGORY 3: Error Handling (Invalid Input)
    # ==========================================
    def test_too_high(self):
        """Example: A score that is above the limit."""
        self.assertEqual(check_student_progress(105), 'Invalid Score')

    # TODO 5: Add a test case for a negative number (e.g. -10).
    # It should return 'Invalid Score'.


if __name__ == '__main__':
    unittest.main()