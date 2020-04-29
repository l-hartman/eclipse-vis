class Calendar(object):
    def __init__(self, filename):
        self.img = loadImage(filename)
        self.render()
        
    def render(self):
        image(self.img, 300, 800)
        text("Calendar", 675, 795)
        
    def update(self, date, type):
        m = int(date.split("/")[1])
        #print(type(m))
        x_offset = 62.5
        x_start = 300 + x_offset / 2 - 10
        x_pos = x_start + x_offset * (m-1)
        
        if type == "l":
            fill(0)
        elif type == "s":
            fill(255)
        rect(x_pos, 810, 20, 90, 7);
