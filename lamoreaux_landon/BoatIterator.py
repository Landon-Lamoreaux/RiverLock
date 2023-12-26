
class BoatIterator:

    def __init__(self, data):
        self.collection = data

    def __iter__(self):
        """
        Setting up the iterator.
        @return: Itself.
        """
        self.index = len(self.collection)
        return self

    def __next__(self):
        """
        The next part of the section that has a boat in it.
        @return: The unit with a boat in it.
        """
        try:
            self.index -= 1
            while self.collection[self.index].get_has_boat() == False:
                self.index -= 1
            if self.index < 0:
                raise StopIteration()
            return self.collection[self.index]
        except:
            raise StopIteration()
