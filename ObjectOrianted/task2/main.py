def menu():
    print('==================================')
    print('1.add new rectangle')
    print('2.print all rectangles')
    print('3.print the highest perimeter rectangle')
    print('4.exit')
    print('==================================')

def main():
    list_rectangles = list()
    while True:
        menu()
        choice = int(input('Enter your choice: '))