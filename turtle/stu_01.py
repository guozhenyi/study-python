import time
import turtle


# 改变画笔颜色
turtle.color("blue")

# 改变画笔宽度
turtle.pensize(10)

#
# 画三角形
#
turtle.forward(100)  # 前进100步
turtle.left(120)  # 左转120度
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

# 抬起画笔（不绘制线条）
turtle.penup()

turtle.left(120)
turtle.forward(200)

# 放下画笔
turtle.pendown()

#
# 正方形
#
turtle.color("red")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)


print(turtle.pos())  # 获取海龟坐标(x,y)


turtle.penup()
turtle.home()  # 将海龟送回起点（这适用于海龟消失在屏幕之外的情况）

print(turtle.pos())

time.sleep(5)  # 延时5秒
turtle.clear()  # 清空屏幕

turtle.pendown()

for x in range(50):
    for c in ("blue", "red", "green"):
        turtle.color(c)
        turtle.forward(x)
        turtle.right(10)

time.sleep(5)
turtle.clear()
turtle.penup()
turtle.home()

#
# 画星型
#
turtle.pendown()
turtle.color("red")
turtle.fillcolor("yellow")

print("Star:")

turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    print(turtle.pos())
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()


# 保持窗口不关闭
turtle.mainloop()
