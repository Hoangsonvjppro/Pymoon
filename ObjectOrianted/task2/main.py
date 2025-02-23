from ObjectOrianted.task2.Rectangle import Rectangle as Rect

def menu():
    print('==================================')
    print('1.add new rectangle')
    print('2.print all rectangles')
    print('3.print the highest perimeter rectangle')
    print('4.exit')
    print('==================================')

def main():
    list_rectangles = []
    while True:
        menu()
        try:
            choice = int(input('Enter your choice: '))
            if choice not in (1, 2, 3, 4):
                print('Invalid choice')
            if choice == 4:
                break
        except ValueError:
            print('Invalid input')
            continue

        if choice == 1:
            length, width = map(float, input('Enter your length and width: ').split(','))
            if length <= 0 or width <= 0:
                print('Length and width must be positive')
                continue
            rect = Rect(length, width)
            list_rectangles.append(rect)
        elif choice == 2:
            for R in list_rectangles:
                print(R.to_string())
        elif choice == 3:
            max_perimeter = 0
            max_rect = None
            for rect in list_rectangles:
                if rect.perimeter() > max_perimeter:
                    max_perimeter = rect.perimeter()
                    max_rect = rect
            if max_rect is not None:
                print(max_rect.to_string())
            else:
                print('No rectangles found')

if __name__ == '__main__':
    main()