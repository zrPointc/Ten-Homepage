"""Python / Flask でホームページを表示する、小さなアプリ。"""

from flask import Flask, render_template
from content import PROFILE, CURRENT_ACTIVITIES, PROJECTS, MEMO_LINES, SOCIAL_LINKS

app = Flask(__name__)


@app.get("/")
def home():
    # Pythonの辞書・リストを、画面のテンプレートに渡しています。
    return render_template(
        "index.html",
        profile=PROFILE,
        activities=CURRENT_ACTIVITIES,
        projects=PROJECTS,
        memo_lines=MEMO_LINES,
        social_links=SOCIAL_LINKS,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
