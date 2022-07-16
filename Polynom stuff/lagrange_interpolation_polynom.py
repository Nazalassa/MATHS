import turtle

pts=((-7,-5.2),(-6,2),(-5,3),(-4,1.5),(-1,-0.5),(2,3),(3.5,3.5),(5,4),(7,-3),(6,-5))

def f(x,pts):
  l=len(pts)
  t=0
  for i in range(l):
    r=1
    for k in range(l):
      if k!=i:
        r*=(x-pts[k][0])/(pts[i][0]-pts[k][0])
    t+=r*pts[i][1]
  return t

t = turtle.Turtle()
t.speed(0)
t.color('grey')
t.hideturtle()

cw, ch = 800, 800
turtle.screensize(canvwidth = cw, canvheight = ch, bg='black')

for n in range(-cw//2, cw//2, 20):
  t.up()
  t.goto(n, -ch/2)
  t.down()
  t.goto(n, ch/2)
for n in range(-ch//2, ch//2, 20):
  t.up()
  t.goto(-cw/2, n)
  t.down()
  t.goto(cw/2, n)

t.pensize(3)
t.up()
t.goto(-cw/2, 0)
t.down()
t.goto(cw/2, 0)
t.up()
t.goto(0, -ch/2)
t.down()
t.goto(0, ch/2)
t.up()
t.pensize(1.5)
t.color('white')

t.goto(-cw/2 - 3, 0)
t.down()

for x in range(-cw//2 - 3, cw//2 + 3):
  t.goto(x,max(-ch/2 - 20, min(ch/2 + 20, f(x/20, pts) * 20)))

t.up()
t.color('red')
t.pensize(8)

for p in pts:
  t.goto(20 * p[0], 20 * p[1])
  t.down()
  t.goto(20 * p[0] + .05, 20 * p[1] + .05)
  t.up()
