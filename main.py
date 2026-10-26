import importlib
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

SCREENS = {
    "login": "ui_log",
    "registration": "ui_registration",
    "twofa": "ui_2fa",

    "user_main": "ui_user_main",
    "user_exercise": "ui_user_exercise",
    "user_history": "ui_user_history",
    "user_progress": "ui_user_progress",
    "user_export": "ui_user_export",

    "prepod_results": "ui_prepod_results",
    "prepod_rule": "ui_prepod_rule",
    "prepod_exercise": "ui_prepod_exercise",
    "prepod_import": "ui_prepod_import",
    "prepod_trash": "ui_prepod_trash",

    "admin_main": "ui_admin_main",
    "admin_edit_user": "ui_admin_edit_user",
    "admin_results": "ui_admin_results",
    "admin_rule": "ui_admin_rule",
    "admin_copies": "ui_admin_copies",
    "admin_logs": "ui_admin_logs",
    "admin_api": "ui_admin_api",
    "admin_trash_users": "ui_admin_trash_users",
    "admin_trash_rule": "ui_admin_trash_rule",
    "admin_export": "ui_admin_export",
}

START_SCREEN = {
    "admin": "admin_main",
    "prepod": "prepod_results",
    "user": "user_main",
}

SIDEBAR = {
    "user": {
        "Проверка": "user_main",
        "Упражнения": "user_exercise",
        "История": "user_history",
        "Прогресс": "user_progress",
    },
    "prepod": {
        "Результаты": "prepod_results",
        "Правила": "prepod_rule",
        "Упражнения": "prepod_exercise",
        "Импорт/Экспорт": "prepod_import",
    },
    "admin": {
        "Главная": "admin_main",
        "Пользователи": "admin_edit_user",
        "Результаты": "admin_results",
        "Справочники": "admin_rule",
        "Копии": "admin_copies",
        "Журналы": "admin_logs",
        "API": "admin_api",
    },
}


EXTRA = {
    "user_history": {"Экспорт": "user_export"},
    "user_progress": {"Экспорт": "user_export"},
    "prepod_rule": {"button_trash": "prepod_trash"},
    "prepod_exercise": {"button_trash": "prepod_trash"},
    "admin_edit_user": {"Экспорт": "admin_export", "button_trash": "admin_trash_users"},
    "admin_rule": {"button_trash": "admin_trash_rule"},
    "admin_results": {"Экспорт": "admin_export"},
    "admin_logs": {"Экспорт": "admin_export"},
}

DIALOGS = {"user_export", "admin_export"}


class Navigator:
    def __init__(self):
        self.window = None
        self.dialog = None
        self.login = ""

    def _build(self, key, parent=None):
        module = importlib.import_module(SCREENS[key])
        win = QMainWindow(parent)
        win.ui = module.Ui_MainWindow()
        win.ui.setupUi(win)
        self._wire(win, key)
        return win

    def go(self, key):
        if self.dialog:
            self.dialog.close()
            self.dialog = None

        new = self._build(key)
        old = self.window

        if old is not None:
            new.resize(old.size())
            new.move(old.pos())
        self.window = new
        if old is not None and old.isMaximized():
            new.showMaximized()
        else:
            new.show()
        if old is not None:
            old.close()

    def open_dialog(self, key):
        if self.dialog:
            self.dialog.close()
        self.dialog = self._build(key, parent=self.window)
        self.dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.dialog.show()

    def _wire(self, win, key):
        ui = win.ui

        if key == "login":
            ui.pushButton.clicked.connect(lambda: self.try_login(win))
            ui.lineEdit_3.returnPressed.connect(lambda: self.try_login(win))
            ui.lineEdit_4.returnPressed.connect(lambda: self.try_login(win))
            ui.pushButton_2.clicked.connect(lambda: self.go("registration"))
            return

        if key == "registration":
            ui.pushButton.clicked.connect(lambda: self.go("twofa"))
            ui.pushButton_2.clicked.connect(lambda: self.go("login"))
            return

        if key == "twofa":
            ui.pushButton.clicked.connect(lambda: self.go("user_main"))
            ui.pushButton_2.clicked.connect(lambda: self.go("registration"))
            return

        role = key.split("_")[0]
        sidebar = SIDEBAR.get(role, {})
        extra = EXTRA.get(key, {})

        for btn in win.findChildren(QPushButton):
            text, name = btn.text(), btn.objectName()

            if text == "Выйти":
                btn.clicked.connect(self.logout)
                continue

            target = extra.get(name) or extra.get(text) or sidebar.get(text)
            if not target or target == key:
                continue
            if target in DIALOGS:
                btn.clicked.connect(lambda checked=False, k=target: self.open_dialog(k))
            else:
                btn.clicked.connect(lambda checked=False, k=target: self.go(k))

        if sidebar and hasattr(ui, "label_6"):
            ui.label_6.setText(self.login)

    def try_login(self, win):
        login = win.ui.lineEdit_3.text().strip().lower()
        start = START_SCREEN.get(login)
        if start is None:
            QMessageBox.warning(
                win, "Вход", "Неверный логин.\nДля проверки введите: admin, prepod или user."
            )
            return
        self.login = login
        self.go(start)

    def logout(self):
        self.login = ""
        self.go("login")


def main():
    app = QApplication(sys.argv)
    nav = Navigator()
    nav.go("login")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()