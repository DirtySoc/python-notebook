import sys

function_1_arg, function_2_arg = 'arg1', 'arg2'

mainMenu = {}
mainMenu['1'] = ('Option 1', function_1, function_1_arg)
mainMenu['2'] = ('Option 2', function_2, function_2_arg)
# ...
# mainMenu['N'] = ('Option N', sys.exit, 0)

def main():
    while True:
        print('\n --MAIN MENU-- \n')
        options = mainMenu.keys()
        for option in options:
            print(option, mainMenu[option][0])
        try: # TODO: Handle user input validation...
            selection = input("\nPlease make a selection: ")
            mainMenu[str(selection)][1](mainMenu[str(selection)][2])
        except KeyError:
            print('\nPlease make a correct selection. Try again.\n')
        except Exception as e:
            print("ERROR: " + str(e))

def function_1(arg1):
    print("Welcome to function_1!")
    return

def function_2(arg1):
    print("Welcome to function_2!")
    return

if __name__ == '__main__':
    main()