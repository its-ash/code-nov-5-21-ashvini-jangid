from json import load as json_load



def get_bmi_category_and_risk(bmi: float) -> tuple:
    if bmi <= 18.4:
        return 'Underweight', 'Malnutrition risk'
    elif bmi <= 24.9:
        return 'Normal weight', 'Low risk'
    elif bmi <= 29.9:
        return 'Overweight', 'Enhanced risk'
    elif bmi <= 34.9:
        return 'Moderately obese', 'Medium risk'
    elif bmi <= 39.9:
        return 'Severely obese', 'High risk'
    return 'Very severely obese', 'Very high risk'


def calculate_bmi(row: dict) -> dict:
    _heightM = row['HeightCm'] / 100
    _BMI = round(row['WeightKg'] / _heightM ** 2, 2)
    _category, _risk = get_bmi_category_and_risk(_BMI)
    return {**row, 'BMI': _BMI, 'BMICategory': _category, 'HealthRisk': _risk}


def process_data(data: list) -> tuple:
    _processed_data = []
    _overweight_count = 0
    for row in data:
        _result = calculate_bmi(row)
        _processed_data.append(_result)
        _overweight_count += 1 if _result['BMICategory'] == 'Overweight' else 0
    return _processed_data, _overweight_count


def read_json(name: str):
    with open(name) as json_file:
        return json_load(json_file)


def save_json(data: list) -> None:
    print('LOG :: data is saved')


if __name__ == "__main__":
    _json_data = read_json('data.json')
    data, overweight_count = process_data(_json_data)
    print("Total Overweight found :", overweight_count)
    save_json(data)
