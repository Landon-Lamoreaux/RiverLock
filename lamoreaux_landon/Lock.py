from RiverPart import RiverPart


class Lock(RiverPart):
    boat = None

    def __init__(self, depth, strat):
        self.water_level = 0
        self.depth = depth
        RiverPart.__init__(self)
        self.string = '_X( ' + str(self.water_level) + ')_'
        self.strategy = strat


    def __str__(self):
        """
        Makes a string representing the class.
        @return: The string.
        """
        self.string = '_'
        if self.boat is None:
            self.string += 'X( '
        else:
            self.string += str(self.boat) + '( '
        self.string += str(self.water_level) + ')_'
        return self.string

    def add_boat(self, new_boat):
        """
        Adds a boat to the lock.
        @param new_boat: The boat being added to the lock.
        @return: Nothing.
        """
        self.boat = new_boat
        self.has_boat = True

    def remove_boat(self):
        """
        Removes the boat from the lock.
        @return: Nothing.
        """
        self.has_boat = False
        self.boat = None

    def update(self, pass_boat, in_boat, out_boat):
        """
        Updates the lock, either adding a boat, removing a boat, adding depth or lowering it.
        @param pass_boat: The boat coming into the lock.
        @param in_boat: If the lock will accept a boat coming into it.
        @param out_boat: If the lock can move it's boat to the next part of the river.
        @return:
        """
        return self.strategy.do_algorithm(self, pass_boat, in_boat, out_boat)

    def get_boat(self):
        """
        @return: The boat in the lock.
        """
        return self.boat
