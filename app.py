from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        user_input = request.form.get("data")
        message = f"You typed: {user_input}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)