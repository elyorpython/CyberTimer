from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow
from Server.MainMenu import MainMenu
from Server.MainToolbar import MainToolbar
from Server.MainTab import MainTab


class MainWindow(QMainWindow):
    """The main window of the CyberClubTimer program"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cyber_ui()

    # The main thing is to display the elements of the main window
    def cyber_ui(self):
        self.setWindowTitle("CYBER TIMER")

        # Connecting the main menu
        self.__create_main_menu()
        # Connecting the main toolbar
        self.__main_toolbar()
        # Connecting the main tab widget
        self.__main_tab_widget()

    # Create Main menu Cyber Club Timer
    def __create_main_menu(self):
        self.cyber_main_menu = MainMenu(parent=self)
        self.setMenuBar(self.cyber_main_menu)

        self.cyber_main_menu.exit_app.triggered.connect(self.close)

    # Create Main toolbar Cyber Club Timer
    def __main_toolbar(self):
        self.cyber_main_toolbar = MainToolbar(main_menu=self.cyber_main_menu, parent=self)
        self.addToolBar(self.cyber_main_toolbar)
        self.cyber_main_toolbar.setIconSize(QSize(35, 35))

    # Create Main tab widget
    def __main_tab_widget(self):
        self.main_tab_widget = MainTab(parent=self)
        self.setCentralWidget(self.main_tab_widget)
