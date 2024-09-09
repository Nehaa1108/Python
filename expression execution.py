# string and Numeric values can operate together with *
a,b =2,3
txt="@"
print(2*txt*3)

# string and string can operate with +(concatenation)
a,b ="2",3
txt="@"
print((a+txt)*3)

# numeric values can operate with all arithmetic operators

a,b=2,3
c=4
print(a+b*c)

# arithmetic expression with integer and float will result in float
a,b=2,3.0
c=a*b
print(c)

# result of division operator with two integer will be float
a,b=20,3.0
c=a/b
print(c)

# integer division with float and int will given int display as float
# give least number(after roundoff)
a,b=1.5,3
c=a//b
print(c)

# 