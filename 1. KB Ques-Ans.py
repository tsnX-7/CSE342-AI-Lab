f = open('input.txt', 'r')
for line in f:
    ans = line.split('. ')
cont = True
tags = ['name', 'study', 'hobby', 'like']
while cont:
    ques = input('Your ques?: ')
    words = ques.split()
    done = False
    for s in words:
        if s in tags:
            for line in ans:
                if s in line:
                    print(line)
                    done = True
                    break
        if done: break
    if done!=True:
        print('Invalid ques')
    cont = 'yes' == input('wanna continue? ')
f.close()
