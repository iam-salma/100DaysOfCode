from flask import Flask, render_template
from datetime import datetime
from post import Post
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def get_all_posts():
    current_yr = datetime.now().strftime("%Y")
    return render_template("index.html", year=current_yr, all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/guess/<name>')
def guess(name):
    agify_response = requests.get(f"https://api.agify.io?name={name}")
    age = agify_response.json()["age"]
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = genderize_response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
