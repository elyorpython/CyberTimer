from PyQt6.QtWidgets import QMenuBar, QToolBar
from PyQt6.QtGui import QAction


class MainMenu(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Menu System
        main_menu = self.addMenu('Система')
        self.__system_connect = main_menu.addAction('Подключиться')
        self.__system_disconnect = main_menu.addAction('Отключиться')
        main_menu.addSeparator()
        self.__change_pass = main_menu.addAction('Сменить пароль')
        # Change language
        self.__change_lang = main_menu.addMenu('Язык')
        main_menu.addSeparator()
        self.__change_lang_ru = self.__change_lang.addAction('Русский')
        self.__change_lang_uz = self.__change_lang.addAction('Узбецкий')
        self.__exit = main_menu.addAction('Выход')
        # Menu view
        view_menu = self.addMenu('Вид')
        self.__runpad = view_menu.addAction('RunPad')
        # Actions menu
        actions_menu = self.addMenu('Действия')
        self.__get_started = actions_menu.addAction('Начать работу')
        self.__get_stopped = actions_menu.addAction('Завершить работу')
        self.__return_part_money = actions_menu.addAction('Вернуть часть сдачи')
        self.__transfer_client = actions_menu.addAction('Пересадить клиеннта')
        self.__pay_addition = actions_menu.addAction('Доплатить')
        actions_menu.addSeparator()
        self.__services = actions_menu.addAction('Услуги')
        actions_menu.addSeparator()
        self.__to_book = actions_menu.addAction('Забронировать')
        self.__cancel_book = actions_menu.addAction('Отменить бронь')
        actions_menu.addSeparator()
        # Sub menu fine
        self.__fine = actions_menu.addMenu('Штраф')
        self.__one_minutes = self.__fine.addAction('1 минута')
        self.__two_minutes = self.__fine.addAction('2 минуты')
        self.__five_minutes = self.__fine.addAction('5 минут')
        self.__ten_minutes = self.__fine.addAction('10 минута')
        self.__fifteen_minutes = self.__fine.addAction('15 минут')
        self.__add_free_time = actions_menu.addAction('Добавить бесплатное время')
        self.__change_tarif = actions_menu.addAction('Сменить тариф')
        actions_menu.addSeparator()
        self.__allow_auth = actions_menu.addAction('Разрешить авторизацию')
        actions_menu.addSeparator()
        # Addtional Functions menu
        self.__addtional_functions = actions_menu.addMenu('Дополнительные функции')
        self.__repair = self.__addtional_functions.addAction('Ремонт')
        self.__addtional_functions.addSeparator()
        self.__logoff = self.__addtional_functions.addAction('Выйти из системы')
        self.__reoot_system = self.__addtional_functions.addAction('Перезагрузка')
        self.__shutdown_system = self.__addtional_functions.addAction('Выключить')
        self.__powen_on = self.__addtional_functions.addAction('Включить')
        self.__complete_tasks = self.__addtional_functions.addAction('Завершить задачи')
        self.__complete_processes_according_tmpl = self.__addtional_functions.addAction('Завершить процессы по шаблону')
        self.__addtional_functions.addSeparator()
        self.__shell_mode = self.__addtional_functions.addAction('Шелл режим')
        self.__upgrade_programm = self.__addtional_functions.addAction('Обновления')
        self.__change_volume_comp = actions_menu.addAction('Изменить громкость на компютере')
        # Operator menu
        operator_menu = self.addMenu('Оператор')
        self.__end_shift = operator_menu.addAction('Завершить смену')
        operator_menu.addSeparator()
        self.__addtional_services = operator_menu.addAction('Дополнительные услуги')
        self.__custoomer_accouunts = operator_menu.addAction('Учетные записи клиентов')
        self.__paying_new_account = operator_menu.addAction('Оплатить новую учетную запись')
        self.__recent_sessions = operator_menu.addAction('Последние сессии')
        operator_menu.addSeparator()
        self.__change_vol_all_comp = operator_menu.addAction('Изменить громкость всего клуба')
        operator_menu.addSeparator()
        self.__show_info_computer = operator_menu.addAction('Информация о компьютере')
        self.__change_backg_color = operator_menu.addAction('Изменить цвет фона')
        self.__settings_interface = operator_menu.addAction('Настройка интерфейса')
        # Manager menu
        manager_menu = self.addMenu('Менеджер')
        self.__get_money = manager_menu.addAction('Забрать деньги')
        manager_menu.addSeparator()
        self.__print_x_report = manager_menu.addAction('Х-отчет')
        self.__print_z_report = manager_menu.addAction('Z-отчет')
        manager_menu.addSeparator()
        self.__tuz_control_clients = manager_menu.addAction('Управление TimerUz клиентами')
        self.__account_clients_manager = manager_menu.addAction('Учетные записи клиентов')
        self.__settings_system = manager_menu.addAction('Настройка программы')
        manager_menu.addSeparator()
        self.__clear_statistic = manager_menu.addAction('Отчистка статстики')
        # Help menu
        help_menu = self.addMenu('Помощь')
        self.__help = help_menu.addAction('Помощь')
        self.__about_tuz = help_menu.addAction('О программе')

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
        return self.__runpad

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
