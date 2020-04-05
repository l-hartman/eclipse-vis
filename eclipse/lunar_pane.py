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
        #self.moon_x_y = [560,700]
        
        self.earth = loadImage("../images/Earth.png")
        self.earth_x_y = [300, 460]
        
        self.sun = loadImage("../images/Sun.png")
        self.sun_x_y = [300,600]
        
        self.display_wait = 20;
        self.total_wait = 100;
        
        self.total_ecl = loadImage("../images/total_eclipse.png")
        self.partial_ecl = loadImage("../images/Partial_lunar.png")
        self.penumbral_ecl = loadImage("../images/Penumbral.png")
        

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
            if x < 3:
                self.eclipse_text.append([self.x + (x*100), self.y + self.h + 15])
                text("Eclipse " + str(x), self.x + (x*100), self.y + self.h + 15)
            else:
                #special case of 4 lunar eclipses
                self.eclipse_text.append([self.x, self.y + self.h + 35])
                text("Eclipse " + str(x), self.x , self.y + self.h + 35)
            x += 1
            
    def hover_check(self,mX,mY):
        fill(0,0,255)
        x = 0
        for ecl in self.eclipse_text:
            if mX > ecl[0] and mX < ecl[0] + 70 and mY > ecl[1] - 10 and mY < ecl[1] + 10: 
                if x < 3: 
                    text("Eclipse " + str(x), self.x + (x*100), self.y + self.h + 15)
                else:
                    text("Eclipse " + str(x), self.x , self.y + self.h + 35)
            x += 1

    def handle_eclipse_onlick(self,mX,mY):
        clicked = None
        for x in range(len(self.eclipse_text)):
            if mX > self.eclipse_text[x][0] and mX < self.eclipse_text[x][0] + 70 and mY > self.eclipse_text[x][1] - 15 and mY < self.eclipse_text[x][1] + 15:
                 #self.lunar_data[x] is chosen data    
                 sizeX_sun, sizeY_sun = 150, 150
                 sizeX_earth, sizeY_earth = 50, 50
                 sizeX_moon, sizeY_moon = 15,15
                 self.sun_x_y = [300,600]
                 self.earth_x_y = [300, 460]
                 
                 return [1, self.lunar_data[x], sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
                 
        return [0]
                
                
    def load_chosen_data(self,data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon):
        #lat 11
        #long 12
        #eclipse type #6
        
        time = millis()
        while self.total_wait > 0:
           
           if millis() - time >= self.display_wait:

             self.total_wait -= 1
             time = millis()
            
             sizeX_sun -= .5
             sizeY_sun -= .5
             self.sun_x_y[1] += .5
             image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
             
        
             self.earth_x_y[0] += 1.2
             self.earth_x_y[1] += 1.2
             image(self.earth,self.earth_x_y[0],self.earth_x_y[1],sizeX_earth,sizeY_earth)
             
             return [1, data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
                
        self.total_wait = 100
        return [2, data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
    
    def keep_chosen_data(self,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon):
        image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
        image(self.earth,self.earth_x_y[0],self.earth_x_y[1],sizeX_earth,sizeY_earth)
        
        #draw Penumbra lines
        stroke(255)
        
        line(self.sun_x_y[0], self.sun_x_y[1]+36, 600, 450) 
        line(self.sun_x_y[0] + sizeX_sun-35, 750, 584, 450)
        
        #draw umbra lines
        line(self.sun_x_y[0], self.sun_x_y[1]+22, 600, 577)
        line(self.sun_x_y[0] + sizeX_sun-23, 750, 465, 450)
        
        #See where to draw moon
        if len(data[6]) == 1:
            e_type = data[6]
        else:
            e_type = data[6][0]
        
        stroke(0)
        fill(255)
        rect(20,475,250,250)
        
        #Display moon position
        if e_type == 'T':
            image(self.moon, 473 , 560, sizeX_moon,sizeY_moon)
            type = "total"
            image(self.total_ecl, 180, 640, 75, 75)
        elif e_type == 'P':
            image(self.moon, 480 , 575, sizeX_moon,sizeY_moon)
            type = "partial"
            image(self.partial_ecl, 180, 640, 75, 75)
        else:
            image(self.moon, 485 , 590, sizeX_moon,sizeY_moon)
            type="penumbral"
            image(self.penumbral_ecl, 180, 640, 75, 75)
        

        fill(0)
        text("On " + data[1] + " there will be a \n" + type + " eclipse at " + data[2] + "." + 
             " A\nlunar eclipse is when the earth\npasses in between the sun and\nthe moon and " + 
             "the earths shadow\nis cast on the moon. With\na " + type + " eclipse you\ncan expect " +
             "it to look\nsimilar to the this\nimage."
             ,22,495)
        
        return [2,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
        
        
