Logger
===========

Logger is a simple Python library for writing to .log files

# How it look?

DEBUG::logger by uueeuu

if time = True

[2025-01-02 20:27:04.673258]::DEBUG::logger by uueeuu

How to import in my project?
===========

* Download Python 3.x
* Clone this repository somewhere
* Move file `logger.py` from repository in your project folder
* Import `logger.py` in your main file

____

```Python
from logger import *

lwrite(INFO, "hi")
#write "hi" -> log.log
```

____

How use in my project?
===========

Logger has five functions:
* lwrite
* lappend
* lmessage
* lclear
* lend

Let's look at each function

### lwrite()

lwrite rewrites all content in the log file

##### syntax:

```Python
lwrite(level, message)
```

level - log level
There are 5 log levels:

_____

* INFO. Just information about process
* DEBUG. Information for debuging
* WARNING. Warning or not critical error
* ERROR. Error lol
* CRITICAL. Fatal error

_____

In level you need to write one of them or you get error

Example:

```Python
lwrite(INFO, "hello world!")
#writing "hello world!" in .log file
```

### lappend()

lappend add new message(with line break) without rewriting

##### syntax:

```Python
lappend(level, message)
```

level - log level
message - your log message

_____

Example:

```Python
lappend(CRITICAL, "FATAL ERROR")
#add message about fatal error
```

### lmessage()

lmessage add message without log level and time

##### syntax:

```Python
lmessage(message)
```

message - your message that needs to be sent to the .log

_____

Example:

```Python
lmessage("fuxking russian kid")
#add message with line break to .log
```

### lclear()

just clear log file

### lend()

Make separation with(or without) symbols

##### syntax:

```Python
lend(sym)
```

sym - character that will split the line

_____

# More info
_____
## Time

If you need time in log make this steps

* Open `logger.py`
* Change `Time` from False -> True

_____

## File name

Default file name is `log.log`, logger create this file if it dont exists.
If you rename `log.log` -> `$random_name.log` then logger create new file log.log and all entries will writing in new `log.log`
But you can change default file name, for this you need:

* Open `logger.py`
* Change `FILE_NAME` from `log.log` -> `coolname.log`