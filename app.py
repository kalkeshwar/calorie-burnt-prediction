from flask import Flask, render_template, request,session
import pandas as pd
import pickle

app=Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    session.pop('Age', None)
    session.pop('Height', None)
    session.pop('Weight', None)
    session.pop('Duration', None)
    session.pop('Heart_Rate', None)
    session.pop('Body_Temp', None)
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Received form submission")
        pickled_model = pickle.load(open("calorie_model.pkl", "rb"))  # Load the model
        Age = float(request.form['Age'])  # Get user input for age
        Height = float(request.form['Height'])  # Get user input for height
        Weight = float(request.form['Weight'])  # Get user input for weight
        Duration = float(request.form['Duration'])  # Get user input for duration
        GenderInput = request.form['Gender']
        if GenderInput == "Male":
            Gender = 0.0
        else:
            Gender = 1.0
        session['Gender'] = GenderInput  # Store gender in session
        Heart_Rate = float(request.form['Heart_Rate'])  # Get user input for heart rate
        Body_Temp = float(request.form['Body_Temp'])  # Get user input for body temperature

        # Store data in session
        session['Age'] = Age
        session['Height'] = Height
        session['Weight'] = Weight
        session['Heart_Rate'] = Heart_Rate
        session['Body_Temp'] = Body_Temp
        session['Duration'] = Duration

        # Create DataFrame with user input
        input_data = {
            'Gender': [Gender],
            'Age': [Age],
            'Height': [Height],
            'Weight': [Weight],
            'Duration': [Duration],  # Corrected order
            'Heart_Rate': [Heart_Rate],
            'Body_Temp': [Body_Temp]
        }
        input_df = pd.DataFrame(input_data)

        print("Input DataFrame:")
        print(input_df)
        print(request.form)

        # Make prediction using the loaded model
        Prediction = pickled_model.predict(input_df)
        Prediction = round(Prediction[0],2)

        # Return the result to the HTML page as a string
        return render_template('index.html', result=f'{Prediction} Calories')
    except KeyError:
        return render_template('index.html', result='Please fill out all fields')
    except Exception as e:
        return render_template('index.html', result=f'Something went wrong: {str(e)}')

    

if __name__ == '__main__' :
    app.run(debug=True)