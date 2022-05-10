#!/.venv/bin/python3.9
from PyQt6.QtWidgets import *
from PyQt6.QtSql import *
from os.path import exists
import sys
import sqlite3

connection = sqlite3.connect("projects.db")

def init_table():
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

# if not exists("projects.db"):
#     print("File projects.db does not exist. Please run initdb.py...")
#     sys.exit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Install App Test")

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()

        model = QSqlTableModel(None, db)
        model.setTable("projects")
        model.select()

        view = QTableView()
        view.setModel(model)

        create_db_btn = QPushButton("Create Database")

        layout = QVBoxLayout()
        layout.addWidget(view)
        layout.addWidget(create_db_btn)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()