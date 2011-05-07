# -*- coding: utf-8 -*-
"""
    pygments.styles.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    The default highlighting style.

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class SingleColorStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """

    default_color = "000000"
    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "",
        Comment:                   "italic #333",
        Comment.Preproc:           "noitalic ",

        Keyword:                   "bold ",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold ",

        Operator:                  "",
        Operator.Word:             "bold ",

        Name.Builtin:              "",
        Name.Function:             "",
        Name.Class:                "bold ",
        Name.Namespace:            "bold ",
        Name.Exception:            "bold ",
        Name.Variable:             "",
        Name.Constant:             "",
        Name.Label:                "",
        Name.Entity:               "bold ",
        Name.Attribute:            "",
        Name.Tag:                  "bold ",
        Name.Decorator:            "",

        String:                    "",
        String.Doc:                "italic",
        String.Interpol:           "bold ",
        String.Escape:             "bold ",
        String.Regex:              "",
        String.Symbol:             "",
        String.Other:              "",
        Number:                    "",

        Generic.Heading:           "bold ",
        Generic.Subheading:        "bold ",
        Generic.Deleted:           "",
        Generic.Inserted:          "",
        Generic.Error:             "",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold ",
        Generic.Output:            "",
        Generic.Traceback:         "",

        Error:                     "border:#FF0000"
    }
