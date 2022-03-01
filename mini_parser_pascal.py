# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:41:20 2020

@author: Edison Andres
"""


import ply.yacc as yacc
from mini_lexer_pascal import tokens
import mini_lexer_pascal
import sys

VERBOSE = 1

def p_programGeneral(p):
	'program : declaration_program declaration_list block'
	pass

def p_programgkjdfgkhdfgkdfhgfgd(p):
	'declaration_program : PROGRAM ID SEMICOLON'
	pass

def p_program(p):
	'program : PROGRAM ID SEMICOLON declaration_list block'
	pass

def p_declaration_list_var(p):
	'declaration_list : VAR declaration_var'
	pass

def p_declaration_var(p):
	'''declaration_var : declaration_id COLON type_specifier SEMICOLON declaration_var
                       | declaration_id COLON type_specifier SEMICOLON
                       | declaration_list'''
	pass

def p_declaration_list_type(p):
	'declaration_list : TYPE declaration_type'
	pass

def p_declaration_type(p):
	'''declaration_type : declaration_id EQUAL type_specifier SEMICOLON declaration_type
                        | declaration_id EQUAL type_specifier SEMICOLON
                        | declaration_list'''
	pass

def p_declaration_list_uses(p):
	'declaration_list : USES declaration_uses'
	pass
    
def p_declaration_uses(p):
	'''declaration_uses : declaration_id SEMICOLON declaration_uses 
                        | declaration_id SEMICOLON 
                        | declaration_list'''
	pass



def p_declaration_id(p):
	'''declaration_id : ID COMMA declaration_id 
                      | ID'''
	pass



def p_type_specifier_1(p):
	'type_specifier : REAL'
	pass

def p_type_specifier_2(p):
	'type_specifier : CHAR'
	pass

def p_type_specifier_3(p):
	'type_specifier : BOOLEAN'
	pass

def p_type_specifier_4(p):
	'type_specifier : STRING'
	pass

def p_type_specifier_5(p):
	'type_specifier : ID'
	pass

def p_type_array(p):
	'type_specifier : ARRAY LBRACKET NUMBER SUBRANGE NUMBER RBRACKET OF type_specifier'
	pass


def p_block(p):
	'block : BEGIN instance END DOT'
	pass

def p_instance(p):
	'''instance : group_instance instance
                | group_instance'''
	pass

def p_group_instance(p):
    '''group_instance : declaration_id SEMICOLON
                    | asignation SEMICOLON
                    | iteration_for
                    | iteration_while
                    | selection_if
                    | read_statement
                    | write_statement'''
    pass

def p_asignation(p):
    'asignation : ID ASSIGNATION expression'
    pass

def p_expression(p):
    '''expression : ID 
                | NUMBER
                | ID LBRACKET ID RBRACKET
                | ID LBRACKET NUMBER RBRACKET'''
    pass

def p_iteration_for(p):
    '''iteration_for : FOR expression TO expression DO BEGIN instance END SEMICOLON
                   | FOR asignation TO expression DO BEGIN instance END SEMICOLON'''
    pass

def p_iteration_while(p):
    'iteration_while : WHILE LPAREN expression_comparison RPAREN DO BEGIN instance END SEMICOLON'
    pass

def p_expression_comparison(p):
    'expression_comparison : expression comparison expression'
    pass

def p_comparison(p):
    '''comparison : EQUAL
                | LESS
                | LESSEQUAL
                | GREATER
                | GREATEREQUAL
                | DEQUAL'''
    pass

def p_seleccion_if(p):
    '''selection_if : IF LPAREN expression_comparison RPAREN THEN BEGIN instance END SEMICOLON
                 | IF LPAREN expression_comparison RPAREN THEN instance
                 | IF LPAREN expression_comparison RPAREN THEN BEGIN instance END SEMICOLON ELSE instance
                 | IF LPAREN expression_comparison RPAREN THEN instance ELSE instance
                 | IF LPAREN expression_comparison RPAREN THEN BEGIN instance END SEMICOLON ELSE BEGIN instance END SEMICOLON
                 | IF LPAREN expression_comparison RPAREN THEN instance ELSE BEGIN instance END SEMICOLON'''
    pass

def p_read_statement(p):
    '''read_statement : READ LPAREN expression RPAREN SEMICOLON
                    | READLN LPAREN expression RPAREN SEMICOLON'''
    pass

def p_write_statement(p):
    '''write_statement : WRITE LPAREN type_out RPAREN SEMICOLON
                     | WRITELN LPAREN type_out RPAREN SEMICOLON'''
    pass

def p_type_out(p):
    '''type_out : ID
                | ID COMMA type_out
                | TEXT
                | TEXT COMMA type_out
                | ID LBRACKET ID RBRACKET
                | ID LBRACKET ID RBRACKET COMMA type_out'''
    pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba_pascal.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input()