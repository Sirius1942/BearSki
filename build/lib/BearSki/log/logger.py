#encoding=utf-8
import logging
import BearSki.RunUnittest as rut


def write(msg, level='INFO', html=False):
    
    lger=_initlogger()
    level = {'TRACE': logging.DEBUG // 2,
                'DEBUG': logging.DEBUG,
                'INFO': logging.INFO,
                'HTML': logging.INFO,
                'WARN': logging.WARN,
                'ERROR': logging.ERROR}[level]
    lger.log(level, msg)

def trace(msg, html=False):
    """Writes the message to the log file using the ``TRACE`` level."""
    write(msg, 'TRACE', html)


def debug(msg, html=False):
    """Writes the message to the log file using the ``DEBUG`` level."""
    write(msg, 'DEBUG', html)


def info(msg, html=False, also_console=False):
    """Writes the message to the log file using the ``INFO`` level.

    If ``also_console`` argument is set to ``True``, the message is
    written both to the log file and to the console.
    """
    write(msg, 'INFO', html)

def warn(msg, html=False):
    """Writes the message to the log file using the ``WARN`` level."""
    write(msg, 'WARN', html)


def error(msg, html=False):
    """Writes the message to the log file using the ``ERROR`` level.

    New in Robot Framework 2.9.
    """
    write(msg, 'ERROR', html)


# def console(msg, newline=True, stream='stdout'):
#     """Writes the message to the console.

#     If the ``newline`` argument is ``True``, a newline character is
#     automatically added to the message.

#     By default the message is written to the standard output stream.
#     Using the standard error stream is possibly by giving the ``stream``
#     argument value ``'stderr'``.
#     """
#     librarylogger.console(msg, newline, stream)

def _initlogger():

    logging.basicConfig(stream=rut.stdout_redirector)
    logger_rf = logging.getLogger("RobotFramework")
    logger_ski = logging.getLogger("BearFramework")
    
    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(filename="test.log")

    logger_rf.setLevel(logging.DEBUG)
    logger_ski.setLevel(logging.DEBUG)
    handler1.setLevel(logging.WARNING)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger_rf.addHandler(handler1)
    logger_rf.addHandler(handler2)
    logger_ski.addHandler(handler1)
    logger_ski.addHandler(handler2)
    
    return logger_ski