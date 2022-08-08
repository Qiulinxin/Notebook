# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Notebook'
copyright = '2022, Qiulinxin'
author = 'Qiulinxin'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
# html_theme = 'alabaster'
# html_theme = 'yummy_sphinx_theme'

html_static_path = ['_static']

# 更改侧边栏标题
html_title = "Notebook"

html_theme_options = {
    "sidebar_hide_name": True,
}

html_theme_options = {
    "navigation_with_keys": True,
}