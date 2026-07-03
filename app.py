from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/insights")
def insights():
    return render_template("insights.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/growth")
def growth():
    return render_template("growth.html")

if __name__ == "__main__":
    app.run(debug=True)
