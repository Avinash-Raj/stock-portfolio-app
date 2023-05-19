from PySide6.QtWidgets import QErrorMessage, QMessageBox


def show_error_message(text, parent=None):
    """
    Supposed to show error message.

    Args:
        text (str): Error text
    """
    message_box = QErrorMessage(parent)
    message_box.setWindowTitle("Validation Error")
    message_box.showMessage(text)


def show_success_message(text, parent):
    """
    Supposed to show success message.
    """
    # Create a QMessageBox instance
    message_box = QMessageBox(parent)

    # Set the message box properties
    message_box.setIcon(QMessageBox.Icon.Information)
    message_box.setText(text)
    message_box.setWindowTitle("Success Message")
    # Display the message box
    message_box.exec()
