from PySide6.QtWidgets import QErrorMessage


def show_error_message(text, parent=None):
    """
    Supposed to show error message.

    Args:
        text (str): Error text
    """
    message_box = QErrorMessage(parent)
    message_box.setWindowTitle("Validation Error")
    message_box.showMessage(text)
