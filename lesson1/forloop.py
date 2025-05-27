for letter in range(ord('a'), ord('z') + 1):
    print(chr(letter))
    
    for _ in range(3):
        print(chr(letter), end=' ')

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)