from BehaviorBoat import BehaviorBoat
from Boat import Boat


# GRADING: MAX_TRAVEL
class MaxSpeed(BehaviorBoat):
    def do_algorithm(self, pass_boat, units, unit, flow, in_boat, out_boat):
        """
        Updates a unit and moves any boats in it forwards if possible.
        @param pass_boat: The boat coming into the section.
        @param units: The list of units in the section.
        @param unit: The unit we are updating.
        @param flow: The flow of the section.
        param in_boat: If the section can accept a boat.
        @param out_boat: If the section can pass a boat onto the next part.
        @return: None.
        """
        curr_boat = unit.get_boat()
        unit.remove_boat()

        if unit.get_index() == len(units) - 1 and out_boat == False:
            unit.add_boat(curr_boat)
            return None

        if unit.index == len(units) - 1:
            return None

        if isinstance(pass_boat, Boat) and unit.index == 0:
            unit.add_boat(pass_boat)

        count = unit.index + 1
        power = curr_boat.get_power()
        while count < (len(units) - 1) and (units[count+1].get_has_boat() == False) and (count - unit.index) < power - flow:
            count += 1

        units[count].add_boat(curr_boat)
        return None
