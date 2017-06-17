Notes on version of tangram.py with classes
========

1. This code seems to work well and do what we want it to. Well done!
2. The print functions aren't ideal because when you call them, they print straightaway. There's no way of getting that output text to do something else with. Python has a better way of doing this. Define a function called `__str__`, which returns a string, and add it to the class. Now `print(square_1)` will work correctly and show the output you chose.
3. Let's import `numpy` as either `np` or `numpy`, as importing it as `py` seems confusing.
4. We could make shapes contain a list of their corners, then some of the functions would be easier as we could just do something for every element of the list, instead of always checking for if there are four corners or not.
5. Do we need another shape class? Is there just one more type of shape which we don't have here (the parallelogram)?