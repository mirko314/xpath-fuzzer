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
        self.weights = {
            ('alt_207', 0): 1.0,
            ('alt_207', 1): 0.0001,
            ('alt_0', 0): 0.001,
            ('alt_0', 1): 0.001,
            ('alt_0', 2): 0.001,
            ('alt_0', 3): 1,
            ('alt_135', 0): 1, # nodeTest nametest
            ('alt_135', 1): 0.001,
            ('alt_135', 2): 0.001,
            ('alt_164', 1): 0.001,
            #nameTest
            ('alt_235', 0): 0.001,
            ('alt_235', 1): 0.001,
            ('alt_235', 2): 1,
            #Nodename
            ('alt_242', 0): 1,
            ('alt_242', 1): 0.001,
            ('alt_242', 2): 0.001,

        }
        super(xpathCustomUnlexer, self).__init__(max_depth=max_depth, weights=self.weights, cooldown=cooldown)
        # self.unlexer = self
        # self.max_depth = max_depth
        # self.cooldown = cooldown
        # self.set_options()

    # You probably want to rewrite this with a distinct CSS fuzzer.
    def style_sheet(self):
        return UnlexerRule(src='* {' \
                                '  background: green;' \
                                '}')
