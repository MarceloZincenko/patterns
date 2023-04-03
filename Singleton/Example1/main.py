from singleton_logger import SingletonObject

def run() -> None:
    logger_object = SingletonObject("./Example1/class_logger.log")
    logger_object.info("This is an info message")
    logger_object = SingletonObject("./Example1/class_logger3.log")
    logger_object.info("This is an info message")
    logger_object = SingletonObject("./Example1/class_logger2.log")
    logger_object.info("This is an info message")
    logger_object = SingletonObject("./Example1/class_logger4.log")
    logger_object.info("This is an info message")
    logger_object = SingletonObject("./Example1/class_logger5.log")
    logger_object.info("This is an info message")

if __name__ == '__main__':
    run()
