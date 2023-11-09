#!/usr/bin/env python3.8

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
import random

class SurveyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Survey')
        self.setGeometry(100, 100, 600, 600)
        self.central_widget = QLabel("Are you gay?", self)
        self.central_widget.setAlignment(Qt.AlignCenter)
        self.central_widget.setStyleSheet("font: 20pt Arial; background-color: white;")
        self.setCentralWidget(self.central_widget)

        self.btn_yes = QPushButton('Yes', self)
        self.btn_yes.setGeometry(350, 100, 100, 50)
        self.btn_yes.setStyleSheet("font: 20pt Arial;")
        self.btn_yes.clicked.connect(self.show_known_message)

        self.btn_no = QPushButton('No', self)
        self.btn_no.setGeometry(170, 100, 100, 50)
        self.btn_no.setStyleSheet("font: 20pt Arial;")
        self.btn_no.clicked.connect(self.show_message)
        self.btn_no.enterEvent = self.motion_mouse

    def show_message(self):
        QMessageBox.information(self, '', 'Ah GAYYYYYYYYYYYYYY!')
        self.close()

    def show_known_message(self):
        QMessageBox.information(self, '', "I knew it!")
        self.close()

    def motion_mouse(self, event):
        self.btn_no.move(random.randint(0, 500), random.randint(0, 500))
        window_width = self.geometry().width()
        window_height = self.geometry().height()
        
        current_width = self.btn_yes.geometry().width()
        current_height = self.btn_yes.geometry().height()
        
        new_width = current_width + 50  # Increase width by 50 pixels (0.5 times the initial width)
        new_height = current_height + 50  # Increase height by 50 pixels (0.5 times the initial height)
        
        x_pos = (window_width - new_width) // 2
        y_pos = (window_height - new_height) // 2
        
        self.btn_yes.setGeometry(x_pos, y_pos, new_width, new_height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SurveyWindow()
    window.show()
    sys.exit(app.exec_())