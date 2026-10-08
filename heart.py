import turtle
import math
import random
import time

def draw_flower(t, c):
    h = t.heading()
    t.penup()
    for _ in range(5):
        t.forward(4)
        t.dot(5, c)
        t.backward(4)
        t.right(72)
    t.dot(4, "white")
    t.setheading(h)

def draw_inner_heart(t, colors):
    t.penup()
    # Draw the inner heart using spaced out multi-color flowers
    for i in range(0, 120, 4):
        a = i * (math.pi * 2) / 120
        x = 16 * (math.sin(a) ** 3) * 2.5
        y = (13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)) * 2.5
        
        t.goto(x, y)
        draw_flower(t, random.choice(colors))

def draw_curve(t, sx, sy, ex, ey, bend):
    dx = ex - sx
    dy = ey - sy
    mx = (sx + ex) / 2
    my = (sy + ey) / 2
    
    cx = mx - dy * bend
    cy = my + dx * bend
    
    t.penup()
    t.goto(sx, sy)
    t.pendown()
    
    for i in range(1, 7):
        st = i / 6
        nx = ((1 - st)**2) * sx + 2 * (1 - st) * st * cx + (st**2) * ex
        ny = ((1 - st)**2) * sy + 2 * (1 - st) * st * cy + (st**2) * ey
        t.goto(nx, ny)

screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Twinkling Heart")

# Lowered tracer to 2 for a noticeably slower, relaxed drawing pace
screen.tracer(2) 

t = turtle.Turtle()
t.speed(0) 
t.hideturtle()

colors = ['red', 'blue', 'lime', 'yellow', 'cyan', 'magenta', 'pink', 'orange', 'violet']
num_lines = 120

# Initial animated draw
draw_inner_heart(t, colors)

for i in range(num_lines):
    a = i * (math.pi * 2) / num_lines
    
    bx = 16 * (math.sin(a) ** 3)
    by = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
    
    ex = bx * 15
    ey = by * 15
    
    sx = bx * 2.5
    sy = by * 2.5
    
    c = random.choice(colors)
    t.color(c)
    
    draw_curve(t, sx, sy, ex, ey, 0.2)
    draw_flower(t, c)

screen.update() 
time.sleep(1)   

# Turn off tracer completely for the instant LED flashing effect
screen.tracer(0) 

try:
    while True:
        t.clear()
        
        # The inner heart will pick new random colors every frame
        draw_inner_heart(t, colors)
        
        for i in range(num_lines):
            a = i * (math.pi * 2) / num_lines
            
            bx = 16 * (math.sin(a) ** 3)
            by = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
            
            ex = bx * 15
            ey = by * 15
            
            sx = bx * 2.5
            sy = by * 2.5
            
            # The outer lines and flowers also get new random colors to simulate LEDs
            c = random.choice(colors)
            t.color(c)
            
            draw_curve(t, sx, sy, ex, ey, 0.2)
            draw_flower(t, c)
            
        screen.update()
        
        # Controls how fast the colors change (LED blink speed)
        time.sleep(0.15)
        
except turtle.Terminator:
    pass
