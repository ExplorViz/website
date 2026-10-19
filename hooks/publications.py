"""Generate the publications page from a BibTeX bibliography file."""

from __future__ import annotations

import logging
import re
from pathlib import Path

from citeproc import Citation, CitationItem, CitationStylesBibliography, CitationStylesStyle, formatter
from citeproc.source.bibtex import BibTeX
from pybtex.database import parse_file

log = logging.getLogger("mkdocs.plugins.publications")

MARKER = "<!-- publications:bib -->"
NUMBER_PREFIX = re.compile(r"^\[\d+\]\s*")


def _config_dir(config) -> Path:
    return Path(getattr(config, "config_file_path", None) or ".").resolve().parent


def _entry_year(entry) -> int:
    year = entry.fields.get("year", "0")
    try:
        return int(str(year).strip())
    except ValueError:
        return 0


def _sorted_keys(bib_path: Path) -> list[str]:
    database = parse_file(str(bib_path))
    return sorted(
        database.entries.keys(),
        key=lambda key: (-_entry_year(database.entries[key]), key),
    )


def _formatters():
    return {
        "html": formatter.html,
        "plain": formatter.plain,
        "markdown": formatter.plain,
    }


def _format_entry(
    key: str,
    bib_path: Path,
    csl_path: Path,
    output: str,
    encoding: str,
    database,
) -> str:
    citeproc_style = CitationStylesStyle(str(csl_path), validate=False)
    bib_source = BibTeX(str(bib_path), encoding=encoding)
    bibliography = CitationStylesBibliography(
        citeproc_style,
        bib_source,
        _formatters()[output],
    )
    bibliography.register(Citation([CitationItem(key)]))
    rendered = str(next(iter(bibliography.bibliography())))
    rendered = NUMBER_PREFIX.sub("", rendered)

    url = database.entries[key].fields.get("url")
    if url and url not in rendered:
        if output == "html":
            rendered = f'{rendered} <a href="{url}">{url}</a>'
        else:
            rendered = f"{rendered} {url}"

    return rendered


def _publications_config(config) -> dict | None:
    top_level = config.get("publications") if hasattr(config, "get") else None
    if isinstance(top_level, dict):
        return top_level

    extra = getattr(config, "extra", None)
    if extra is None and hasattr(config, "get"):
        extra = config.get("extra")
    if hasattr(extra, "get"):
        pubs = extra.get("publications")
        if isinstance(pubs, dict):
            return pubs
    return None


def render_publications(config) -> str:
    pubs = _publications_config(config)
    if not pubs:
        raise ValueError("Missing `publications` configuration in mkdocs.yml (under `extra`)")

    root = _config_dir(config)
    bib_path = (root / pubs["bibliography"]).resolve()
    csl_path = (root / pubs["csl"]).resolve()
    encoding = pubs.get("encoding", "utf-8")
    output = pubs.get("output", "html")

    if output not in _formatters():
        raise ValueError(f"Unsupported publications.output: {output!r}")

    if not bib_path.is_file():
        raise FileNotFoundError(f"Bibliography not found: {bib_path}")
    if not csl_path.is_file():
        raise FileNotFoundError(f"CSL style not found: {csl_path}")

    database = parse_file(str(bib_path))
    items = [
        _format_entry(key, bib_path, csl_path, output, encoding, database)
        for key in _sorted_keys(bib_path)
    ]

    if output == "html":
        return "\n".join(f"- {item}" for item in items)
    return "\n".join(f"- {item}" for item in items)


def on_page_markdown(markdown, page, config, files, **kwargs):
    if MARKER not in markdown:
        return markdown

    try:
        body = render_publications(config)
    except Exception as exc:
        log.error("Failed to render publications: %s", exc)
        raise

    return markdown.replace(MARKER, body)
