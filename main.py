from Progress import Bar
from time import sleep as slp

def main():
    max = 1000
    for i in range(max):
        if i % 10 == 0:
            print(Bar(max, i, True, 'cyan', 'magenta', '=', '-'), end='\r')
        slp(0.1)

if __name__ == '__main__':
    main()