from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=str(request.form.get('cut')),
            color=str(request.form.get('color')),
            clarity=str(request.form.get('clarity'))
        )

        df = data.get_data_as_dataframe()
        prediction_pipeline = PredictPipeline()
        pred = prediction_pipeline.predict(df)

        final_result = pred[0]

        return render_template('form.html', final_result=f"The price of Diamond is ${final_result}")

    

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)