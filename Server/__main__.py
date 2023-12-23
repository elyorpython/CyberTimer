import sys
from DataBase import DataBase
from MainWindow import MainWindow

app = DataBase(sys.argv)
main_window = MainWindow()
main_window.showMaximized()

result = app.exec()
sys.exit(result)