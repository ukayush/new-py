#Important point about string 
# 1> String constructor is str()
# 2> String literal is string '', "", """""",''''''
# 3> String is a set of sequence of elements
# 4> String is immutable 
# 5> String support indexing
# 6> String support slicing 

#Any thing which is incide ("",'',''')quotes is a string 
a=str(   )                           # the space we can see her is the string , Here str() is an empty string
print(a)
# To prove that it is a string we will >
b=str()
print(type(b),"b")
# NOW ABOUT "INDEXING" through indexing we saperate the perticular thing we wnt from the data tupe
# indexing of any data type starts with 0 when it is starting from left to right.
# and ndexing of any data type starts with -1 when it is starting from right to left.
# example =     When right to left. =   -5,-4,-3,-2,-1
#                   Data type =          A, Y, U, S, H
#               When left to right.=     0, 1, 2, 3, 4
# For example i only need 'U' from AYUSH then i will >
s="AYUSH"
print(s[2])        #As result i got 'U' as i desire when i use the left to right way
s="AYUSH"
print(s[-3])       #As result i got 'U' as i desire when i use the right to left way