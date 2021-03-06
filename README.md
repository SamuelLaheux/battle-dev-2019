# Battle-dev-2019 (November)

https://www.isograd.com/FR/solutionconcours.php

## Exercise 1

### Code to run to solve exercise 1

```python
python3 ex1_short_straw.py
```

### Exercise statement

#### Objective
During a seminar with your company in an exotic country, you have the
opportunity to participate in several activities. The excursion to an island looks
nice but you prefer to take part in the 2-day hike. The scenery on the paths is
beautiful and you've never slept under the stars before.

You've been gone for more than 10 hours and unfortunately not everything is
going according to plan. It rains a lot, the landscapes are not that nice and you are
exhausted. You thought resting in the tents was going to make you feel better, but
you realize there's one missing.

The sun is almost down and you have to find a solution quickly. It's decided, a
person has to sacrifice himself and it's going to be a short straw. You collect as
much piece of wood as there are people and each your turn you will draw one.
Whoever pulls the smallest piece of wood will sleep without a tent.

You need to determine the first name of the person who is going to sleep without
a tent.

You are assured that there is no equality possible.

#### Data format

##### Input
Row 1: an integer N between 10 and 100 corresponding to the number of people
participating in the hike.

Rows 2 to N+1: a string comprising between 5 and 10 lower case characters and
a integer between 1 and 1000 separated by a space representing respectively the
first name of a participant and the length of his piece of wood in centimeters.

##### Output
The first name of the person who will sleep without a tent.


## Exercise 2

### Code to run to solve exercise 2

```python
python3 ex2_wooden_frame.py
```

### Exercise statement

#### Objective
For your grandmother's 80th birthday, you are responsible for preparing the gift: a
square wooden frame to paste a picture of the star of the evening.

Because your budget is tight, you decide to build the frames in your workshop. You
decide to reuse old materials. You have a box full of thin planks of wood of the same
thickness and width but of different lengths. Your grandmother won't blame you if the
frames aren't all the same size, having said that - she insists that they're square.
You then decide to randomly take 4 boards in the box and cut them, if necessary, in
order to build the largest square frame possible.

Note that when you cut a board, you keep the part you are interested in and you throw
the second part into the box, you can no longer use it for this frame.
The objective is to determine how many centimeters you need to throw back into the
box if you build the largest square frame possible.

#### Data format

##### Input
Rows 1 to 4: an integer between 10 and 1,000 representing to the length of a wooden
plank expressed in centimeters.

##### Output
An integer representing the number of centimeters of wood you throw into the
cardboard if you build the largest square frame possible.
