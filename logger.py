from datetime import datetime
import sys #useless


#initialization time
data = datetime.now()


#log levels
INFO = "INFO"
WARNING = "WARNING"
DEBUG = "DEBUG"
CRITICAL = "CRITICAL"
ERROR = "ERROR"


#file name
FILE_NAME = "log.log"


#config
ltime = False
"""
must be:

    ltime = False
        log with level, but without time

    ltime = True
        log with level and time

"""


#first function
def lwrite(level, message: str):

    """
    completely overwrites the log file

    syntax:
        lwrite(log level(see str 10), "just message")
        if you write something other than the log level in the level, there will be an error in the log file
    """

    try:

        if level == INFO or level == WARNING or level == DEBUG or level == CRITICAL:
            if ltime:
                with open(FILE_NAME, 'w', encoding='utf-8') as ft:
                    ft.write(f"[{data}]")
                    ft.write("::")
                    ft.write(level)
                    ft.write("::")
                    ft.write(message)
                    print(f"your message['{message}'] overwrite in {FILE_NAME} with time and log lvl")

            else:

                with open(FILE_NAME, 'w', encoding='utf-8') as f:
                    f.write(level)
                    f.write("::")
                    f.write(message)
                    print(f"your message['{message}'] overwrite in {FILE_NAME}")

        else:
            if ltime:

                with open(FILE_NAME, 'a', encoding='utf-8') as ftl:
                    ftl.write("\n")
                    ftl.write(f"[{data}]")
                    ftl.write("::")
                    ftl.write(CRITICAL)
                    ftl.write("::")
                    ftl.write("ERROR, incorrect log level")
                    print(f"error 1: {level} != log level. Fix this end restart programm")

            else: 

                with open(FILE_NAME, 'a', encoding='utf-8') as f:
                    f.write("\n")
                    f.write(CRITICAL)
                    f.write("::")
                    f.write("ERROR, incorrect log level")
                    print(f"error 1: {level} != log level. Fix this end restart programm")

    except TypeError:
        with open(FILE_NAME, 'a', encoding='utf-8') as fTE:           
            fTE.write(f"error 3: message == {message} != str. Fix and restart programm")
            print(f"error 3: message == {message} != str. Fix and restart programm")



def lappend(level, message: str):

    """
    add a message in .log file

    syntax:
        lappend(log level, "message")
    """

    try:

        if level == INFO or level == WARNING or level == DEBUG or level == CRITICAL:

            if ltime:

                with open(FILE_NAME, 'a', encoding='utf-8') as ft:
                    ft.write("\n")
                    ft.write(f"[{data}]")
                    ft.write("::")
                    ft.write(level)
                    ft.write("::")
                    ft.write(message)
                    print(f"your message['{message}'] add in {FILE_NAME} with time and log lvl")
            
            else:

                with open(FILE_NAME, 'a', encoding='utf-8') as f:
                    f.write("\n")
                    f.write(level)
                    f.write("::")
                    f.write(message)
                    print(f"your message['{message}'] add in {FILE_NAME}")

        else:
            if ltime:

                with open(FILE_NAME, 'a', encoding='utf-8') as ftl:
                    ftl.write("\n")
                    ftl.write(f"[{data}]")
                    ftl.write("::")
                    ftl.write(CRITICAL)
                    ftl.write("::")
                    ftl.write("ERROR, incorrect log level")
                    print(f"error 1: {level} != log level. Fix this end restart programm")

            else:

                with open(FILE_NAME, 'a', encoding='utf-8') as fl:
                    fl.write("\n")
                    fl.write(CRITICAL)
                    fl.write("::")
                    fl.write("ERROR, incorrect log level")
                    print(f"error 1: {level} != log level. Fix this end restart programm")

    except TypeError:
        with open(FILE_NAME, 'a', encoding='utf-8') as fTE:           
            fTE.write(f"error 3: message == {message} != str. Fix and restart programm")
            print(f"error 3: message == {message} != str. Fix and restart programm")



def lmessage(message):

    """
    add message in log file, without level and time

    syntax:
        lmessage("hello world")
    """

    with open(FILE_NAME, 'a', encoding="utf-8") as f:
        f.write("\n")
        f.write(message)
        print(f"your message ['{message}'] add in {FILE_NAME}")


def lclear():

    """
    unuseless
    """

    with open(FILE_NAME, 'w') as f:
        f.write("")
        print(f"you clear {FILE_NAME}")


#just line feed
def lend(sym: str=""):

    """
    line feed with use symbols

    syntax:
        lend("your symbol")
    """

    try:
        with open(FILE_NAME, 'a', encoding='utf-8') as f:
            f.write("\n")
            f.write("\n")
            f.write(sym * 100)
            f.write("\n")

        if sym == "":
            print("line feed without symbols")

        else:
            print(f"line feed with {sym}")

    except TypeError:
        lappend(CRITICAL, f"Error 2: {sym} is not str")
        print(f"Error 2: sym == {sym} != str")


#test
lappend(DEBUG, "logger by Pe2h334")
lmessage("version: a2.2")
lend("#")