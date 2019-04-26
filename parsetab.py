
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVMODleftLESSMOREBACK COMMA DECADE DECL DIV EQU EQUTO HEX INT64 LARRY LESS LOOP LPAREN LSTATE MINUS MOD MORE MUL NEWLINE NOEQU NOTSO NUM OTHERWISE PLUS RARRY REPEAT RPAREN RSTATE SEMI SO TEXT WORDstatement : statement NEWLINE statement\n                 | statement NEWLINE statement NEWLINEstatement : exassign\n                 | declare\n                 | exprint\n                 | exif\n                 | exelif\n                 | exloop\n                 | exrepeat\n                 | statement NEWLINE\n                 | NEWLINE statement\n                 | exloop NEWLINE\n                 exif : SO LPAREN expression RPAREN LSTATE statement RSTATE\n             | SO LPAREN expression RPAREN NEWLINE LSTATE statement RSTATEexelif : exif exelseexelse : OTHERWISE LSTATE statement LSTATE OTHERWISE\n               | OTHERWISE LSTATE NEWLINE statement RSTATEexloop : LOOP LPAREN expression RPAREN LSTATE statement RSTATE\n             | LOOP LPAREN expression RPAREN LSTATE NEWLINE statement RSTATEexrepeat : REPEAT LPAREN expression RPAREN LSTATE statement RSTATE\n                | REPEAT LPAREN expression RPAREN NEWLINE LSTATE statement RSTATEexpression : expression PLUS expression                  \n                  | term PLUS term\n                  | term PLUS expression\n                  | expression MINUS expression\n                  | term MINUS term\n                  | term MINUS expression\n                  | expression MUL expression\n                  | term MUL term\n                  | term MUL expression\n                  | expression DIV expression\n                  | term DIV term\n                  | term DIV expression\n                  | expression MOD expression\n                  | term MOD term\n                  | term MOD expressionterm : WORD\n           | arraysh\n           | NUMexpression : termexpression : MINUS expressionexpression : LPAREN expression RPARENexassign : WORD EQU expression\n                  | arraysh EQU expression\n                  expression : expression EQUTO expressionexpression : expression NOEQU expressionexpression : expression LESS expressionexpression : expression MORE expressiondeclare : DECL WORD\n               | DECL WORD EQU termarraysh : WORD LARRY NUM RARRY\n               | WORD LARRY WORD RARRYdeclare : DECL WORD EQU LSTATE arrayX RSTATEdeclare : DECL WORD LARRY NUM RARRYdeclare : DECL WORD LARRY NUM RARRY EQU LSTATE arrayX RSTATEarrayX : NUM arrayYarrayY : COMMA NUM arrayY\n              | empty empty emptyexprint : TEXT LPAREN WORD printMore RPARENprintMore : "," expression printMore\n                 | empty empty emptyempty :'
    
_lr_action_items = {'NEWLINE':([0,1,2,3,4,5,6,7,8,9,17,18,19,21,25,30,31,32,33,34,37,38,41,48,49,50,65,67,68,69,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,106,108,109,111,112,113,120,121,122,123,124,125,129,130,131,132,133,134,138,139,140,141,],[2,17,2,-3,-4,-5,-6,-7,21,-9,2,17,-15,-12,-49,48,50,-37,-43,-40,-38,-39,-44,2,17,2,-41,-52,-51,-50,107,110,17,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,-54,-59,2,123,2,-16,-17,-53,17,2,17,2,17,2,-13,17,-18,17,-20,17,-14,-19,-21,-55,]),'WORD':([0,2,12,17,22,23,24,26,27,28,29,31,35,36,42,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,106,108,109,121,123,125,],[10,10,25,10,32,39,32,44,32,32,32,10,32,32,32,10,10,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,10,10,10,10,10,10,]),'DECL':([0,2,17,31,48,50,106,108,109,121,123,125,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'TEXT':([0,2,17,31,48,50,106,108,109,121,123,125,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'SO':([0,2,17,31,48,50,106,108,109,121,123,125,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'LOOP':([0,2,17,31,48,50,106,108,109,121,123,125,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'REPEAT':([0,2,17,31,48,50,106,108,109,121,123,125,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,3,4,5,6,7,8,9,17,18,19,21,25,30,32,33,34,37,38,41,48,65,67,68,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,111,112,113,129,131,133,138,139,140,141,],[0,-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,-12,-49,-1,-37,-43,-40,-38,-39,-44,-2,-41,-52,-51,-50,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,-54,-59,-16,-17,-53,-13,-18,-20,-14,-19,-21,-55,]),'LSTATE':([3,4,5,6,7,8,9,17,18,19,20,21,25,30,32,33,34,37,38,41,42,48,49,65,67,68,69,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,107,110,111,112,113,117,129,131,133,138,139,140,141,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,31,-12,-49,-1,-37,-43,-40,-38,-39,-44,70,-2,78,-41,-52,-51,-50,106,108,109,-11,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,-54,-59,121,125,-16,-17,-53,128,-13,-18,-20,-14,-19,-21,-55,]),'RSTATE':([3,4,5,6,7,8,9,17,18,19,21,25,30,32,33,34,37,38,41,48,65,67,68,69,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,114,116,120,122,124,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-15,-12,-49,-1,-37,-43,-40,-38,-39,-44,-2,-41,-52,-51,-50,112,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,113,-62,-54,-59,-16,-17,-53,-56,-62,129,131,133,-62,-62,-13,138,-18,139,-20,140,-57,-58,141,-14,-19,-21,-55,]),'OTHERWISE':([6,78,129,138,],[20,111,-13,-14,]),'EQU':([10,11,25,67,68,102,],[22,24,42,-52,-51,117,]),'LARRY':([10,25,32,],[23,43,23,]),'LPAREN':([13,14,15,16,22,24,27,28,29,35,36,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,],[26,27,28,29,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'MINUS':([22,24,27,28,29,32,33,34,35,36,37,38,41,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[35,35,35,35,35,-37,52,61,35,35,-38,-39,52,52,52,52,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-41,52,-52,-51,35,-22,-25,-28,-31,-34,52,52,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,52,]),'NUM':([22,23,24,27,28,29,35,36,42,43,51,52,53,54,55,56,57,58,59,60,61,62,63,64,70,73,115,128,],[38,40,38,38,38,38,38,38,38,71,38,38,38,38,38,38,38,38,38,38,38,38,38,38,101,38,126,101,]),'PLUS':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,51,60,-38,-39,51,51,51,51,-41,51,-52,-51,-22,-25,-28,-31,-34,51,51,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,51,]),'MUL':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,53,62,-38,-39,53,53,53,53,53,53,-52,-51,53,53,-28,-31,-34,53,53,-47,-48,62,53,62,53,-29,-30,-32,-33,-35,-36,-42,53,]),'DIV':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,54,63,-38,-39,54,54,54,54,54,54,-52,-51,54,54,-28,-31,-34,54,54,-47,-48,63,54,63,54,-29,-30,-32,-33,-35,-36,-42,54,]),'MOD':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,55,64,-38,-39,55,55,55,55,55,55,-52,-51,55,55,-28,-31,-34,55,55,-47,-48,64,55,64,55,-29,-30,-32,-33,-35,-36,-42,55,]),'EQUTO':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,56,-40,-38,-39,56,56,56,56,-41,56,-52,-51,-22,-25,-28,-31,-34,56,56,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,56,]),'NOEQU':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,57,-40,-38,-39,57,57,57,57,-41,57,-52,-51,-22,-25,-28,-31,-34,57,57,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,57,]),'LESS':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,58,-40,-38,-39,58,58,58,58,58,58,-52,-51,58,58,58,58,58,58,58,-47,-48,-23,58,-26,58,-29,58,-32,58,-35,58,-42,58,]),'MORE':([32,33,34,37,38,41,45,46,47,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,59,-40,-38,-39,59,59,59,59,59,59,-52,-51,59,59,59,59,59,59,59,-47,-48,-23,59,-26,59,-29,59,-32,59,-35,59,-42,59,]),'RPAREN':([32,34,37,38,44,45,46,47,65,66,67,68,72,74,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,105,118,119,],[-37,-40,-38,-39,-62,75,76,77,-41,99,-52,-51,103,-62,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,-62,-62,-60,-61,]),',':([32,34,37,38,44,65,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,],[-37,-40,-38,-39,73,-41,-52,-51,-22,-25,-28,-31,-34,-45,-46,-47,-48,-23,-24,-26,-27,-29,-30,-32,-33,-35,-36,-42,73,]),'RARRY':([39,40,71,],[67,68,102,]),'COMMA':([101,126,],[115,115,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,2,17,31,48,50,106,108,109,121,123,125,],[1,18,30,49,30,79,120,122,124,130,132,134,]),'exassign':([0,2,17,31,48,50,106,108,109,121,123,125,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'declare':([0,2,17,31,48,50,106,108,109,121,123,125,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'exprint':([0,2,17,31,48,50,106,108,109,121,123,125,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'exif':([0,2,17,31,48,50,106,108,109,121,123,125,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'exelif':([0,2,17,31,48,50,106,108,109,121,123,125,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'exloop':([0,2,17,31,48,50,106,108,109,121,123,125,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'exrepeat':([0,2,17,31,48,50,106,108,109,121,123,125,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'arraysh':([0,2,17,22,24,27,28,29,31,35,36,42,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,106,108,109,121,123,125,],[11,11,11,37,37,37,37,37,11,37,37,37,11,11,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,11,11,11,11,11,11,]),'exelse':([6,],[19,]),'expression':([22,24,27,28,29,35,36,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,],[33,41,45,46,47,65,66,80,81,82,83,84,85,86,87,88,90,92,94,96,98,104,]),'term':([22,24,27,28,29,35,36,42,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,],[34,34,34,34,34,34,34,69,34,34,34,34,34,34,34,34,34,89,91,93,95,97,34,]),'printMore':([44,104,],[72,118,]),'empty':([44,74,101,104,105,116,126,127,],[74,105,116,74,119,127,116,136,]),'arrayX':([70,128,],[100,137,]),'arrayY':([101,126,],[114,135,]),}

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
  ('expression -> term','expression',1,'p_expression_standalone','parser.py',114),
  ('expression -> MINUS expression','expression',2,'p_expression_negative','parser.py',119),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parenthesis','parser.py',124),
  ('exassign -> WORD EQU expression','exassign',3,'p_expression_assign','parser.py',128),
  ('exassign -> arraysh EQU expression','exassign',3,'p_expression_assign','parser.py',129),
  ('expression -> expression EQUTO expression','expression',3,'p_expression_EQUTO','parser.py',135),
  ('expression -> expression NOEQU expression','expression',3,'p_expression_NEQU','parser.py',139),
  ('expression -> expression LESS expression','expression',3,'p_expression_LESS','parser.py',144),
  ('expression -> expression MORE expression','expression',3,'p_expression_MORE','parser.py',149),
  ('declare -> DECL WORD','declare',2,'p_declare_const','parser.py',157),
  ('declare -> DECL WORD EQU term','declare',4,'p_declare_const','parser.py',158),
  ('arraysh -> WORD LARRY NUM RARRY','arraysh',4,'p_defineexp_arrayshort','parser.py',167),
  ('arraysh -> WORD LARRY WORD RARRY','arraysh',4,'p_defineexp_arrayshort','parser.py',168),
  ('declare -> DECL WORD EQU LSTATE arrayX RSTATE','declare',6,'p_defineexp_arraya','parser.py',172),
  ('declare -> DECL WORD LARRY NUM RARRY','declare',5,'p_defineexp_arrayb','parser.py',177),
  ('declare -> DECL WORD LARRY NUM RARRY EQU LSTATE arrayX RSTATE','declare',9,'p_defineexp_arrayc','parser.py',182),
  ('arrayX -> NUM arrayY','arrayX',2,'p_arrayX_simple','parser.py',187),
  ('arrayY -> COMMA NUM arrayY','arrayY',3,'p_arrayY_simple','parser.py',192),
  ('arrayY -> empty empty empty','arrayY',3,'p_arrayY_simple','parser.py',193),
  ('exprint -> TEXT LPAREN WORD printMore RPAREN','exprint',5,'p_exprint','parser.py',202),
  ('printMore -> , expression printMore','printMore',3,'p_print_content','parser.py',207),
  ('printMore -> empty empty empty','printMore',3,'p_print_content','parser.py',208),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',215),
]
