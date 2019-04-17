import pygame

from array import *


T = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
player=0
opponent=1
cmd=1

run=True

green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
blue=(204,229,255)
green=(204,255,204)
yellow=(255,255,153)

pygame.init()
win=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win.fill((240,230,140))

w, h = pygame.display.get_surface().get_size()

img = pygame.image.load('wood.png')
img1 = pygame.image.load('tt.png')
img2 =pygame.image.load('tile_0.png')
img3 =pygame.image.load('tile_1.png')

pygame.font.init()
myfont1 = pygame.font.SysFont('Comic Sans MS', 22,True)
myfont = pygame.font.SysFont('Comic Sans MS', 30,True)


textsurface = myfont1.render('RESTART', False, (240,230,140))
textsurface1 = myfont1.render('SOUND', False, (240,230,140))
textsurface2 = myfont1.render('QUIT', False, (240,230,140))
textsurface3 = myfont1.render('HOME', False, (240,230,140))
textsurface4 = myfont.render('!!!COMPUTER WON!!!', False, (0,0,0))
textsurface5 = myfont.render('PLAYER WON', False, (0,0,0))
textsurface6 = myfont.render('!GAME TIED!', False, (0,0,0))
textsurface7 = myfont.render('INVALID CHOICE!', False, (0,0,0))
textsurface8 = myfont.render('INVALID CHOICE!', False, (240,230,140))



win.blit(img,(w-170,0))
win.blit(img,(w-370,0))
win.blit(img,(20,0))
win.blit(img,(220,0))
win.blit(img1,(410,0))
win.blit(textsurface,(45,80))
win.blit(textsurface1,(255,80))
win.blit(textsurface2,(w-130,80))
win.blit(textsurface3,(w-330,80))

   

pygame.draw.line(win, black, [w/2-150,h/2-50], [w/2+150,h/2-50], 10)
pygame.draw.line(win, black, [w/2-150,h/2+50], [w/2+150,h/2+50],10)
pygame.draw.line(win, black, [w/2-50,h/2-150], [w/2-50,h/2+150], 10)
pygame.draw.line(win, black, [w/2+50,h/2-150], [w/2+50,h/2+150],10)


def isMoveLeft(T):
    for i in range(0,3):
        for j in range(0,3):
            if T[i][j]==-1:
                return True
    else:
       return False

def evaluate(board) : 
    
    for  row in range(0,3): 
        if board[row][0]==board[row][1] and  board[row][1]==board[row][2] : 
            if board[row][0]==player: 
                return +10 
            elif board[row][0]==opponent :
                return -10  
  
    for  col in range(0,3): 
        if board[0][col]==board[1][col] and  board[1][col]==board[2][col]:
            if board[0][col]==player : 
                return +10 
            elif board[0][col]==opponent : 
                return -10
         
    if  board[0][0]==board[1][1] and  board[1][1]==board[2][2] :
    
        if board[0][0]==player : 
            return +10 
        elif board[0][0]==opponent : 
            return -10  
  
    if  board[0][2]==board[1][1] and  board[1][1]==board[2][0] : 
        if  board[0][2]==player :
            return +10 
        elif board[0][2]==opponent : 
            return -10 
  
    return 0; 


def minimax(board,depth,isMax):  
    score = evaluate(T)
  
    if score == 10 :
        return score; 
  
    if score == -10 : 
        return score; 
  
    if isMoveLeft(T)==False : 
        return 0; 
  
    if isMax : 
     
        best = -1000  
        for i in range(0,3):        
            for j in range(0,3): 
                if T[i][j]==-1 : 
                    T[i][j] = player; 
                    best = max( best, minimax(board, depth+1, not isMax) ) 
                    T[i][j] = -1; 
                    
        return best; 
     
   
    else : 
         best = 1000; 
         for i in range(0,3):
            for j in range(0,3): 
                if T[i][j]== -1 :
                    T[i][j] = opponent; 
                    best = min(best,minimax(board, depth+1, not isMax))
                    T[i][j] = -1; 
                
            
         return best; 


def findBestMove(board): 
    bestVal = -1000; 
    row = -1; 
    col = -1; 
  
    for i in range(0,3) :
        for j in range(0,3) :
            if board[i][j]==-1 :  
                board[i][j] = player  
                moveVal = minimax(T, 0, False) 
 
                board[i][j] = -1 
                if moveVal > bestVal : 
                 
                    row = i; 
                    col = j; 
                    bestVal = moveVal; 
                
  
    #print("The value of the best Move is : ",bestVal) 
    return row,col 




def IsNotOccupied(T,a):
    if a==1 and (T[0][0]==1  or T[0][0]==0):
       win.blit(textsurface7,(550,600)) 
       return False
    if a==2 and (T[0][1]==1  or T[0][1]==0):
       win.blit(textsurface7,(550,600))
       return False
    if a==3 and (T[0][2]==1  or T[0][2]==0):
       win.blit(textsurface7,(550,600)) 
       return False
    if a==4 and (T[1][0]==1  or T[1][0]==0):
       win.blit(textsurface7,(550,600))
       return False
    if a==5 and (T[1][1]==1  or T[1][1]==0):
       win.blit(textsurface7,(550,600))   
       return False
    if a==6 and (T[1][2]==1  or T[1][2]==0):
       win.blit(textsurface7,(550,600))
       return False
    if a==7 and (T[2][0]==1  or T[2][0]==0):
       win.blit(textsurface7,(550,600)) 
       return False
    if a==8 and (T[2][1]==1  or T[2][1]==0):
       win.blit(textsurface7,(550,600)) 
       return False
    if a==9 and (T[2][2]==1  or T[2][2]==0):
       win.blit(textsurface7,(550,600)) 
       return False

    return True 

def function(x,y):
    if x==0 and y==0:
        win.blit(img2,(552,250))
    if x==0 and y==1:
        win.blit(img2,(652,250))
    if x==0 and y==2:
        win.blit(img2,(752,250))
    if x==1 and y==0:
        win.blit(img2,(552,350))
    if x==1 and y==1:
        win.blit(img2,(652,350))
    if x==1 and y==2:
        win.blit(img2,(752,350))
    if x==2 and y==0:
        win.blit(img2,(552,450))
    if x==2 and y==1:
        win.blit(img2,(652,450))
    if x==2 and y==2:
        win.blit(img2,(752,450))
     
 


def main():
    x,y=findBestMove(T)
    T[x][y]=0
    return x,y
     


       

def button(txt,x,y,wid,ht,ic,ac,action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if action=="restart":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            textsurface = myfont1.render('RESTART', False, (250,160,122))
            win.blit(textsurface,(45,80))
            if click[0]==1:
               run=False
               win.fill((240,230,140))
               pygame.time.wait(1000)
               run=True
               pygame.mixer.music.load('music.mp3')
               pygame.mixer.music.play(-1)
               pygame.mixer.music.set_volume(1.0)               
               T[0][0]=-1
               T[0][1]=-1
               T[0][2]=-1
               T[1][0]=-1
               T[1][1]=-1
               T[1][2]=-1
               T[2][0]=-1
               T[2][1]=-1
               T[2][2]=-1
               

               
        else:
            textsurface = myfont1.render('RESTART', False, (240,230,140))
            win.blit(textsurface,(45,80))

    
    if action=="sound":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            textsurface1 = myfont1.render('SOUND', False, (250,160,122))
            win.blit(textsurface1,(255,80))
            if click[0]==1 and pygame.mixer.music.get_volume()>0.0 :
               pygame.mixer.music.set_volume(0.0)               
            elif click[0]==1 and pygame.mixer.music.get_volume()==0.0 :
               pygame.mixer.music.set_volume(1.0)               
 
            
        else:
            textsurface1 = myfont1.render('SOUND', False, (240,230,140))
            win.blit(textsurface1,(255,80))
        

    if action=="quit":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            textsurface2 = myfont1.render('QUIT', False, (250,160,122))
            win.blit(textsurface2,(w-130,80))
            if click[0]==1:
               pygame.quit()
               exit()
        else:
            textsurface2 = myfont1.render('QUIT', False, (240,230,140))
            win.blit(textsurface2,(w-130,80))

    if action=="put1":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and IsNotOccupied(T,1):
               win.blit(textsurface8,(550,600)) 
               T[0][0]=1 
               win.blit(img3,(547,250))
               pygame.display.update()
               pygame.mouse.set_visible(False)
               pygame.time.wait(1000)
               if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)
  
              
        
    if action=="put2":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,2):
              win.blit(textsurface8,(550,600))   
              T[0][1]=1  
              win.blit(img3,(647,250))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  z=evaluate(T)
                  pygame.display.update()
        pygame.mouse.set_visible(True)


    if action=="put3":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,3):
              win.blit(textsurface8,(550,600))   
              T[0][2]=1  
              win.blit(img3,(747,250))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True) 
    
    
    if action=="put4":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and IsNotOccupied(T,4):
              win.blit(textsurface8,(550,600))   
              T[1][0]=1 
              win.blit(img3,(547,350))
              s=isWinner(T)
              print(s)
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
    pygame.mouse.set_visible(True) 
     
    
    if action=="put5":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,5):
              win.blit(textsurface8,(550,600))   
              T[1][1]=1  
              win.blit(img3,(647,350))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)
              

              
    if action=="put6":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and IsNotOccupied(T,6):
              win.blit(textsurface8,(550,600))      
              T[1][2]=1  
              win.blit(img3,(747,350))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)
    

    if action=="put7":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,7):
              win.blit(textsurface8,(550,600))  
              T[2][0]=1  
              win.blit(img3,(547,450))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)


    if action=="put8":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,8):
              win.blit(textsurface8,(550,600)) 
              T[2][1]=1  
              win.blit(img3,(647,450))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)
    
    
    
    if action=="put9":
        if x+wid > cur[0] > x and y+ht > cur[1] > y:
            if click[0]==1 and  IsNotOccupied(T,9):
              win.blit(textsurface8,(550,600))   
              T[2][2]=1  
              win.blit(img3,(747,450))
              pygame.display.update()
              pygame.mouse.set_visible(False)
              pygame.time.wait(1000)
              if isMoveLeft(T)==True:
                  x,y = main()
                  function(x,y)
                  pygame.mouse.set_visible(True)
                  pygame.display.update()
        pygame.mouse.set_visible(True)
  
 

pygame.display.update()


def isWinner(T):
    if T[0][0]==0 and T[0][1]==0 and T[0][2]==0:
       pygame.draw.line(win, black, [w/2-150,h/2-100], [w/2+150,h/2-100], 10) 
       win.blit(textsurface4,(550,600))
       return -1
    elif T[1][0]==0 and T[1][1]==0 and T[1][2]==0:
       pygame.draw.line(win, black, [w/2-150,h/2], [w/2+150,h/2], 10) 
       win.blit(textsurface4,(550,600))
       return -1
    elif T[2][0]==0 and T[2][1]==0 and T[2][2]==0:
       pygame.draw.line(win, black, [w/2-150,h/2+100], [w/2+150,h/2+100], 10)
       win.blit(textsurface4,(550,600))
       return -1
    elif T[0][0]==0 and T[1][0]==0 and T[2][0]==0:
       pygame.draw.line(win, black, [w/2-100,h/2-150], [w/2-100,h/2+150], 10) 
       win.blit(textsurface4,(550,600))
       return -1
    elif T[0][1]==0 and T[1][1]==0 and T[2][1]==0:
       pygame.draw.line(win, black, [w/2,h/2-150], [w/2,h/2+150], 10) 
       win.blit(textsurface4,(550,600))
       return -1
    elif T[0][2]==0 and T[1][2]==0 and T[2][2]==0:
       pygame.draw.line(win, black, [w/2+100,h/2-150], [w/2+100,h/2+150], 10) 
       win.blit(textsurface4,(550,600))
       return -1
    elif T[0][0]==0 and T[1][1]==0 and T[2][2]==0:
       pygame.draw.line(win, black, [w/2-150,h/2-150], [w/2+150,h/2+150], 10)  
       win.blit(textsurface4,(550,600))
       return -1
    elif T[2][0]==0 and T[0][1]==0 and T[0][2]==0:
       pygame.draw.line(win, black, [w/2+150,h/2-150], [w/2-150,h/2+150], 10)   
       win.blit(textsurface4,(550,600))
       return -1
    elif not isMoveLeft(T): 
       win.blit(textsurface6,(600,600))
       return -1
    return 0
    
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
    

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.blit(img,(w-170,0))
    win.blit(img,(w-370,0)) 
    win.blit(img,(20,0))
    win.blit(img,(220,0))
    win.blit(img1,(410,0))
    
    win.blit(textsurface,(45,80))
    win.blit(textsurface1,(255,80))
    win.blit(textsurface2,(w-130,80))
    win.blit(textsurface3,(w-330,80))
   
   
    pygame.draw.line(win, black, [w/2-150,h/2-50], [w/2+150,h/2-50], 10)
    pygame.draw.line(win, black, [w/2-150,h/2+50], [w/2+150,h/2+50],10)
    pygame.draw.line(win, black, [w/2-50,h/2-150], [w/2-50,h/2+150], 10)
    pygame.draw.line(win, black, [w/2+50,h/2-150], [w/2+50,h/2+150],10)
  
    button("QUIT",w-165,65,140,70,black,black,action="quit")
    button("SOUND",225,65,140,70,black,black,action="sound")
    button("RESTART",25,65,140,70,black,black,action="restart")

    if isMoveLeft(T)==True and isWinner(T)==0:
       button("PUT1",w/2-150,h/2-150,100,100,black,black,action="put1")
       button("PUT2",w/2-50,h/2-150,100,100,black,black,action="put2")
       button("PUT3",w/2+50,h/2-150,100,100,black,black,action="put3")
    
       button("PUT4",w/2-150,h/2-50,100,100,black,black,action="put4")
       button("PUT5",w/2-50,h/2-50,100,100,black,black,action="put5")
       button("PUT6",w/2+50,h/2-50,100,100,black,black,action="put6")
    
       button("PUT7",w/2-150,h/2+50,100,100,black,black,action="put7")
       button("PUT8",w/2-50,h/2+50,100,100,black,black,action="put8")
       button("PUT9",w/2+50,h/2+50,100,100,black,black,action="put9")

    pygame.display.update()
    s=isWinner(T)
    pygame.display.update()


    



 
