# Standard Library Imports
# ----------------------------------------------------------------
import sys
from os.path import exists

# 3rd Party Imports
# ----------------------------------------------------------------
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QPushButton,
    QTableView, 
    QVBoxLayout,
    QLabel,
    QWidget,
    QDialog,
    QDialogButtonBox,
    QMenu
)
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
# ----------------------------------------------------------------

class AddItemDlg(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Item to Database")
        buttons = QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Cancel
        
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = QLabel("Something happened, would you like to apply changes?")
        self.layout.addWidget(msg)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class InitDBDlg(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Initialize Database?")
        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = QLabel("Are you sure you would like to initialize the database?")
        self.layout.addWidget(msg)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Widget Definitions
        # ----------------------------------------------------------------
        top_label = QLabel("Data from 'projects.db':")
        top_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        bot_label = QLabel("Function Buttons:")
        self.db_view = QTableView()

        init_db_btn = QPushButton("Create Database")
        init_db_btn.clicked.connect(self.init_db_btn)

        del_db_btn = QPushButton("Delete Database")
        del_db_btn.clicked.connect(self.del_db_btn)

        add_btn = QPushButton("Add Item")
        add_btn.clicked.connect(self.add_btn)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_view)
        # ----------------------------------------------------------------

        # Layout Definition
        # ----------------------------------------------------------------
        layout = QVBoxLayout()
        layout.addWidget(top_label)
        layout.addWidget(self.db_view)
        layout.addWidget(bot_label)
        layout.addWidget(init_db_btn)
        layout.addWidget(del_db_btn)
        layout.addWidget(add_btn)
        layout.addWidget(refresh_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # ----------------------------------------------------------------

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    # Function Button Method Definitions:
    # --------------------------------------------------------------------
    def init_db_btn(self):
        if not exists("projects.db"):
            dlg = InitDBDlg()
            if dlg.exec():
                print("DB Initialized!")
            else:
                print("Initialization canceled")
            connection = sqlite3.connect("projects.db")
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE projects
                (url TEXT, descr TEXT, income INTEGER)
            """)
            cursor.execute("""
                INSERT INTO projects VALUES
                ('giraffes.io', 'Uber, but with giraffes', 1900),
                ('dronesweaters.com', 'Clothes for cold drones', 3000),
                ('hummingpro.io', 'Online humming courses', 120000)
            """)
            connection.commit()
        else:
            dlg = QDialog()
            
        
    def del_db_btn(self):
        print("Deleted DB")

    def add_btn(self):
        print("Added item")
        dlg = AddItemDlg(self)
        if dlg.exec():
            print("changes applied!")
        else:
            print("dialog canceled")

    def refresh_view(self):
        print("Refreshed")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()