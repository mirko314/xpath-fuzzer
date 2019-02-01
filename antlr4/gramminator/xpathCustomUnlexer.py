# Copyright (c) 2017 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from xpathUnlexer import xpathUnlexer

from grammarinator.runtime import *


class xpathCustomUnlexer(xpathUnlexer):

    def __init__(self, *, max_depth=float('inf'), weights=None, cooldown=1.0):
        self.weights = dict()
        super(xpathCustomUnlexer, self).__init__(max_depth=max_depth, weights=weights, cooldown=cooldown)
        # self.unlexer = self
        # self.max_depth = max_depth
        # self.cooldown = cooldown
        # self.set_options()

    # You probably want to rewrite this with a distinct CSS fuzzer.
    def style_sheet(self):
        return UnlexerRule(src='* {' \
                                '  background: green;' \
                                '}')
