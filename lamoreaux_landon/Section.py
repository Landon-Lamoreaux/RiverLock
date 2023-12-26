from RiverPart import RiverPart
from Unit import Unit
from BoatIterator import BoatIterator


class Section(RiverPart):

    def __init__(self, length, flow):
        self.length = length
        self.flow = flow
        self.unit = []
        self.num_boats = 0

        RiverPart.__init__(self)

        for i in range(0, length):
            new_unit = Unit(i)
            self.unit.append(new_unit)


    def __str__(self):
        """
        Gets a string representing the class.
        @return: The string we got to represent the class.
        """
        self.string = ''
        for i in self.unit:
            self.string += str(i)
        return self.string

    def add_boat(self, boat):
        """
        Adds a boat to the front of the section.
        @param boat: The boat being added.
        @return: Nothing.
        """
        self.unit[0].add_boat(boat)
        self.num_boats += 1

    def update(self, pass_boat, in_boat, out_boat):
        """
        Updates the section, moving all the boats forward in the section.
        @param pass_boat: A boat coming into the section.
        @param in_boat: If we can accept the boat coming in.
        @param out_boat: If we can send a boat out of the section.
        @return: The boat leaving the system.
        """
        next_boat = None
        for i in self.boat_iterator():
            if i.get_index() == len(self.unit) - 1:
                next_boat = i.get_boat().update(pass_boat, self.unit, i, self.flow, in_boat, out_boat)
            else:
                i.get_boat().update(pass_boat, self.unit, i, self.flow, in_boat, out_boat)
        if pass_boat is not None:
            self.unit[0].add_boat(pass_boat)
            return None
        return next_boat


    def get_num_boats(self):
        """
        Gets the number of boats in the section.
        @return: Returns the number of boats in the sections.
        """
        count = 0
        for i in self.boat_iterator():
            count += 1
        return count

    def get_flow(self):
        """
        @return: The flow of the river.
        """
        return self.flow

    def boat_iterator(self):
        """
        @return: A boat iterator instance.
        """
        return BoatIterator(self.unit)
