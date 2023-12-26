class Unit:

    def __init__(self, index):
        self.string = '〜〜〜'
        self.boat = None
        self.has_boat = False
        self.index = index


    def add_boat(self, new_boat):
        """
        Adding a boat to the unit.
        @param new_boat: The boat being added.
        @return: Nothing.
        """
        self.boat = new_boat
        self.string = str(self.boat) + '〜〜'
        self.has_boat = True

    def remove_boat(self):
        """
        Removes the boat from the unit.
        @return: Nothing.
        """
        self.boat = None
        self.has_boat = False
        self.string = '〜〜〜'

    def get_boat(self):
        """
        @return: The boat in the unit.
        """
        return self.boat

    def get_has_boat(self):
        """
        @return: Whether or not the unit has a boat.
        """
        return self.has_boat

    def __str__(self):
        """
        @return: A string representing the class.
        """
        return self.string

    def sec_str(self):
        """
        Makes a string for the second layer for the unit.
        @return: The string it made.
        """
        if self.has_boat:
            if self.boat.get_id() / 10 < 1:
                return str(self.boat.get_id()) + self.string[1:]
            else:
                return str(self.boat.get_id()) + self.string[2:]
        return self.string

    def get_index(self):
        """
        @return: The location of the unit in the section.
        """
        return self.index
