# 点のホームページ

赤黒の色づかいと、手描きの線・貼り紙・小さなメモを合わせた個人サイトです。
PythonのFlaskで動きます。スマートフォンではプロフィールと本文が縦に並びます。

## Windowsで動かす

このフォルダをVS Codeで開き、ターミナルで順番に実行します。

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

ブラウザで http://127.0.0.1:5000/ を開きます。終了はターミナルで `Ctrl+C` です。
`python` が見つからない場合は `py`、または `uv venv` と `uv pip install -r requirements.txt` を使えます。

## 最初に編集する場所

| ファイル | 変えられるもの |
|---|---|
| `content.py` | 名前、自己紹介、制作中のもの、メモ、SNSリンク |
| `static/style.css` | 色、余白、文字の大きさ、手描き風の装飾 |
| `templates/index.html` | 画面の構造 |
| `static/images/profile.png` | プロフィールのイラスト |

たとえば `content.py` の `SOCIAL_LINKS` にある `url` を自分のプロフィールURLにすると、SNSリンクになります。
X・YouTube・TikTokは `fksts10`、GitHubは `zrPointc` を設定しています。
空欄の項目はリンクにせず「準備中」と表示します。
メモやキャラクターはホームページのデザイン案をもとにした初期内容です。自由に差し替えられます。

文章を変更したらPythonをいったん終了して起動し直し、ブラウザを再読み込みしてください。

## 公開版のしくみ

```powershell
.venv\Scripts\python.exe export.py
```

Python / Flaskが作ったページを `dist/` に書き出します。
今回の公開版はそのHTML・CSS・画像を配信する静的サイトです。公開先でPythonが常時動いている構成ではありません。
自分のPCでは `app.py` でFlaskを動かせます。
入力の保存やログインはありません。制作カードは開くと説明が表示されます。

本文はHTMLテンプレート側で自動的にエスケープされます。
Flaskの開発サーバーは自分のPCで確認する用途です。Flask自体をインターネット公開する場合は、Flask対応の運用環境を用意してください。

## 素材

プロフィールのイラストは、このサイト向けに生成したオリジナルの仮キャラクターです。
見出しの手描き風フォントはGoogle FontsのYomogi、本文はZen Maru Gothicを利用します。
読み込めない場合も端末の日本語フォントで表示できます。
