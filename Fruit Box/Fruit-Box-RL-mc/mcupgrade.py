import copy
import multiprocessing.managers
import numpy as np
import random
import multiprocessing
import os
import time

def set_saved_board():
    global now_board, sum_matrix
    now_board = copy.deepcopy(saved_board)
    sum_matrix = np.zeros((10, 19))

def get_sum(x_top,y_top,x_bottom,y_bottom):
    global sum_matrix, now_board
    total = (
        sum_matrix[x_bottom,y_bottom] -
        sum_matrix[x_top,y_bottom] -
        sum_matrix[x_bottom, y_top] +
        sum_matrix[x_top, y_top]
    )
    return total
 
def get_legal_actions():
    global now_board, sum_matrix
    actions = []
    for i in range(1,10):
        for j in range(1,19):
            sum_matrix[i][j] = (
                now_board[i-1][j-1] +
                sum_matrix[i-1][j] +
                sum_matrix[i][j-1] -
                sum_matrix[i-1][j-1]
            )
    for i in range(9):
        for j in range(18):
            for a in range(i + 1, 10):
                for b in range(j + 1, 19):
                    #action = {'x_top':i, 'x_bottom':a, 'y_top':j, 'y_bottom':b}
                    action = [i,a,j,b]
                    if get_sum(i,j,i+1,b) == 0:
                        continue
                    if get_sum(a-1,j,a,b) == 0:
                        continue
                    if get_sum(i,j,a,j+1) == 0:
                        continue
                    if get_sum(i,b-1,a,b) == 0:
                        continue
                    if get_sum(i,j,a,b) == 10:
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
    global now_board, sigma, end_reward
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
        end_reward = score
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
    
def training(time_check,num,t_time):
    global end_reward
    if(time_check):
        start_time = time.time()
        i=1
        while(time.time()-start_time<t_time):
            set_saved_board()
            update_state_value_function([])
            print("episode : ",i,", final reward : ", end_reward)
            i+=1
    else:
        for i in range(num):
            set_saved_board()
            update_state_value_function([])
            print("episode : ",i+1,", final reward : ", end_reward)

def solve_it():
    set_saved_board()
    while(True):
        render()
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
        #print(max_value)
        for i in range(max_action[0],max_action[1]):
            for j in range(max_action[2],max_action[3]):
                now_board[i][j]=0
    print("Score : ",162-np.count_nonzero(now_board))

def render():
    global now_board
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("   " + " ".join(f"{i:2}" for i in range(18)))
    print("  +" + "---" * 18 + "+")

    for i in range(9):
        row_str = f"{i:2}|"
        for j in range(18):
            cell_value = now_board[i, j]
            cell_str = f"{cell_value:2}" if cell_value != 0 else " ."
            row_str += f" {cell_str}"
        row_str += " |"
        print(row_str)
    
    print("  +" + "---" * 18 + "+")

#######################################################

seed = 1
time_training = False
training_time = 10
training_num = 100
sigma=0.5

#######################################################
if seed is not None:
    np.random.seed(seed)

saved_board = np.random.randint(1,10,(9,18))
sum_matrix = np.zeros((10, 19))
now_board = []
set_saved_board()
state_value_dict=dict()
state_times_dict=dict()
state_value_dict[make_board_to_string()] = 0
state_times_dict[make_board_to_string()] = 0
end_reward=0
training(time_training,training_num,training_time)
solve_it()