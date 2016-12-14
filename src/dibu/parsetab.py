
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '17CBB4B9FC36E63F9C3779C9A905EB2B'
    
_lr_action_items = {'RPAREN':([23,24,],[25,26,]),'STRING':([8,],[9,]),'EQUALS':([7,],[8,]),'LBRACKET':([8,],[10,]),'NUM':([8,12,14,20,22,],[11,16,18,23,24,]),'COMMA':([9,11,13,16,18,19,25,26,],[-8,-7,17,20,22,-10,-9,27,]),'LPAREN':([8,10,27,],[12,14,14,]),'RBRACKET':([15,26,28,],[19,-11,-12,]),'ID':([0,2,4,6,9,11,13,17,19,21,25,],[4,4,7,-4,-8,-7,-5,7,-10,-6,-9,]),'$end':([0,1,2,3,5,6,9,11,13,19,21,25,],[-3,0,-3,-1,-2,-4,-8,-7,-5,-10,-6,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'state':([0,2,],[2,2,]),'program':([0,2,],[3,5,]),'params':([4,17,],[6,21,]),'valor':([8,],[13,]),'array':([10,27,],[15,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> program','start',1,'p_start','parser_rules.py',20),
  ('program -> state program','program',2,'p_program_nonempty','parser_rules.py',37),
  ('program -> <empty>','program',0,'p_program_empty','parser_rules.py',41),
  ('state -> ID params','state',2,'p_state','parser_rules.py',45),
  ('params -> ID EQUALS valor','params',3,'p_params_nonrecursive','parser_rules.py',80),
  ('params -> ID EQUALS valor COMMA params','params',5,'p_params_recursive','parser_rules.py',86),
  ('valor -> NUM','valor',1,'p_valor_number','parser_rules.py',95),
  ('valor -> STRING','valor',1,'p_valor_string','parser_rules.py',99),
  ('valor -> LPAREN NUM COMMA NUM RPAREN','valor',5,'p_valor_point','parser_rules.py',103),
  ('valor -> LBRACKET array RBRACKET','valor',3,'p_valor_array','parser_rules.py',107),
  ('array -> LPAREN NUM COMMA NUM RPAREN','array',5,'p_array_element','parser_rules.py',111),
  ('array -> LPAREN NUM COMMA NUM RPAREN COMMA array','array',7,'p_array_recursive','parser_rules.py',115),
]
