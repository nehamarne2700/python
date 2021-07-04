class MyException(Exception):
    message=''

    def __init__(self,message="MyException Occurred"):
        self.message=message
        super().__init__(self.message)

    def getMessage(self):
        return self.message

    def __str__(self):
        return (repr('MyException Occurred'))