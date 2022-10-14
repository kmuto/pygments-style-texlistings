# -*- coding: utf-8 -*-
"""
    texlistings
    ~~~~~~

    Simulated TeX Listings color scheme.
    Simulated Visual Source Code color scheme. (low quality)
    Simulated gedit+sh color scheme. (low quality)
    Simulated Google colab color scheme. (low quality)

    Based upon the pygments-style-github of Hugo Maia Vieira.

    .. _pygments-style-github: https://github.com/hugomaiavieira/pygments-style-github

    :copyright: Copyright 2022 Kenshi Muto
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Literal, Name, \
     Operator, Text


class TeXListingsStyle(Style):
    """
    Simulated TeX listings color scheme.
    """

    default_style = ''

    background_color = '#ffffff'

    styles = {
        #Comment.Multiline:              'italic #157947',
        #Comment.Preproc:                'italic #157947',
        #Comment.Single:                 'italic #157947',
        #Comment.Special:                'italic #157947',
        Comment:                        'italic #157947',
        Error:                          'bg:#e3d2d2 #a61717',
        #Generic.Deleted:                'bg:#ffdddd #000000',
        #Generic.Emph:                   'italic #000000',
        #Generic.Error:                  '#aa0000',
        #Generic.Heading:                '#999999',
        #Generic.Inserted:               'bg:#ddffdd #000000',
        #Generic.Output:                 '#888888',
        #Generic.Prompt:                 '#555555',
        #Generic.Strong:                 'bold',
        #Generic.Subheading:             '#aaaaaa',
        #Generic.Traceback:              '#aa0000',
        #Keyword.Constant:               '#000000',
        #Keyword.Declaration:            '#000000',
        Keyword.Namespace:              '#ec008c',
        #Keyword.Pseudo:                 '#000000',
        #Keyword.Reserved:               '#000000',
        #Keyword.Type:                   '#000000',
        #Keyword:                        '#ec008c',
        #Literal.Number.Float:           '#009999',
        #Literal.Number.Hex:             '#009999',
        #Literal.Number.Integer.Long:    '#009999',
        #Literal.Number.Integer:         '#009999',
        #Literal.Number.Oct:             '#009999',
        #Literal.Number:                 '#009999',
        #Literal.String.Backtick:        '#d14',
        #Literal.String.Char:            '#d14',
        #Literal.String.Doc:             '#d14',
        Literal.String.Double:          '#0000ff',
        Literal.String.Escape:          '#0000ff',
        #Literal.String.Heredoc:         '#d14',
        Literal.String.Interpol:        '#0000ff',
        #Literal.String.Other:           '#d14',
        #Literal.String.Regex:           '#009926',
        Literal.String.Single:          '#0000ff',
        #Literal.String.Symbol:          '#990073',
        Literal.String:                 '#0000ff',
        #Name.Attribute:                 '#008080',
        Name.Builtin.Pseudo:            '#000000',
        Name.Builtin:                   '#ec008c',
        #Name.Class:                     'bold #445588',
        #Name.Constant:                  '#008080',
        #Name.Decorator:                 'bold #3c5d5d',
        #Name.Entity:                    '#800080',
        #Name.Exception:                 'bold #990000',
        #Name.Function:                  'bold #990000',
        #Name.Label:                     'bold #990000',
        #Name.Namespace:                 '#555555',
        #Name.Tag:                       '#000080',
        #Name.Variable.Class:            '#008080',
        #Name.Variable.Global:           '#008080',
        #Name.Variable.Instance:         '#008080',
        #Name.Variable:                  '#008080',
        Operator.Word:                  '#ec008c',
        #Operator:                       'bold #000000',
        #Text.Whitespace:                '#bbbbbb',
    }

class Gedit_sh_Style(Style):
    """
    Simulated gedit sh color scheme.
    """

    default_style = ''

    background_color = '#ffffff'

    styles = {
        Comment.Hashbang:               'bold #0000ff',
        #Comment.Multiline:              'italic #157947',
        #Comment.Preproc:                'italic #157947',
        #Comment.Single:                 'italic #157947',
        #Comment.Special:                'italic #157947',
        Comment:                        '#1a7bc7',
        #Error:                          'bg:#e3d2d2 #a61717',
        #Generic.Deleted:                '#bf2801',
        #Generic.Emph:                   'italic #000000',
        #Generic.Error:                  '#aa0000',
        #Generic.Heading:                '#999999',
        #Generic.Inserted:               '#53a72f',
        #Generic.Output:                 '#888888',
        #Generic.Prompt:                 '#555555',
        #Generic.Strong:                 'bold',
        #Generic.Subheading:             '#aaaaaa',
        #Generic.Traceback:              '#aa0000',
        #Keyword.Constant:               '#0087b4',
        #Keyword.Declaration:            '#000000',
        #Keyword.Namespace:              '#a9175d',
        #Keyword.Pseudo:                 '#000000',
        #Keyword.Reserved:               '#000000',
        #Keyword.Type:                   '#000000',
        #Keyword:                        '#a9175d',
        #Literal.Number.Float:           '#009999',
        #Literal.Number.Hex:             '#009999',
        #Literal.Number.Integer.Long:    '#009999',
        #Literal.Number.Integer:         '#009999',
        #Literal.Number.Oct:             '#009999',
        #Literal.Number:                 '#0087b4',
        #Literal.String.Backtick:        '#d14',
        #Literal.String.Char:            '#d14',
        #Literal.String.Doc:             '#d14',
        #Literal.String.Double:          '#0000ff',
        #Literal.String.Escape:          '#0000ff',
        #Literal.String.Heredoc:         '#d14',
        #Literal.String.Interpol:        '#0000ff',
        #Literal.String.Other:           '#d14',
        #Literal.String.Regex:           '#009926',
        #Literal.String.Single:          '#0000ff',
        #Literal.String.Symbol:          '#990073',
        Literal.String:                 '#ff00ff',
        #Name.Attribute:                 '#008080',
        #Name.Builtin.Pseudo:            '#000000',
        Name.Builtin:                   'bold #a72626',
        #Name.Class:                     'bold #445588',
        #Name.Constant:                  '#008080',
        #Name.Decorator:                 'bold #3c5d5d',
        #Name.Entity:                    '#800080',
        #Name.Exception:                 'bold #990000',
        #Name.Function:                  'bold #990000',
        #Name.Label:                     'bold #990000',
        #Name.Namespace:                 '#555555',
        #Name.Tag:                       '#000080',
        #Name.Variable.Class:            '#008080',
        #Name.Variable.Global:           '#008080',
        #Name.Variable.Instance:         '#008080',
        Name.Variable:                  '#6a5acd',
        #Operator.Word:                  '#ec008c',
        Operator:                       'bold #a64198',
        #Text.Whitespace:                '#bbbbbb',
    }

class VSMarkerStyle(Style):
    """
    Simulated Visual Source Code Marker color scheme.
    """

    default_style = ''

    background_color = '#ffffff'

    styles = {
        #Comment.Multiline:              'italic #157947',
        #Comment.Preproc:                'italic #157947',
        #Comment.Single:                 'italic #157947',
        #Comment.Special:                'italic #157947',
        #Comment:                        'italic #157947',
        #Error:                          'bg:#e3d2d2 #a61717',
        Generic.Deleted:                '#bf2801',
        #Generic.Emph:                   'italic #000000',
        #Generic.Error:                  '#aa0000',
        #Generic.Heading:                '#999999',
        Generic.Inserted:               '#53a72f',
        #Generic.Output:                 '#888888',
        #Generic.Prompt:                 '#555555',
        #Generic.Strong:                 'bold',
        #Generic.Subheading:             '#aaaaaa',
        #Generic.Traceback:              '#aa0000',
        Keyword.Constant:               '#0087b4',
        #Keyword.Declaration:            '#000000',
        Keyword.Namespace:              '#a9175d',
        #Keyword.Pseudo:                 '#000000',
        #Keyword.Reserved:               '#000000',
        #Keyword.Type:                   '#000000',
        Keyword:                        '#a9175d',
        #Literal.Number.Float:           '#009999',
        #Literal.Number.Hex:             '#009999',
        #Literal.Number.Integer.Long:    '#009999',
        #Literal.Number.Integer:         '#009999',
        #Literal.Number.Oct:             '#009999',
        Literal.Number:                 '#0087b4',
        #Literal.String.Backtick:        '#d14',
        #Literal.String.Char:            '#d14',
        #Literal.String.Doc:             '#d14',
        #Literal.String.Double:          '#0000ff',
        #Literal.String.Escape:          '#0000ff',
        #Literal.String.Heredoc:         '#d14',
        #Literal.String.Interpol:        '#0000ff',
        #Literal.String.Other:           '#d14',
        #Literal.String.Regex:           '#009926',
        #Literal.String.Single:          '#0000ff',
        #Literal.String.Symbol:          '#990073',
        Literal.String:                 '#123392',
        #Name.Attribute:                 '#008080',
        #Name.Builtin.Pseudo:            '#000000',
        Name.Builtin:                   '#a9175d',
        #Name.Class:                     'bold #445588',
        #Name.Constant:                  '#008080',
        #Name.Decorator:                 'bold #3c5d5d',
        #Name.Entity:                    '#800080',
        #Name.Exception:                 'bold #990000',
        #Name.Function:                  'bold #990000',
        #Name.Label:                     'bold #990000',
        #Name.Namespace:                 '#555555',
        #Name.Tag:                       '#000080',
        #Name.Variable.Class:            '#008080',
        #Name.Variable.Global:           '#008080',
        #Name.Variable.Instance:         '#008080',
        #Name.Variable:                  '#008080',
        #Operator.Word:                  '#ec008c',
        Operator:                       '#a9175d',
        #Text.Whitespace:                '#bbbbbb',
    }

class GoogleColabStyle(Style):
    """
    Simulated Google Colab color scheme.
    """

    default_style = ''

    background_color = '#ffffff'

    styles = {
        #Comment.Multiline:              'italic #157947',
        #Comment.Preproc:                'italic #157947',
        #Comment.Single:                 'italic #157947',
        #Comment.Special:                'italic #157947',
        Comment:                        '#028102',
        #Error:                          'bg:#e3d2d2 #a61717',
        #Generic.Deleted:                '#bf2801',
        #Generic.Emph:                   'italic #000000',
        #Generic.Error:                  '#aa0000',
        #Generic.Heading:                '#999999',
        #Generic.Inserted:               '#53a72f',
        #Generic.Output:                 '#888888',
        #Generic.Prompt:                 '#555555',
        #Generic.Strong:                 'bold',
        #Generic.Subheading:             '#aaaaaa',
        #Generic.Traceback:              '#aa0000',
        Keyword.Constant:               '#0000ff',
        #Keyword.Declaration:            '#000000',
        Keyword.Namespace:              '#af00db',
        #Keyword.Pseudo:                 '#000000',
        #Keyword.Reserved:               '#000000',
        #Keyword.Type:                   '#000000',
        #Keyword:                        '#0000ff', # defに使いたいがダメだ…
        Keyword:                        '#af00db',
        #Literal.Number.Float:           '#009999',
        #Literal.Number.Hex:             '#009999',
        #Literal.Number.Integer.Long:    '#009999',
        #Literal.Number.Integer:         '#009999',
        #Literal.Number.Oct:             '#009999',
        Literal.Number:                 '#0c895c',
        #Literal.String.Backtick:        '#d14',
        #Literal.String.Char:            '#d14',
        #Literal.String.Doc:             '#d14',
        #Literal.String.Double:          '#0000ff',
        #Literal.String.Escape:          '#0000ff',
        #Literal.String.Heredoc:         '#d14',
        #Literal.String.Interpol:        '#0000ff',
        #Literal.String.Other:           '#d14',
        #Literal.String.Regex:           '#009926',
        #Literal.String.Single:          '#0000ff',
        #Literal.String.Symbol:          '#990073',
        Literal.String:                 '#a41818',
        #Name.Attribute:                 '#008080',
        #Name.Builtin.Pseudo:            '#000000',
        Name.Builtin:                   '#7b6029',
        Name.Class:                     '#0c895c',
        #Name.Constant:                  '#008080',
        #Name.Decorator:                 'bold #3c5d5d',
        #Name.Entity:                    '#800080',
        #Name.Exception:                 'bold #990000',
        Name.Function:                  '#7b6029',
        #Name.Label:                     'bold #990000',
        #Name.Namespace:                 '#555555',
        #Name.Tag:                       '#000080',
        #Name.Variable.Class:            '#008080',
        #Name.Variable.Global:           '#008080',
        #Name.Variable.Instance:         '#008080',
        #Name.Variable:                  '#008080',
        #Operator.Word:                  '#ec008c',
        #Operator:                       '#a9175d',
        #Text.Whitespace:                '#bbbbbb',
    }
