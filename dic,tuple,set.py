Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4}
s
{1, 2, 3, 4}
s.add(5)
s
{1, 2, 3, 4, 5}
s.update([6,7])
s
{1, 2, 3, 4, 5, 6, 7}
s.discard(3)
s
{1, 2, 4, 5, 6, 7}
s.remove(2)
s
{1, 4, 5, 6, 7}
s.remove(3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.remove(3)
KeyError: 3
s1={3,4,5,6,7}
s2={1,2,3,4,5}
s1|s2
{1, 2, 3, 4, 5, 6, 7}
s1&s2
{3, 4, 5}
s1-s2
{6, 7}
s2-s1
{1, 2}
{1, 2}
{1, 2}
type(s1)
<class 'set'>
ss={1,2,3,4,5,1,2,3
    ss
    
SyntaxError: '{' was never closed
    ss={1,2,3,4,5,1,2,3}
    
SyntaxError: unexpected indent
ss={1,2,3,4,5,1,2,3}
    
ss
    
{1, 2, 3, 4, 5}
print(s1.symmetric_difference(s2))
    
{1, 2, 6, 7}
s1.issuperset(s2)
    
False
t=(1,2,3,4,"pavan")
    
t
    
(1, 2, 3, 4, 'pavan')
t=(1,2,3,4,"pavan")

t

(1, 2, 3, 4, 'pavan')
    
SyntaxError: multiple statements found while compiling a single statement
t.index(4)
    
3
t.count(4)
    
1
d={1:"pavan",2:"icecream"}
    
d
    
{1: 'pavan', 2: 'icecream'}
d.key([1,2])
    
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d.key([1,2])
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
dict_keys([1,2])
    
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict_keys([1,2])
NameError: name 'dict_keys' is not defined
d.keys()
...     
dict_keys([1, 2])
>>> d.values()
...     
dict_values(['pavan', 'icecream'])
>>> d.items()
...     
dict_items([(1, 'pavan'), (2, 'icecream')])
>>> l=[1,2,3,4]
...     
>>> tuple.(l)
...     
SyntaxError: invalid syntax
>>> tuple(l)
...     
(1, 2, 3, 4)
>>> d={sys:'paper',sep:"pen"}
...     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d={sys:'paper',sep:"pen"}
NameError: name 'sys' is not defined. Did you mean: 'ss'?
>>> d={ss:'paper',sep:"pen"}
...     
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d={ss:'paper',sep:"pen"}
NameError: name 'sep' is not defined. Did you mean: 'set'?
>>> KeyboardInterrupt
>>> KeyboardInterrupt
