# Main Python program:
# Note: Here we are assuming that you have already taken size of matrix and then values in matrix(0's & 1's only) from user.
#
# As a Developer write a program for matcing following constraints:
#
# You are given a two-dimensional array (matrix) of potentially unequal height and width
# containing only Os and 1s. Each 0 represents land, and each 1 represents part of a river.
# A river consists of any number of 1s that are either horizontally or vertically adjacent
# (but not diagonally adjacent). The number of adjacent 1s forming a river determine its
# size. Write a function that returns an array of the sizes of all rivers represented in the
# input matrix. Note that these sizes do not need to be in any particular order.
#
# Now from returned array of sizes You need to print "Guess the size of River" on each index, take input from user as guesses for each entry.
#
# If all entered sizes match then show You are the winner.
# If 60% of the inputs match with sizes in array of river sizes,show you got second position.
# else Show "Invest more money on Almonds, then come back".
#
# Now console should Ask if you wanted to play again:
# IF Yes : Redirect to the Matrix Input.
# Else : Exit
#
#
# Sample input:
# [1,0,0,1,0]
# (1,0,1,0,0)
# [0,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,1,0,
#
# Sizes of River = [1,2,2,2,5] note:  This should not be visible to the user , this a reference for accuracy of output.
#
#
# Sample output:
# Guess the size of River : input from user : note : This size should be compared with size present on specific or random index in river sizes array.
# Guess the size of River : input from user : 5
# you are the winner .
#
#
#


