from abc import abstractmethod


class Generic:
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
