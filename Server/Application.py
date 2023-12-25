import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        database = QSqlDatabase.addDatabase('QPSQL')
        database.setHostName(DATABASE_HOST)
        database.setDatabaseName(DATABASE_NAME)
        database.setPort(DATABASE_PORT)
        database.setUserName(DATABASE_USER)
        database.setPassword(DATABASE_PASSWORD)
        connect_ok = database.open()

        if connect_ok:
            print('Connected to the database', file=sys.stderr)
        else:
            print('Connection FAILED', file=sys.stderr)
