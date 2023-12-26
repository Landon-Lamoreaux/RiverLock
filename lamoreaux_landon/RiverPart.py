class RiverPart:

    def __init__(self):
        self.string = ''
        self.string = ''
        self.has_boat = False
        self.boat = None

    def __str__(self):
        """
        @return: The string representing the river part.
        """
        return self.string

    def get_has_boat(self):
        """
        @return: If the part has a boat.
        """
        return self.has_boat

    def get_string(self):
        """
        @return: The string for the class.
        """
        return self.string
