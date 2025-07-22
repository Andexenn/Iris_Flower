from flask import Flask, render_template, jsonify, request
import pickle

app = Flask(__name__)

with open('Iris_classification.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == "POST":
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        features = [sepal_length, sepal_width, petal_length, petal_width]
        prediction = model.predict([features])[0]

        return render_template('predict.html', prediction = prediction)
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
