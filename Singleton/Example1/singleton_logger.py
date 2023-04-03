class SingletonObject(object):

    instance = None # class attribute

    class __SingletonObject():
        """This is a private class """
        def __init__(self, file_name: str) -> None:
            """Return a Logger object whose file_name is *file_name*"""
            self.file_name=file_name
    
        def __str__(self) -> str:
            return "{0!r} {1}".format(self, self.file_name)
        
        def _write_log(self, level: str, msg: str) -> None:
            """Writes a message to the file_name for a specific Logger instance"""
            with open(self.file_name, "a") as log_file:
                log_file.write(f"[{level}] {msg}\n")
        
        def critical(self, msg) -> None:
            self._write_log("CRITICAL",msg)
        
        def error(self, msg) -> None:
            self._write_log("ERROR", msg)
        
        def warn(self, msg) -> None:
            self._write_log("WARN", msg)
        
        def info(self, msg) -> None:
            self._write_log("INFO", msg)
        
        def debug(self, msg) -> None:
            self._write_log("DEBUG", msg)

    def __new__(cls, file_name: str) -> __SingletonObject:
        """new is a class mehtod:it receives the class as a parameter and then uses 
        the class definition to construct a new instance of the class and store in instance class variable"""
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject(file_name)
        
        return SingletonObject.instance
