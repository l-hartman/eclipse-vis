class Calendar(object):
    def __init__(self, filename):
        self.img = loadImage(filename)
        self.render()
        
    def render(self):
        image(self.img, 300, 800)
        text("Calendar", 675, 795)
        
    def draw_eclipse(self):
        pass
        
        
