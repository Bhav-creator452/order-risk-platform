# Order Risk Engine

A simple rule-based fraud and risk scoring system built in Python.

## Features

* Rule-based risk scoring
* Object-Oriented Design
* Abstraction using Abstract Base Classes
* Polymorphism through interchangeable risk rules
* Logging support
* Command Line Interface (CLI)

## Risk Rules

* High Amount Rule
* New Customer Rule
* Account Age Rule
* Large Item Count Rule
* Country Mismatch Rule

## Risk Labels

| Score | Label  |
| ----- | ------ |
| 0 - 2 | LOW    |
| 3 - 5 | MEDIUM |
| 6+    | HIGH   |

## Run

```bash
python cli.py json_samples/high_risk_order.json
```

## Sample Files

```text
json_samples/low_risk_order.json
json_samples/medium_risk_order.json
json_samples/high_risk_order.json
```

## Requirements

Python 3.10+

## Project Structure

```text
models.py
rules.py
scorer.py
cli.py
json_samples/
README.md
```
