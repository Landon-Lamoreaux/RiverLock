class RiverIterator:

    def __init__(self, data):
        self.collection = data

    # GRADING: ITER_ALL
    def __iter__(self):
        """
        Setting up the iterator.
        @return: Itself.
        """
        self.index = len(self.collection)
        return self

    def __next__(self):
        """
        Iterates through the collection backwards.
        @return: The next item in the collection.
        """
        try:
            self.index -= 1
            if self.index < 0:
                raise StopIteration()
            return self.collection[self.index]
        except:
            raise StopIteration()
