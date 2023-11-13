import random

def calculate_conflicts(state):
    N = 8
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_neighbor(state):
    N = len(state)
    neighbor = state.copy()
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    neighbor[i] = j
    return neighbor

def hill_climbing(N):
    cur_state = [random.randint(0, N-1) for _ in range(N)]
    print(cur_state)
    cur_conflicts = calculate_conflicts(cur_state)

    it = 0
    while True:
        if cur_conflicts == 0:
            print("Search iterations: ", it)
            return cur_state
        
        neighbor = generate_neighbor(cur_state)
        neighbor_conflicts = calculate_conflicts(neighbor)
        
        if neighbor_conflicts <= cur_conflicts:
            cur_state = neighbor
            cur_conflicts = neighbor_conflicts
        it+=1
    return None  


N = 8    
solution = hill_climbing(N)
for row in solution:
    print(" ".join(["#" if col == row else "." for col in range(N)]))



