class LunarPane(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.lunar_data = []
        self.eclipse_text = []
        self.space = loadImage("../images/space.jpg")
        self.moon = loadImage("../images/Moon.png")
        
        self.earth = loadImage("../images/Earth.png")
        self.earth_x_y = [230,420]
        
        self.sun = loadImage("../images/Sun.png")
        self.sun_x_y = [300,600]
        
        self.display_wait = 20;
        self.total_wait = 100;
        

    def render(self,la):
        #rect
        fill(255)
        rect(self.x,self.y,self.w,self.h)
        
        self.loadBaseImage()
        
        self.lunar_data = la
        
    def loadBaseImage(self):
        image(self.space,self.x+1,self.y+1,self.w-1,self.h-1)
        
        
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
                 #self.lunar_data[x] is chosen data    
                 sizeX_sun, sizeY_sun = 150, 150
                 sizeX_earth, sizeY_earth = 300,200
                 self.sun_x_y = [300,600]
               
                 return [1, self.lunar_data[x], sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth]
                 
        return [0]
                
                
    def load_chosen_data(self,data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth):
        #lat 11
        #long 12
        #eclipse type #6
        
        if len(data[6]) == 1:
            e_type = data[6]
        else:
            e_type = data[6][0]
        
        time = millis()
        while self.total_wait > 0:
           
           if millis() - time >= self.display_wait:

             self.total_wait -= 1
             time = millis()
            
             sizeX_sun -= .5
             sizeY_sun -= .5
             self.sun_x_y[1] += .5
             image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
             
             #image(self.moon,80,600,sizeX,sizeY)
             
             image(self.earth,self.earth_x_y[0],self.earth_x_y[1],sizeX_earth,sizeY_earth)
             #sizeX_earth -=
             
             return [1, data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth]
                
        
        self.total_wait = 100
        return [2, data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth]
    
    def keep_chosen_data(self,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth):
        image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
        image(self.earth,self.earth_x_y[0],self.earth_x_y[1],sizeX_earth,sizeY_earth)
        return [2,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth]
       
        

        
            
        
        
        
        
        
        
