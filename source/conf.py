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
    "sidebar_hide_name": False,
}

# 控制使用左右箭头浏览文档
html_theme_options = {
    "navigation_with_keys": True,
}



# 编辑按钮
# 唯一支持的值是"edit"（默认值）和None.
'''
在使用GitHub存储库作为源，
在Read the Docs上生成文档时自动添加。
'''
html_theme_options = {
    "top_of_page_button": None,
}

# 代码块样式
# pygments_style = "sphinx"
# pygments_dark_style = "monokai"