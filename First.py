def firstfunction():
    print("Hello world!")
    print('What is your name?')
    myName = input()
    print('It is good to meet you, ' +myName)
    print('The length of my name is: ')
    print(len(myName))

if __name__ == '__main__':
    firstfunction()