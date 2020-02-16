from abc import ABC, abstractmethod
class DAO(ABC):
    @abstractmethod
    def __init__(self, db):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def __del__(self):
        self.conn.close()
