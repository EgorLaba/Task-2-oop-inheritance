from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, model_name, engine_power, color, manufacture_year, manufacture_country, doors_сount, hijacked_status, load_capacity):
        Vehicle.__init__(self, model_name, engine_power, color, manufacture_year, manufacture_country, doors_сount, hijacked_status)
        self.__load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, load_capacity):
        if load_capacity >= 200 and load_capacity <= 15000:
            self.__load_capacity = load_capacity
        else:
            print("Error")






