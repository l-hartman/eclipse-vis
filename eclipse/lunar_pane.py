class LunarPane(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.lunar_data = []
        self.eclipse_text = []

    def render(self,la):
        #rect
        fill(255)
        rect(self.x,self.y,self.w,self.h)
        
        self.loadBaseImage()
        
        self.lunar_data = la
        
    def loadBaseImage(self):
        space = loadImage("../images/space.jpg")
        image(space,self.x+1,self.y+1,self.w-1,self.h-1)
        
        
    def year_eclipses(self):
        x = 0
        fill(255)
        textSize(15)
        self.eclipse_text = []
        for eclipse in self.lunar_data:
            text("Eclipse " + str(x), self.x + (x*100), self.y + self.h + 15)
            self.eclipse_text.append([self.x + (x*100), self.y + self.h + 15])
            x += 1
            
    def hover_check(self,mX,mY):
        fill(0,0,255)
        x = 0
        for ecl in self.eclipse_text:
            if mX > ecl[0] and mX < ecl[0] + 70 and mY > ecl[1] - 15 and mY < ecl[1] + 15:  
                text("Eclipse " + str(x), self.x + (x*100), self.y + self.h + 15)
           
            x += 1

    def handle_eclipse_onlick(self,mX,mY):
        clicked = None
        for x in range(len(self.eclipse_text)):
            if mX > self.eclipse_text[x][0] and mX < self.eclipse_text[x][0] + 70 and mY > self.eclipse_text[x][1] - 15 and mY < self.eclipse_text[x][1] + 15:
                 self.load_chosen_data(self.lunar_data[x])
                
    def load_chosen_data(self,data):
        #lat 11
        #long 12
        print(data)
        
        
        
