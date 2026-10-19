# website

Source code files for ExplorViz's website using `mkdocs`

## Preview

For externally managed Python environments, use the project script (creates `.venv/` automatically):

```bash
./scripts/mkdocs.sh serve
```

Or set up a virtual environment yourself:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

With Docker (installs `requirements.txt` in the container so publication hooks work):

```bash
./scripts/docker-serve.sh
```

## Build

```bash
./scripts/mkdocs.sh build
```

Or, with an activated `.venv` as above:

```bash
mkdocs build
```

```bash
./scripts/docker-build.sh
```

## Publications

Publications on the [Publications](src/4-publications.md) page are generated at build time from the BibTeX file `bibliography/explorviz.bib`. Entries are sorted with the newest year first.

Reference formatting is controlled in `mkdocs.yml` under `extra.publications`:

- `bibliography`: path to the `.bib` file
- `csl`: path to a [Citation Style Language](https://citationstyles.org/) (`.csl`) file, e.g. `bibliography/styles/ieee.csl`
- `output`: `html` (default) or `plain
