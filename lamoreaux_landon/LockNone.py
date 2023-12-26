from BehaviorLock import BehaviorLock


class LockNone(BehaviorLock):
    def do_algorithm(self, lock, pass_boat, in_boat, out_boat):
        """
        Updating the lock that doesn't need to fill up.
        @param lock: The lock we are updating.
        @param pass_boat: The boat coming into the lock.
        @param in_boat: If a lock can accept a boat.
        @param out_boat: If a lock can pass a boat on.
        @return: The boat in the lock.
        """
        temp = None
        if lock.has_boat:
            temp = lock.boat
            lock.remove_boat()
        if pass_boat is not None:
            lock.add_boat(pass_boat)
        return temp
