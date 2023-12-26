from Section import Section
from Lock import Lock
from RiverIterator import RiverIterator
from SectionIterator import SectionIterator
from LockNone import LockNone
from LockBasic import LockBasic
from LockFastEmpty import LockFastEmpty
from Boat import Boat


class RiverSystem:

    def __init__(self):
        """
        Initializes the class.
        """
        self.river = []
        self.num_boats = 1
        self.create_default_river()


    def add_section(self, length, flow):
        """
        Adds a new section to the end of the river.
        @param length: The number of units in the section.
        @param flow: The flow of the section.
        @return: Nothing.
        """
        temp = Section(length, flow)
        self.river.append(temp)

    def add_lock(self, depth, strategy):
        """
        Adds a new lock to the end of the river.
        @param depth: The depth of the lock.
        @param strategy: The filling/emptying strategy of the lock
        @return: Nothing.
        """
        temp = Lock(depth, strategy)
        self.river.append(temp)

    def __str__(self):
        """
        Generates a string from the class.
        @return: temp, a string representing the class.
        """
        temp = ''

        for i in self.river:
            temp += str(i)

        return temp

    def add_boat(self, boat):
        """
        Adds a boat to the beginning of the river.
        @param boat: The boat being added to the river.
        @return: Nothing.
        """
        self.river[0].add_boat(boat)

    def create_default_river(self):
        """
        Creates a default river for boats to move through.
        @return: Nothing.
        """
        self.river = []
        self.river.append(Section(6, 0))
        self.river.append(Lock(0, LockNone()))
        self.river.append(Section(3, 1))

    def create_tester_river(self):
        """
        Creates a tester river for boats to move through.
        @return: Nothing.
        """
        self.river = []
        self.river.append(Section(5, 0))
        self.river.append(Lock(0, LockNone()))
        self.river.append(Section(6, 2))
        self.river.append(Lock(2, LockBasic()))
        self.river.append(Section(3, 3))
        self.river.append(Lock(5, LockFastEmpty()))


    def update(self):
        """
        Updates the whole system moving boats down the river that can move.
        And filling or emptying locks.
        @return: Nothing.
        """
        boat = None
        out_boat = True
        count = len(self.river) - 1
        # GRADING: LOOP_ALL
        for i in self.river_iterator():
            in_boat, out_boat = self.can_update_part(count)
            if in_boat:
                boat = self.get_prev_boat(count)
            else:
                boat = None
            i.update(boat, in_boat, out_boat)
            count -= 1

    def can_update_part(self, index):
        """
        Checks if a river part can send a boat to the next part.
        Also checks if a river part can get a boat from a previous part.
        @param index: The location we are at in the river system.
        @return: 2 booleans that tell if a river part can pass a boat into the next part,
                 or can accept a boat from the previous part.
        """
        in_boat = False
        out_boat = False

        if index == len(self.river) - 1:
            temp = self.river[index]
            if isinstance(temp, Lock):
                if temp.water_level + 1 == temp.depth:
                    out_boat = True
            else:
                out_boat = True
        else:
            temp = self.river[index]
            next = self.river[index + 1]
            if isinstance(temp, Lock):
                if temp.water_level >= temp.depth - 1:
                    out_boat = self.check_inst(next)
            else:
                out_boat = self.check_inst(next)
        if index - 1 > -1:
            prev = self.river[index - 1]
            if isinstance(prev, Lock):
                if prev.water_level == prev.depth - 1 or prev.water_level == prev.depth:
                    if isinstance(temp, Lock) and not temp.get_has_boat() and temp.water_level <= 1:
                        in_boat = True
                    if isinstance(temp, Section) and (out_boat or not temp.unit[0].get_has_boat()):
                        in_boat = True
            else:
                if prev.unit[len(prev.unit) - 1].get_has_boat():
                    if isinstance(temp, Lock) and not temp.get_has_boat() and temp.water_level <= 1:
                        in_boat = True
                    if isinstance(temp, Section) and (out_boat or not temp.unit[0].get_has_boat()):
                        in_boat = True

        return in_boat, out_boat

    def check_inst(self, inst):
        """
        Checks If an instance can move a boat forward.
        @param inst: The river part we are checking.
        @return: If we can move forward or not.
        """
        if isinstance(inst, Lock) and not inst.get_has_boat() and inst.water_level == 0:
            return True
        if isinstance(inst, Section) and not inst.unit[0].get_has_boat():
            return True
        return False

    def get_prev_boat(self, index):
        """
        Gets the boat from the previous river part.
        @param index: The location we are at in the river right now.
        @return: Either the boat that is moving on, or None if not.
        """
        if isinstance(self.river[index - 1], Lock):
            boat = self.river[index - 1].get_boat()
            self.river[index - 1].remove_boat()
            if isinstance(boat, Boat) and ((isinstance(self.river[index - 1].strategy, LockBasic)) or
                                           isinstance(self.river[index - 1].strategy, LockFastEmpty)):
                self.river[index - 1].water_level += 2
                if isinstance(self.river[index - 1].strategy, LockFastEmpty):
                    self.river[index - 1].water_level += 1
            return boat
        else:
            if isinstance(self.river[index], Lock):
                if self.river[index].water_level > 1 or self.river[index].get_has_boat() == True:
                    return None
            boat = self.river[index - 1].unit[self.river[index - 1].length - 1].get_boat()
            self.river[index - 1].unit[self.river[index - 1].length - 1].remove_boat()
            return boat

    def second_layer(self):
        """
        Complies a string representing the second layer of the string with the boat ID's.
        @return: The string it created.
        """
        temp = ''
        for i in range(0, len(self.river)):
            if type(self.river[i]) is Lock:
                if self.river[i].boat is not None:
                    temp += str(self.river[i].boat.get_id())
                    if self.river[i].boat.get_id() / 10 < 1:
                        temp += '.'
                else:
                    temp += '..'
                temp += '.....'
            else:
                for j in self.river[i].unit:
                    temp += j.sec_str()

        return temp

    def river_iterator(self):
        """
        Gets and returns an iterator for the river.
        @return: An iterator that iterates through the river.
        """
        return RiverIterator(self.river)

    def section_iterator(self):
        """
        Gets and returns an iterator that only grabs the sections in the river.
        @return: An iterator that iterates over only the sections in the river.
        """
        return SectionIterator(self.river)
