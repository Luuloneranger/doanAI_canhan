from collections import deque
import heapq
from queue import PriorityQueue
import copy
import random
from math import *

T = 1
Start = [[2, 6, 5], [0, 8, 7], [4, 3, 1]]
Start_DFS  = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
Goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

Moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def tim_X(x):
    for i in range(3):
        for j in range(3):
            if Goal[i][j] == x :
                return i,j

def khoang_cach_mahathan(Matran_HienTai):
    sum = 0
    for i in range(3):
        for j in range(3):
            if(Matran_HienTai[i][j] != 0):
                pos_x,pos_y = tim_X(Matran_HienTai[i][j])
                sum += abs(i-pos_x) + abs(j - pos_y)
    return sum

def Tim_0(Matran_hientai):
    for i in range(3):
        for j in range(3):
            if Matran_hientai[i][j] == 0:
                return i, j

def Check(x, y):   
    return 0 <= x < 3 and 0 <= y < 3

def Chiphi(matran_HienTai):
    dem = 0
    for i in range(3):
        for j in range(3):
            if matran_HienTai[i][j] != Goal[i][j]:
                dem+=1
    return dem

def DiChuyen(Matran_HienTai, x, y, new_x, new_y):
    new_state = copy.deepcopy(Matran_HienTai)
    new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
    return new_state

def print_matrix(matran):
    for i in range(3):
        for j in range(3):
            print(matran[i][j]," ")
        print("\n")

def BFS(start):
    queue = deque([(start,[])])
    visited = set()
    
    while queue:
        matran_hientai, path = queue.popleft()
        visited.add(str(matran_hientai))
        
        if matran_hientai == Goal:
            path.append(Goal)
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_x=new_X,new_y= new_Y)
                if(str(new_matran) not in visited):
                    queue.append((new_matran,path+[matran_hientai]))
    return None

def UCS(start):
    qp = PriorityQueue()
    qp.put( (0,start,[]) )
    
    visited = set()
    
    while not qp.empty():
        chiphi,matran_hientai, path = qp.get()
        visited.add(str(matran_hientai))
        
        if matran_hientai == Goal:
            path.append(Goal)
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_x=new_X,new_y=new_Y)
                if str(new_matran) not in visited:
                    qp.put((chiphi+Chiphi(new_matran),new_matran,path+[matran_hientai]))
    return None

def change_matran_string(matran):
    return ''.join(str(num) for row in matran for num in row)

def DFS(start):
    stack = [(start,[])]
    visited = set()
    
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    while stack:
        matran_hientai, path = stack.pop()
        if change_matran_string(matran_hientai) == change_matran_string(Goal):
            path.append(matran_hientai)
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in move:
            new_X = x + dx
            new_Y = y + dy
            if (Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                if change_matran_string(new_matran) not in visited:
                    visited.add(change_matran_string(new_matran))
                    new_path = path + [matran_hientai]
                    stack.append((new_matran,new_path))
    return None

def DFS_limited(matran_hientai,limit,path,visited):
    
    if change_matran_string(matran_hientai) == change_matran_string(Goal):
        path.append(Goal)
        return path
    
    if limit == 0:
        return None
    
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    
    x,y = Tim_0(matran_hientai)
        
    for dx,dy in move:
        new_X = x + dx
        new_Y = y + dy
        if (Check(new_X,new_Y)):
            new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
            if change_matran_string(new_matran) not in visited:
                visited.add(change_matran_string(new_matran))
                new_path = path + [matran_hientai]
                res = DFS_limited(new_matran,limit - 1, new_path,visited)
                if res is not None:
                    return res
    return None

def IDDFS(Start,max_depth=50):
    for depth in range(max_depth):
        visited = set()
        result = DFS_limited(Start, depth, [], visited)
        if result is not None:
            return result  
    return None  

def Greedy(Start):
    qp = PriorityQueue()
    qp.put( (0,Start,[]) )
    
    visited = set()
    
    while not qp.empty():
        chiphi1,matran_hientai, path = qp.get()
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_x=new_X,new_y=new_Y)
                if str(new_matran) not in visited:
                    visited.add(str(new_matran))
                    qp.put((khoang_cach_mahathan(new_matran),new_matran,path+[matran_hientai]))
    return None

def A_Star(Start):
    qp = PriorityQueue()
    qp.put( (0,0,Start,[]) )
    
    visited = set()
    
    while not qp.empty():
        f_n,chiphi,matran_hientai, path = qp.get()
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_x=new_X,new_y=new_Y)
                if str(new_matran) not in visited:
                    visited.add(str(new_matran))
                    f_new = chiphi + khoang_cach_mahathan(new_matran)
                    qp.put((f_new,chiphi+Chiphi(new_matran),new_matran,path+[matran_hientai]))
    return None

def IDA_limit(Start,limit):
    qp = PriorityQueue()
    qp.put( (0,0,Start,[]) )
    
    visited = set()
    
    while not qp.empty():
        f_n,chiphi,matran_hientai, path = qp.get()
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
        
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_x=new_X,new_y=new_Y)
                if str(new_matran) not in visited:
                    visited.add(str(new_matran))
                    f_new = chiphi + khoang_cach_mahathan(new_matran)
                    if f_new <= limit:
                        qp.put((f_new,chiphi+Chiphi(new_matran),new_matran,path+[matran_hientai]))
    return None

def IDA(Start,limit):
    check = None
    while check == None:
        limit = limit + limit/2
        check = IDA_limit(Start=Start,limit= limit )
    return check

# local search algorithms 
# A./ Simple hill climbing 

def Stochastic_Hill_Climbing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    
    while stack:
        matran_hientai, path = stack.pop()
    
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
    
        x,y = Tim_0(matran_hientai)
        
        random_state = []
        
        for dx,dy in Moves:
            new_X = dx + x
            new_Y = dy + y 
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                if(str(new_matran) not in visited) :
                    if(khoang_cach_mahathan(new_matran) < khoang_cach_mahathan(matran_hientai)):
                        random_state.append(new_matran)
        
        if random_state:
            new_state = random.choice(random_state)
            visited.add(str(new_state))
            stack.append((new_state,path + [matran_hientai]))
        else :
            return path
    return []

def Hill_Climbing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    
    while stack:
        matran_hientai, path = stack.pop()
    
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
    
        x,y = Tim_0(matran_hientai)
        
        list_state = PriorityQueue()
        
        for dx,dy in Moves:
            new_X = dx + x
            new_Y = dy + y 
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                if(str(new_matran) not in visited) :
                    if(khoang_cach_mahathan(new_matran) < khoang_cach_mahathan(matran_hientai)):
                        list_state.put((khoang_cach_mahathan(new_matran),new_matran))
        
        if not list_state.empty(): 
            chiphi_tmp,new_state = list_state.get()
            visited.add(str(new_state))
            stack.append((new_state,path + [matran_hientai]))
        else :
            return path
    return []

def Simple_Hill_Climbing(Start):
    pass

def Simulated_Annealing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    
    while stack:
        matran_hientai, path = stack.pop()
    
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
    
        x,y = Tim_0(matran_hientai)
        
        list_state = PriorityQueue()
        
        for dx,dy in Moves:
            new_X = dx + x
            new_Y = dy + y 
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                if(str(new_matran) not in visited) :
                    list_state.put((khoang_cach_mahathan(new_matran),new_matran))
        
        if not list_state.empty(): 
            chiphi_tmp,new_state = list_state.get()
            if chiphi_tmp > khoang_cach_mahathan(matran_hientai):
                p = random.uniform(0,1)
                if p < exp(-(khoang_cach_mahathan(matran_hientai) - chiphi_tmp)/T):
                    visited.add(str(new_state))
                    stack.append((new_state,path + [matran_hientai]))
                    break
                else:
                    for i in range(len(list_state.queue)):
                        chiphi_state ,state = list_state.get()
                        if p < exp(-(khoang_cach_mahathan(matran_hientai) - chiphi_state)/T):
                            visited.add(str(state))
                            stack.append((new_state,path + [matran_hientai]))
                            break
            else:
                visited.add(str(new_state))
                stack.append((new_state,path + [matran_hientai]))
        else :
            return path
    return []


def Beam_Search(Start, beam_width=3):
    from queue import PriorityQueue
    current_level = [(Start, [])]
    visited = set()

    while current_level:
        next_level_candidates = PriorityQueue()

        for state, path in current_level:
            if state == Goal:
                return path + [Goal]

            x, y = Tim_0(state)

            for dx, dy in Moves:
                nx, ny = x + dx, y + dy
                if Check(nx, ny):
                    new_state = DiChuyen(state, x, y, nx, ny)
                    if str(new_state) not in visited:
                        visited.add(str(new_state))
                        next_level_candidates.put((Chiphi(new_state), new_state, path + [state]))

        current_level = []
        for _ in range(min(beam_width, next_level_candidates.qsize())):
            _, new_state, new_path = next_level_candidates.get()
            current_level.append((new_state, new_path))

    return []

def Goal_Test(state):
    return state == Goal

def Result_States(state,moves):
    result_states = []
    x, y = Tim_0(state)
    
    dx,dy = moves
    new_X = dx + x
    new_Y = dy + y 
    if Check(new_X, new_Y):
        new_matran = DiChuyen(state, x, y, new_X, new_Y)
        result_states.append(new_matran)
    return result_states

def AND_OR_Search(start):
    plan = OR_Search(start, [])
    return plan

def OR_Search(state, path):
    if Goal_Test(state):
        return []
    if any(state == p for p in path):
        return 'Failure'
    for move in Moves:
        result_states = Result_States(state, move)
        if not result_states:
            continue
        plan = AND_Search(result_states, path + [state])
        if plan != 'Failure':
            return (move, plan)
    return 'Failure'

def AND_Search(states, path):
    plan = {}
    for s in states:
        subplan = OR_Search(s, path)
        if subplan == 'Failure':
            return 'Failure'
        plan[change_matran_string(s)] = subplan
    return plan

def TIm_Path(plan, state):
    path = [state]
    current_state = state
    while isinstance(plan, tuple):
        move, subplans = plan
        x, y = Tim_0(current_state)
        dx, dy = move
        new_x, new_y = x + dx, y + dy
        next_state = DiChuyen(current_state, x, y, new_x, new_y)
        path.append(next_state)
        state_str = change_matran_string(next_state)
        if state_str not in subplans:
            break
        plan = subplans[state_str]
        current_state = next_state
    return path


def sinh_khong_gian_niem_tin(state):
    x, y = Tim_0(state)
    tap_trang_thai = []

    for dx, dy in Moves:
        new_x, new_y = x + dx, y + dy
        if Check(new_x, new_y):
            trang_thai_chinh = DiChuyen(state, x, y, new_x, new_y)
            tap_trang_thai.append(trang_thai_chinh)
    return tap_trang_thai

def giai_qua_khong_gian_niem_tin(start_state):
    tap_trang_thai = sinh_khong_gian_niem_tin(start_state)
    ket_qua = []
    for trang_thai in tap_trang_thai:
        duong_di = BFS(trang_thai)
        if duong_di:
            ket_qua.append((trang_thai, duong_di))
        else:
            print("Khong tim thay duong di cho trang thai:", trang_thai)
    return ket_qua

def BackTracking_Search(State,Path,Visited,depth=100):
    if State == Goal:
        return Path + [Goal]

    if depth == 0:
        return None
    
    x,y = Tim_0(State)
    for dx,dy in Moves:
        new_X = dx + x
        new_Y = dy + y 
        if(Check(new_X,new_Y)):
            new_matran = DiChuyen(State,x,y,new_X,new_Y)
            if str(new_matran) not in Visited:
                Visited.add(str(new_matran))
                result = BackTracking_Search(new_matran,Path + [State],Visited,depth-1)
                if result:
                    return result
    return []

def Xet_matran_Giai_dc(State):
    state = []
    for i in range(3):
        for j in range(3):
            if (State[i][j]!=0):
                state.append(State[i][j])
    
    dem = 0
    for i in range(len(state)):
        for j in range(i+1,len(state)):
            if state[i] > state[j]:
                dem += 1
    if dem % 2 == 0:
        return True
    return False

State_Belief = [[1, 2, 3],[], []]

def Sinh_State(soluong = 100):
    ds_State = []
    Phan_codinh = [1,2,3]
    Phan_random = [x for x in range(9) if x not in Phan_codinh]
    for i in range(soluong):
        random.shuffle(Phan_random)
        State = [Phan_codinh, Phan_random[:3], Phan_random[3:]]
        if (Xet_matran_Giai_dc(State)):
            ds_State.append(State)
    return ds_State

def Giai_niem_tin_mot_phan_bangBFS():
    tap_trang_thai = Sinh_State(10)
    ket_qua = []
    for trang_thai in tap_trang_thai:
        duong_di = BFS(trang_thai)
        if duong_di:
            ket_qua.append((trang_thai, duong_di))
        else:
            print("Khong tim thay duong di cho trang thai:", trang_thai)
    return ket_qua

# Thuật toán tạo ra nhiều tập hợp trạng thái (Kiểm thử, Backtracking, AC-3)

# Thuật toán kiểm thử
def Ktra_matran_khong_trung(State):
    check = []
    for i in range(3):
        for j in range(3):
            if State[i][j] != 0:
                if State[i][j] not in check:
                    check.append(State[i][j])
                else:
                    return False
    return True

# def sinh_trang_thai_co_the_trung_lap(values = [0, 1, 2, 3, 4, 5, 6, 7, 8]):
#     states = []
#     dem = 0
#     for a in values:
#         for b in values:
#             for c in values:
#                 for d in values:
#                     for e in values:
#                         for f in values:
#                             for g in values:
#                                 for h in values:
#                                     for i in values:
#                                         matrix = [
#                                             [a, b, c],
#                                             [d, e, f],
#                                             [g, h, i]
#                                         ]
#                                         states.append(matrix)
#                                         dem += 1
#                                         if(dem == 1000):
#                                             return states
    # return states

def rang_buoc(State):
    while len(State) < 3:
        State.append([0,0,0])
    
    for row in State:
        while len(row) < 3:
            row.append(0)
    
    pt_canxet = [item for row in State for item in row if item != 0]
    
    if len(pt_canxet) != len(set(pt_canxet)):
        return False
    
    a = b = c = d = e = f = g = h = i = 0
    a,b,c = State[0]
    d,e,f = State[1]
    g,h,i = State[2]
    if c != 0 and d != 0 and e != 0:
        if c + d != e:
            return False
    
    if f != 0 and g != 0:
        if f < g:
            return False
    
    if h != 0 and i != 0:
        if abs(h - i) != 1:
            return False
    
    return True

def matran1D_to_2D(matran_1D):
    matran_2d = [matran_1D[i:i + 3] for i in range(0, len(matran_1D), 3)]
    return matran_2d

state = []
lst_state =[]
check = [True for i in range(9)]

def Sinh_trang_thai_khong_trung_lap(n):
    global lst_state
    if len(state) == n :
        State = matran1D_to_2D(state)
        lst_state.append(copy.deepcopy(State))
        return 
    for i in range(n):
        if check[i] == True :
            state.append(i)
            check[i] = False
            Sinh_trang_thai_khong_trung_lap(n)
            state.pop()
            check[i] = True
    return lst_state

def Kiem_Thu_Algorithm():
    lst_State = Sinh_trang_thai_khong_trung_lap(9)
    for state in lst_State:
        if rang_buoc(state) == False:
            print(f"ma tran {state} khong thoa yeu cau")
        else:
            print(f"ma tran {state} thoa yeu cau")

def BackTracking():
    global lst_state
    State = matran1D_to_2D(state)
    if rang_buoc(State) == False: 
        return 
    if len(state) == 9 :
        lst_state.append(copy.deepcopy(State))
        return 
    for i in range(9):
        if check[i] == True :
            state.append(i)
            check[i] = False
            BackTracking()
            state.pop()
            check[i] = True
    return lst_state

