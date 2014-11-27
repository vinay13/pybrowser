#!usr/bin/python
def closure(grammar, i, x, ab, cd,j):
next_state = [ (rule[0], [], rule[1], j)
for rule in grammar
if cd <> [] and rule[0] == cd[0]
]
return next_state
'''
grammar = [
("exp", ["exp", "+", "exp"]),
("exp", ["exp", "-", "exp"]),
("exp", ["(", "exp", ")"]),
("exp", ["num"]),
("t", ["I", "like", "t"]),
("t", [""])
]
print closure(grammar,0,"exp",["exp","+"],["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp"],["+","exp"]) == []
'''
