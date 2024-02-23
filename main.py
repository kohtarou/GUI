import sys
from PySide6.QtWidgets import QApplication
from calendar_widget import CalendarWidget

def main():
    app = QApplication(sys.argv)

    calendar = CalendarWidget()
    calendar.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()