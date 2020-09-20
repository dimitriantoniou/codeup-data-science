#float
type(99.9)

"False"
#str
type("False")

False
#bool
type(False)

'0'
#str
type('0')

0
#int
type(0)

True
#bool
type(True)

'True'
#str
type('True')

[{}]
#tuple
type([{}])

{'a': []}
#dict
type({'a':[]})


print('1' + 2)
#12
print(6 % 4)
#2
type(6 % 4)
#int
type(type(6 % 4))
#int
print('3 + 4 is ' + 3 + 4)
#3 + 4 is 7
print(0 < 0)
#false
print('False' == False)
#true
print(True == 'True')
#true
print(5 >= -5)
#true
#print(!False or False)
#true
print(True or "42")
#true
#print(!True && !False)
#false
print(6 % 5)
#1
print(5 < 4 and 1 == 1)
#false
print('codeup' == 'codeup' and 'codeup' == 'Codeup')
#false
#print(4 >= 0 and 1 !== '1')
#false
print(6 % 3 == 0)
#true
print(5 % 2 != 0)
#true
print([1] + 2)
#undefined
print([1] + [2])
#1,2
[1] * 2
[1] * [2]
[] + [] == []
{} + {}