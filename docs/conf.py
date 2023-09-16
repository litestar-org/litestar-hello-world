"""Sphinx configuration."""
from __future__ import annotations

from functools import partial
from typing import Any

from sphinx.addnodes import document
from sphinx.application import Sphinx

__all__ = ["setup", "update_html_context"]


project = "litestar-hello-world"
copyright = "2023, Litestar-Org"
author = "Litestar-Org"

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "auto_pytabs.sphinx_ext",
    "tools.sphinx_ext",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sqlalchemy": ("https://docs.sqlalchemy.org/en/20/", None),
}


napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {"special-members": "__init__", "show-inheritance": True, "members": True}
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"

nitpicky = True

auto_pytabs_min_version = (3, 8)
auto_pytabs_max_version = (3, 11)
auto_pytabs_compat_mode = True

autosectionlabel_prefix_document = True

suppress_warnings = [
    "autosectionlabel.*",
    "ref.python",  # TODO: remove when https://github.com/sphinx-doc/sphinx/issues/4961 is fixed
]

html_theme = "litestar_sphinx_theme"
html_static_path = ["_static"]
html_js_files = ["versioning.js"]
html_css_files = ["style.css"]
html_show_sourcelink = False
html_title = "Litestar Project Template"


html_theme_options = {
    "use_page_nav": False,
    "github_repo_name": "litestar-hello-world",
    "logo": {
        "link": "https://github.com/litestar-org/litestar-hello-world.git",
    },
    "extra_navbar_items": {
        "Documentation": "index",
        "Community": {
            "Contributing": {
                "description": "Learn how to contribute to the Litestar project",
                "link": "https://docs.litestar.dev/2/contribution-guide.html",
                "icon": "contributing",
            },
            "Code of Conduct": {
                "description": "Review the etiquette for interacting with the Litestar community",
                "link": "https://github.com/litestar-org/.github/blob/main/CODE_OF_CONDUCT.md",
                "icon": "coc",
            },
        },
        "Help": "https://github.com/orgs/litestar-org/discussions",
    },
}


def update_html_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: document,
) -> None:
    context["generate_toctree_html"] = partial(context["generate_toctree_html"], startdepth=0)


def setup(app: Sphinx) -> dict[str, bool]:
    app.setup_extension("litestar_sphinx_theme")
    app.setup_extension("pydata_sphinx_theme")
    app.connect("html-page-context", update_html_context)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
