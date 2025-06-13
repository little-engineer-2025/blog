# My nerd blog


This blog will speak about technical stuff that I play
or try on my personal systems.

## Getting started

**One time task**

- Install dependencies:

  ```sh
  sudo dnf install -y toolbox direnv

  pushd ~
  mkdir opt
  cd opt
  git clone https://github.com/little-engineer-2025/toolbox-sh
  cd toolbox-sh
  ./toolbox.sh install
  popd
  ```

- Clone this repository: `git clone https://github.com/little-engineer-2025/blog.git`
- Create your `.envrc` file.

  ```sh
  echo 'export TOOLBOX="blog-dev"' >> .envrc
  direnv allow
  ```

- Create toolbox: `toolbox.sh create`

**Day to day**

- Enter in the toolbox and activate the virtual environment:

  ```sh
  toolbox.sh enter
  source .venv/bin/activate
  ```

- Keep server running ( listening at http://localhost:8000 )

  ```sh
  make serve
  ```

- Create a new branch for your new article: `git checkout -b my-article`
- Create a new article: `make new-article`
- Edit your new article at: `content/...` and refresh the content
  on your browser.
- When the article looks ready, change `Status: draft` to `Status: published`
- Commit regularly, and reorg your commits before push.
- When everything is done, create your pull request, and after review and merge
  your article is published.

## References

- Main cover photo from: https://c1.wallpaperflare.com/preview/811/367/789/technology-computer-creative-design.jpg
- Photo by form PxHere (Cover photo).
- Favicon generated from: https://favicon.io/

