import argparse
import math
import turtle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numverts', type=int)
    parser.add_argument('-d', '--density', default=1, type=int)
    args = parser.parse_args()
    turtle.setup(width=800, height=800)
    turtle.setworldcoordinates(-1.1, -1.1, 1.1, 1.1)
    turtle.hideturtle()
    #turtle.tracer(0, 0)
    turtle.penup()
    # Place vertices
    a = math.tau/args.numverts # Angle between verts
    b = math.tau/4 # 90 degree offset
    verts = tuple((math.cos(a*x + b), math.sin(a*x + b))
            for x in range(args.numverts))
    # If numverts and density are not coprime, it will result in multiple
    # disconnected polygons
    gcd = math.gcd(args.numverts, args.density)
    for i in range(gcd):
        draw_polygon(verts[i::gcd], args.density//gcd)
    turtle.update()
    turtle.exitonclick()

def draw_polygon(verts, denom):
    turtle.goto(verts[0])
    turtle.pendown()
    i = 0
    while True:
        i = (i+denom)%len(verts)
        turtle.goto(verts[i])
        if i == 0: break
    turtle.penup()

main()
