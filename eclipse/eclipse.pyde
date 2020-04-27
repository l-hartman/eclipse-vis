import description_pane as dp
import search_bar as sb
import lunar_pane as lp
import solar_pane as sp
import calendar

my_map = None
lunar_arr = []
solar_arr = []
lunar_data = None
solar_data = None
searcher = None
lpaner = None
draw_l_years = False
draw_s_years = False
dpane = None
spaner = False

zoom_in_lunar = [0]
zoom_in_solar = [0]


def setup():
    global my_map
    global lunar_data
    global solar_data
    global searcher
    global lpaner
    global dpane
    global spaner
    global cal
    
    lunar_data = load_lunar_data("../data/lunar.csv")
    solar_data = load_solar_data("../data/solar.csv")
    
    size(1200,1000)
    
    my_map = loadImage("../images/Map.jpg")

    searcher = sb.SearchBar()
    lpaner = lp.LunarPane(300,450,300,300)
    dpane = dp.DescriptionPane(20, 70, 250, 330)
    spaner = sp.SolarPane(750,450,300,300)
    cal = calendar.Calendar("../images/calendar.png")
    
def draw():
    #Search bar
    global my_map
    global solar_arr
    global lunar_arr
    global searcher
    global lpaner
    global draw_l_years
    global draw_s_years
    global zoom_in_lunar
    global zoom_in_solar
    global dpane
    global spaner
        
    background(150)
    #Mapping
    image(my_map,300,20)
    map_legend()
    lunar_area_text()
    solar_area_text()

    map_lunar_points(lunar_arr)
    map_solar_points(solar_arr)
    #solar_area_rect()
    cal.render()
    dpane.render()
    searcher.render()
    lpaner.render(lunar_arr)
    spaner.render(solar_arr)
    
    if draw_l_years:
        lpaner.year_eclipses()
    lpaner.hover_check(mouseX,mouseY)
    
    if zoom_in_lunar[0] == 1:
        zoom_in_lunar = lpaner.load_chosen_data(zoom_in_lunar[1], zoom_in_lunar[2], zoom_in_lunar[3], zoom_in_lunar[4], zoom_in_lunar[5], zoom_in_lunar[6], zoom_in_lunar[7])
    elif zoom_in_lunar[0] == 2:
        zoom_in_lunar = lpaner.keep_chosen_data(zoom_in_lunar[1], zoom_in_lunar[2], zoom_in_lunar[3], zoom_in_lunar[4], zoom_in_lunar[5], zoom_in_lunar[6], zoom_in_lunar[7])
        
    if draw_s_years:
        spaner.year_eclipses()
    spaner.hover_check(mouseX, mouseY)
    
    if zoom_in_solar[0] == 1:
        zoom_in_solar = spaner.load_chosen_data(zoom_in_solar[1], zoom_in_solar[2], zoom_in_solar[3], zoom_in_solar[4], zoom_in_solar[5], zoom_in_solar[6], zoom_in_solar[7])
    elif zoom_in_solar[0] == 2:
        zoom_in_solar = spaner.keep_chosen_data(zoom_in_solar[1], zoom_in_solar[2], zoom_in_solar[3], zoom_in_solar[4], zoom_in_solar[5], zoom_in_solar[6], zoom_in_solar[7])
        
        
def map_legend():
    #1050
    fill(0)
    circle(1060, 194, 14)
    text("Lunar Eclipses", 1070, 200)
    fill(255)
    circle(1060, 245, 14)
    text("Solar Eclipses", 1070, 250)
    
def lunar_year(chosen_year):
    global lunar_data
    global lunar_arr
    lunar_arr = []
    for row in lunar_data:
        cal_year = row[1].split('/')
        
        if cal_year[0] == chosen_year:
            lunar_arr.append(row)

def solar_year(chosen_year):
    global solar_data
    global solar_arr
    solar_arr = []
    for row in solar_data:
        cal_year = row[1].split('/')

        if cal_year[0] == chosen_year:
            solar_arr.append(row)        

def lunar_area_text():
    fill(0)
    textSize(30)
    textAlign(CENTER)
    text('Lunar',450,445)
    
#def solar_area_rect():
#    fill(255)
#    rect(750,450,300,300)

def solar_area_text():
    fill(0)
    textSize(30)
    textAlign(CENTER)
    text('Solar',900,445)
    
def map_lunar_points(lunar_arr):
    #width 750
    #height 377
    for row in lunar_arr:
        latitude = row[11]
        longitude = row[12]
        x_cord = map(float(longitude), -180, 180, 300, 1050)
        y_cord = map(float(latitude), -90, 90, 20, 397)
        fill(0)
        circle(x_cord, y_cord, 15)
        if over_eclipse(x_cord, y_cord, 15) and row[0] != dpane.cur_id:
            dpane.update(row, "lunar")
    
def map_solar_points(solar_arr):
    #width 750
    #height 377
    for row in solar_arr:
        latitude = row[9]
        longitude = row[10]
        x_cord = map(float(longitude), -180, 180, 300, 1050)
        y_cord = map(float(latitude), -90, 90, 20, 397)
        fill(255)
        circle(x_cord, y_cord,15)
        if over_eclipse(x_cord, y_cord, 15) and row[0] != dpane.cur_id:
            dpane.update(row, "solar")

def mouseClicked():
    global zoom_in_lunar
    global zoom_in_solar
    searcher.handle_toggle_onclick(mouseX, mouseY)
    zoom_in_lunar = lpaner.handle_eclipse_onlick(mouseX, mouseY)
    zoom_in_solar = spaner.handle_eclipse_onclick(mouseX,mouseY)

def keyPressed():
    global draw_l_years
    global draw_s_years
    if searcher.toggled:
        if key == "\n":
            lunar_year(searcher.cur_val)
            solar_year(searcher.cur_val)
            draw_l_years = True
            draw_s_years = True
            redraw()
        elif key == '\b':
            searcher.cur_val = searcher.cur_val[:-1]
        else:
            if ((key >= '0' and key <= '9') or key == '-') and len(searcher.cur_val) < searcher.max_chars:
                searcher.cur_val = searcher.cur_val + key



def over_eclipse(x, y, diameter):
  dis_x = x - mouseX
  dis_y = y - mouseY
  if sqrt(dis_x*dis_x + dis_y*dis_y) < diameter/2:
    return True
  else:
    return False

######################
#Cleaning and Loading
######################
def load_solar_data(filename):
    table = []
    x = 0
    with open(filename, mode='r') as myfile:
        for row in myfile:
            row = row.strip('\n')
            row = row.split(',')
            if x == 0:
                pass
            else:
                cal_date = row[1].split()
                row[1] = cal_date[0] + '/' + str(month_to_num(cal_date[1])) + '/' + str(cal_date[2])
                row[9] = lat_direction_to_degree(row[9])
                row[10] = long_direction_to_degree(row[10])
                row[14] = central_duration_clean(row[14])
                table.append(row)
                
            x += 1
    return table

def load_lunar_data(filename):
    table = []
    x = 0
    with open(filename, mode='r') as myfile:
        
        for row in myfile:
            row = row.strip('\n')
            row = row.split(',')
            if x == 0:
                pass
            else:
                cal_date = row[1].split()
                row[1] = cal_date[0] + '/' + str(month_to_num(cal_date[1])) + '/' + str(cal_date[2])
                row[11] = lat_direction_to_degree(row[11])
                row[12] = long_direction_to_degree(row[12])
                table.append(row)
                
            x += 1
    return table

def month_to_num(m):
    return{
            'January' : 1,
            'February' : 2,
            'March' : 3,
            'April' : 4,
            'May' : 5,
            'June' : 6,
            'July' : 7,
            'August' : 8,
            'September' : 9, 
            'October' : 10,
            'November' : 11,
            'December' : 12
    }[m]
    
def central_duration_clean(t):
    if t != '-':
        return t[:2] + '-' + t[3:5]
    return t
    
def lat_direction_to_degree(lat):
    degree = lat[:-1]
    if lat[-1] == 'N':
        return degree
    else:
        return '-' + degree
    
def long_direction_to_degree(l):
    degree = l[:-1]
    if l[-1] == 'E':
        return degree
    else:
        return '-' + degree
