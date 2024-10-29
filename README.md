# SkolBlog-Pelican

SkolBlog-Pelican is a custom theme designed for [Pelican](https://getpelican.com/), a static site generator written in Python. This theme is primarily designed for personal use, but others are welcome to use and modify it.

## Features

- Simple and clean design
- Responsive layout (PC and mobile compatible)
- Customizable header and footer
- Archive and category pages
- Tag cloud support

## Installation

1. Clone the repository into your Pelican project's theme directory:

   ```bash
   git clone https://github.com/sakadonohito/skolblog-pelican.git themes/skolblog-pelican
   ```

2. Update your `pelicanconf.py` to use the theme:

   ```python
   THEME = 'themes/skolblog-pelican'
   ```

## Usage

Customize the theme by editing the following files:
- `templates/`: Modify HTML templates for various pages.
- `static/css/`: Customize styles using the `style.css` file.

### Plugin 
pelicanconf.pyに以下を追加してください。
season_pages.pyをpelicanのpluginディレクトリに移す場合はプラグイン用の設定を生かしてそれ以降のコードはコメントアウトしてください。

```pytohn
# pelicanconf.py
SEASONS_SAVE_AS = 'seasons.html'  # 保存先パスを設定
TEMPLATE_PAGES = {
    'seasons.html': 'seasons.html',
    '404.html': '404.html'
}

# プラグインを使えるように設定(pelicanのpluginsディレクトリにコピーして使う場合)
#PLUGIN_PATHS = ['plugins']  # プラグインがあるディレクトリを指定
#PLUGINS = ['season_pages']  # プラグインファイル名（拡張子なし）

# 今回はpluginファイルをテーマに依存するものとしてテーマディレクトリ配下に配置しているので
# 標準設定の代わりに以下のように記述する
# pelicanのpluginsディレクトリにコピーして使う場合は以下のコードはコメントアウトする
import sys
sys.path.append('../themes/skolblog-pelican/plugin')  # プラグインのディレクトリをインポートパスに追加
import season_helper # カスタムプラグインをインポートして機能を有効化
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Author

- [sakadonohito](https://github.com/sakadonohito)

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request with your improvements.
