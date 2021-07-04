class Account :
    def __init__(self):
        self.__name=''
        self.__ano=0
        self.__bal=0

    def __init__(self,name,ano,bal):
        self.__name=name
        self.__ano=ano
        self.__bal=bal

    @property
    def name(self):
        return self.__name

    @property
    def ano(self):
        return self.__ano

    @property
    def bal(self):
        return self.__bal

    @name.setter
    def name(self,name):
        self.__name=name

    @bal.setter
    def bal(self,bal):
        self.__bal=bal

