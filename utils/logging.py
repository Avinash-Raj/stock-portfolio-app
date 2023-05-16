import logging

from PySide6 import QtCore


def qt_message_handler(mode, context, message):
    # convert Qt message type to Python logging level
    if mode == QtCore.QtMsgType.QtDebugMsg:
        level = logging.DEBUG
    elif mode == QtCore.QtMsgType.QtInfoMsg:
        level = logging.INFO
    elif mode == QtCore.QtMsgType.QtWarningMsg:
        level = logging.WARNING
    elif mode == QtCore.QtMsgType.QtCriticalMsg:
        level = logging.CRITICAL
    else:
        level = logging.ERROR

    # log the message using Python's logging module
    logging.log(level, message)


def setup_logging():
    # install the custom message handler
    QtCore.qInstallMessageHandler(qt_message_handler)

    # configure Python's logging module
    logging.basicConfig(level=logging.DEBUG)
