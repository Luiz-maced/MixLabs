from flask import (
    Flask,
    Response,
    send_file,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    flash,
    session,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("mixlabs.html")

if __name__ == "__main__":
    app.run(debug=True)