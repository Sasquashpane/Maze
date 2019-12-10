import random

def setup():
    size(400,400)
char_width=20


def draw():
    for j in range(height /char_width):
        for i in range(width /char_width):
            draw_slash(random.random(), j*char_width, char_width*i)
            #draw_slash(True,0, char_width * i)
            #draw_slash(True,20,20)
            
noLoop()            

    
def draw_slash(fwd_slash,top,left):
    if fwd_slash >.5:
        line(left+char_width,top,left,top+char_width)
    else:
        line(left, top, left+char_width, top+char_width)  

    
