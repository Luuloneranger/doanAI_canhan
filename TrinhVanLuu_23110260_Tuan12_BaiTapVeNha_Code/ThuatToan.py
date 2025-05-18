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


def Stochastic_Hill_Climbing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    visited.add(str(Start))
    
    result = []
    result.append(Start)
    
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
            result.append(new_state)
        else :
            return path
    return result

def Steepest_Hill_Climbing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    visited.add(str(Start))
    
    result = []
    result.append(Start)
    
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
            result.append(new_state)
        else :
            return path
    return result

def Simple_Hill_Climbing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    visited.add(str(Start))
    
    result = []
    result.append(Start)
    
    while stack:
        matran_hientai, path = stack.pop()
        if matran_hientai == Goal:
            path = path + [Goal]
            return path
    
        x,y = Tim_0(matran_hientai)
        
        for dx,dy in Moves:
            new_X = dx + x
            new_Y = dy + y 
            if(Check(new_X,new_Y)):
                new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                if(str(new_matran) not in visited) :
                    if(khoang_cach_mahathan(new_matran) < khoang_cach_mahathan(matran_hientai)):
                        visited.add(str(new_matran))
                        stack.append((new_matran,path + [matran_hientai]))
                        result.append(new_matran)
                        break
        
    return result

def Simulated_Annealing(Start):
    stack = [ ( Start , [] ) ]
    visited = set()
    
    result = []
    result.append(Start)
    
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
                    result.append(new_state)
                    break
                else:
                    for i in range(len(list_state.queue)):
                        chiphi_state ,state = list_state.get()
                        if p < exp(-(khoang_cach_mahathan(matran_hientai) - chiphi_state)/T):
                            visited.add(str(state))
                            stack.append((new_state,path + [matran_hientai]))
                            result.append(new_state)
                            break
            else:
                visited.add(str(new_state))
                stack.append((new_state,path + [matran_hientai]))
                result.append(new_state)
        else :
            return path
    return result

def Beam_Search(Start, beam_width=3):

    queue = [(khoang_cach_mahathan(Start), Start, [])]
    visited = set()

    result = []
    
    while queue:
        for i in range(min(beam_width, len(queue))):
            chiphi,matran_hientai,path = queue.pop()
            
            result.append(matran_hientai)
            
            if matran_hientai == Goal:
                path.append(Goal)
                return path
            
            visited.add(str(matran_hientai))
            x,y = Tim_0(matran_hientai)
            
            for dx,dy in Moves:
                new_X = dx + x
                new_Y = dy + y 
                if(Check(new_X,new_Y)):
                    new_matran = DiChuyen(matran_hientai,x,y,new_X,new_Y)
                    if str(new_matran) not in visited:
                        visited.add(str(new_matran))
                        queue.append((khoang_cach_mahathan(new_matran),new_matran,path + [matran_hientai]))
        queue.sort(key = lambda x : x[0])
        queue = queue[:beam_width]
    return result


def sinh_cac_ca_the(state,soluong = 2):
    i = 0
    lst_buoc_di = []
    while i <= soluong:
        move = random.choice(Moves)
        x,y = Tim_0(state)
        dx,dy = move
        new_X,new_Y = dx + x,dy + y
        if Check(new_X,new_Y):
            new_matran = DiChuyen(state,x,y,new_X,new_Y)
            if new_matran not in lst_buoc_di:
                lst_buoc_di.append(new_matran)
                state = new_matran
                chiphi = khoang_cach_mahathan(new_matran)
                i += 1
    return (lst_buoc_di, chiphi)

def lai_tao(cha, me):
    mid = min(len(cha), len(me)) // 2
    con = cha[:mid] + me[mid:]
    return con

def dot_bien(lst_state,tile = 0.15):
    new_state = copy.deepcopy(lst_state)
    for i in range(1,len(lst_state)):
        if random.random() <= tile :
            x,y = Tim_0(lst_state[i])
            moves = random.choice(Moves)
            dx,dy = moves
            new_X,new_Y = dx + x,dy + y
            if Check(new_X,new_Y):
                new_matran = DiChuyen(lst_state[i],x,y,new_X,new_Y)
                if new_matran not in new_state:
                    new_state[i] = new_matran
    return new_state    

def Genetic_Algorithm(state,soluong = 10,thehe = 200):
    res = [state]
    for i in range(thehe):
        lst_ca_the = []
        for i in range(soluong):
            ca_the = sinh_cac_ca_the(state)
            lst_ca_the.append(ca_the)
        
        lst_ca_the.sort(key=lambda x: x[1])
        
        for path,chiphi in lst_ca_the:
            if Goal in path:
                return path
        
        hai_ca_the_best = lst_ca_the[:2].copy()
        cha,me = hai_ca_the_best[0][0], hai_ca_the_best[1][0]
        
        con  = lai_tao(cha,me)
        state = dot_bien(con)[-1]
        res.append(state)
    return res

def Tim_Path( path):
    new_path = []
    for i in path:
        new_path.append(i)
        if i == Goal:
            break
    return new_path


def Result_States(state,moves):
    result_states = []
    x, y = Tim_0(state)
    
    lst_dichuyen = [moves,(0,1),(0,-1)]
    for i in lst_dichuyen:
        dx, dy = i
        new_X = dx + x
        new_Y = dy + y 
        if Check(new_X, new_Y):
            new_matran = DiChuyen(state, x, y, new_X, new_Y)
            result_states.append(new_matran)
    # dx,dy = moves
    # new_X = dx + x
    # new_Y = dy + y 
    # if Check(new_X, new_Y):
    #     new_matran = DiChuyen(state, x, y, new_X, new_Y)
    #     result_states.append(new_matran)
        
    #     for move in Moves:
    #         if move != moves:
    #             new_dx, new_dy = new_X + move[0], new_Y + move[1]
    #             if Check(new_dx, new_dy):
    #                 new_matran_tmp = DiChuyen(new_matran, new_X, new_Y, new_dx, new_dy)
    #                 result_states.append(new_matran_tmp)
    weight = []
    for i in range(len(result_states)):
        weight.append((i + 1)*10)
    
    if len(result_states) == 0:
        return None
    res = random.choices(result_states,weights= weight, k=1)
    
    return res[0]

def AND_OR_Search(start,depth = 300):
    plan = OR_Search(start,[],visited=set(),depth=depth)
    return plan

def OR_Search(state, path = [],visited = set(),depth=100):
    if state == Goal or depth <= 0: 
        return path
    
    if str(state) in visited:
        return None
    visited.add(str(state))
    
    for move in Moves:
        result_states = Result_States(state, move)
        if not result_states:
            continue
        plan = AND_Search(result_states, path + [state],visited.copy(),depth=depth-1)
        if plan:
            return plan
    return None

def AND_Search(states, path,visited,depth):
    if Goal in states:
        return path + [Goal]
    result = OR_Search(states, path + [states] ,visited,depth=depth-1)
    if result:
        return result
    return None
    

def moitruong_niem_tin():
    pass

# def sinh_khong_gian_niem_tin(state):
#     x, y = Tim_0(state)
#     tap_trang_thai = []

#     for dx, dy in Moves:
#         new_x, new_y = x + dx, y + dy
#         if Check(new_x, new_y):
#             trang_thai_chinh = DiChuyen(state, x, y, new_x, new_y)
#             tap_trang_thai.append(trang_thai_chinh)
#     return tap_trang_thai

# def giai_qua_khong_gian_niem_tin(start_state):
#     tap_trang_thai = sinh_khong_gian_niem_tin(start_state)
#     ket_qua = []
#     for trang_thai in tap_trang_thai:
#         duong_di = BFS(trang_thai)
#         if duong_di:
#             ket_qua.append((trang_thai, duong_di))
#         else:
#             print("Khong tim thay duong di cho trang thai:", trang_thai)
#     return ket_qua

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

# tap = Giai_niem_tin_mot_phan_bangBFS()
# for i in tap:
#     print("Trang thai:", i[0],"\n")
#     print("Duong di:", i[1])
#     print("\n")

def Sinh_trang_thai_cho_mtnt(soluong = 100):
    ds_trang_thai = []
    state = [x for x in range(9)]
    for i in range(soluong):
        random.shuffle(state)
        new_state = [state[0:3], state[3:6], state[6:9]]
        if (Xet_matran_Giai_dc(new_state)):
            ds_trang_thai.append(new_state)
    return ds_trang_thai    

def Giai_niem_tin_A_star():
    tap_trang_thai = Sinh_trang_thai_cho_mtnt(10)
    ketqua =[]
    for trang_thai in tap_trang_thai:
        duong_di = A_Star(trang_thai)
        if duong_di:
            ketqua.append((trang_thai, duong_di))
        else:
            print("Khong tim thay duong di cho trang thai:", trang_thai)
    return ketqua



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

# Kiem_Thu_Algorithm()

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

# print("Cac ma tran thoa yeu cau thuat toan Backtracking:")
# lst_state = BackTracking()
# for step in lst_state:
#     print(step,"\n")


val = [0,1,2,3,4,5,6,7,8]   
domain = {var: list(range(9)) for var in val}

def sinh_cac_cap():
    cap = []
    for i in range(9):
        for j in range(9):
            if i != j:
                cap.append((i, j))
    return cap

def constraint(x,y,Xi,Xj):
    if x == y:
        return False
    if (Xi, Xj) in [(0, 1), (1, 0)]:
        if x + y != 3:
            return False
    if (Xi, Xj) in [(5, 6)]:
        if x >= y :
            return False
    return True 

def taodomain(domain,Xi,Xj):
    flag = False
    giam = []
    for x in domain[Xi]:
        check = False
        for j in domain[Xj]:
            if constraint(x, j, Xi, Xj):
                check= True
                break
        if not check:
            giam.append(x)
            flag = True
    
    for x in giam:
        domain[Xi].remove(x)

    return flag

def Ac3(domain):
    queue = deque (sinh_cac_cap())
    while queue:
        Xi, Xj = queue.popleft()
        if taodomain( domain,Xi, Xj):
            if not domain[Xi]:
                return False
    return True

state = []

def rangbuoc_theo_constraint(state):
    a = b = c = d = e = f = g = h = i = 0
    a,b,c = state[:3]
    d,e,f = state[3:6]
    g,h,i = state[6:9]
    if a + b != 3:
        return False
    if f >= g :
        return False
    return True

def backtracking_AC3(state = [],depth = 10):
    if len(state) == 9 :
        if rangbuoc_theo_constraint(state):
            print("ma tran:")
            for i in range(0, 9, 3):
                print(state[i:i+3])
            return state
    else :
        None 
    if depth == 0:
        return None
    var = len(state)
    for value in domain[var]:
        flag = True
        for i in range(len(state)):
            if not constraint(state[i], value, i, var):
                flag = False
                break
        if flag:
            state.append(value)
            backtracking_AC3(state)
            state.pop()
    return None

print("Cac ma tran thoa yeu cau thuat toan Backtracking + AC3:")
backtracking_AC3()

def thuong(state):
    if state != Goal:
        return -1
    else:
        return 100

def Q_Learning(start,epsilon=0.1, episodes=1,alpha=0.1,gamma=0.9):
    lst_path = []
    Q_Table = {}
    
    for i in range(3):
        for j in range(3):
            Q_Table[(i,j)] = [0, 0, 0, 0] # khởi tạo Q-table và điền giá trị vào 
    
    for _ in range(episodes): # bắt đầu một episode
        matran_hientai = start
        path = [matran_hientai]
        
        while matran_hientai != Goal:
            x, y = Tim_0(matran_hientai)
            
            if random.random() < epsilon:
                move = random.randint(0, 3)
            else:
                move = Q_Table[(x,y)].index(max(Q_Table[(x,y)]))
            
            dx,dy = Moves[move]
            new_x, new_y = x + dx, y + dy
            
            if Check(new_x, new_y):
                new_state = DiChuyen(matran_hientai, x, y, new_x, new_y)  
                path.append(new_state) 
                
                Q_cu = Q_Table[(x,y)][move]
                
                Thuong = thuong(new_state)
                Q_Table[(x,y)][move] = Q_cu + alpha *(Thuong + gamma* max(Q_Table[(new_x,new_y)]) - Q_cu )
                
                matran_hientai = new_state
        path.append(Goal)
    return path
