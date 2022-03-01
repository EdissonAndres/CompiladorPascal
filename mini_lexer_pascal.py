"""
@author: Edison Andres
         Alejandro Rios
"""

import ply.lex as lex
import sys

# list of tokens
tokens = (
    
    # Reserverd words
    'ABSOLUTE',
    'ARRAY',
    'BEGIN',
    'CONST',
    'DESTRUCTOR',
    'DIV',
    'DOWNTO',
    'END',
    'FOR',
    'FUNCTION',
    'IF',
    'IN',
    'INTERFACE',
    'LABEL',
    'NIL',
    'OBJECT',
    'OR',
    'PRIVATE',
    'PROGRAM',
    'REPEAT',
    'SHL',
    'TO',
    'UNIT',
    'USES',
    'VIRTUAL',
    'WITH',
    'AND',
    'ASM',
    'CASE',
    'CONSTRUCTOR',
    'EXTERNAL',
    'DO',
    'ELSE',
    'FILE',
    'FORWARD',
    'GOTO',
    'IMPLEMENTATION',
    'INLINE',
    'INTERRUPT',
    'AMPERSANTMOD',
    'NOT',
    'OF',
    'PACKED',
    'PROCEDURE',
    'RECORD',
    'SET',
    'SHR',
    'THEN',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'XOR',
    'WRITELN',
    'WRITE',
    'READLN',
    'READ',
    'CHAR',
    'BOOLEAN',
    'REAL',
    'STRING',
    
    # Symbols
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'LESS',
    'GREATER',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'DOT',
    'APOSTROPHE',
    'POINTER',
    
    # Compound Symbols 
    'LESSEQUAL',
    'GREATEREQUAL',
    'DEQUAL',
    'ASSIGNATION',
    'SUBRANGE',

    # Others   
    'ID', 
    'NUMBER',
    'TEXT',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_DOT = r'\.'
t_APOSTROPHE = r'\''
t_POINTER = r'\^'


# Funtions for Reserverd words

def t_WRITELN(t):
    r'(?i)writeln'
    return t

def t_WRITE(t):
    r'(?i)write'
    return t

def t_READLN(t):
    r'(?i)readln'
    return t

def t_READ(t):
    r'(?i)read'
    return t

def t_CHAR(t):
    r'(?i)char'
    return t

def t_REAL(t):
    r'(?i)real'
    return t

def t_BOOLEAN(t):
    r'(?i)boolean'
    return t

def t_STRING(t):
    r'(?i)string'
    return t

def t_ABSOLUTE(t):
    r'(?i)absolute'
    return t

def t_ARRAY(t):
    r'(?i)array'
    return t

def t_BEGIN(t):
    r'(?i)begin'
    return t

def t_CONST(t):
    r'(?i)const'
    return t

def t_DESTRUCTOR(t):
    r'(?i)destructor'
    return t

def t_DIV(t):
    r'(?i)div'
    return t

def t_DOWNTO(t):
    r'(?i)downto'
    return t

def t_END(t):
    r'(?i)end'
    return t

def t_FOR(t):
    r'(?i)for'
    return t

def t_FUNCTION(t):
    r'(?i)function'
    return t

def t_IF(t):
    r'(?i)if'
    return t

def t_IN(t):
    r'(?i)in'
    return t

def t_INTERFACE(t):
    r'(?i)interface'
    return t

def t_LABEL(t):
    r'(?i)label'
    return t

def t_NIL(t):
	r'(?i)nil'
	return t

def t_OBJECT(t):
    r'(?i)object'
    return t

def t_OR(t):
    r'(?i)or'
    return t

def t_PRIVATE(t):
	r'(?i)private'
	return t

def t_PROGRAM(t):
    r'(?i)program'
    return t

def t_REPEAT(t):
	r'(?i)repeat'
	return t
	
def t_SHL(t):
	r'(?i)shl'
	return t

def t_TO(t):
	r'(?i)to'
	return t

def t_UNIT(t):
	r'(?i)unit'
	return t

def t_USES(t):
	r'(?i)uses'
	return t

def t_VIRTUAL(t):
	r'(?i)virtual'
	return t

def t_WITH(t):
	r'(?i)with'
	return t

def t_AND(t):
	r'(?i)and'
	return t

def t_ASM(t):
	r'(?i)asm'
	return t

def t_CASE(t):
	r'(?i)case'
	return t

def t_CONSTRUCTOR(t):
	r'(?i)constructor'
	return t

def t_EXTERNAL(t):
	r'(?i)external'
	return t

def t_DO(t):
	r'(?i)do'
	return t

def t_ELSE(t):
	r'(?i)else'
	return t

def t_FILE(t):
	r'(?i)file'
	return t

def t_FORWARD(t):
	r'(?i)forward'
	return t

def t_GOTO(t):
	r'(?i)goto'
	return t

def t_IMPLEMENTATION(t):
	r'(?i)implementacion'
	return t

def t_INLINE(t):
	r'(?i)inline'
	return t

def t_INTERRUPT(t):
	r'(?i)interrupt'
	return t

def t_AMPERSANTMOD(t):
	r'(?i)ampersantmod'
	return t

def t_NOT(t):
	r'(?i)not'
	return t

def t_OF(t):
	r'(?i)of'
	return t

def t_PACKED(t):
	r'(?i)packed'
	return t

def t_PROCEDURE(t):
	r'(?i)procedure'
	return t

def t_RECORD(t):
	r'(?i)record'
	return t

def t_SET(t):
	r'(?i)set'
	return t

def t_SHR(t):
	r'(?i)shr'
	return t

def t_THEN(t):
	r'(?i)then'
	return t

def t_TYPE(t):
	r'(?i)type'
	return t

def t_UNTIL(t):
	r'(?i)until'
	return t

def t_VAR(t):
	r'(?i)var'
	return t

def t_WHILE(t):
	r'(?i)while'
	return t

def t_XOR(t):
	r'(?i)xor'
	return t


# Funtions for Compound Symbols 
def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'<>'
	return t

def t_ASSIGNATION(t):
	r':='
	return t

def t_SUBRANGE(t):
	r'\.\.'
	return t


# Funtions for Other 
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_TEXT(t):
    r'(\'(.)*\')'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'


def t_comments1(t):
    r'\(\*(.|\n)*\*\)'
    t.lexer.lineno += t.value.count('\n')

def t_comments2(t):
    r'\{(.|\n)*\}'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba_pascal.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()