import sys

if sys.platform == "win32":
    from ctypes import windll
    #Enables ANSI escape sequences
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)

class colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    NORMAL = '\033[1;0m'

    BG_RED = '\033[1;41m\033[1;37m'
    BG_GREEN = '\033[1;42m\033[1;37m'
    BG_YELLOW = '\033[1;43m\033[1;37m'
    BG_BLUE = '\033[1;44m\033[1;37m'
    BG_PURPLE = '\033[1;45m\033[1;37m'
    BG_CYAN = '\033[1;46m\033[1;37m'
    BG_WHITE = '\033[1;47m\033[1;30m'

    ENDC = '\033[0m'

    def cprint(color, message, end=None):
        print(color + message + colors.ENDC, end=end)
