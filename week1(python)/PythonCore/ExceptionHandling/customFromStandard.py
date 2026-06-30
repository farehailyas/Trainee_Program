class NetworkFailure(RuntimeError):
    def __init__ (self , message):
        self.message= message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

def checkNetwork():
    try:
        raise NetworkFailure("Conection failure occur")

    except NetworkFailure as e:
        print(e)
checkNetwork()