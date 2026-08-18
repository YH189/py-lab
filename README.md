# BMI Health Risk Calculator

A Python function that calculates Body Mass Index (BMI) from weight and height, then classifies the result into a WHO-standard health risk category.

## What is BMI

BMI is a screening metric that estimates whether a person's weight is healthy relative to their height, calculated as:

    BMI = weight (kg) / height (m)^2

## Features

- Validates that weight and height are numeric values
- Validates that weight and height are greater than zero
- Calculates BMI using the standard formula
- Classifies the result into one of four categories: Underweight, Normal weight, Overweight, Obese

## Usage

```python
from main import calculate_bmi_risk

calculate_bmi_risk(70, 1.75)
# Normal weight
```

## Classification Ranges

| BMI Range     | Category      |
|---------------|---------------|
| Below 18.5    | Underweight   |
| 18.5 - 24.9   | Normal weight |
| 25.0 - 29.9   | Overweight    |
| 30.0 and up   | Obese         |

## Running

    python main.py

## Notes

BMI is a general screening tool and does not account for factors such as muscle mass, bone density, or body composition. It should not be used as a sole indicator of health status.
