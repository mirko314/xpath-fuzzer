# Generated by Grammarinator 18.10

import json
import random

from os.path import dirname, join

from grammarinator.runtime import *
from xpathUnparser import xpathUnparser


with open(join(dirname(__file__), 'xpath.json')) as f:
    tags = json.load(f)



class xpathCustomUnparser(xpathUnparser):

    attr_stack = []
    tag_stack = []
    tags = set()

    def __init__(self, unlexer):
        super(xpathCustomUnparser, self).__init__(unlexer)
        # self.tag_names = list(tags.keys())

    # Override the original random_decision implementation in a way to increase the number of generated nodes.
    def random_decision(self):
        # Playing with size.
        if self.node_cnt < self.max_cnt // 4:
            return random.randint(0, 1000) > 100
        return random.randint(0, 1000) < 400

    # def nCName(self):
    #     current = self.create_node(UnparserRule(name='nCName'))
    #     current += "Book"
    #     return current


    def functionName(self):

        current = self.create_node(UnparserRule(name='functionName'))
        name = "string"
        current += UnlexerRule(src=name)
        return current
    functionName.min_depth = 1