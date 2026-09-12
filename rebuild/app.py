from flask import Flask, render_template
from content import PROFILE, CURRENT_ACTIVITIES, SOCIAL_LINKS
from posts import load_posts
from projects import load_projects

app = Flask(__name__)

@app.get("/")
def home():
    # Pythonの辞書・リストを、画面のテンプレート(HTML？)に渡している。
    return render_template(
        "index.html",
        profile=PROFILE,
        activities=CURRENT_ACTIVITIES,
        projects=load_projects(),
        social_links=SOCIAL_LINKS,
        latest_posts=load_posts()[:3],
    )


if __name__ == "__main__":
    app.run()