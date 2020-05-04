words = []
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
    
    def S(self):
        self.A()
        self.B()

    def A(self):
        if self.nextchar == "1":
            self.expect("1")
            self.C()
        elif self.nextchar == "-":
            self.expect("-")
            self.expect("1")
            self.C()
        else:
            raise ParseError(f'Unexpected token: `{self.nextchar}`.')

    def B(self):
        if self.nextchar == "+":
            self.expect("+")
            self.A()
        else:
            return

    def C(self):
        if self.nextchar == "i":
            self.expect("i")
        else:
            return

    def parse(self):
        self.S()

        if self.nextchar != '':
            raise ParseError(f'Parser finished before input: `{self.nextchar + self.word}` left.')


for word in words:
    parser = Parser(word)
    try:
        parser.parse()
    except ParseError as e:
        print(f'{word} | {e}')
    else:
        print(f'{word} | Accepted')
