import os

grammar = dict()

with open('grammar.txt', 'r') as f:
    while line := f.readline():
        print(line.strip())
        line = line.split('->')
        grammar[line[0].strip()] = [prod.strip() if prod.strip() != 'ϵ' else '' for prod in line[1].split('|')]

print(grammar)

with open('built_parser.py', 'w+') as f:
    print("""words = []
nextchar = ''

with open('words.txt', 'r') as f:
    while line := f.readline():
        words.append(line.strip())


class ParseError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Parser:
    def __init__(self, word):
        self.word = word
        self.scan()

    def scan(self):
        if self.word == '':
            self.nextchar = ''
        else:
            self.nextchar = self.word[0]
            self.word = self.word[1:]

    def expect(self, char):
        if self.nextchar != char:
            raise ParseError(f'Unexpected token: `{self.nextchar}`. Expected `{char}`.')
        
        self.scan()
    """, file=f)

    for nonterm, prod in grammar.items():
        print(f"    def {nonterm}(self):", file=f)
        if len(prod) == 1:
            for char in prod[0]:
                if char.isupper():
                    print(f'        self.{char}()', file=f)
                else:
                    print(f'        self.expect("{char}")', file=f)
            print(file=f)
        else:
            has_epsilon = False
            for i, p in enumerate(prod):
                if p == '':
                    has_epsilon = True
                    continue
                if i == 0 or (i == 1 and prod[0] == ''):
                    print(f'        if self.nextchar == "{p[0]}":', file=f)
                else:
                    print(f'        elif self.nextchar == "{p[0]}":', file=f)
                for char in p:
                    if char.isupper():
                        print(f'            self.{char}()', file=f)
                    else:
                        print(f'            self.expect("{char}")', file=f)
            if has_epsilon:
                print('        else:', file=f)
                print('            return', file=f)
            else:
                print('        else:', file=f)
                print("            raise ParseError(f'Unexpected token: `{self.nextchar}`.')", file=f)

            print(file=f)

    print('    def parse(self):', file=f)
    print(f'        self.{list(grammar.keys())[0]}()', file=f)
    print("""
        if self.nextchar != '':
            raise ParseError(f'Parser finished before input: `{self.nextchar + self.word}` left.')


for word in words:
    parser = Parser(word)
    try:
        parser.parse()
    except ParseError as e:
        print(f'{word} | {e}')
    else:
        print(f'{word} | Accepted')""", file=f)