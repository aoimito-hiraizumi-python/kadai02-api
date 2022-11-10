from flask import Flask, jsonify, render_template, redirect, request
import secrets
import process

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        outfile = request.form["uploadFile"]

        if outfile == "cat":
            out = process.cat()

        elif outfile == "dog":
            out = process.dog()

        else:
            out = process.fox()
            
        return render_template("upload.html", out=out)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
