'''
Requirement:
Define 2 functions to output the following lyrics:

One little, two little, three little Indians
Four little, five little, six little Indians
Seven little, eight little, nine little Indians
Ten little Indian boys.

Ten little, nine little, eight little Indians
Seven little, six little, five little Indians
Four little, three little, two little Indians
One little Indian boy.

In the above 8 lines, 6 of them are quite similar, 2 of them are similar.

The name of the 2 functions are:
lyric_main(<You_define_parameter_here>)
lyric_end(<You_define_parameter_here>)
HINT: You can define multiple parameters inside the parentheses, separated by ','
'''

'''
For the first 3 sentences, the number goes up: one -> two -> three, four -> five -> six
For the last 3 sentences, the number goes down: ten -> nine -> eight

So we need 2 parameters:
1) start_number. int type
2) ascending. bool type

'''

number_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def lyric_main(start_number, ascending):

    # because list is 0 based, so start_number should be decreased by 1
    start_number -= 1

    if ascending:
        number_strs = number_list[start_number : start_number + 3]
    else:
        number_strs = number_list[start_number: start_number - 3: -1]

    print(f'{number_strs[0].title()} little, {number_strs[1]} little, {number_strs[2]} little Indians')


def lyric_end(start_number):
    start_number -= 1
    print(f'{number_list[start_number].title()} little Indian ', end = '')
    print('boys.' if start_number != 0 else 'boy.')


lyric_main(1, True)
lyric_main(4, True)
lyric_main(7, True)
lyric_end(10)

lyric_main(10, False)
lyric_main(7, False)
lyric_main(4, False)
lyric_end(1)