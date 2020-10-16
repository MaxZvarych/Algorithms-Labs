class Film:
    def __init__(self, name="Titanic", duration_in_minutes=150, number_of_responces=101):
        self.name=name
        self.duration_in_minutes=duration_in_minutes
        self.number_of_responces=number_of_responces

    # def __del__(self):
    #     print("Видалення екземпляра:"+ self.__str__())
    #     del self.name
    #     del self.duration_in_minutes
    #     del self.number_of_responces

    def __str__(self):
        return "Film:" + self.name +\
               ", duration_in_minutes:" + str(self.duration_in_minutes) +\
               ", number_of_responces:" + str(self.number_of_responces)
