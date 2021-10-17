'''
Requirement:
The Tower of Hanoi puzzle was invented by the French mathematician Edouard Lucas in 1883.
He was inspired by a legend that tells of a Hindu temple where the puzzle was presented to young priests.
At the beginning of time, the priests were given three poles and a stack of 64 gold disks,
each disk a little smaller than the one beneath it.

Their assignment was to transfer all 64 disks from one of the three poles to another, with two important constraints.
1) They could only move one disk at a time.
2） They could never place a larger disk on top of a smaller one.

The priests worked very efficiently, day and night, moving one disk every second.
When they finished their work, the legend said, the temple would crumble into dust and the world would vanish.

Although the legend is interesting, you need not worry about the world ending any time soon.
The number of moves required to correctly move a tower of 64 disks is 2^64−1=18,446,744,073,709,551,615.
At a rate of one move per second, that is 584,942,417,355 years! Clearly there is more to this puzzle than meets the eye.
'''


def tower_of_hanoi(n, from_rod, to_rod, help_rod):

    # base case:
    if n == 1:
        print(f'Move disk {n} from {from_rod} to {to_rod}')


    # recursive call
    else:
        # step 1) Move n-1 disks from 'from_rod' to 'help_rod' via 'to_rod'
        tower_of_hanoi(n-1, from_rod, help_rod, to_rod)

        # step 2) Move disk n from 'from_rod' to 'to_rod'
        print(f'Move disk {n} from {from_rod} to {to_rod}')

        # step 3) Move n-1 disks from 'help_rod' to 'to_rod' via 'from_rod'
        tower_of_hanoi(n - 1, help_rod, to_rod, from_rod)



tower_of_hanoi(6, 'A', 'C', 'B')