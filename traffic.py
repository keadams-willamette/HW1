from pgl import GWindow, GRect, GOval

WIDTH = 300
HEIGHT = WIDTH * 3
LIGHT_SIZE = WIDTH * 0.8
UNLIT_COLOR = "#333333"



from pgl import GWindow, GRect, GOval

GW_WIDTH = 600
GW_HEIGHT = GW_WIDTH
RADIUS_L = 0.4 * GW_WIDTH
RADIUS_M = 0.5 * RADIUS_L
RADIUS_S = 0.25 * RADIUS_M

def draw_yinyang():
    """
    Draws a yin-yang symbol centered on the window using purely
    circles and rectangles.
    """
    rect=GRect(0,0,50,50)
    gw.add(rect)





draw_yinyang()


circ = GOval(0,0,50,50)
circ.set_filled(True)
circ.set_color("black")
  


gw = GWindow(WIDTH, HEIGHT)
paint_it_black()

red_light = create_light(WIDTH / 2, 0.5 * WIDTH)
yellow_light = create_light(WIDTH / 2, 1.5 * WIDTH)
green_light = create_light(WIDTH / 2, 2.5 * WIDTH)

gw.add(red_light)
gw.add(yellow_light)
gw.add(green_light)


def red_light_off():
    red_light.set_fill_color("black")
    

def red_light_on():
    red_light.set_fill_color("red")
    x+=5
    gw.set_timeout(red_light_off, x)

gw.set_interval(red_light_on, 5000)
