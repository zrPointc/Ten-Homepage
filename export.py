"""Flaskと同じページを、公開用のHTMLと画像に書き出します。"""

from pathlib import Path
from shutil import copytree
from app import app

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "dist"


def export_site():
    OUTPUT.mkdir(exist_ok=True)
    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise RuntimeError(f"ページの生成に失敗しました: {response.status_code}")
        (OUTPUT / "index.html").write_bytes(response.data)
    copytree(ROOT / "static", OUTPUT / "static", dirs_exist_ok=True)
    print("公開用ページを dist/index.html に書き出しました。")


if __name__ == "__main__":
    export_site()
