from colorama import Fore, Back

def Bar(min: float, max: float, actual: float, get=False, Color="None", BG="None", char='|', space=' '):

    if (len(char) > 1 or len(char) < 1):
        char = '|'

    if (len(space) > 1 or len(space) < 1):
        space = ' '

    if (space == char):
        space = ' '
        char = '|'

    printString = ''
    match Color.lower():
        case 'green':
            printString += Fore.GREEN
        case 'blue':
            printString += Fore.BLUE
        case 'red':
            printString += Fore.RED
        case 'magenta':
            printString += Fore.MAGENTA
        case 'cyan':
            printString += Fore.CYAN
        case 'white':
            printString += Fore.WHITE
        case 'yellow':
            printString += Fore.YELLOW
        case 'black':
            printString += Fore.BLACK
    
    match BG.lower():
        case 'green':
            printString += Back.GREEN
        case 'blue':
            printString += Back.BLUE
        case 'red':
            printString += Back.RED
        case 'magenta':
            printString += Back.MAGENTA
        case 'cyan':
            printString += Back.CYAN
        case 'white':
            printString += Back.WHITE
        case 'yellow':
            printString += Back.YELLOW
        case 'black':
            printString += Back.BLACK

    printString += f'{int((actual / max) * 100)}% '

    actualPercent = int((actual / max) * 100)

    for i in range(actualPercent):
        printString += char

    for i in range(100 - actualPercent):
        printString += space

    printString += f'  {actual}/{max}'

    if not get:
        print(printString, end="\r")
    else:
        return printString