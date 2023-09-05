#Snake 
#Author Nameless
#CopyRight:  Nah f*k that sh*t

import pygame,sys,random,time
from pygame.locals import*


#game variables 
win_x =680
win_y = 480
fps = 20
color =(12,12,12)
head = [160,60] # head positions will be updated so as to move the snake    
snake_body = [[160,60],[140,60],[120,60]]
move = 'right'
trigger = True


# initialisation
pygame.init()
pygame.mixer.init()




clock = pygame.time.Clock() 

win = pygame.display.set_mode((win_x,win_y))
pygame.display.set_caption('Snake')



while True:
    # Event handling
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        elif event.type ==  KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
     # This section assigns the move variable with direction strings depending on the key pressed           
        if event.type == KEYDOWN:     
            if event.key == K_UP:
                move = 'up'
            if event.key == K_LEFT:
                move = 'left'            
            if event.key == K_RIGHT:
                move = 'right' 
            if event.key == K_DOWN:
                move = 'down'
            
            
            
  # The position of the snake is updated depending on what direction string is assigned to move           
    if move == 'up':
        head[1] -= 20
    if move == 'down':
        head[1] += 20 
    if move == 'right':
        head[0] += 20         
    if move == 'left':
        head[0] -= 20
      
    
    win.fill('black')
    #draw a grid on window
    for x in range(0,win_x-19,20):
        for y in range(0,win_y-19,20):
           cell = pygame.Rect(x,y,20,20)
           pygame.draw.rect(win,color,cell,1)
   
    
    #apple placement on screen
    if trigger:
        apple = [random.randint(0,(win_x-20)//20)*20,random.randint(0,(win_y-20)//20)*20]
        trigger = False
  
     
    # This section grows the snake  
    snake_body.insert(0,list(head))
   
    if head == apple :
        
        # Plays the Sound Effect if the snake eats the Apple
        boom = pygame.mixer.Sound('boom.wav')
        boom.set_volume(2.5)
        boom.play()
        time.sleep(0.2)
        boom.stop()
        trigger = True
       
   
    else:
      snake_body.pop()  
              
   
#drawing Graphics    
    # drawing the snake   
    for coord in snake_body:
        skin = pygame.Rect(coord[0],coord[1],20,20)
        pygame.draw.rect(win,'green',skin)        
    
     
     #drawing the apple   
    food = pygame.image.load('Apple.png')       
    win.blit(food,(apple[0],apple[1]))
    
    
    pygame.display.update()
    clock.tick(fps) 