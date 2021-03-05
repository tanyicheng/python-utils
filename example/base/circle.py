import turtle

t = turtle.Pen()

for i in range(5):
    t.penup()  # 抬笔
    t.goto(0, -i * 10)  # 指针下移
    t.pendown()  # 落笔
    t.circle(20 + i * 10)  # 画圆

turtle.done()
