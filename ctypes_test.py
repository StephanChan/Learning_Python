from ctypes import *
string_buffer=create_string_buffer(10)
string_buffer.value=b"hello"#always put b before the string
print('string_buffer: ',string_buffer.raw)
print('string_buffer_id',id(string_buffer))
string_buffer.value=b'world'
print('string_buffer_id',id(string_buffer))#create_string_buffer type are mutable

p=c_char_p(b"hello!")
print('p: ',p.value)
print('p_id: ',id(p))
p=c_char_p(b"world")
print('p_id: ',id(p))#c_char_p type are imutable, so the id changed

num=c_int(3)
print('pointer of integer: ',byref(num))# pointer_to_int instance, it can only be use in c functions
print('contents in pointer: ',pointer(num).contents)#really create a pointer, but slower than byref
#pointer(num) equals to POINTER(c_int)(num)
class POINT(Structure):#python version of structure in C
    _fields_=[('x',c_int),('y',c_int*3)]


a_point=POINT(1,(2,3,4))#initiate structure
print('a_point.x: ',a_point.x)
print('a_point.y: ',a_point.y[0])

class a_pointer(Structure):
    _fields_=[('values',POINTER(c_int))]#pointer_to_c_int type
a_c_list=(c_int*3)(1,2,3)#create c_int array
my_pointer=a_pointer(a_c_list)# or use pointer(num) as parameter
print('my_pointer.values: ',my_pointer.values[1])

cast_type=cast((c_long*3)(2,3,4),POINTER(c_double))#pointer type conversion use cast
print('cast type: ',type(cast_type))

#c_int.in_dll(dllname,"variable name")
#create a pointer array of c_int array in python
p_type=POINTER(c_int)
d2=(p_type*3)()
c_list=(c_int*10)()
py_list=[1,2,3,4,5,6,7,8,9,0]
for i in range(len(py_list)):
    c_list[i]=c_int(py_list[i])
d2[0]=c_list
print(d2[0])






