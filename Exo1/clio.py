class Clio():
    price_range = [8000, 30000]
    doors = (3,5)
    price = 20000
    colors = { 
        "red" : 11111111,
        "black" : 22222222,
        "bleu" : 33333333,
        "white" : 44444444,
        "purple" : 55555555
    }

    def __init__(self, number_doors, color):
        self.number_doors = number_doors
        self.color_number = False
        self.color = color 

    @property
    def number_doors(self):
        return self.__number_doors

    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Clio.doors :
            self.__number_doors = number_doors
        else:
            self.__number_doors = False

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        try: 
            Clio.colors[color]
            self.__color = color
            self.color_number = Clio.colors[color]
        except KeyError as e :
            print ("La couelur n'existe pas")
            exit()

    @classmethod
    def uptade_price(cls, price):
        try:
            if cls.price_range[0] <= price <= cls.price_range[1]:
                cls.price = price
            else:
                raise Exception("ce prix n'est pas autorise ")
        except Exception as e:
            print("un probleme est survenue {}".format(e)) 
            exit()


