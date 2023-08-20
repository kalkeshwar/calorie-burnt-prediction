# Calories Burnt Prediction

This repository contains code that predicts calories burned based on user input. The prediction model is built using the XGBoost regressor and utilizes user inputs such as gender, age, height, weight, exercise duration, heart rate, and body temperature.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x is installed on your machine.
- Required Python packages are installed. You can install them using the following command:

  ```bash
  pip install flask pandas scikit-learn xgboost
  ```
## Getting Started(Run locally)

#### 1. Clone the repository
```bash
  git clone https://github.com/kalkeshwar/calorie-burnt-prediction.git
```
#### 2. Navigate to working directory
```bash
  cd calories-burnt-prediction
```
#### 3. Install the requirements 
```bash
   pip install flask pandas scikit-learn xgboost
```
#### 4. Run the Flask app
```bash
   python app.py
```
The app will run locally and can be accessed in your web browser at `http://127.0.0.1:5000/`.

## Usage

1. Fill in the required inputs in the form (Gender, Age, Height, Weight, Duration, Heart Rate, Body Temperature).
2. Click the "Calculate" button to predict calorie burn based on your inputs.
3. The estimated calorie burn will be displayed on the page.

## Contributing

Contributions are always welcome!

If you'd like to improve the project or fix any issues, feel free to create a pull request.