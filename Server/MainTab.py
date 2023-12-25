from PyQt6.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QTableView, QListWidget


class MainTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        sessions_tab_widget = QWidget()
        message_tab_widget = QWidget()
        reports_tab_widget = QWidget()

        self.addTab(sessions_tab_widget, "Sessions")
        self.addTab(message_tab_widget, "Messages")
        self.addTab(reports_tab_widget, "Reports")

        computer_tab_layout = QVBoxLayout(sessions_tab_widget)
        sessions_list = QListWidget()
        computer_tab_layout.addWidget(sessions_list)

        message_tab_layout = QVBoxLayout(message_tab_widget)
        message_log_table = QTableView()
        message_tab_layout.addWidget(message_log_table)

        reports_tab_layout = QVBoxLayout(reports_tab_widget)
        reports_tab_table = QTableView()
        reports_tab_layout.addWidget(reports_tab_table)
