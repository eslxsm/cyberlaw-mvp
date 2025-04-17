from flask import Flask, render_template, request, redirect, send_file
from fir_generator import generate_fir_pdf
from prompts import generate_ai_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        crime = request.form["crime"]
        user_input = request.form["details"]
        response = generate_ai_response(crime, user_input)
        return render_template("report.html", response=response, crime=crime, user_input=user_input)
    return render_template("report.html", response=None)

@app.route("/fir", methods=["POST"])
def fir():
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "crime": request.form["crime"],
        "details": request.form["details"],
        "legal_advice": request.form["legal_advice"]
    }
    pdf_path = generate_fir_pdf(data)
    return send_file(pdf_path, as_attachment=True)

@app.route("/awareness")
def awareness():
    return render_template("awareness.html")
if __name__ == "__main__":
    app.run(debug=True)

