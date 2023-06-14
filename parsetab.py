
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW ASSIGN FNAME LAMBDA LPAREN RPARENline : func\n            | FNAME ASSIGN funcfunc : term\n            | LAMBDA FNAME ARROW functerm : single\n            | term singlesingle : FNAME\n              | LPAREN func RPAREN'
    
_lr_action_items = {'FNAME':([0,3,4,5,6,7,8,9,10,14,15,],[3,-7,10,11,-5,10,10,-6,-7,10,-8,]),'LAMBDA':([0,7,8,14,],[5,5,5,5,]),'LPAREN':([0,3,4,6,7,8,9,10,14,15,],[7,-7,7,-5,7,7,-6,-7,7,-8,]),'$end':([1,2,3,4,6,9,10,13,15,16,],[0,-1,-7,-3,-5,-6,-7,-2,-8,-4,]),'ASSIGN':([3,],[8,]),'RPAREN':([4,6,9,10,12,15,16,],[-3,-5,-6,-7,15,-8,-4,]),'ARROW':([11,],[14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,],[1,]),'func':([0,7,8,14,],[2,12,13,16,]),'term':([0,7,8,14,],[4,4,4,4,]),'single':([0,4,7,8,14,],[6,9,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> func','line',1,'p_line','lcyacc.py',5),
  ('line -> FNAME ASSIGN func','line',3,'p_line','lcyacc.py',6),
  ('func -> term','func',1,'p_func','lcyacc.py',13),
  ('func -> LAMBDA FNAME ARROW func','func',4,'p_func','lcyacc.py',14),
  ('term -> single','term',1,'p_term','lcyacc.py',21),
  ('term -> term single','term',2,'p_term','lcyacc.py',22),
  ('single -> FNAME','single',1,'p_single','lcyacc.py',29),
  ('single -> LPAREN func RPAREN','single',3,'p_single','lcyacc.py',30),
]
