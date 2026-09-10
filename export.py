"""Flaskと同じページを、公開用のHTMLと画像に書き出します。"""

from pathlib import Path
from shutil import copytree, rmtree
from app import app
from posts import load_posts

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "dist"


def export_site():
    if OUTPUT.exists():
        rmtree(OUTPUT)
    OUTPUT.mkdir()
    with app.test_client() as client:
        pages = [("/", OUTPUT / "index.html"), ("/diary/", OUTPUT / "diary" / "index.html")]
        pages.extend(
            (f"/diary/{post['slug']}/", OUTPUT / "diary" / str(post["slug"]) / "index.html")
            for post in load_posts()
        )
        for url, destination in pages:
            response = client.get(url)
            if response.status_code != 200:
                raise RuntimeError(f"{url} の生成に失敗しました: {response.status_code}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(response.data)
    copytree(ROOT / "static", OUTPUT / "static", dirs_exist_ok=True)
    print("公開用ページを dist/index.html に書き出しました。")


if __name__ == "__main__":
    export_site()
