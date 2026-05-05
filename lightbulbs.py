class SmartBulb:
    def __init__(self, room_name):
        self.room_name = room_name
        self._is_on = False
        self._brightness = 0  # Percent between 0 and 100
    def turn_on(self):
        self._is_on=True
        self._brightness=100
    def turn_off(self):
        self._is_on=False
        self._brightness=0
    def __repr__(self):
        if self._is_on:
            return(f"[{self.room_name}:ON @ {self._brightness}%]")
        else:
            return(f"[{self.room_name}:OFF]")
    def toggle(self):
        if not self._is_on:
            self.turn_on
        else:
            self.turn_off
    def get_brightness(self):
        return(self._brightness)

    def set_brightness(self,level):
        if level>100:
            level=100
        if level<=0:
            self._is_on=False
            self._brightness=0

        else:
            self._is_on=True
            self._brightness=level









if __name__ == "__main__":
    kitchen = SmartBulb("Kitchen")
    lroom = SmartBulb("Living Room")
    broom = SmartBulb("Bathroom")
    all = [kitchen, lroom, broom]

    """#Part A Testing
    print(kitchen._is_on)
    kitchen.turn_on()
    print(kitchen._is_on)
    kitchen.turn_on()
    print(kitchen._is_on)
    kitchen.turn_off()
    print(kitchen._is_on)
    kitchen.turn_off()
    print(kitchen._is_on)

    ## Part B Testing, uncomment when ready
    broom.turn_on()
    print(all)"""

    ## Part C Testing, uncomment when ready
    print(kitchen)
    kitchen.toggle()
    print(kitchen)
    kitchen.toggle()
    print(kitchen)
    kitchen.set_brightness(50)
    kitchen.toggle()
    print(kitchen)

    ## Part D Testing, uncomment when ready
    print(lroom)
    lroom.set_brightness(50)
    print("50",lroom)
    lroom.set_brightness(-50)
    print("0",lroom)
    lroom.set_brightness(500)
    print("100",lroom)
