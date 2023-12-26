# RiverLock Program

This project was created for my Programming Languages class to teach me Python, the Stratagy pattern and the Iterator pattern.

It was written in Python 3.11

This program moves a boat through a series of locks in a river. The user can create a river, or use the default river. The user can add a default boat to the river, or create their own boats to add to the river. The menu goes as follows:
```
1) Add Default Boat
2) Update One Tick
3) Update X Ticks
4) Show Section Details
5) Add Boat
6) Make Tester
7) Make New Simulator
0) Quit
```

Option 1 adds a default boat to the start of the river. <br />
Option 2 updates the river/boat one tick, this will move the boat down the river by an amount dependent on the boats engine power and the rivers flow. It will also update the locks once. <br />
Option 3 does the same thing as option 2 but a user specified number of times. <br />
Option 4 will show the details of each section in the river. <br />
Option 5 lets the user create a custom boat to the start of the river. <br />
Option 6 makes a default tester river for the boats to go down. <br />
Option 7 allows the user to make a custom new river for the boats to go down. <br />
Option 0 exits the program.

If a boat is in a lock or the lock has a raised water level, any boats behind the lock must wait until the boat leaves the lock and/or the lock has returned to the lower water level. Boats cannot pass eachother in the river.
River locks will raise their water level by 1 each tick if they contain a boat. If a lock is empty and the water level is high, then they will lower the water level each tick by 1 if its a slow lock, or by 2 if its a fast emptying lock.

A lock looks like this: ```_X( 0)_``` The X is replaced with a boat if there is a boat in the lock. The number in the parentheses is the height of the water in the lock. <br />
A river section lookes like 1 or more of these: 〜〜〜 <br />
A boat looks like: ```⛴```

A river can be contructed with any number of sections or locks in any order or arangment.
