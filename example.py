from logger import Logger

# init your script
log = Logger()

def function1():
    log("[important]: This is a log")
    function2()
	
def function2():
    log("[important]: This is other log")
	
if __name__ == "__main__":
    function1()
