#!/usr/bin/python
def shift(tokens, i, x, ab, cd, j):
if cd <> [] and tokens[i] == cd[0]:
return (x, ab+[cd[0]], cd[1:], j)
else:
return None
'''
print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
