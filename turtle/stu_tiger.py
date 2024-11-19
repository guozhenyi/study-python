import time
import turtle as t

COLOR = "#B2814D"


def set_start(x, y, w, c=COLOR):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.setheading(t.towards(0, 0))
    t.width(w)
    t.pencolor(c)
    t.pendown()
    t.speed(0)


def left_rotate(time, angle, length):
    for i in range(time):
        t.left(angle)
        t.forward(length)


def right_rotate(time, angle, length):
    for i in range(time):
        t.right(angle)
        t.forward(length)


def draw_circle(radius, color, color2=""):
    if color2 == "":
        color2 = color
    t.penup()
    t.setheading(t.towards(0, 0))
    t.right(90)
    t.pencolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.fillcolor(color2)
    t.end_fill()


def fill_color(color):
    def decorator_all(func):
        def wrapper(*args, **kwargs):
            t.begin_fill()
            func(*args, **kwargs)
            t.fillcolor(color)
            t.end_fill()

        return wrapper

    return decorator_all


def fill_color_patch(x, y, c="#fffffb"):
    set_start(x, y, 1, c=c)
    t.forward(1)


def head_outline():
    set_start(0, -40, 2.5)
    t.right(90)
    left_rotate(5, 3, 14)
    left_rotate(5, 8, 8)
    left_rotate(10, 5, 6.5)
    left_rotate(5, 5.5, 10)
    left_rotate(25, 4, 10)
    left_rotate(6, 5.5, 5)
    left_rotate(7, 3, 7)
    left_rotate(5, 10, 8)
    left_rotate(5, 3, 14)


@fill_color("#fdb933")
def draw_head():
    head_outline()
    t.pencolor("#CDCDCD")
    t.goto(0, -40)


@fill_color("#fffffb")
def draw_face():
    set_start(0, -40, 2.5)
    t.right(90)
    left_rotate(5, 3, 14)
    left_rotate(1, 80, 2.5)
    t.pencolor("#fffffb")
    left_rotate(12, 5, 6.5)
    left_rotate(5, 6, 15)
    left_rotate(5, 5, 10)
    left_rotate(5, 12, 10)
    t.backward(0.5)
    t.left(65)
    t.pencolor(COLOR)
    t.backward(3)
    left_rotate(5, 3, 14)
    t.forward(5)


def draw_moustache():
    fill_color_patch(-41, -31)
    t.begin_fill()
    set_start(-41, -31, 2.5)
    t.right(180)
    left_rotate(4, 20, 4)
    left_rotate(1, 90, 8)
    t.right(150)
    left_rotate(4, 25, 3)
    t.forward(6)
    left_rotate(1, 110, 5.5)
    t.right(165)
    left_rotate(4, 15, 3.2)
    t.left(150)
    right_rotate(3, 30, 2.2)
    right_rotate(1, 105, 5)
    t.left(130)
    right_rotate(6, 5, 1.8)
    right_rotate(1, 130, 2)
    t.left(60)
    left_rotate(2, 30, 1)
    left_rotate(4, 28, 4)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(-45, -28, 2.5)
    t.right(70)
    left_rotate(5, 2.5, 4)
    left_rotate(4, 9, 3)
    left_rotate(5, 3, 4.5)


def draw_mouth():
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    left_rotate(1, 85, 35)
    left_rotate(1, 70, 7)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    right_rotate(1, 78, 36)
    right_rotate(1, 65, 6)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    left_rotate(1, 85, 30)
    right_rotate(1, 108, 12)
    right_rotate(1, 140, 5)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    right_rotate(1, 75, 28)
    left_rotate(1, 85, 10)
    left_rotate(1, 130, 8)
    set_start(3, 0, 2.5)
    t.left(90)
    right_rotate(5, 5, 4.8)
    right_rotate(4, 18, 1.8)
    left_rotate(1, 3, 27)
    right_rotate(4, 18, 1)
    right_rotate(1, 15, 22)
    t.right(88)
    right_rotate(9, 1, 4.5)
    t.begin_fill()
    set_start(3, 0, 2.5)
    t.left(90)
    right_rotate(4, 5, 4.8)
    right_rotate(1, 5, 2)
    right_rotate(1, 67, 37)
    right_rotate(1, 86, 18)
    t.fillcolor("#f15a22")
    t.end_fill()
    t.begin_fill()
    set_start(3, 0, 2.5)
    t.pencolor("#aa2116")
    t.left(90)
    right_rotate(2, 5, 6)
    t.right(120)
    left_rotate(10, 6, 2)
    t.right(55)
    left_rotate(11, 5.5, 1.8)
    right_rotate(1, 110, 10)
    t.right(100)
    right_rotate(9, 1, 4.5)
    t.fillcolor("#aa2116")
    t.end_fill()
    set_start(3, 0, 2.5)
    t.left(90)
    right_rotate(5, 5, 4.8)
    right_rotate(4, 18, 1.8)
    left_rotate(1, 3, 27)
    right_rotate(4, 18, 1)
    right_rotate(1, 15, 22)
    t.right(88)
    right_rotate(9, 1, 4.5)
    set_start(21, 10, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")
    set_start(10, 16, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")
    set_start(21, 19, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")
    set_start(-57, 16, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")
    set_start(-51, 24, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")
    set_start(-64, 24, 1, c="#fdb933")
    draw_circle(2.3, "#fdb933")


def draw_nose():
    set_start(6, 37, 1)
    t.pencolor("#e0861a")
    t.right(150)
    t.begin_fill()
    left_rotate(6, 3, 4)
    left_rotate(6, 15, 3)
    left_rotate(6, 3, 4)
    t.fillcolor("#e0861a")
    t.end_fill()
    set_start(6, 37, 1.5)
    t.right(120)
    t.begin_fill()
    left_rotate(5, 4, 4)
    left_rotate(3, 10, 3)
    left_rotate(5, 4, 4)
    left_rotate(7, 15, 0.8)
    left_rotate(5, 4, 4)
    left_rotate(5, 8, 2)
    left_rotate(5, 4, 4)
    left_rotate(7, 15, 0.8)
    t.fillcolor("#b4532a")
    t.end_fill()
    set_start(-16, 36, 1)
    t.pencolor("#d1923f")
    t.right(75)
    t.begin_fill()
    right_rotate(4, 15, 2)
    right_rotate(5, 26, 1)
    right_rotate(4, 15, 2)
    right_rotate(5, 26, 1)
    t.fillcolor("#d1923f")
    t.end_fill()
    set_start(-25, 25, 1)
    t.pencolor("#130c0e")
    t.left(110)
    t.begin_fill()
    left_rotate(6, 15, 1.5)
    left_rotate(5, 15, 1)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-10, 24, 1)
    t.pencolor("#130c0e")
    t.left(175)
    t.begin_fill()
    right_rotate(6, 15, 1.2)
    right_rotate(5, 15, 1)
    t.fillcolor("#130c0e")
    t.end_fill()


def draw_eye():
    set_start(-50, 34, 1, c="#130c0e")
    t.left(115)
    t.begin_fill()
    left_rotate(8, 6.5, 7)
    left_rotate(5, 15, 7)
    left_rotate(5, 10, 5.5)
    left_rotate(5, 15, 6)
    left_rotate(5, 5, 9.5)
    left_rotate(4, 30, 2)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-57, 40, 1, c="#fffffb")
    t.left(112)
    t.begin_fill()
    left_rotate(8, 6.5, 5)
    left_rotate(5, 15, 6)
    left_rotate(5, 10, 4.5)
    left_rotate(5, 15, 5)
    left_rotate(5, 6.5, 7)
    left_rotate(4, 15, 2)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(-90, 62, 1, c="#563624")
    draw_circle(15, "#563624")
    set_start(-84, 59, 1, c="#130c0e")
    draw_circle(9, "#130c0e")
    set_start(-90, 63, 1, c="#fffffb")
    draw_circle(3.5, "#fffffb")
    set_start(16, 25, 1, c="#130c0e")
    t.right(150)
    t.begin_fill()
    right_rotate(8, 6.5, 7)
    right_rotate(5, 15, 7)
    right_rotate(5, 10, 5.5)
    right_rotate(5, 15, 6)
    right_rotate(5, 5, 9.5)
    right_rotate(4, 30, 2)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(24, 28, 1, c="#fffffb")
    t.right(135)
    t.begin_fill()
    right_rotate(8, 7, 5)
    right_rotate(5, 15, 5.5)
    right_rotate(5, 10, 4.5)
    right_rotate(5, 15, 4.5)
    right_rotate(5, 6.5, 6.5)
    right_rotate(4, 13, 2)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(57, 48, 1, c="#563624")
    draw_circle(15, "#563624")
    set_start(53, 44, 1, c="#130c0e")
    draw_circle(9, "#130c0e")
    set_start(38, 47, 1, c="#fffffb")
    draw_circle(3.5, "#fffffb")


def draw_brow():
    set_start(12, 88, 1, c="#130c0e")
    t.right(82)
    t.begin_fill()
    left_rotate(3, 3, 5)
    right_rotate(5, 4, 6)
    right_rotate(7, 24, 2.3)
    right_rotate(3, 5, 4.5)
    left_rotate(1, 90, 8)
    t.left(95)
    left_rotate(3, 8, 5)
    right_rotate(3, 25, 1.2)
    right_rotate(3, 11, 1.5)
    right_rotate(3, 25, 1.2)
    right_rotate(3, 3, 4.5)
    left_rotate(1, 85, 7)
    left_rotate(1, 90, 15)
    right_rotate(5, 30, 2.2)
    right_rotate(3, 9, 6)
    right_rotate(6, 3, 5)
    right_rotate(8, 18, 1.3)
    right_rotate(3, 10, 5.3)
    left_rotate(1, 90, 8)
    t.left(112)
    right_rotate(3, 3, 4.5)
    right_rotate(3, 25, 1)
    right_rotate(3, 10, 1.5)
    right_rotate(3, 28, 1)
    left_rotate(3, 5, 3)
    left_rotate(3, 25, 1)
    left_rotate(3, 5, 1.8)
    left_rotate(1, 90, 17)
    right_rotate(3, 35, 0.8)
    right_rotate(3, 10, 3)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(88, -16, 1, c="#130c0e")
    t.begin_fill()
    right_rotate(5, 15, 3)
    right_rotate(4, 5.5, 3)
    right_rotate(3, 28, 1)
    right_rotate(5, 6, 4)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(106, 9, 1, c="#130c0e")
    t.right(15)
    t.begin_fill()
    right_rotate(5, 5, 5.5)
    right_rotate(5, 29, 3)
    right_rotate(5, 5, 4.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(110, 36, 1, c="#130c0e")
    t.left(20)
    t.begin_fill()
    right_rotate(3, 10, 2)
    right_rotate(3, 10, 6)
    right_rotate(5, 29, 2)
    t.forward(20)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(75, 76, 1, c="#130c0e")
    t.right(105)
    t.begin_fill()
    left_rotate(5, 10, 4)
    right_rotate(6, 28, 2)
    right_rotate(5, 10, 5)
    right_rotate(6, 25, 2)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-75, 100, 1, c="#130c0e")
    t.right(108)
    t.begin_fill()
    right_rotate(3, 3, 8)
    right_rotate(4, 35, 2)
    right_rotate(8, 9, 3.2)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-145, 58, 1, c="#130c0e")
    t.right(30)
    t.begin_fill()
    left_rotate(5, 15, 5)
    left_rotate(3, 18, 3)
    t.left(92)
    right_rotate(4, 5, 6)
    right_rotate(1, 5, 4)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-148, 46, 1, c="#130c0e")
    t.left(40)
    t.begin_fill()
    right_rotate(5, 10, 6.5)
    right_rotate(4, 32, 2)
    right_rotate(4, 10, 6.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-138, 7, 1, c="#130c0e")
    t.left(10)
    t.begin_fill()
    left_rotate(5, 8, 4)
    left_rotate(6, 20, 1.5)
    left_rotate(4, 8, 4.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    head_outline()


def draw_ear():
    set_start(101, 74, 2.5)
    t.left(150)
    t.begin_fill()
    left_rotate(5, 6, 3)
    left_rotate(5, 12, 5)
    left_rotate(3, 13, 12)
    left_rotate(5, 12, 7)
    left_rotate(4, 16, 5)
    t.fillcolor("#fdb933")
    t.end_fill()
    set_start(94, 89, 1, c="#f3715c")
    t.right(168)
    t.begin_fill()
    left_rotate(5, 17, 6)
    left_rotate(4, 20, 5)
    t.goto(94, 89)
    t.fillcolor("#f3715c")
    t.end_fill()
    set_start(-125, 98, 2.5)
    t.right(165)
    t.begin_fill()
    right_rotate(5, 6, 3)
    right_rotate(5, 12, 5)
    right_rotate(3, 13, 12)
    right_rotate(5, 12, 7)
    right_rotate(4, 16, 4.5)
    t.fillcolor("#fdb933")
    t.end_fill()
    set_start(-115, 110, 1, c="#f3715c")
    t.left(160)
    t.begin_fill()
    right_rotate(5, 17, 6)
    right_rotate(4, 20, 5.5)
    t.goto(-115, 110)
    t.fillcolor("#f3715c")
    t.end_fill()
    head_outline()


def draw_cap():
    set_start(55, 123, 2.5)
    t.right(150)
    left_rotate(13, 11, 12)
    set_start(18, 170, 2.5)
    t.right(180)
    t.begin_fill()
    left_rotate(10, 16, 4)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(55, 123, 2.5)
    t.right(150)
    t.begin_fill()
    left_rotate(13, 11, 12)
    t.fillcolor("#FF0000")
    t.end_fill()
    set_start(55, 123, 2.5)
    t.right(113)
    t.begin_fill()
    left_rotate(15, 5, 8.6)
    t.fillcolor("#228B22")
    t.end_fill()
    set_start(30, 142, 2.5)
    t.right(170)
    left_rotate(18, 8.9, 5)
    set_start(-2, 150, 2.5)
    t.left(178)
    right_rotate(4, 5, 6)
    set_start(55, 123, 2.5)
    t.begin_fill()
    t.goto(50.13, 124.56)
    t.setheading(148.5)
    left_rotate(12, 4, 10)
    t.fillcolor("#fdb933")
    t.end_fill()


def draw_shadow():
    fill_color_patch(75, -155)
    _draw_shadow()


@fill_color("#fab27b")
def _draw_shadow():
    set_start(75, -155, 1, c="#fab27b")
    left_rotate(5, 8, 5)
    left_rotate(10, 4, 10)
    left_rotate(5, 6, 9)
    left_rotate(4, 30, 4.5)
    left_rotate(5, 3.5, 16)
    left_rotate(3, 3.5, 18)
    left_rotate(3, 8, 5)
    left_rotate(4, 20, 1.5)
    t.goto(75, -155)


def draw_body():
    fill_color_patch(0, -40)
    set_start(0, -40, 2.5)
    t.right(90)
    t.begin_fill()
    left_rotate(2, 3, 14)
    t.width(2.4)
    t.goto(53, -74)
    t.pencolor("#87481f")
    t.left(20)
    right_rotate(5, 16, 1.3)
    right_rotate(4, 8, 8)
    right_rotate(1, 15, 2)
    right_rotate(1, 30, 7)
    right_rotate(3, 28, 2)
    right_rotate(1, 5, 4)
    right_rotate(1, 90, 6)
    right_rotate(1, 180, 10)
    right_rotate(3, 5, 8)
    right_rotate(3, 10, 6.5)
    right_rotate(2, 15, 2)
    right_rotate(4, 7, 4.5)
    left_rotate(2, 18, 1)
    left_rotate(4, 12, 5)
    left_rotate(4, 15, 3)
    left_rotate(4, 7, 4)
    right_rotate(1, 82, 2)
    right_rotate(4, 8, 7)
    right_rotate(2, 12, 2)
    right_rotate(4, 28, 1.5)
    right_rotate(1, 10, 6)
    right_rotate(1, 60, 4.5)
    t.right(170)
    right_rotate(5, 10, 5)
    right_rotate(10, 2.5, 5)
    t.goto(-71.81, -32.68)
    t.setheading(345.5)
    t.width(2.5)
    t.pencolor(COLOR)
    left_rotate(2, 3, 14)
    t.fillcolor("#fdb933")
    t.end_fill()
    set_start(0, -42, 1)
    t.right(90)
    t.pencolor("#fffffb")
    t.begin_fill()
    right_rotate(5, 12, 5)
    right_rotate(3, 13, 15)
    right_rotate(3, 25, 12)
    t.backward(1)
    t.right(23)
    left_rotate(3, 15, 6)
    t.right(5)
    right_rotate(3, 20, 11)
    right_rotate(3, 15, 12)
    right_rotate(3, 15, 10)
    right_rotate(1, 15, 20)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(37, -125, 1)
    t.pencolor("#130c0e")
    t.begin_fill()
    right_rotate(1, 5, 8)
    right_rotate(4, 30, 1.5)
    right_rotate(1, 20, 6)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(29, -130, 1)
    t.pencolor("#130c0e")
    t.begin_fill()
    t.left(20)
    right_rotate(2, 5, 5)
    left_rotate(4, 30, 1.5)
    left_rotate(2, 10, 4)
    right_rotate(3, 20, 2)
    t.left(155)
    left_rotate(3, 8, 5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-62, -139, 1)
    t.pencolor("#130c0e")
    t.begin_fill()
    t.right(65)
    left_rotate(2, 10, 4)
    left_rotate(3, 25, 1.5)
    left_rotate(1, 10, 2)
    left_rotate(3, 28, 1.5)
    right_rotate(3, 10, 3.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-71, -118, 1)
    t.pencolor("#130c0e")
    t.begin_fill()
    t.right(50)
    left_rotate(4, 10, 2.5)
    left_rotate(5, 28, 1.5)
    right_rotate(3, 10, 2.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(-75, -94, 1)
    t.pencolor("#130c0e")
    t.begin_fill()
    t.right(30)
    left_rotate(4, 10, 2.5)
    left_rotate(5, 28, 1.5)
    right_rotate(3, 10, 2.5)
    t.fillcolor("#130c0e")
    t.end_fill()


def draw_left_hand():
    set_start(0, -40, 2.5)
    t.right(90)
    left_rotate(4, 3, 14)
    left_rotate(1, 3, 8)
    right_rotate(1, 33, 3)
    t.begin_fill()
    left_rotate(1, 0, 4)
    left_rotate(3, 7, 7)
    left_rotate(4, 18, 3.8)
    set_start(103, -26, 2.5)
    right_rotate(3, 20, 4.5)
    right_rotate(3, 20, 2.5)
    right_rotate(2, 20, 2)
    right_rotate(2, 18, 5)
    right_rotate(5, 30, 1.5)
    right_rotate(1, 5, 8)
    right_rotate(1, 180, 2)
    right_rotate(2, 40, 3.5)
    set_start(106, -8, 2.5)
    t.right(90)
    right_rotate(2, 10, 4)
    right_rotate(4, 24, 3)
    right_rotate(2, 10, 4)
    right_rotate(2, 20, 5)
    right_rotate(5, 26, 1.2)
    right_rotate(2, 10, 4)
    right_rotate(1, 190, 4)
    right_rotate(1, 90, 3)
    set_start(128, -12, 2.5)
    t.left(155)
    right_rotate(3, 20, 5.5)
    right_rotate(2, 25, 1.5)
    right_rotate(1, 25, 4)
    right_rotate(3, 25, 2)
    right_rotate(2, 10, 3)
    set_start(124, -30, 2.5)
    t.left(150)
    right_rotate(8, 25, 2)
    right_rotate(1, 15, 3)
    right_rotate(2, 28, 2)
    set_start(115, -35, 2.5)
    t.left(100)
    right_rotate(5, 26, 1.8)
    right_rotate(1, 25, 5)
    set_start(103, -31, 2.5)
    t.left(135)
    right_rotate(5, 10, 5)
    right_rotate(4, 15, 6)
    left_rotate(1, 100, 7)
    t.right(120)
    right_rotate(3, 12, 2.5)
    t.left(170)
    right_rotate(3, 15, 3)
    t.right(110)
    right_rotate(3, 12, 3)
    t.left(140)
    right_rotate(3, 12, 3)
    t.right(120)
    right_rotate(3, 10, 3.5)
    left_rotate(1, 125, 10)
    right_rotate(3, 23, 3)
    right_rotate(3, 9, 9.5)
    t.fillcolor("#fdb933")
    t.end_fill()
    set_start(115, -35, 2.5)
    t.left(100)
    t.begin_fill()
    right_rotate(5, 26, 1.8)
    right_rotate(1, 25, 5)
    t.pencolor("#fffffb")
    t.width(1)
    t.left(90)
    right_rotate(4, 40, 2)
    t.left(90)
    right_rotate(4, 40, 1)
    left_rotate(1, 135, 5)
    t.right(80)
    right_rotate(3, 26, 4.5)
    t.right(130)
    left_rotate(3, 28, 3)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(61, -33, 1)
    t.left(118)
    t.pencolor("#130c0e")
    t.begin_fill()
    right_rotate(3, 5, 3.5)
    right_rotate(4, 32, 1.5)
    right_rotate(3, 12, 2.7)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(78, -36, 1)
    t.left(110)
    t.pencolor("#130c0e")
    t.begin_fill()
    left_rotate(3, 5, 3.5)
    t.right(50)
    right_rotate(4, 20, 1)
    right_rotate(5, 10, 3)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(94, -35, 1)
    t.left(125)
    t.pencolor("#130c0e")
    t.begin_fill()
    left_rotate(3, 5, 2)
    t.right(50)
    right_rotate(4, 25, 2)
    right_rotate(3, 10, 2.2)
    t.fillcolor("#130c0e")
    t.end_fill()


def draw_right_hand():
    fill_color_patch(-44.24, -37.54)
    set_start(-44.24, -37.54, 2.5)
    t.setheading(351.5)
    t.begin_fill()
    t.right(177)
    right_rotate(4, 3, 14)
    t.right(3)
    t.goto(-106, -22)
    set_start(-106, -22, 2.5)
    t.right(175)
    right_rotate(3, 5, 5.5)
    right_rotate(3, 22, 4)
    t.right(80)
    left_rotate(2, 25, 4)
    left_rotate(4, 35, 5.5)
    left_rotate(3, 30, 1.5)
    left_rotate(3, 20, 2)
    left_rotate(1, 10, 2.5)
    t.right(120)
    left_rotate(3, 20, 2.5)
    set_start(-143, -2, 2.5)
    t.left(120)
    left_rotate(4, 25, 3.5)
    left_rotate(1, 35, 3)
    left_rotate(2, 15, 3)
    left_rotate(5, 22, 3.5)
    left_rotate(2, 20, 2.5)
    set_start(-155, -7, 2.5)
    t.left(170)
    left_rotate(2, 35, 3.5)
    left_rotate(2, 12, 4.5)
    left_rotate(3, 28, 4)
    left_rotate(3, 10, 3)
    left_rotate(3, 28, 3.5)
    set_start(-158, -27, 2.5)
    t.right(130)
    left_rotate(3, 30, 2.5)
    left_rotate(4, 13, 4)
    left_rotate(4, 35, 2.5)
    set_start(-135, -25, 2.5)
    t.right(95)
    left_rotate(3, 12, 9)
    left_rotate(4, 12, 4)
    right_rotate(1, 90, 8)
    t.left(120)
    left_rotate(3, 12, 3)
    t.right(160)
    left_rotate(3, 10, 4)
    t.left(120)
    left_rotate(3, 12, 3.5)
    t.right(145)
    left_rotate(3, 10, 3.5)
    t.left(125)
    left_rotate(3, 10, 3.5)
    right_rotate(1, 135, 10)
    t.fillcolor("#fdb933")
    t.end_fill()
    fill_color_patch(-107, -23)
    t.begin_fill()
    set_start(-107, -23, 1)
    t.pencolor("#130c0e")
    t.right(90)
    right_rotate(3, 3, 3.5)
    left_rotate(5, 25, 1)
    left_rotate(3, 15, 3.2)
    t.fillcolor("#130c0e")
    t.end_fill()
    fill_color_patch(-122, -25)
    t.begin_fill()
    set_start(-122, -25, 1)
    t.pencolor("#130c0e")
    t.right(120)
    left_rotate(3, 5, 2)
    left_rotate(4, 30, 1.4)
    left_rotate(3, 15, 3)
    t.fillcolor("#130c0e")
    t.end_fill()


def draw_clothes():
    set_start(0, -40, 2.5)
    t.right(90)
    t.begin_fill()
    left_rotate(3, 3, 14)
    t.goto(47.57, -36.43)
    t.setheading(94.25)
    t.left(171)
    left_rotate(3, 9, 9.5)
    left_rotate(1, 9, 3)
    left_rotate(2, 23, 2.5)
    t.right(150)
    left_rotate(3, 10, 5)
    right_rotate(3, 10, 10)
    right_rotate(1, 20, 4)
    right_rotate(2, 10, 4)
    t.right(90)
    left_rotate(5, 5, 10)
    t.fillcolor("#FF0000")
    t.end_fill()
    set_start(0, -40, 2.5)
    t.right(90)
    t.begin_fill()
    left_rotate(1, 3, 14)
    left_rotate(1, 3, 13)
    t.right(88)
    right_rotate(5, 5, 10)
    t.goto(21.85, -91.11)
    t.setheading(197.25)
    right_rotate(1, 20, 4)
    right_rotate(2, 10, 4)
    t.right(90)
    left_rotate(5, 5, 10)
    t.fillcolor("#228B22")
    t.end_fill()
    set_start(-44.24, -37.54, 2.5)
    t.setheading(351.5)
    t.begin_fill()
    t.right(177)
    right_rotate(2, 3, 14)
    right_rotate(1, 3, 7)
    t.left(65)
    left_rotate(4, 7, 10)
    left_rotate(3, 6, 10)
    left_rotate(1, 0, 2)
    t.left(128)
    right_rotate(6, 7, 6.1)
    right_rotate(2, 7, 6.1)
    t.left(125)
    right_rotate(5, 4, 11)
    t.fillcolor("#FF0000")
    t.end_fill()
    set_start(-44.24, -37.54, 2.5)
    t.setheading(351.5)
    t.begin_fill()
    t.right(177)
    right_rotate(1, 3, 14)
    right_rotate(1, 3, 8)
    t.left(92)
    left_rotate(4, 8, 7)
    t.right(10)
    right_rotate(4, 3, 6)
    t.goto(-59.29, -87.30)
    t.setheading(2.5)
    right_rotate(2, 7, 6.1)
    t.left(125)
    right_rotate(5, 4, 11)
    t.fillcolor("#228B22")
    t.end_fill()


def draw_tail():
    set_start(53, -74, 2.4, c="#87481f")
    t.begin_fill()
    t.setheading(26)
    right_rotate(5, 16, 1.3)
    right_rotate(1, 8, 8)
    right_rotate(1, 8, 4)
    t.left(60)
    right_rotate(1, 3, 3)
    t.pencolor(COLOR)
    t.forward(5)
    right_rotate(4, 3, 8)
    left_rotate(3, 3, 7)
    left_rotate(2, 5, 3)
    left_rotate(5, 6, 6)
    left_rotate(3, 8, 7)
    left_rotate(5, 12, 6)
    left_rotate(5, 10, 6)
    left_rotate(5, 15, 2)
    left_rotate(2, 20, 2)
    left_rotate(3, 10, 3)
    right_rotate(2, 13, 5)
    right_rotate(2, 20, 6)
    right_rotate(2, 12, 6)
    right_rotate(5, 7.5, 5)
    right_rotate(6, 3, 4)
    left_rotate(4, 2, 8.5)
    t.fillcolor("#fdb933")
    t.end_fill()
    set_start(53, -74, 2.4, c="#87481f")
    t.begin_fill()
    t.setheading(26)
    right_rotate(5, 16, 1.3)
    right_rotate(1, 8, 8)
    right_rotate(1, 8, 3)
    t.left(60)
    right_rotate(1, 3, 2)
    t.pencolor("#130c0e")
    left_rotate(3, 25, 2)
    left_rotate(3, 5, 1.8)
    left_rotate(1, 78, 8.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(83, -81, 1, c="#130c0e")
    t.begin_fill()
    t.left(140)
    right_rotate(5, 8, 2)
    left_rotate(1, 105, 5)
    right_rotate(2, 3, 5.5)
    t.left(50)
    left_rotate(3, 15, 4.1)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(109, -89, 1, c="#130c0e")
    t.begin_fill()
    t.left(150)
    right_rotate(3, 5, 2)
    right_rotate(4, 15, 2)
    left_rotate(1, 125, 6)
    left_rotate(2, 3, 7)
    t.left(85)
    left_rotate(3, 15, 6.05)
    t.left(68)
    right_rotate(3, 5, 5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(132, -88, 1, c="#130c0e")
    t.begin_fill()
    t.left(180)
    right_rotate(5, 10, 4.1)
    left_rotate(1, 100, 6)
    left_rotate(2, 5, 7)
    t.left(75)
    left_rotate(5, 10, 5)
    t.left(75)
    right_rotate(3, 8, 4.5)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(150, -71, 1, c="#130c0e")
    t.begin_fill()
    t.right(140)
    right_rotate(5, 15, 5.8)
    left_rotate(1, 130, 6)
    left_rotate(2, 10, 5)
    t.left(30)
    left_rotate(5, 15, 5.6)
    t.left(81)
    right_rotate(3, 8, 3)
    t.fillcolor("#130c0e")
    t.end_fill()
    set_start(147, -51, 1, c="#130c0e")
    t.begin_fill()
    t.right(125)
    right_rotate(5, 10, 4)
    t.left(145)
    left_rotate(2, 10, 6.5)
    left_rotate(6, 14, 2)
    left_rotate(4, 22, 2)
    t.fillcolor("#130c0e")
    t.end_fill()


def draw_drum():
    set_start(-136, -12, 2, c="#87481f")
    t.begin_fill()
    right_rotate(1, 78, 17)
    right_rotate(5, 30, 1.2)
    right_rotate(1, 30, 17)
    t.fillcolor("#FF0000")
    t.end_fill()
    set_start(-140, -2, 2, c="#87481f")
    t.begin_fill()
    left_rotate(1, 108, 10)
    right_rotate(1, 90, 4)
    left_rotate(5, 16, 7)
    left_rotate(5, 19, 6.5)
    t.forward(4)
    left_rotate(5, 18, 7.5)
    left_rotate(5, 18, 6.1)
    left_rotate(1, 180, 3)
    left_rotate(1, 95, 10)
    t.fillcolor("#FF0000")
    t.end_fill()
    set_start(-156.34, 48.19, 1, c="#87481f")
    t.setheading(199)
    t.left(12)
    left_rotate(10, 14.5, 5.8)
    set_start(-140, 12, 1, c="#87481f")
    t.setheading(20)
    t.begin_fill()
    left_rotate(5, 14, 5.2)
    left_rotate(3, 15, 4.5)
    left_rotate(5, 18, 5)
    left_rotate(5, 16, 5.5)
    left_rotate(3, 18, 5)
    t.fillcolor("#fffffb")
    t.end_fill()
    set_start(-143, 14, 2.5, c="#FF0000")
    left_rotate(1, 117, 17)
    left_rotate(1, 90, 9)
    t.left(90)
    left_rotate(3, 5, 3.5)
    set_start(-146.8, 14, 2.5, c="#FF0000")
    left_rotate(1, 120, 14)
    set_start(-150, 34, 2.5, c="#FF0000")
    left_rotate(1, 120, 8.5)
    t.left(100)
    left_rotate(3, 17, 4)
    set_start(-140, 16, 2.5, c="#FF0000")
    left_rotate(1, 115, 14)
    right_rotate(1, 90, 13)
    t.right(90)
    right_rotate(4, 16, 4.5)
    set_start(-136, 18, 2.4, c="#FF0000")
    left_rotate(1, 112, 12)
    set_start(-142, 24, 2.5, c="#FF0000")
    left_rotate(1, 35, 10)
    set_start(-145, 32, 2.5, c="#FF0000")
    left_rotate(1, 115, 6)
    right_rotate(1, 85, 10)
    t.right(40)
    right_rotate(3, 18, 2)
    right_rotate(1, 95, 10)
    set_start(-149, 44, 2.5, c="#FF0000")
    t.left(60)
    right_rotate(3, 22, 3)
    set_start(-166, 20, 2.4)
    t.right(100)
    right_rotate(4, 32, 3)
    right_rotate(2, 12, 3.5)
    left_rotate(2, 10, 4)
    left_rotate(4, 25, 2.5)
    set_start(-196, 35, 2.4)
    draw_circle(3.5, COLOR, "#FF0000")
    set_start(-127, 38, 2.4)
    t.left(60)
    right_rotate(4, 32, 3)
    right_rotate(2, 12, 3.5)
    left_rotate(6, 28, 2)
    left_rotate(3, 15, 2)
    set_start(-115, 33, 2.4)
    draw_circle(3.5, COLOR, "#FF0000")


if __name__ == "__main__":
    t.title("小老虎")
    t.setup(420, 400, 150, 150)
    t.screensize(400, 380, "#FFE4E1")
    time.sleep(3)
    draw_head()
    draw_face()
    draw_eye()
    draw_nose()
    draw_mouth()
    draw_ear()
    draw_cap()
    draw_brow()
    draw_shadow()
    draw_body()
    draw_moustache()
    draw_left_hand()
    draw_right_hand()
    draw_clothes()
    draw_tail()
    draw_drum()
    set_start(1000, 1000, 2.5)
    t.done()
