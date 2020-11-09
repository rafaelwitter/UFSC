import numpy 

class HashTable:
    def __init__(self, positions):
        self.__positions = positions
        self.__keys = 0
        self.__load_factor = 0
        self.__array = None
    

    def create_array(self):
        self.__array = numpy.empty(self.__positions)
        return (f'Array com {self.__positions} posições criado!')
    
    
    def add_element(self, element: object):
        destined_group = (5 * element.get_numero() + 3)
        if self.__array[destined_group] == None:
            self.__array[destined_group] = element
        else:
            e = self.__array[destined_group]
            element.set_proximo(e)
            self.__array[destined_group] = element


    def contain_element(self, element: object):
        destined_group = (5 * element.get_numero() + 3)
        if self.__array[destined_group] == element:
            return True
        else:
            e = self.__array[destined_group]
            while e != element:
                if e == None:
                    return None
                else:
                    e.get_proximo()
            return True

    
    def remove_element(self, element: object):
        destined_group = (5 * element.get_numero() + 3)
        if self.__array[destined_group] == element:
            e = self.__array[destined_group]
            self.__array[destined_group] = e.get_proximo()
        else:
            e = self.__array[destined_group]
            while e.get_proximo() != element:
                if e.get_proximo() == None:
                    raise Exception(f'O elemento {element} não está presente no Hash!')
                else:
                    e = e.get_proximo()
            
            if e.get_proximo() is None:





