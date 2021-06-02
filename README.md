# 🐍 Python logger file
Logger script that write logs in chosen file

##  Usage
Let's assume you have the following script:

```py
from logger import Logger

logger = Logger()

def function1():
    logger("[important]: This is a log")
    function2()
	
def function2():
    logger("[important]: This is other log")
	
if __name__ == "__main__":
    function1()
```

## Output
The output will be:
```sh
~$ python3 your_script.py
[important]: This is a log
[important]: This is other log
```

The output file will be, for example:
```sh
20210601123512.txt
```
```
[important]: This is a log
[important]: This is other log
```

You may want to change the output file name or extension. So just configure this:

```py
logger = Logger(file="filenameoutput", extension="db")
```

This output will be:
```sh
filenameoutput.db
```

## License
This project has a MIT License
