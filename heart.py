import turtle
import math
import random
import time

def get_evenly_spaced_angles(num_points):
    """
    Approximates the curve to find angles that result in evenly 
    spaced points along the heart's perimeter based on arc length.
    """
    steps = 2000
    angles = [i * (math.pi * 2) / steps for i in range(steps)]
    
    # Compute physical distances on the base curve
    distances = [0.0]
    for i in range(1, steps):
        a1, a2 = angles[i-1], angles[i]
        x1 = 16 * (math.sin(a1) ** 3)
        y1 = 13 * math.cos(a1) - 5 * math.cos(2 * a1) - 2 * math.cos(3 * a1) - math.cos(4 * a1)
        x2 = 16 * (math.sin(a2) ** 3)
        y2 = 13 * math.cos(a2) - 5 * math.cos(2 * a2) - 2 * math.cos(3 * a2) - math.cos(4 * a2)
        distances.append(distances[-1] + math.hypot(x2 - x1, y2 - y1))
        
    total_length = distances[-1]
    target_spacing = total_length / num_points
    
    a_vals = []
    current_target = 0.0
    
    # Interpolate angles based on uniform distance segments
    for i in range(steps - 1):
        while distances[i] <= current_target < distances[i+1]:
            fraction = (current_target - distances[i]) / (distances[i+1] - distances[i])
            a_vals.append(angles[i] + fraction * (angles[i+1] - angles[i]))
            current_target += target_spacing
            if len(a_vals) == num_points:
                return a_vals
    return a_vals

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

def draw_inner_heart(t, colors, a_vals):
    t.penup()
    # Draw the inner heart using the evenly spaced angles (skipping every 4 for breathing room)
    for a in a_vals[::4]:
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

screen.tracer(2) 

t = turtle.Turtle()
t.speed(0) 
t.hideturtle()

colors = ['red', 'blue', 'lime', 'yellow', 'cyan', 'magenta', 'pink', 'orange', 'violet']
num_lines = 120

# Generate perfectly uniform angles based on curve distance
a_vals = get_evenly_spaced_angles(num_lines)

# Initial animated draw
draw_inner_heart(t, colors, a_vals)

for a in a_vals:
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

screen.tracer(0) 

try:
    while True:
        t.clear()
        
        draw_inner_heart(t, colors, a_vals)
        
        for a in a_vals:
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
        time.sleep(0.15)
        
except turtle.Terminator:
    pass
