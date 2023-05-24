from posts import posts


@posts.route("/")
def post_list():
    return "Hello, blueprint!"