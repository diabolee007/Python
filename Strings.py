print(len('Hello world')) #returns 11
print(len('America')) #returns 7

country = 'united states'

print(str.upper('united states')) # will print in caps
print(str.lower('EBCDIC')) # will print lowercase

print(str (22/7)) # will print as text

print('hello world' [0:5]) # will only print hello

print('God speed America'[:-9]) # will print from 4 character to 9th or negative to start from right

message = 'this is sample text'
print(message.find('bogus')) # will return index starting point

message='I love my country'
print(message)
m = message.replace('my country', 'USA') # will replace text
print(m)


message = 'They like pizza'
print(message)
p = message.replace('pizza', 'Subway')
print(p)

# marks = int(input('enter marks: '))
#if marks < 0 or marks >100:
#    print('invalid marks')
#elif marks < 50:
#    print('Fail')
#elif marks < 70:
#    print('Pass')
#elif marks < 90:
#    print('Merit')
#else:
#    print('Distinction')


for c in range(10):
    print('coffee Please!')


