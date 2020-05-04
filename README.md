# RecursiveDescent
There are two important text files: `grammar.txt` and `words.txt`.

### Setup
```
$ conda env create -f environment.yml
$ conda activate tc
```

### Files

In `grammar.txt` you can specify the grammar, keeping in mind the following rules:
```
Nonterm -> Nonterm Nonterm
Nonterm -> term1 ... term | term2 ... term Nonterm ... Nonterm | ϵ

e.g.:
1. Any Nonterminal either produces only Nonterminals or at least one terminal and optionally more terminals and Nonterminals, with no terminals in between, or, finally, epsilon (character ϵ).
2. The first terminals produced MUST be unique
3. Nonterminals are CAPITAL LETTERS
4. Terminals are ANYTHING ELSE
```

Example grammar that (mostly accepts complex numbers with coefficients = 1:
```
S -> AB
A -> 1C | -1C
B -> +A | ϵ
C -> i | ϵ
```

In `words.txt` you can specify a list of words, each on a new line, that will be parsed.

### Running

Run (tested in Python 3.8) `build_parser.py`. This will create a file `parser.py` that, when run, will output if the words are accepted or the corresponding error.
