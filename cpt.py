
rect_y = 0
rect_x = 450
col11 = random(1,255)
col21 = random(1,255)
col12 = random(1,255)
col22 = random(1,255)
col13 = random(1,255)
col23 = random(1,255)
def setup():
    size(1000,500)


def draw():
    global rect_y, rect_x, col11, col21, col12, col22, col13, col23
    background(0)
    
    #collision right
    if rect_x >= 600:
        rect_x = 600
    #left
    elif rect_x <= 290:
        rect_x = 450       
        col11 = random(1,255)
        col21 = random(1,255)
        col12 = random(1,255)
        col22 = random(1,255)
        col13 = random(1,255)
        col23 = random(1,255)
        
    for num in range(1,255,10):
            print random(num)
    
    #left box
    fill(col11,col12,col13)
    rect(0,0,300,500)
    
    #right box
    fill(col21,col22,col23)
    rect(700,0,300,500)
    
    #mid box
    fill(col11,col12,col13)
    rect(rect_x,rect_y,100,100)
    
    #reset
    if rect_y == 500:
        rect_y = -50
    
    rect_y+=1
def keyPressed():
    global rect_x
    if key == 'd':
        rect_x += 10
    elif key == 'a':
        rect_x -= 10
    
    #controls
    

    print rect_x
