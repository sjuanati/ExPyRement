from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0: {"post_id": 0, "title": "Hello, world", "content": "This is my first blog post!"}
}


@app.route("/")
def home():  # function name doesn't matter
    return render_template("home.html", posts=posts)


@app.route("/post/<int:post_id>")  # post_ id will be replaced by an int. Eg: /post/0
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template(
            "404.html", message=f"A post with id {post_id} was not found."
        )
    return render_template("post.html", post=post)


# GET is needed to initially display the form.
# POST is used when submitting the form.
@app.route("/post/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(posts)
        posts[post_id] = {"post_id": post_id, "title": title, "content": content}
        # tells the browser to load the post page
        return redirect(url_for("post", post_id=post_id))
    return render_template("create.html")


# ensure that a certain block of code is only executed when the script is run as a
# standalone file, and not when it's imported as a module into another script
if __name__ == "__main__":
    app.run(debug=True)  # some more info in case of error
