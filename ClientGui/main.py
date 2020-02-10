from ClientGui.DatbaseCheck import DatabaseCheck
from ClientGui.Login import Login
from ClientGui.MainGui import MainGui


def main():
    if DatabaseCheck(None, None, None).check_ip() is True:
        MainGui(None).run()
    else:
        Login().run()


if __name__ == '__main__':
    main()
