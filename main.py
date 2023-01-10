import unittest
from tests.test_challenge import Challenge_Baufest

if __name__ == "__main__":
    test_cases = [
        Challenge_Baufest,

    ]

    suites = []
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        suites.append(suite)

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suites))
