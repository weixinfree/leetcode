import re
from typing import *
from dataclasses import dataclass
import operator

# "(1+(4+5+2)-3)+(6+8)"

class TokDef:
    t_INT = r'\d+'
    t_ADD = r'\+'
    t_SUB = r'-'
    t_LP = r'\('
    t_RP = r'\)'
    t_IGNORE = r'\s+'


@dataclass
class Tok:
    tok_type: str
    tok_value: str
    tok_span: Tuple[int, int]


def tokenize(tok_def: Any, source: str) -> Iterable[Tok]:
    tok_li = [(name[2:], regex) for name, regex in vars(
        tok_def).items() if name.startswith('t_')]
    pat = "|".join(f'(?P<{name}>{regex})' for name, regex in tok_li)

    last_tok_end = 0
    for tok in re.finditer(pat, source):
        tok_name = tok.lastgroup
        tok_value = tok.group(tok_name)
        if tok.start() != last_tok_end:
            raise CalcException(f"unknown id: {source[last_tok_end:tok.start()]}")
        last_tok_end = tok.end()

        if tok_name != "IGNORE":
            yield Tok(tok_name, tok_value, tok.span())

class Parser:
    def __init__(self, source: str):
        self.source = source
        self.toks = tokenize(TokDef, source)
        self.tok: Tok = None
        self.next_tok: Tok = next(self.toks, None)

    def advance(self):
        self.tok, self.next_tok = self.next_tok, next(self.toks, None)
        # print(self.tok, self.next_tok)

    def accept(self, *tok_types: List[str]):
        if self.next_tok and self.next_tok.tok_type in tok_types:
            self.advance()
            return True
        else:
            return False

    def expect(self, *tok_types: List[str]):
        assert self.next_tok.tok_type in tok_types
        self.advance()

    def expr(self):
        term = self.term()
        result = term
        while self.accept("ADD", "SUB"):
            op = operator.add if self.tok.tok_type == "ADD" else operator.sub
            rt = self.term()
            result = op(result, rt)
        return result

    def term(self):
        if self.accept("LP"):
            r = self.expr()
            self.expect("RP")
            return r
        else:
            self.expect("INT")
            return int(self.tok.tok_value)

class Solution:
    def calculate(self, s: str) -> int:
        return Parser(s).expr()


if __name__ == '__main__':
    assert Parser(" 2-1 + 2 ").expr() == 3
    assert Parser("1 + 1").expr() == 2
    assert Parser("(1+(4+5+2)-3)+(6+8)").expr() == 23

