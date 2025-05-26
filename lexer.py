# lexer.py
import ply.lex as lex

# List of token names
tokens = [
    'ID', 'NUMBER', 'CHARACTER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQ', 'EQEQ', 'NEQ', 'LT', 'LE', 'GT', 'GE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA',
    'AMPERSAND','AND', 'OR', 'NOT'
]

# Reserved words (C keywords)
reserved = {
    'int': 'INT',
    'char': 'CHAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'printf': 'PRINTF',
    'scanf': 'SCANF'
}

tokens += list(reserved.values())

# Regular expressions for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQ        = r'='
t_EQEQ      = r'=='
t_NEQ       = r'!='
t_LT        = r'<'
t_LE        = r'<='
t_GT        = r'>'
t_GE        = r'>='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_AMPERSAND = r'&'
t_SEMI      = r';'
t_COMMA     = r','
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'

# Regex for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Regex for numeric constants
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regex for character constants
def t_CHARACTER(t):
    r'\'([^\\\n]|(\\.))\''
    t.value = t.value[1:-1]
    return t

# Regex for string literals
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

# Ignored characters
t_ignore = ' \t'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# For testing
if __name__ == "__main__":
    with open("compiler for c/yest.c", "r") as f:
        data = f.read()
    lexer.input(data)
    for tok in lexer:
        print(tok)
