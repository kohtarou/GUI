from PySide6.QtWidgets import QCalendarWidget

class CalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # ここでカレンダーウィジェットのカスタマイズを行うことができます。