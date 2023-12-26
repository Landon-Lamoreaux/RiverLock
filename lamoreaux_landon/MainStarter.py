'''
Grading tags in for all lines marked with *			Yes

Tierless str meets D in SOLID (hidden test)*			Yes
Check if above is done, but not its test was not reached	___

1. Initial Show system\Got it compiling
Menu\initial system working				Yes
Bad input handled						Yes

2. Add Default
Added and shown properly				Yes
Second+ item ignored					Yes

3. Basic Update (single)
Moves along section						Yes
String format correct					Yes
Iterator used*							Yes

4. Basic Update (multiple)				Yes

5. Multi Update
Updates correctly						Yes
Bad input handled						Yes

6. Show details
Shows details properly 					Yes
Iterator used*							Yes

6. Add user specified item
Basic movement still works				Yes
Powered works							Yes
No passing							    Yes

7. Tester part 1
Boats works up to second lock 			Yes
Formatting correct 						Yes

8. Tester part 2
Boats works up to end					Yes
Strategy pattern for basic fill*		Yes
Strategy pattern for fast empty*		Yes

9. Custom belt **
String formatting correct				Yes
Everything still works 					Yes
Bad input handled 						Yes
'''

import traceback
from RiverSystem import RiverSystem
from LockNone import LockNone
from LockBasic import LockBasic
from LockFastEmpty import LockFastEmpty
from Boat import Boat
from Steady import Steady
from Lock import Lock
from Section import Section
from MaxSpeed import MaxSpeed

river_system = RiverSystem()
num_boats = 1


def cleanInput(prompt):
    result = input(prompt)
    # Strips out blank lines in input.
    while result == '':
        result = input()

    return result


def main():
    global num_boats

    river_system.create_default_river()

    menu = "\n" \
           "1) Add Default Boat\n" \
           "2) Update One Tick\n" \
           "3) Update X Ticks\n" \
           "4) Show Section Details\n" \
           "5) Add Boat\n" \
           "6) Make Tester\n" \
           "7) Make New Simulator\n" \
           "0) Quit\n"


    choice = int(-1)

    while choice != 0:
        try:
            if -1 <= choice <= 7:
                print(river_system)
                print(river_system.second_layer())

            print(menu)
            choice = int(cleanInput("Choice:> "))

            # Add default box.
            if choice == 1:
                if river_system.river[0].get_string()[0] == '⛴':
                    num_boats += 1
                    continue
                river_system.add_boat(Boat(num_boats, 1, Steady()))
                num_boats += 1

            # Update one time.
            elif choice == 2:
                river_system.update()

            # Update X number of times.
            elif choice == 3:
                num_times = int(cleanInput("How many updates:> "))
                choice = -2
                for i in range(0, num_times):
                    river_system.update()
                    print(river_system)
                    print(river_system.second_layer())


            # Print out station details.
            elif choice == 4:
                count = 1

                # GRADING: LOOP_RESTRICT
                for i in river_system.section_iterator():
                    print('Section ' + str(count))
                    count += 1
                    print('Boats: ' + str(i.get_num_boats()) + ' Flow: ' + str(i.get_flow()) + '\n')
                choice = -2

            # Make a new box of any size.
            elif choice == 5:
                engine_power = int(cleanInput("What engine power:> "))
                travel_method = int(cleanInput("What travel method. (1) Steady or (2) Max :> "))
                if travel_method != 1 and travel_method != 2:
                    print('Input an option in the range 1-2')
                    continue
                if river_system.river[0].get_string()[0] == '⛴':
                    num_boats += 1
                    continue
                if travel_method == 1:
                    river_system.river[0].add_boat(Boat(num_boats, engine_power, Steady()))
                else:
                    river_system.river[0].add_boat(Boat(num_boats, engine_power, MaxSpeed()))
                num_boats += 1


            # Make new system.
            elif choice == 6:
                river_system.create_tester_river()

            # Make new system.
            elif choice == 7:
                river_system.river = []
                ans = 'y'
                while ans != 'n':
                    try:
                        part = int(cleanInput("Section (1) or Lock (2):> "))
                        if part == 1:
                            length = int(cleanInput("Length:> "))
                            flow = int(cleanInput("Flow:> "))
                            river_system.add_section(length, flow)
                        elif part == 2:
                            strategy = int(cleanInput("Fill behavior: None (1), Basic (2), or Fast Empty (3):> "))
                            depth = int(cleanInput("Depth:> "))
                            if strategy == 1:
                                strat = LockNone()
                            elif strategy == 2:
                                strat = LockBasic()
                            elif strategy == 3:
                                strat = LockFastEmpty()
                            else:
                                raise Exception
                            river_system.add_lock(depth, strat)
                        else:
                            print("Input an option in the range 1-2")
                    except:
                        print("Cannot accept value")
                    ans = cleanInput("Add another component (n to stop):> ")


            # Debug/check for D in SOLID in __str__.
            elif choice == -1:
                # Creating the 3 boats:
                boat1 = Boat(num_boats, 1, Steady())
                num_boats += 1
                boat2 = Boat(num_boats, 1, Steady())
                num_boats += 1
                boat3 = Boat(num_boats, 1, Steady())
                num_boats += 1

                # Adding them to the section, lock and system and printing them out.
                section = Section(1, 1)
                lock = Lock(0, LockNone())
                section.add_boat(boat1)
                lock.add_boat(boat2)

                # GRADING: TO_STR
                print(str(boat1))
                print(str(section))
                print(str(lock))
                river_system.add_boat(boat3)

            elif choice == 0 or choice == '0':
                choice = 0
            else:
                print("Input an option in the range 0-7")

        except ValueError:
            print('Please, input a positive integer')
            choice = -2

        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    main()
