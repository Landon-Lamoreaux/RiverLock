class Boat:
    id = 0
    power = 0

    def __init__(self, boat_id, power, strategy):
        self.id = boat_id
        self.power = power
        self.strategy = strategy
        self.location = 0


    def __str__(self):
        """
        @return: A string representing the class.
        """
        return '⛴'

    def get_id(self):
        """
        @return: The boat's ID.
        """
        return self.id

    def update(self, pass_boat, units, unit, flow, in_boat, out_boat):
        """
        Calls the strategy to update the unit and move the boat forwards.
        @param pass_boat: The boat moving into the section.
        @param units: The list of units in the section.
        @param unit: The unit this boat is in.
        @param flow: The flow value of the section.
        @param in_boat: If a boat can move into the section.
        @param out_boat: If a boat can leave the section.
        @return: The output of the strategy.
        """
        return self.strategy.do_algorithm(pass_boat, units, unit, flow, in_boat, out_boat)

    def get_location(self):
        """
        @return: The index the boat is in in the section.
        """
        return self.location

    def update_location(self, new_loc):
        """
        Updating the boat's location.
        @param new_loc: The new location of the boat.
        @return: Nothing.
        """
        self.location = new_loc

    def get_power(self):
        """
        @return: The engine power of the boat.
        """
        return self.power

    def update_strat(self, strategy):
        """
        Updates the strategy of the boat.
        @param strategy: The strategy the boat will use from now on to update.
        @return: Nothing.
        """
        self.strategy = strategy
