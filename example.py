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

    def scan(self, ):
        if self.word == '':
            self.nextchar = ''
        else:
            self.nextchar = self.word[0]
            self.word = self.word[1:]

    def expect(self, char):
        if self.nextchar != char:
            raise ParseError(f'Unexpected token: `{self.nextchar}`. Expected `{char}`.')
        
        self.scan()

    def A(self):
        self.expect('a')
        self.B()

    def B(self):
        if self.nextchar == 'b':
            self.expect('b')
            self.expect('c')
            self.A()
        else:
            return
    
    def parse(self):
        self.A()
        if self.nextchar == '':
            print('Accepted')
        else:
            raise ParseError(f'Parser finished before input: `{self.nextchar + self.word}` left.')


for word in words:
    parser = Parser(word)
    try:
        parser.parse()
    except ParseError as e:
        print(e)
