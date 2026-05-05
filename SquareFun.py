from pgl import GWindow, GRect, GOval

WIDTH = 800  # width of window
HEIGHT = 400  # height of window
BOX_SIZE = 50  # width and height of box
DART_SIZE = BOX_SIZE / 2  # diameter of dart
DART_X = 267-240  # dart thrown horizontal position
DART_Y = HEIGHT / 2  # dart thrown vertical position
STEP_INTERVAL = 10  # ms

gw = GWindow(WIDTH, HEIGHT)
rect = GRect(0, HEIGHT / 2 - BOX_SIZE / 2, BOX_SIZE, BOX_SIZE)
rect.set_filled(True)
rect.set_color("red")
gw.add(rect)
oval = GOval(DART_X, DART_Y - DART_SIZE / 2, DART_SIZE, DART_SIZE)
oval.set_filled(True)

def throw_dart():
    """
    'Throws' a dart to a position on the window, drawing a circle at that position
    """
    gw.oval = GOval(DART_X, DART_Y - DART_SIZE / 2, DART_SIZE, DART_SIZE)
    gw.oval.set_filled(True)
    gw.add(oval)
    print(rect.get_x())
    

def square_move():
    rect.move(9,0)
def check():
    print(rect.get_x())
def size():
    size=rect.get_width()+1
    rect.set_size(size,size)
def dart_move():
    oval.move(9,0)




gw.set_interval(square_move, 48)
gw.set_interval(size, 50)
gw.set_timeout(check, 5000) 
gw.set_timeout(throw_dart, 1490)
gw.set_interval(dart_move, 48)









