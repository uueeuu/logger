Logger
===========

logger is a simple Python library for writing to .log files

How to import in my project?
===========

* Download Python 3.x
* Clone this repository somewhere
* Move file `logger.py` from repository in your project folder
* Import `logger.py` in your main file

____

```Python
from log_edit import *

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

let's look at each function

### lwrite()

lwrite rewrites all content in the log file

##### syntax:

```Python
lwrite(level, message)
```

level - log level
there are 3 log levels:

_____

* INFO. Just information about process
* DEBUG. Information for debuging
* WARNING. Warning or not critical error
* ERROR. Error lol
* CRITICAL. Fatal error

_____

In level you need to write one of them or you get error

example:

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

example:

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

example:

```Python
lmessage("fuxking russian kid")
#add message with line break to .log
```

### lclear()

just clear log file

### lend()

make separation with(or without) symbols

##### syntax:

```Python
lend(sym)
```

sym - character that will split the line

_____

# More info
_____
## Time

if you need time in log make this steps

* Open `logger.py`
* Change `Time` from False -> True

_____

## File name

default file name is `log.log`, logger create this file if it dont exists.
If you rename `log.log` -> `$random_name.log` then logger create new file log.log and all entries will writing in new `log.log`
but you can change default file name, for this you need:

* Open `logger.py`
* Change `FILE_NAME` from `log.log` -> `coolname.log`