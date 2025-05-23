#!/data/data/com.termux/files/usr/bin/env python3 
from collections import Counter as cntr
from copy import copy
import random
from random import randint


class Hat:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = self.make_contents(self.kwargs)
        self.contents_cpy = copy(self.contents)
    # End __init__() 


    # Not actually used in tests 
    def __str__(self) -> str:
        desc = 'Hat:\n'
        for key, value in self.kwargs.items():
            desc += str(key)+'='+str(value)+'\n'
        return desc
    # End __str__()


    def draw(self, nb: int) -> list:
        """
        Draw nb balls from hat
        """
        # Refresh contents from copy
        self.contents = copy(self.contents_cpy)
        sz = len(self.contents)
        drawn = []

        for _ in range(nb):
            # Return full contents randomised
            # to pass test 
            if sz == 0:
                break
            b = randint(1, sz)
            drawn.append(self.contents[b-1])
            del self.contents[b-1]
            sz -= 1

        return drawn
    # End draw() 


    def make_contents(self, ball_dict: dict) -> list:
        """
        Make a 'contents' list from dict
        """
        cont =[]
        for key, value in ball_dict.items():
            for _ in range(value):
                cont.append(key)
        if not cont:
            cont.append('black')

        return cont
    # End make_contents() 
# End class


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Run probability experiments
    """
    expected = hat.make_contents(expected_balls)
    num_balls = num_balls_drawn
    N = num_experiments
    M = 0

    ## Internal function
    def compare(list1: list, list2: list) -> bool:
        count1 = cntr(list1)
        count2 = cntr(list2)
        for el, cnt in count2.items():
            if count1[el] < cnt: 
                return False
        return True
    ##

    for _ in range(N):
        drawn_balls = hat.draw(num_balls)
        if compare(drawn_balls, expected):
            M += 1
    # Return probability     
    return M/N
# End experiment() 


# Run a test experiment
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=200000)

print(probability)

"""
Build a Probability Calculator Project


Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.


Create Hat Class

First, create a Hat class. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {'red': 2, 'blue': 1}, contents should be ['red', 'red', 'blue'].

The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.


Create experiment() function

Next, create an experiment function  (not inside the Hat class). This function should accept the following arguments:

hat:
A hat object containing balls that should be copied inside the function.

expected_balls:
An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {'blue':2, 'red':1}.

num_balls_drawn:
The number of balls to draw out of the hat in each experiment.

num_experiments:
The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The experiment function should return a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times, M, you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

The output would be something like this:
0.356

Since this is based on random draws, the probability will be slightly different each time the code is run.

Hint: Consider using the modules that are already imported at the top. Do not initialize random seed within the file.
"""
