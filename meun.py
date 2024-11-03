from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication([])

menu_window = QWidget()

text = QLabel("Hello World")

line = QVBoxLayout()
line.addWidget(text)
menu_window.setLayout(line)

menu_window.show()

app.exec()