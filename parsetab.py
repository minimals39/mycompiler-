
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVMODleftLESSMOREBACK COMMA DECADE DECL DIV EQU EQUTO HEX HEXT INT64 LARRY LESS LOOP LPAREN LSTATE MINUS MOD MORE MUL NEWLINE NOEQU NOTSO NUM OTHERWISE PLUS RARRY REPEAT RPAREN RSTATE SEMI SO TEXT WORDstatement : statement NEWLINE statement\n                 | statement NEWLINE statement NEWLINEstatement : exassign\n                 | declare\n                 | exprint\n                 | exif\n                 | exelif\n                 | exloop\n                 | exrepeat\n                 | statement NEWLINE\n                 | NEWLINE statement\n                 | exloop NEWLINE\n                 exif : SO LPAREN expression RPAREN LSTATE statement RSTATE\n             | SO LPAREN expression RPAREN NEWLINE LSTATE statement RSTATEexelif : exif exelseexelse : OTHERWISE LSTATE statement LSTATE OTHERWISE\n               | OTHERWISE LSTATE NEWLINE statement RSTATEexloop : LOOP LPAREN expression RPAREN LSTATE statement RSTATE\n             | LOOP LPAREN expression RPAREN LSTATE NEWLINE statement RSTATEexrepeat : REPEAT LPAREN expression RPAREN LSTATE statement RSTATE\n                | REPEAT LPAREN expression RPAREN NEWLINE LSTATE statement RSTATEexpression : expression PLUS expression                  \n                  | term PLUS term\n                  | term PLUS expression\n                  | expression MINUS expression\n                  | term MINUS term\n                  | term MINUS expression\n                  | expression MUL expression\n                  | term MUL term\n                  | term MUL expression\n                  | expression DIV expression\n                  | term DIV term\n                  | term DIV expression\n                  | expression MOD expression\n                  | term MOD term\n                  | term MOD expressionterm : WORD\n           | arraysh\n           | NUMterm : HEXT HEXexpression : termexpression : MINUS expressionexpression : LPAREN expression RPARENexassign : WORD EQU expression\n                  | arraysh EQU expression\n                  expression : expression EQUTO expressionexpression : expression NOEQU expressionexpression : expression LESS expressionexpression : expression MORE expressiondeclare : DECL WORD\n               | DECL WORD EQU termarraysh : WORD LARRY NUM RARRY\n               | WORD LARRY WORD RARRYdeclare : DECL WORD EQU LSTATE arrayX RSTATEdeclare : DECL WORD LARRY NUM RARRYdeclare : DECL WORD LARRY NUM RARRY EQU LSTATE arrayX RSTATEarrayX : NUM arrayYarrayY : COMMA NUM arrayY\n              | empty empty emptyexprint : TEXT LPAREN WORD printMore RPARENprintMore : "," expression printMore\n                 | empty empty emptyempty :'
    
_lr_action_items = {'NEWLINE':([0,1,2,3,4,5,6,7,8,9,17,18,19,21,25,30,31,32,33,34,37,38,42,49,50,51,66,68,69,70,71,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,110,111,113,114,115,122,123,124,125,126,127,131,132,133,134,135,136,140,141,142,143,],[2,17,2,-3,-4,-5,-6,-7,21,-9,2,17,-15,-12,-50,49,51,-37,-44,-41,-38,-39,-45,2,17,2,-42,-40,-53,-52,-51,109,112,17,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,-55,-60,2,125,2,-16,-17,-54,17,2,17,2,17,2,-13,17,-18,17,-20,17,-14,-19,-21,-56,]),'WORD':([0,2,12,17,22,23,24,26,27,28,29,31,35,36,43,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,108,110,111,123,125,127,],[10,10,25,10,32,40,32,45,32,32,32,10,32,32,32,10,10,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,10,10,10,10,10,10,]),'DECL':([0,2,17,31,49,51,108,110,111,123,125,127,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'TEXT':([0,2,17,31,49,51,108,110,111,123,125,127,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'SO':([0,2,17,31,49,51,108,110,111,123,125,127,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'LOOP':([0,2,17,31,49,51,108,110,111,123,125,127,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'REPEAT':([0,2,17,31,49,51,108,110,111,123,125,127,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,3,4,5,6,7,8,9,17,18,19,21,25,30,32,33,34,37,38,42,49,66,68,69,70,71,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,113,114,115,131,133,135,140,141,142,143,],[0,-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,-12,-50,-1,-37,-44,-41,-38,-39,-45,-2,-42,-40,-53,-52,-51,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,-55,-60,-16,-17,-54,-13,-18,-20,-14,-19,-21,-56,]),'LSTATE':([3,4,5,6,7,8,9,17,18,19,20,21,25,30,32,33,34,37,38,42,43,49,50,66,68,69,70,71,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,109,112,113,114,115,119,131,133,135,140,141,142,143,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,31,-12,-50,-1,-37,-44,-41,-38,-39,-45,72,-2,80,-42,-40,-53,-52,-51,108,110,111,-11,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,-55,-60,123,127,-16,-17,-54,130,-13,-18,-20,-14,-19,-21,-56,]),'RSTATE':([3,4,5,6,7,8,9,17,18,19,21,25,30,32,33,34,37,38,42,49,66,68,69,70,71,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,113,114,115,116,118,122,124,126,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,-12,-50,-1,-37,-44,-41,-38,-39,-45,-2,-42,-40,-53,-52,-51,114,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,115,-63,-55,-60,-16,-17,-54,-57,-63,131,133,135,-63,-63,-13,140,-18,141,-20,142,-58,-59,143,-14,-19,-21,-56,]),'OTHERWISE':([6,80,131,140,],[20,113,-13,-14,]),'EQU':([10,11,25,69,70,104,],[22,24,43,-53,-52,119,]),'LARRY':([10,25,32,],[23,44,23,]),'LPAREN':([13,14,15,16,22,24,27,28,29,35,36,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,],[26,27,28,29,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'MINUS':([22,24,27,28,29,32,33,34,35,36,37,38,42,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[35,35,35,35,35,-37,53,62,35,35,-38,-39,53,53,53,53,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-42,53,-40,-53,-52,35,-22,-25,-28,-31,-34,53,53,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,53,]),'NUM':([22,23,24,27,28,29,35,36,43,44,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,75,117,130,],[38,41,38,38,38,38,38,38,38,73,38,38,38,38,38,38,38,38,38,38,38,38,38,38,103,38,128,103,]),'HEXT':([22,24,27,28,29,35,36,43,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'PLUS':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,52,61,-38,-39,52,52,52,52,-42,52,-40,-53,-52,-22,-25,-28,-31,-34,52,52,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,52,]),'MUL':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,54,63,-38,-39,54,54,54,54,54,54,-40,-53,-52,54,54,-28,-31,-34,54,54,-48,-49,63,54,63,54,-29,-30,-32,-33,-35,-36,-43,54,]),'DIV':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,55,64,-38,-39,55,55,55,55,55,55,-40,-53,-52,55,55,-28,-31,-34,55,55,-48,-49,64,55,64,55,-29,-30,-32,-33,-35,-36,-43,55,]),'MOD':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,56,65,-38,-39,56,56,56,56,56,56,-40,-53,-52,56,56,-28,-31,-34,56,56,-48,-49,65,56,65,56,-29,-30,-32,-33,-35,-36,-43,56,]),'EQUTO':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,57,-41,-38,-39,57,57,57,57,-42,57,-40,-53,-52,-22,-25,-28,-31,-34,57,57,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,57,]),'NOEQU':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,58,-41,-38,-39,58,58,58,58,-42,58,-40,-53,-52,-22,-25,-28,-31,-34,58,58,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,58,]),'LESS':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,59,-41,-38,-39,59,59,59,59,59,59,-40,-53,-52,59,59,59,59,59,59,59,-48,-49,-23,59,-26,59,-29,59,-32,59,-35,59,-43,59,]),'MORE':([32,33,34,37,38,42,46,47,48,66,67,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,60,-41,-38,-39,60,60,60,60,60,60,-40,-53,-52,60,60,60,60,60,60,60,-48,-49,-23,60,-26,60,-29,60,-32,60,-35,60,-43,60,]),'RPAREN':([32,34,37,38,45,46,47,48,66,67,68,69,70,74,76,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,120,121,],[-37,-41,-38,-39,-63,77,78,79,-42,101,-40,-53,-52,105,-63,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,-63,-63,-61,-62,]),',':([32,34,37,38,45,66,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,],[-37,-41,-38,-39,75,-42,-40,-53,-52,-22,-25,-28,-31,-34,-46,-47,-48,-49,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-43,75,]),'HEX':([39,],[68,]),'RARRY':([40,41,73,],[69,70,104,]),'COMMA':([103,128,],[117,117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,2,17,31,49,51,108,110,111,123,125,127,],[1,18,30,50,30,81,122,124,126,132,134,136,]),'exassign':([0,2,17,31,49,51,108,110,111,123,125,127,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'declare':([0,2,17,31,49,51,108,110,111,123,125,127,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'exprint':([0,2,17,31,49,51,108,110,111,123,125,127,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'exif':([0,2,17,31,49,51,108,110,111,123,125,127,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'exelif':([0,2,17,31,49,51,108,110,111,123,125,127,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'exloop':([0,2,17,31,49,51,108,110,111,123,125,127,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'exrepeat':([0,2,17,31,49,51,108,110,111,123,125,127,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'arraysh':([0,2,17,22,24,27,28,29,31,35,36,43,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,108,110,111,123,125,127,],[11,11,11,37,37,37,37,37,11,37,37,37,11,11,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,11,11,11,11,11,11,]),'exelse':([6,],[19,]),'expression':([22,24,27,28,29,35,36,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,],[33,42,46,47,48,66,67,82,83,84,85,86,87,88,89,90,92,94,96,98,100,106,]),'term':([22,24,27,28,29,35,36,43,52,53,54,55,56,57,58,59,60,61,62,63,64,65,75,],[34,34,34,34,34,34,34,71,34,34,34,34,34,34,34,34,34,91,93,95,97,99,34,]),'printMore':([45,106,],[74,120,]),'empty':([45,76,103,106,107,118,128,129,],[76,107,118,76,121,129,118,138,]),'arrayX':([72,130,],[102,139,]),'arrayY':([103,128,],[116,137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement NEWLINE statement','statement',3,'p_statement_multiple','parser.py',15),
  ('statement -> statement NEWLINE statement NEWLINE','statement',4,'p_statement_multiple','parser.py',16),
  ('statement -> exassign','statement',1,'p_statement_simple','parser.py',20),
  ('statement -> declare','statement',1,'p_statement_simple','parser.py',21),
  ('statement -> exprint','statement',1,'p_statement_simple','parser.py',22),
  ('statement -> exif','statement',1,'p_statement_simple','parser.py',23),
  ('statement -> exelif','statement',1,'p_statement_simple','parser.py',24),
  ('statement -> exloop','statement',1,'p_statement_simple','parser.py',25),
  ('statement -> exrepeat','statement',1,'p_statement_simple','parser.py',26),
  ('statement -> statement NEWLINE','statement',2,'p_statement_simple','parser.py',27),
  ('statement -> NEWLINE statement','statement',2,'p_statement_simple','parser.py',28),
  ('statement -> exloop NEWLINE','statement',2,'p_statement_simple','parser.py',29),
  ('exif -> SO LPAREN expression RPAREN LSTATE statement RSTATE','exif',7,'p_exif','parser.py',40),
  ('exif -> SO LPAREN expression RPAREN NEWLINE LSTATE statement RSTATE','exif',8,'p_exif','parser.py',41),
  ('exelif -> exif exelse','exelif',2,'p_exelif','parser.py',49),
  ('exelse -> OTHERWISE LSTATE statement LSTATE OTHERWISE','exelse',5,'p_exelse','parser.py',54),
  ('exelse -> OTHERWISE LSTATE NEWLINE statement RSTATE','exelse',5,'p_exelse','parser.py',55),
  ('exloop -> LOOP LPAREN expression RPAREN LSTATE statement RSTATE','exloop',7,'p_exloop','parser.py',63),
  ('exloop -> LOOP LPAREN expression RPAREN LSTATE NEWLINE statement RSTATE','exloop',8,'p_exloop','parser.py',64),
  ('exrepeat -> REPEAT LPAREN expression RPAREN LSTATE statement RSTATE','exrepeat',7,'p_exrepeat','parser.py',71),
  ('exrepeat -> REPEAT LPAREN expression RPAREN NEWLINE LSTATE statement RSTATE','exrepeat',8,'p_exrepeat','parser.py',72),
  ('expression -> expression PLUS expression','expression',3,'p_expression_operators','parser.py',80),
  ('expression -> term PLUS term','expression',3,'p_expression_operators','parser.py',81),
  ('expression -> term PLUS expression','expression',3,'p_expression_operators','parser.py',82),
  ('expression -> expression MINUS expression','expression',3,'p_expression_operators','parser.py',83),
  ('expression -> term MINUS term','expression',3,'p_expression_operators','parser.py',84),
  ('expression -> term MINUS expression','expression',3,'p_expression_operators','parser.py',85),
  ('expression -> expression MUL expression','expression',3,'p_expression_operators','parser.py',86),
  ('expression -> term MUL term','expression',3,'p_expression_operators','parser.py',87),
  ('expression -> term MUL expression','expression',3,'p_expression_operators','parser.py',88),
  ('expression -> expression DIV expression','expression',3,'p_expression_operators','parser.py',89),
  ('expression -> term DIV term','expression',3,'p_expression_operators','parser.py',90),
  ('expression -> term DIV expression','expression',3,'p_expression_operators','parser.py',91),
  ('expression -> expression MOD expression','expression',3,'p_expression_operators','parser.py',92),
  ('expression -> term MOD term','expression',3,'p_expression_operators','parser.py',93),
  ('expression -> term MOD expression','expression',3,'p_expression_operators','parser.py',94),
  ('term -> WORD','term',1,'p_value','parser.py',107),
  ('term -> arraysh','term',1,'p_value','parser.py',108),
  ('term -> NUM','term',1,'p_value','parser.py',109),
  ('term -> HEXT HEX','term',2,'p_value_hex','parser.py',113),
  ('expression -> term','expression',1,'p_expression_standalone','parser.py',118),
  ('expression -> MINUS expression','expression',2,'p_expression_negative','parser.py',123),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parenthesis','parser.py',128),
  ('exassign -> WORD EQU expression','exassign',3,'p_expression_assign','parser.py',132),
  ('exassign -> arraysh EQU expression','exassign',3,'p_expression_assign','parser.py',133),
  ('expression -> expression EQUTO expression','expression',3,'p_expression_EQUTO','parser.py',139),
  ('expression -> expression NOEQU expression','expression',3,'p_expression_NEQU','parser.py',143),
  ('expression -> expression LESS expression','expression',3,'p_expression_LESS','parser.py',148),
  ('expression -> expression MORE expression','expression',3,'p_expression_MORE','parser.py',153),
  ('declare -> DECL WORD','declare',2,'p_declare_const','parser.py',161),
  ('declare -> DECL WORD EQU term','declare',4,'p_declare_const','parser.py',162),
  ('arraysh -> WORD LARRY NUM RARRY','arraysh',4,'p_defineexp_arrayshort','parser.py',171),
  ('arraysh -> WORD LARRY WORD RARRY','arraysh',4,'p_defineexp_arrayshort','parser.py',172),
  ('declare -> DECL WORD EQU LSTATE arrayX RSTATE','declare',6,'p_defineexp_arraya','parser.py',176),
  ('declare -> DECL WORD LARRY NUM RARRY','declare',5,'p_defineexp_arrayb','parser.py',181),
  ('declare -> DECL WORD LARRY NUM RARRY EQU LSTATE arrayX RSTATE','declare',9,'p_defineexp_arrayc','parser.py',186),
  ('arrayX -> NUM arrayY','arrayX',2,'p_arrayX_simple','parser.py',191),
  ('arrayY -> COMMA NUM arrayY','arrayY',3,'p_arrayY_simple','parser.py',196),
  ('arrayY -> empty empty empty','arrayY',3,'p_arrayY_simple','parser.py',197),
  ('exprint -> TEXT LPAREN WORD printMore RPAREN','exprint',5,'p_exprint','parser.py',206),
  ('printMore -> , expression printMore','printMore',3,'p_print_content','parser.py',211),
  ('printMore -> empty empty empty','printMore',3,'p_print_content','parser.py',212),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',219),
]
