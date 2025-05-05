import pygame as pg 
from ThuatToan import *
import time

figure = (1200,800)
pg.init()

screen = pg.display.set_mode(figure)
screen.fill("white")

def draw_8_puzzel(matran,posx_bd = 10,posy_bd=125,phong = 36):
    font = pg.font.Font(None,phong)
    y1 = posy_bd
    for j in range(3):
        x1 = posx_bd
        for i in range(3):
            nhap = str(matran[j][i])
            if nhap == "0":
                x1 += 100
                continue
            else: 
                square = pg.draw.rect(screen,"#4a90e2",
                                [x1,y1,100,100],border_radius=15)
                pg.draw.rect(screen,"#3f51b5",
                                [x1,y1,100,100],width=5,border_radius=15)
                van_ban = font.render(nhap, True, "#FFFFFF")
                screen.blit(van_ban,van_ban.get_rect(center = square.center) )
                x1 += 100
        y1 += 100

def draw_button(pos,text,phong):
    font = pg.font.Font(None,phong)
    square= pg.draw.rect(screen,"#607D8B",pos,border_radius=14)
    nhap = text
    test = font.render(nhap,True,"#FFFFFF")
    screen.blit(test,test.get_rect(center = square.center)) 
    return square

def VeChu(phong,vitri,chu,color="#263238"):
    font = pg.font.Font(None,phong)
    nhap = chu
    text = font.render(nhap,True,color)
    screen.blit(text,vitri)

def Change_color(square,color,radius=14):
    pg.draw.rect(screen,color,square,border_radius=radius)
    pg.display.update(square)


running = True
select = ""
index = 0
path = []
check = 0
index_xem = 0
time_algorithm = 0
while running:
    screen.fill("#f4f7f8")
    pg.draw.line(screen,"black",(705,0),(705,800),width=1)
    pg.draw.line(screen,"black",(705,380),(1200,380),width=1)
    Algorithm = VeChu(36,[710,10],"Algorithm:")
    
    btn_dfs = draw_button([710,40,80,60],"DFS",26) 
    btn_ucs = draw_button([810,40,80,60],"UCS",26)
    btn_iddfs = draw_button([910,40,80,60],"IDDFS",26)
    btn_bfs = draw_button([1010,40,80,60],"BFS",26)
    btn_Greedy = draw_button([1110,40,80,60],"Greedy",26)
    btn_A_Star = draw_button([710,120,80,60],"A_Star",26)
    btn_IDA = draw_button([810,120,80,60],"IDA_Star",26)
    btn_Stochastic_HillClimbing = draw_button([910,120,80,60],"SHC",26)
    btn_HillClimbing = draw_button([1010,120,80,60],"HC",26)
    btn_Simulated_Annealing = draw_button([1110,120,80,60],"SA",26)
    btn_Beam_Search = draw_button([710,200,80,60],"Beam",26)
    btn_AND_OR_Search = draw_button([810,200,80,60],"AOS",26)
    btn_KhongGianNiemTin_BFS = draw_button([910,200,80,60],"BFS_KGNT",26)
    
    btn_after = draw_button([550,700,100,80],"->",63)
    btn_prev = draw_button([10,700,100,80],"<-",63)
    
    Title = VeChu(60,[200,0],"8 Puzzel Game",color="#009688")
    Begin = draw_8_puzzel(Start)
    batdau = VeChu(36,(100,100),"Start:")
    End = draw_8_puzzel(Goal,400)
    ketthuc = VeChu(36,(450,100),"Goal:")

    Road = VeChu(36,(10,450),"Path:")
    
    ThongTin = VeChu(36,[710,400],"Infomation: ")
    Buoc = VeChu(36,[710,450],f"Step: {len(path)}",color="#263238")
    Time = VeChu(36,[710,500],f"Time: {time_algorithm:.2f} s",color="#263238")
    
    if index < len(path):
        draw_8_puzzel(path[index],210,430)
        pg.time.delay(200)
        index += 1
        
    if index == len(path) and 0 <= index_xem < len(path) :
        draw_8_puzzel(path[index_xem],210,430)
        pg.time.delay(200)
    
    if index_xem < 0 or index_xem > len(path)-1:
        VeChu(36,[200,725],"This step does not exist.!")
        pg.time.delay(1000)
        if index_xem < 0:
            index_xem = 0
        else :
            index_xem = len(path)-1
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if btn_dfs.collidepoint(event.pos):
                select = "DFS"
                index = 0
                index_xem = 0
            elif btn_iddfs.collidepoint(event.pos):
                select = "IDS"
                index = 0
                index_xem = 0
            elif btn_ucs.collidepoint(event.pos):
                select = "UCS"
                index = 0
                index_xem = 0
            elif btn_bfs.collidepoint(event.pos):
                select = "BFS"
                index = 0
                index_xem = 0
            elif btn_Greedy.collidepoint(event.pos):
                select = "Greedy"
                index = 0
                index_xem = 0
            elif btn_A_Star.collidepoint(event.pos):
                select = "A_Star"
                index = 0
                index_xem = 0
            elif btn_prev.collidepoint(event.pos):
                index_xem -= 1
            elif btn_after.collidepoint(event.pos):
                index_xem +=1
            elif btn_IDA.collidepoint(event.pos):
                select = "IDA"
                index = 0
            elif btn_Stochastic_HillClimbing.collidepoint(event.pos):
                select = "SHC"
                index = 0
            elif btn_HillClimbing.collidepoint(event.pos):
                select = "HC"
                index = 0
            elif btn_Simulated_Annealing.collidepoint(event.pos):
                select = "SA"
                index = 0
            elif btn_Beam_Search.collidepoint(event.pos):
                select = "Beam"
                index = 0
            elif btn_AND_OR_Search.collidepoint(event.pos):
                select = "AOS"
                index = 0
            elif btn_KhongGianNiemTin_BFS.collidepoint(event.pos):
                select = "BFS_KGNT"
                index = 0
    if index == 0 :
        start_time = time.time()
        if select == "DFS":
            path = DFS(Start)
        elif select == "BFS":
            path = BFS(Start)  
        elif select == "IDDFS":
            path = IDDFS(Start)
        elif select == "UCS":
            path = UCS(Start)
        elif select == "Greedy":
            path = Greedy(Start)
        elif select == "A_Star":
            path = A_Star(Start)
        elif select == "IDA" :
            path = IDA(Start,10)
        elif select == "SHC":
            path = Stochastic_Hill_Climbing(Start_DFS)
        elif select == "HC":
            path = Hill_Climbing(Start_DFS)
        elif select == "SA":
            path = Simulated_Annealing(Start_DFS)
        elif select == "Beam":
            path = Beam_Search(Start,3)
        elif select == "AOS":
            plan = AND_OR_Search(Start_DFS)
            path = TIm_Path(plan, Start_DFS)
        elif select == "BFS_KGNT":
            tap = giai_qua_khong_gian_niem_tin(Start_DFS)
            path = tap[0][1]
        end_time = time.time()
        time_algorithm = end_time - start_time
    pg.display.flip()
pg.quit()
