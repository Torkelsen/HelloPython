import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        grid = QGridLayout()
        # super() is eq to base in C#
        super().__init__()
        self.setWindowTitle("Age Calculator")
        # Create Widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        dob_label = QLabel("Date of Birth DD/MM/YYYY:")
        self.dob_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        year_of_birth = datetime.strptime(self.dob_line_edit.text(), "%d/%M/%Y").date().year
        age = current_year - year_of_birth
        name = self.name_line_edit.text()
        self.output_label.setText(f"{name} is {age} years old.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
