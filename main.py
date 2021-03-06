import json

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
    with open("blog-data.txt") as data:
        json_data = json.load(data)

    return render_template("index.html", jdata=json_data)




@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form_entry", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("form_entry.html")
    else:
        return render_template("contact.html")

@app.route("/post/<title>")
def post(title):
    with open("blog-data.txt") as data:
        json_data = json.load(data)
        post_data = json_data[int(title) - 1]
    return render_template("post.html", data=post_data)



if __name__ == "__main__":
    app.run(debug=True)

