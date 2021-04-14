from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        text = request.form.get('username')
        return render_template("login.html",
        output = text,
        user_text = text)

if __name__ == "__main__":
    app.run()
