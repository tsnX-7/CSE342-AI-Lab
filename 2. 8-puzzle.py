import heapq
# d = [-3,3,1,-1]
d = [-1, -3, 1, 3]
vis = {}
states = []
par = {}

def isValid(x):
    return 0<=x<9

def heuristic(puzzle):
    mis = 0
    for i in range(9):
        if puzzle[i]!=goal[i]:
            mis+=1
    return mis

def call_a_star(given):
    pq = [(0, 0, given)]
    heapq.heapify(pq)

    while pq:
        cost, lv, cur_state = heapq.heappop(pq)
        states.append(cur_state)

        if cur_state == goal:
            print(lv)
            return True
        
        for i in range(9):
            if cur_state[i]=='0':
                pos = i
                break
        
        for i in range(4):
            mov = pos+d[i]
            if isValid(mov):
                x, y = pos, mov
                if x>y:
                    x,y=y,x
                temp = cur_state[:x] + cur_state[y] + cur_state[x+1:y] + cur_state[x] + cur_state[y+1:]
                if vis.get(temp, -1)==-1:
                    h_val = lv +1 + heuristic(temp)
                    par[temp] = cur_state
                    heapq.heappush(pq, (h_val, lv+1, temp))
                    vis[temp] = 1
    return False


                



given = "437685210"
goal = "012345678"
if call_a_star(given):
    print("alhamdulillah")
    temp = goal
    path = []
    while temp!=given:
        path.append(temp)
        temp = par[temp]
    path.append(given)
    print(len(path))
    print(path[::-1])
else:
    print("Oops!")
