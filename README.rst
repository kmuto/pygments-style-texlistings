Install
=======

Using PyPI and pip
------------------

::

    $ (sudo) pip install pygments-style-texlistings


Manual
------

::

    $ git clone git://github.com/kmuto/pygments-style-texlistings.git
    $ cd pygments-style-texlistings
    $ (sudo) python setup.py install


Usage example
=============

::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='texlistings').style
    <class 'pygments_style_texlistings.TeXListingsStyle'>

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='vsmarker').style
    <class 'pygments_style_texlistings.VSMarkerStyle'>

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='geditsh').style
    <class 'pygments_style_texlistings.Gedit_sh_Style'>

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='googlecolab').style
    <class 'pygments_style_texlistings.GoogleColabStyle'>


Export the style as CSS
========================

::

    pygmentize -S texlistings -f html > texlistings.css

    pygmentize -S vsmarker -f html > vsmarker.css

    pygmentize -S geditsh -f html > geditsh.css

    pygmentize -S googlecolab -f html > googlecolab.css


Using in LaTeX documents
========================

See the minted package at http://minted.googlecode.com


Extra information
=================

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/


Thanks
------

This package is based upon the pygments-style-github of Hugo Maia Vieira.

.. _pygments-style-github: https://github.com/hugomaiavieira/pygments-style-github
