import sys
from Server.MainWindow import MainWindow
from Server.Application import Application


if __name__ == "__main__":
    connection = Application(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(connection.exec())
