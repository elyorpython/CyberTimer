from PyQt6.QtWidgets import QMenuBar


class MainMenu(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Menu System
        main_menu = self.addMenu('System')
        self.__system_connect = main_menu.addAction('Connect')
        self.__system_disconnect = main_menu.addAction('Disconnect')
        main_menu.addSeparator()
        self.__change_pass = main_menu.addAction('Change your password')
        # Change language
        self.__change_lang = main_menu.addMenu('Language')
        main_menu.addSeparator()
        self.__change_lang_ru = self.__change_lang.addAction('Russian')
        self.__change_lang_uz = self.__change_lang.addAction('Uzbek')
        self.__exit = main_menu.addAction('Exit')
        # Menu view
        view_menu = self.addMenu('View')
        self.__run_pad = view_menu.addAction('RunPad')
        # Actions menu
        actions_menu = self.addMenu('Actions')
        self.__get_started = actions_menu.addAction('Get started')
        self.__get_stopped = actions_menu.addAction('Get stopped')
        self.__return_part_money = actions_menu.addAction('Return part of the change')
        self.__transfer_client = actions_menu.addAction('Transplant the client')
        self.__pay_addition = actions_menu.addAction('Pay in addition')
        actions_menu.addSeparator()
        self.__services = actions_menu.addAction('Services')
        actions_menu.addSeparator()
        self.__to_book = actions_menu.addAction('Get reservation')
        self.__cancel_book = actions_menu.addAction('Cancel your reservation')
        actions_menu.addSeparator()
        # Sub menu fine
        self.__fine = actions_menu.addMenu('Fine')
        self.__one_minutes = self.__fine.addAction('1 minutes')
        self.__two_minutes = self.__fine.addAction('2 minutes')
        self.__five_minutes = self.__fine.addAction('5 minutes')
        self.__ten_minutes = self.__fine.addAction('10 minutes')
        self.__fifteen_minutes = self.__fine.addAction('15 minutes')
        self.__add_free_time = actions_menu.addAction('Add free time')
        self.__change_tariff = actions_menu.addAction('Change the tariff')
        actions_menu.addSeparator()
        self.__allow_auth = actions_menu.addAction('Allow authorization')
        actions_menu.addSeparator()
        # Additional Functions menu
        self.__additional_functions = actions_menu.addMenu('Additional functions')
        self.__repair = self.__additional_functions.addAction('Repair')
        self.__additional_functions.addSeparator()
        self.__logoff = self.__additional_functions.addAction('Log out of the system')
        self.__reboot_system = self.__additional_functions.addAction('Reboot')
        self.__shutdown_system = self.__additional_functions.addAction('Switch off')
        self.__power_on = self.__additional_functions.addAction('Turn on')
        self.__complete_tasks = self.__additional_functions.addAction('Complete tasks')
        self.__complete_processes_according_tmpl = self.__additional_functions.addAction('Complete the processes '
                                                                                         'according to the template')
        self.__additional_functions.addSeparator()
        self.__shell_mode = self.__additional_functions.addAction('Shell mode')
        self.__upgrade_program = self.__additional_functions.addAction('Updates')
        self.__change_volume_comp = actions_menu.addAction('Change the volume on the computer')
        # Operator menu
        operator_menu = self.addMenu('Operator')
        self.__end_shift = operator_menu.addAction('End the shift')
        operator_menu.addSeparator()
        self.__additional_services = operator_menu.addAction('Additional services')
        self.__customer_accounts = operator_menu.addAction('Customer accounts')
        self.__paying_new_account = operator_menu.addAction('Pay for a new account')
        self.__recent_sessions = operator_menu.addAction('Recent sessions')
        operator_menu.addSeparator()
        self.__change_vol_all_comp = operator_menu.addAction('Change the volume of the entire club')
        operator_menu.addSeparator()
        self.__show_info_computer = operator_menu.addAction('Information about the computer')
        self.__change_background_color = operator_menu.addAction('Change the background color')
        self.__settings_interface = operator_menu.addAction('Configuring the interface')
        # Manager menu
        manager_menu = self.addMenu('Manager')
        self.__get_money = manager_menu.addAction('To take the money')
        manager_menu.addSeparator()
        self.__print_x_report = manager_menu.addAction('Х-reports')
        self.__print_z_report = manager_menu.addAction('Z-reports')
        manager_menu.addSeparator()
        self.__tuz_control_clients = manager_menu.addAction('Managing CyberTimer clients')
        self.__account_clients_manager = manager_menu.addAction('Customer accounts')
        self.__settings_system = manager_menu.addAction('Setting up the program')
        manager_menu.addSeparator()
        self.__clear_statistic = manager_menu.addAction('Cleaning the static')
        # Help menu
        help_menu = self.addMenu('Help')
        self.__help = help_menu.addAction('Help')
        self.__about_cyber = help_menu.addAction('About')

    @property
    def system_connect(self):
        return self.__system_connect

    @property
    def system_disconnect(self):
        return self.__system_disconnect

    @property
    def change_pass(self):
        return self.__change_pass

    @property
    def change_lang(self):
        return self.__change_lang

    @property
    def change_lang_ru(self):
        return self.__change_lang_ru

    @property
    def change_lang_uz(self):
        return self.__change_lang_uz

    @property
    def exit_app(self):
        return self.__exit

    @property
    def runpad(self):
        return self.__run_pad

    @property
    def get_started(self):
        return self.__get_started

    @property
    def get_stopped(self):
        return self.__get_stopped

    @property
    def return_part_money(self):
        return self.__return_part_money

    @property
    def transfer_client(self):
        return self.__transfer_client

    @property
    def pay_addition(self):
        return self.__pay_addition

    @property
    def settings_system(self):
        return self.__settings_system
