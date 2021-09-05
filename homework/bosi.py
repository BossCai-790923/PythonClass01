cups=['ball','none','none']
def A_turn(list):
    list.insert(0,list.pop(1))
    return list
def B_turn(list):
    list.insert(1,list.pop(2))
    return list
def C_turn(list):
    list.reverse()
    return list



if __name__=="__main__":
    input1=input()
    inputlist=list(input1)
    for i in inputlist:
        if i == 'A':
            A_turn(cups)
        if i == 'B':
            B_turn(cups)
        if i == 'C':
            C_turn(cups)

    print(cups.index('ball')+1)