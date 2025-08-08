from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and scaler
db = joblib.load('model/dbscan_model.joblib')
scaler = joblib.load('model/scaler.joblib')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        life = float(request.form["life"])
        mortality = float(request.form["mortality"])
        gdp = float(request.form["gdp"])
        x = np.array([[life, mortality, gdp]])
        x_scaled = scaler.transform(x)
        cluster = db.fit_predict(x_scaled)[0]
        cluster_label = "Noise (-1)" if cluster == -1 else f"Cluster {cluster}"
        return render_template("index.html", result=cluster_label)
    except Exception as e:
        return render_template("index.html", result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
