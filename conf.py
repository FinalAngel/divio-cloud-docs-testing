# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- sys.path preparation ----------------------------------------------------
#

import os
import sys
sys.path.insert(0, os.path.abspath("."))


#
# -- Project information ------------------------------------------------------
#

project = "Developer Handbook"
full_title = project + " Documentation"
copyright = "2017-2020, Divio"
author = "Divio Technologies AB"
version = "1.0"
release = version

#
# -- General configuration ----------------------------------------------------
#

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "sphinx_inline_tabs",
]

mermaid_version="8.5.2"

#
# -- Options for the theme ----------------------------------------------------
#

html_theme = "furo"
html_theme_options = {
    "show_cloud_banner": False,
    "segment_id": "FT34iqltJg6YdIX5fcyIt5J035FmSAAq",
    "style_external_links": True,
    "navigation_depth": 2,
}
html_theme_options = {
    "sidebar_hide_name": True,
}

#
# -- Options for HTML output --------------------------------------------------
#

html_title = full_title
htmlhelp_basename = "DivioClouddeveloperhandbookdoc"

#
# -- Options for Sphinx -------------------------------------------------------
#

source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "env"]
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

#
# -- Options for latex output -------------------------------------------------
#

latex_engine = "xelatex"
latex_documents = [
    (master_doc, htmlhelp_basename + ".tex", full_title, author, "manual"),
]

latex_elements = {
    "papersize": "a4paper",
    "fontpkg": r"""
        \setmainfont{Nunito}
        \setsansfont{Nunito}
        \newfontfamily\sbfseries{Nunito Bold}
        \newfontfamily\lfseries{Nunito Light}
        \newfontfamily\elfseries{Nunito Light}
    """,
    "fncychap": "",
    "sphinxsetup": r"TitleColor={RGB}{0,187,255}, HeaderFamily=\bfseries",
    "preamble": r"""
        \usepackage[titles]{tocloft}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{0.75cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
        \definecolor{divio}{RGB}{0,187,255}
    """,
}
