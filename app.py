from flask import Flask, render_template

app = Flask(__name__)

bookmark = [
    {
        "user": "Janusz",
        "url": "faceebok.com",
        "description": "opis"
    },
    {
        "user": "Janusz",
        "url": "krakow.com",
        "description": "opis"
    },
    {"user": "Rychard",
     "url": "google.com",
     "description": "opis"
     }
]

def get_latest_bookmarks(limit):
    return bookmarks[:limit]


@app.route("/")
@app.route("/index2")
def index():
    return render_template("index.html", bookmarks=get_latest_bookmarks(2))


@app.route("/add")
def add():
    return render_template("add.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
