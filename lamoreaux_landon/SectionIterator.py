from Lock import Lock


class SectionIterator:

    def __init__(self, data):
        self.collection = data

    # GRADING: ITER_RESTRICT
    def __iter__(self):
        """
        Setting up the iterator.
        @return: Itself.
        """
        self.index = -1
        return self

    def __next__(self):
        """
        Grabs the next section in the river.
        @return: Returns the next section in the river.
        """
        try:
            self.index += 1
            while isinstance(self.collection[self.index], Lock):
                self.index += 1
            return self.collection[self.index]
        except:
            raise StopIteration()
