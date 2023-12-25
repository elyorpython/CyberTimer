from PyQt6.QtWidgets import QToolBar, QToolButton


class MainToolbar(QToolBar):
    def __init__(self, main_menu, parent=None):
        super().__init__("Основной панель", parent)
        self.main_menu = main_menu
        self.setMovable(False)
        self.setMinimumHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        # Добавьте действия на тулбар
        get_started_action = self.main_menu.get_started
        pay_addition_action = self.main_menu.pay_addition
        get_stopped_action = self.main_menu.get_stopped
        transfer_client_action = self.main_menu.transfer_client

        # Icon toolbar
        # get_started_action.setIcon(QIcon('../icons/start-time.svg'))
        # pay_addition_action.setIcon(QIcon('../icons/additional-payment.svg'))
        # get_stopped_action.setIcon(QIcon('../icons/stop-time.svg'))
        # transfer_client_action.setIcon(QIcon('../icons/transfer-comp.svg'))

        # Button tooolbar
        get_started_button = QToolButton()
        get_started_button.setDefaultAction(get_started_action)
        pay_addition_button = QToolButton()
        pay_addition_button.setDefaultAction(pay_addition_action)
        get_stopped_button = QToolButton()
        get_stopped_button.setDefaultAction(get_stopped_action)
        transfer_client_button = QToolButton()
        transfer_client_button.setDefaultAction(transfer_client_action)

        self.addAction(get_started_action)
        self.addAction(pay_addition_action)
        self.addAction(get_stopped_action)
        self.addAction(transfer_client_action)
        self.addSeparator()
