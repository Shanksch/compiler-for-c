import ply.yacc as yacc
from lexer import tokens  # Import tokens from lexer.py

symbol_table = {}

# --- Grammar Rules ---

temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f't{temp_count}'

def new_label():
    global label_count
    label_count += 1
    return f'L{label_count}'

intermediate_code = []

def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_function_definition(p):
    'statement : type ID LPAREN RPAREN block'
    p[0] = ('func', p[1], p[2], p[5])

def p_block(p):
    'block : LBRACE program RBRACE'
    p[0] = ('block', p[2])

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_statement
                 | while_statement
                 | io_statement
                 | block'''
    p[0] = p[1]

def p_declaration(p):
    'declaration : type ID SEMI'
    symbol_table[p[2]] = p[1]
    p[0] = ('declare', p[1], p[2])

def p_declaration_assign(p):
    'declaration : type ID EQ expression SEMI'
    symbol_table[p[2]] = p[1]
    intermediate_code.append(f"{p[2]} = {p[4]}")
    p[0] = ('declare_assign', p[1], p[2], p[4])

def p_type(p):
    '''type : INT
            | CHAR'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID EQ expression SEMI'
    if p[1] not in symbol_table:
        print(f"Semantic Error: Undeclared variable '{p[1]}'")
    intermediate_code.append(f"{p[1]} = {p[3]}")
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN block
                    | IF LPAREN expression RPAREN block ELSE block'''
    if len(p) == 6:
        label = new_label()
        intermediate_code.append(f"ifFalse {p[3]} goto {label}")
        p[5]  # already executed in block
        intermediate_code.append(f"{label}:")
    else:
        label_else = new_label()
        label_end = new_label()
        intermediate_code.append(f"ifFalse {p[3]} goto {label_else}")
        p[5]
        intermediate_code.append(f"goto {label_end}")
        intermediate_code.append(f"{label_else}:")
        p[7]
        intermediate_code.append(f"{label_end}:")

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN block'
    start = new_label()
    end = new_label()
    intermediate_code.append(f"{start}:")
    intermediate_code.append(f"ifFalse {p[3]} goto {end}")
    p[5]
    intermediate_code.append(f"goto {start}")
    intermediate_code.append(f"{end}:")

def p_io_statement(p):
    '''io_statement : PRINTF LPAREN STRING RPAREN SEMI
                    | SCANF LPAREN STRING COMMA AMPERSAND ID RPAREN SEMI'''
    if p[1] == 'printf':
        intermediate_code.append(f'print "{p[3]}"')
    else:
        if p[6] not in symbol_table:
            print(f"Semantic Error: Undeclared variable '{p[6]}'")
        intermediate_code.append(f'scanf {p[6]}')

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQEQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression AND expression
                  | expression OR expression'''
    temp = new_temp()
    intermediate_code.append(f"{temp} = {p[1]} {p[2]} {p[3]}")
    p[0] = temp

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_character(p):
    'expression : CHARACTER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] not in symbol_table:
        print(f"Semantic Error: Undeclared variable '{p[1]}'")
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax Error: Unexpected token '{p.value}' at line {p.lineno}")
    else:
        print("Syntax Error: Unexpected end of input")

parser = yacc.yacc()

# Test driver
if __name__ == "__main__":
    with open("yest.c", "r") as f:
        data = f.read()
    parser.parse(data)
    print("\nParsing completed.\n")
    print("Generated Intermediate Code:\n")
    for line in intermediate_code:
        print(line)

def generate_intermediate_code(parsed_tree):
    return intermediate_code
