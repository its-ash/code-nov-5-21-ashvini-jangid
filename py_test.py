import unittest
from py_task import get_bmi_category_and_risk, calculate_bmi


class TaskTest(unittest.TestCase):
    def test_bmi_category_and_risk_at_20(self):
        self.assertEqual(get_bmi_category_and_risk(20),
                         ("Normal weight", "Low risk"))

    def test_bmi_category_and_risk_at_40(self):
        self.assertEqual(get_bmi_category_and_risk(40),
                         ("Very severely obese", "Very high risk"))

    def test_calculate_bmi(self):
        _test_cases = [
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        ]

        _results_data = [
            {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'BMI': 32.79,
                'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
            {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMI': 23.77,
                'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
            {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMI': 22.5,
                'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
        ]

        for _test_case, _result in zip(_test_cases, _results_data):
            self.assertEqual(calculate_bmi(_test_case), _result)


if __name__ == "__main__":
    unittest.main()
