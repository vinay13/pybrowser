from reduction import *
from shift import *
from closure import *
grammar = [
("s", ["P"]), #s -> p
("P", ["(", "P", ")"]), #p -> (p)
("P", []), #p ->
]
tokens = ["(", "(",")", ")"]
def addtochart(theset, index, elt):
if not (elt in theset[index]):
theset[index] = [elt] + theset[index]
return True
return False
def parse(tokens, grammar):
tokens = tokens + ["end_of_input_marker"]
chart = {}
start_rule = grammar[0] #s -> p
for i in range(len(tokens)+1):
chart[i] = [ ]
start_state = (start_rule[0], [], start_rule[1], 0)
chart[0] = [start_state]
for i in range(len(tokens)):
while True:
changes = False
for state in chart[i]:
x = state[0]
ab = state[1]
cd = state[2]
j = state[3]
#current state x->ab.cd , j
#c can also have its own procedure calls
#so computing [CLOSURE]
next_states = closure(grammar,i,x,ab,cd,j)
for next_state in next_states:
changes = addtochart(chart,i,next_state) or changes
#current state x->ab.cd , j
#if token[i] == c
#make a next state x -> abc.d , j
#in chart[i+1] using [SHIFT]
next_states = shift(tokens,i,x,ab,cd,j)
if next_states <> None:
any_changes = addtochart(chart,i+1,next_state) or any_changes
#current state == x->ab.cd , j
#when cd is [] , the state is just x-> ab. , j
#for each p->q.xr , l in chart[j]
# now we do [REDUCTOIN]
next_states = reduction(chart,i,x,ab,cd,j)
for next_state in next_states:
changes = addtochart(chart,i,next_state) or changes
if not changes:
break
# this is pure debugging information so relax!!!
for i in range(len(tokens)):
print "== chart " + str(i)
for state in chart[i]:
x = state[0]
ab = state[1]
cd = state[2]
j = state[3]
print " " + x + "-->",
for sym in ab:
print " " + sym,
print " .",
for sym in cd:
print " " + sym,
print "from " + str(j)
accepting_state = (start_rule[0],start_rule[1],[],0)
return accepting_state in chart[len(tokens)-1]
result = parse(tokens, grammar)
print result
