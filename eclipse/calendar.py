class Calendar(object):
    def __init__(self, filename):
        self.img = loadImage(filename)
        self.render()
        
    def render(self):
        image(self.img, 300, 800)
        
    def draw_eclipse(self):
        pass
        
        
