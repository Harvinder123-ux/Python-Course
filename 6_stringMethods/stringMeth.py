#before goint to string methods lets little talk about idetation in python
def function():
    print(); #the space around tell us you are in function


#now lets talk about string methods
name = "abhii"
num = "7"

#strings is immutable - mean we cant change them although with the print we can create another same string with the same value
print(name[0:3])#will start from zero and go till 2 {3-1} (n-1)
print(name[1:4])#will start from zero and go till 3 {4-1} (n-1)
print(name.upper()) #is used for covert text in uppercases
print(name.capitalize()) #is used for covert the text/word first letter in capitalize
print(name.count("i")) #is used for count the chracters in word or string
print(name.isalnum()) #is word alphanumeric mean is its does contain alphabets and numbers expact special chracters like $%#*\
print(num.isnumeric()) #is the value is in numbers or not
print(num.isalpha())  #is aplphabetic



# some other thing about string we can write string python in these ways
name = "abhi"
name2 = 'abhi'\
       'is good boy'
name3 = '''abhi is a alone 
and the honored one'''

print(name, name2, name3)


