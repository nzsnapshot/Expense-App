def main():
    try:
        a = int(input('Enter a number: '))
        if a != int:
            print('False')
        else:
            print("True")
    except ValueError: 
        a = input("Please enter another number:")

main()