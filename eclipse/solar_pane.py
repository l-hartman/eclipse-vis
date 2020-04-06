class SolarPane(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.sa = None
        self.eclipse_text = []
        
        self.moon = loadImage("../images/Moon.png")
        self.moon_x_y = [800,460]
        
        self.earth = loadImage("../images/Earth.png")
        
        self.sun = loadImage("../images/Sun.png")
        self.sun_x_y = [750,600]
        
        self.display_wait = 20;
        self.total_wait = 100;
        self.hybrid_counter = 0
        
        self.annular = loadImage("../images/annular-eclipse.png")
        self.hybrid = loadImage("../images/hybrid_solar.png")
        self.partial = loadImage("../images/partial_solar.png")
        self.total = loadImage("../images/total_eclipse_solar.png")
        
        
    
    def render(self, solArr):
        #rect
        fill(255)
        rect(self.x,self.y,self.w,self.h)
        
        self.sa = solArr
        
    def year_eclipses(self):
        x = 0
        fill(255)
        textSize(15)
        self.eclipse_text = []
        for eclipse in self.sa:
            if x < 3:
                self.eclipse_text.append([self.x + (x*100), self.y + self.h + 15])
                text("Eclipse " + str(x+1), self.x + (x*100), self.y + self.h + 15)
            else:
                #special case of 4 lunar eclipses
                self.eclipse_text.append([self.x, self.y + self.h + 35])
                text("Eclipse " + str(x+1), self.x , self.y + self.h + 35)
            x += 1
        
    def hover_check(self,mX,mY):
        fill(0,0,255)
        x = 0
        for ecl in self.eclipse_text:
            if mX > ecl[0] and mX < ecl[0] + 70 and mY > ecl[1] - 10 and mY < ecl[1] + 10: 
                if x < 3: 
                    text("Eclipse " + str(x+1), self.x + (x*100), self.y + self.h + 15)
                else:
                    text("Eclipse " + str(x+1), self.x , self.y + self.h + 35)
            x += 1
            
    def handle_eclipse_onclick(self,mX,mY):
        clicked = None
        for x in range(len(self.eclipse_text)):
            if mX > self.eclipse_text[x][0] and mX < self.eclipse_text[x][0] + 70 and mY > self.eclipse_text[x][1] - 15 and mY < self.eclipse_text[x][1] + 15:
                 #self.lunar_data[x] is chosen data    
                 sizeX_sun, sizeY_sun = 150, 150
                 sizeX_earth, sizeY_earth = 50, 50
                 sizeX_moon, sizeY_moon = 25,25
                 self.sun_x_y = [750,600]
                 self.moon_x_y = [800, 460]
                                  
                 return [1, self.sa[x], sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
                 
        return [0]
        
        
    def load_chosen_data(self,data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon):

        time = millis()
        while self.total_wait > 0:
           
           if millis() - time >= self.display_wait:

             self.total_wait -= 1
             time = millis()
            
             sizeX_sun -= .5
             sizeY_sun -= .5
             self.sun_x_y[1] += .5
             image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
             
        
             self.moon_x_y[0] += 1.1
             self.moon_x_y[1] += 1.05
             image(self.moon,self.moon_x_y[0],self.moon_x_y[1],sizeX_moon,sizeY_moon)
             
             return [1, data, sizeX_sun, sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
                
        self.total_wait = 100
        return [2, data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
    
    def keep_chosen_data(self,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon):
        #draw Penumbra lines
        
        stroke(0)
        
        line(self.sun_x_y[0], self.sun_x_y[1]+34, 1050, 474)
        line(self.sun_x_y[0] + sizeX_sun-35, 750, 1027, 450)
        
        
        #draw umbra lines
        line(self.sun_x_y[0], self.sun_x_y[1]+30, 1050, 525) 
        line(self.sun_x_y[0] + sizeX_sun-30, 750, 973, 450)

        if len(data[6]) == 1:
            e_type = data[6]
        else:
            e_type = data[6][0]
            
        stroke(0)
        fill(255)
        rect(20,475,250,250)
        
        
        if e_type == 'T':
            type = "total"
            fill(0)
            triangle(912,570,972,530,927,590)
            image(self.earth, 940 , 510, sizeX_earth, sizeY_earth)
            image(self.total, 180, 640, 75, 75)
        elif e_type == 'P':
            type = "partial"
            fill(155)
            #triangle(912, 570, 972, 526, 946, 526)
            #triangle(927,590, 976,526, 981,548)
            image(self.earth, 980 , 510, sizeX_earth, sizeY_earth)
            image(self.partial, 180, 640, 75, 75)
        elif e_type == 'H':
            if self.hybrid_counter < 30:
                fill(0)
                triangle(912,570,972,530,927,590)
                image(self.earth, 940 , 510, sizeX_earth, sizeY_earth)
                self.hybrid_counter += 1
            elif self.hybrid_counter < 60:
                fill(155)
                triangle(1025,450,1050,sizeY_earth+422,972,530)
                image(self.earth, 1003 , 451, sizeX_earth, sizeY_earth)
                self.hybrid_counter += 1
            else:
                self.hybrid_counter = 0
            type = "hybrid"
            image(self.hybrid, 180, 640, 75, 75)
        else:
            type = "annular"
            fill(155)
            triangle(1025,450,1050,sizeY_earth+422,972,530)
            image(self.earth, 1003 , 451, sizeX_earth, sizeY_earth)
            image(self.annular, 180, 640, 75, 75)
        
        image(self.sun,self.sun_x_y[0],self.sun_x_y[1],sizeX_sun,sizeY_sun)
        image(self.moon,self.moon_x_y[0],self.moon_x_y[1],sizeX_moon,sizeY_moon)
        

        

        fill(0)
        text("On " + data[1] + " there will be a \n" + type + " eclipse at " + data[2] + "." + 
             " A\nsolar eclipse is when the moon\npasses in between the sun and\nthe earth and " + 
             "the moons shadow\nis cast on the earth. With\na(n) " + type + " eclipse you\ncan expect " +
             "it to look\nsimilar to this\nimage."
             ,22,495)

    
        return [2,data,sizeX_sun,sizeY_sun, sizeX_earth, sizeY_earth, sizeX_moon, sizeY_moon]
