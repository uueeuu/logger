Logger
===========

logger is a simple Python library for writing to .log files

How to import in my project?
===========

* Download Python 3.x
* Clone this repository somewhere
* Move file `log_edit.py` from repository in your project folder
* Import `log_edit.py` in your main file

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
syntax:

```Python
lwrite(level, message)
```

level - log level
there are 3 log levels:
    * INFO. Just information about process
    * DEBUG. Information for debuging
    * WARNING. Warning or not critical error
    * ERROR. Error lol
    * CRITICAL. Fatal error

In level you need to write one of them or you get error

example:

```Python
lwrite(INFO, "hello world!")
#writing "hello world!" in .log file
```