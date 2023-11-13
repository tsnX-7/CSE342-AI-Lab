import itertools

s1, s2, s3 = input('Enter your string: ').split()
letters = set(s1+s2+s3)
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    map = dict(zip(letters, perm))
    if map[s1[0]]==0 or map[s2[0]]==0:
        continue
    if len(s1)==len(s2) and len(s3)>len(s2) and map[s3[0]]!=1:
        continue

    cnt1, mul = 0, 1
    for i in s1[::-1]:
        cnt1+= map[i]*mul
        mul*=10

    cnt2, mul = 0, 1
    for i in s2[::-1]:
        cnt2+= map[i]*mul
        mul*=10

    cnt3, mul = 0, 1
    for i in s3[::-1]:
        cnt3+= map[i]*mul
        mul*=10

    if cnt1+cnt2==cnt3:
        print(map)
        print()
        print(s1, "\t ", cnt1)
        print(s2, "\t ", cnt2)
        print("--------------------")
        print(s3, "\t", cnt3)
        break
    else:
        print("No solution")
        break


'''
send more money
two two four
point zero energy
'''
