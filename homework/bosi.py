# caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
caps = ['F', 'F', 'F', 'F', 'B', 'B', 'B', 'B', 'F', 'F', 'F', 'F', 'F']
def yells (list):
    int_f=0
    int_b=0
    lenth=len(list)


    for x in range(lenth):
        if list[x]=='F':
            int_f+=1
        if list[x]=='B':
            int_b+=1
    if int_b>int_f:
        for i in range(lenth):
            if lenth>=i+2:
                if list[i]=='F' and list[i+1]=='F' and list[i+2]=='F':
                    print(f'People in {i} through {i+2} ,please flip your caps')
                    list[i+2]=''

                    continue
            if lenth>i+1:
                if list[i]=='F' and list[i+1]=='F':
                    print(f'People in {i} through {i+1} ,please flip your caps')
                    list[i+1]=''

                    continue
            if lenth>=i:
                if list[i]=='F':
                    print(f'People in {i} ,please flip your caps')
                    continue
    if int_b<int_f:
        for i in range(lenth):
            if lenth>=i+2:
                if list[i]=='B' and list[i+1]=='B' and list[i+2]=='B':
                    print(f'People in {i} through {i+2} ,please flip your caps')
                    list[i+2]=''

                    continue

            if lenth>i+1:
                if list[i]=='B' and list[i+1]=='B':
                    print(f'People in {i} through {i+1} ,please flip your caps')
                    list[i+1]=''
                    continue
            if lenth>=i:
                if list[i]=='B':
                    print(f'People in {i} ,please flip your caps')
                    continue
yells(caps)