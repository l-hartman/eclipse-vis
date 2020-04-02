import time

class SearchBar(object):
    toggled = False
    
    def __init__(self, 
                x=20, 
                y=30, 
                w=120,
                h=22,
                line_color="#11355F",
                bg_color="#C7DFFC",
                text_color="#000000",
                init_val="click",
                max_chars=5,
                title="Enter a year"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.line_color = line_color
        self.bg_color = bg_color
        self.text_color = text_color
        self.init_val = init_val
        self.max_chars = max_chars
        self.title = title
        
        self.toggled = False
        self.cursor_timer = Timer()
        self.cur_val = init_val
        self.rendered = False

        
    def render(self):
        if self.toggled:
            strokeWeight(1.5)
            stroke(self.line_color)
        else:
            strokeWeight(1.0)
            stroke(0)

        # draw box
        fill(self.bg_color)
        rect(self.x, self.y, self.w, self.h)
        
        # set text style and format
        textAlign(LEFT)
        textSize(15)
        fill(0,0,0)
        
        # write title, should only draw this once
        text(self.title, 20, 20)
    
        if self.toggled and self.cursor_timer.elapsed_time() > 1.0:
            text(self.cur_val + "|", 22, 48, 10)
            if self.cursor_timer.elapsed_time() > 1.6:
                self.cursor_timer.reset()
        else:
            text(self.cur_val, 22, 48, 10)
        
        self.rendered = True
        
    def handle_toggle_onclick(self, mx, my):
        def mouse_in_x(mx):
            return mx >= self.x and mx <= (self.x + self.w)
        def mouse_in_y(my):
            return my >= self.y and my <= (self.y + self.h)
            
        if mouse_in_x(mx) and mouse_in_y(my):
            self.toggled = True
            self.cur_val = ""
        else:
            self.toggled = False
            

class Timer(object):
    def __init__(self):
        self.start = time.time()
    
    def reset(self):
        self.start = time.time()
    
    def elapsed_time(self):
        return time.time() - self.start
        
        
