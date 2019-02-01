# Copyright (c) 2017 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from xpathUnlexer import xpathUnlexer

from grammarinator.runtime import *


class xpathCustomUnlexer(xpathUnlexer):

    # You probably want to rewrite this with a distinct CSS fuzzer.
    def style_sheet(self):
        return UnlexerRule(src='* {' \
                                '  background: green;' \
                                '}')
