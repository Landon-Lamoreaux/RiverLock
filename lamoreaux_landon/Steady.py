from BehaviorBoat import BehaviorBoat
from Boat import Boat


# GRADING: STEADY_TRAVEL
class Steady(BehaviorBoat):
    def do_algorithm(self, pass_boat, units, unit, flow, in_boat, out_boat):
        """
        Updates a unit and moves any boats in it forwards if possible.
        @param pass_boat: The boat coming into the section.
        @param units: The list of units in the section.
        @param unit: The unit we are updating.
        @param flow: The flow of the section.
        @param in_boat: If the section can accept a boat.
        @param out_boat: If the section can pass a boat onto the next part.
        @return: The boat that is moving to the next section.
        """
        curr_boat = unit.get_boat()
        unit.remove_boat()

        if unit.get_index() == len(units) - 1 and out_boat == False:
            unit.add_boat(curr_boat)
            return None

        if isinstance(pass_boat, Boat) and unit.index == 0:
            unit.add_boat(pass_boat)

        if unit.get_index() < len(units) - 1:
            if not units[unit.get_index() + 1].get_has_boat():
                units[unit.get_index() + 1].add_boat(curr_boat)
                return None

        if (unit.get_index() + 1 < len(units) and units[unit.get_index() + 1].get_has_boat() == True):
            unit.add_boat(curr_boat)
            return None

        return curr_boat


'''
    curr_boat = None
    prev_boat = pass_boat
    for i in units:
        curr_boat = i.get_boat()
         if i.get_has_boat():
             i.remove_boat()
             num_boats -= 1
         if prev_boat is not None:
            i.add_boat(prev_boat)
            num_boats += 1
        prev_boat = curr_boat
        curr_boat = None
    return prev_boat'''