import copy
import multiprocessing.managers
import numpy as np
import random
import multiprocessing

def set_saved_board():
    global now_board
    now_board = copy.deepcopy(saved_board)
    
def get_legal_actions():
    global now_board
    actions = []
    for i in range(9):
        for j in range(18):
            for a in range(i + 1, 10):
                for b in range(j + 1, 19):
                    #action = {'x_top':i, 'x_bottom':a, 'y_top':j, 'y_bottom':b}
                    action = [i,a,j,b]
                    sum=0
                    check=0
                    for k1 in range(i,a):
                        check += now_board[k1][j]
                    if not(check):
                        continue
                    for k1 in range(i,a):
                        check += now_board[k1][b-1]
                    if not(check):
                        continue
                    for k2 in range(j,b):
                        check += now_board[i][k2]
                    if not(check):
                        continue
                    for k2 in range(j,b):
                        check += now_board[a-1][k2]
                    if not(check):
                        continue
                    for k1 in range(i,a):
                        for k2 in range(j,b):
                            sum+=now_board[k1][k2]
                    if sum == 10:
                        actions.append(action)
    return actions

def make_board_to_string():
    global now_board
    count = 0
    for i in range(9):
        for j in range(18):
            count *= 2
            if(now_board[i][j]==0):
                count+=1
    return count

def update_state_value_function(history):
    global now_board, sigma
    actions = get_legal_actions()
    #prev_state = make_board_to_string()
    if not(actions):
        score=162-np.count_nonzero(now_board)
        for state in history:
            if not(state in state_value_dict):
                state_value_dict[state]=0
                state_times_dict[state]=0
            state_value_dict[state] += score
            state_times_dict[state] += 1
        return
    action = random.sample(actions,k=1)[0]
    explo = random.uniform(0, 1)
    if(explo<sigma):
        max_action = None
        max_value=0
        for one in actions:
            copy_board = copy.deepcopy(now_board)
            for i in range(one[0],one[1]):
                for j in range(one[2],one[3]):
                    copy_board[i][j]=0
            count = 0
            for i in range(9):
                for j in range(18):
                    count *= 2
                    if(copy_board[i][j]==0):
                        count+=1
            if(count in state_value_dict):
                value = state_value_dict[count]/state_times_dict[count]
                if(value>=max_value):
                    max_action = one
                    max_value = value
        action=one
    #print(action)
    #print(now_board)
    for i in range(action[0],action[1]):
        for j in range(action[2],action[3]):
            now_board[i][j]=0

    next_state = make_board_to_string()
    history.append(next_state)
    update_state_value_function(history)
    
def training(num):
    for i in range(num):
        set_saved_board()
        update_state_value_function([])
        print(i,"time", len(state_value_dict))

def solve_it():
    set_saved_board()
    while(True):
        print(now_board)
        actions = get_legal_actions()
        if not (actions):
            break
        max_value=0
        max_action=None
        #print(actions)
        for action in actions:
            copy_board = copy.deepcopy(now_board)
            for i in range(action[0],action[1]):
                for j in range(action[2],action[3]):
                    copy_board[i][j]=0
            count = 0
            for i in range(9):
                for j in range(18):
                    count *= 2
                    if(copy_board[i][j]==0):
                        count+=1
            if(count in state_value_dict):
                value = state_value_dict[count]/state_times_dict[count]
                if(value>=max_value):
                    max_action = action
                    max_value = value
        print(max_value)
        for i in range(max_action[0],max_action[1]):
            for j in range(max_action[2],max_action[3]):
                now_board[i][j]=0
        
saved_board = np.random.randint(1,10,(9,18))
now_board = []
set_saved_board()
state_value_dict=dict()
state_times_dict=dict()
state_value_dict[make_board_to_string()] = 0
state_times_dict[make_board_to_string()] = 0
sigma=0.5
training(100)
solve_it()

"""
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    procs=[]
    state_value_dict=manager.dict()
    state_times_dict=manager.dict()
    state_value_dict[make_board_to_string()] = 0
    state_times_dict[make_board_to_string()] = 0
    for i in range(4):
        p = multiprocessing.Process(target=training, args=(10,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()    
    #training(10)
    solve_it()
"""