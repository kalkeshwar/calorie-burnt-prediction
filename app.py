from flask import Flask, render_template,request,session
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    session.pop('Age', None)
    session.pop('Height', None)
    session.pop('weight', None)
    session.pop('duration', None)
    session.pop('Heart_rate', None)
    session.pop('Body_temp', None)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    selected_option = request.form.get('Gender')
    if(selected_option == "Male"):
        input1=0.0
        session['Gender']=input1
    else:  
        input1=1.0
        session['Gender']=input1
    
    input2 = float(request.form['Age'])
    session['Age']=input2
    
    input3 = float(request.form['Height'])
    session['Height']=input3
    input4 = float(request.form['weight'])
    session['weight']=input4
    input5 = float(request.form['duration'])
    session['duration']=input5
    input6 = float(request.form['Heart_rate'])
    session['Heart_rate']=input6
    input7 = float(request.form['Body_temp'])
    session['Body_temp']=input7
    
    # loading the data from csv file to a Pandas DataFrame
    calories = pd.read_csv('calories.csv')

    exercise_data = pd.read_csv('exercise.csv')

    calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)

    calories_data.replace({"Gender":{'male':0,'female':1}}, inplace=True)

    X = calories_data.drop(columns=['User_ID','Calories'], axis=1)
    Y = calories_data['Calories']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    # loading the model
    model = XGBRegressor(objective='reg:squarederror')

    # training the model with X_train
    model.fit(X_train, Y_train)

    # Add the inputs from the HTML form to X_test
    X_test.loc[len(X_test)] = [input1, input2,input3,input4,input5,input6,input7]

    test_data_prediction = model.predict(X_test.iloc[-1:])  # Predict only the last row (inputs from HTML)

    result = metrics.mean_absolute_error([Y_test.iloc[-1]], test_data_prediction)  # Calculate MAE for last row

    return render_template('index.html', result=test_data_prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
