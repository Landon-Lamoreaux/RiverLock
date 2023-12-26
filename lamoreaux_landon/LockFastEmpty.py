from BehaviorLock import BehaviorLock


# GRADING: FAST_EMPTY
class LockFastEmpty(BehaviorLock):
    def do_algorithm(self, lock, pass_boat, in_boat, out_boat):
        """
        Updates the lock once, lowers the depth by 2 each time.
        @param lock: The lock being updated.
        @param pass_boat: The boat coming into the lock.
        @param in_boat: If the lock can accept a boat.
        @param out_boat: If the lock can pass a boat to the next section.
        @return: The boat moving on, if it can. None otherwise.
        """
        if lock.water_level > 0 and lock.get_has_boat() == False:
            lock.water_level -= 2
            if lock.water_level < 0:
                lock.water_level = 0
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
