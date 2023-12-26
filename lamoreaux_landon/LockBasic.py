from BehaviorLock import BehaviorLock


# GRADING: BASIC_FILL
class LockBasic(BehaviorLock):
    def do_algorithm(self, lock, pass_boat, in_boat, out_boat):
        """
        Updates the lock one time.
        @param lock: The lock being updated.
        @param pass_boat: The boat coming into the lock
        @param in_boat: If the lock can accept a new boat.
        @param out_boat: If the lock can move a boat out.
        @return: The boat in the lock if it's moving on.
        """

        if lock.water_level != 0 and lock.get_has_boat() == False:
            lock.water_level -= 1
        if not lock.get_has_boat() and pass_boat is None:
            return None

        if not lock.get_has_boat():
            lock.add_boat(pass_boat)
            return None

        if lock.water_level < lock.depth and lock.get_has_boat() == True:
            lock.water_level += 1
        if lock.water_level == lock.depth and lock.get_has_boat() == True:
            temp = lock.get_boat()
            lock.remove_boat()
            return temp
