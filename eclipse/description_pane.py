class DescriptionPane(object):
    solar_attributes = [
        'Catalog Number', 
        'Calendar Date', 
        'Eclipse Time', 
        'Delta T (s)', 
        'Lunation Number', 
        'Saros Number', 
        'Eclipse Type', 
        'Gamma', 
        'Eclipse Magnitude', 
        'Latitude', 
        'Longitude', 
        'Sun Altitude', 
        'Sun Azimuth', 
        'Path Width (km)', 
        'Central Duration'
    ]
    
    lunar_attributes = [
        'Catalog Number', 
        'Calendar Date', 
        'Eclipse Time', 
        'Delta T (s)', 
        'Lunation Number', 
        'Saros Number', 
        'Eclipse Type', 
        'Quincena Solar Eclipse', 
        'Gamma', 
        'Penumbral Magnitude', 
        'Umbral Magnitude', 
        'Latitude', 
        'Longitude', 
        'Penumbral Eclipse Duration (m)', 
        'Partial Eclipse Duration (m)', 
        'Total Eclipse Duration (m)'
    ]
    
    def __init__(self,x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        # current data becomes a row from lunar/solar.csv
        self.current_data = None
        # is current description for a lunar or solar eclipse?
        self.eclipse_type = ""
        self.cur_id = ""

    def render(self):
        fill(255)
        rect(self.x, self.y, self.w, self.h)
        self.write_description()

    def update(self, eclipse_data, eclipse_type):
        self.current_data = eclipse_data
        self.eclipse_type = eclipse_type
        self.cur_id = eclipse_data[0]
        
    def write_description(self):
        if self.eclipse_type == "lunar":
            textAlign(LEFT)
            textSize(15)
            fill(0,0,0)
            y_cord = self.y + 35
            text("Lunar Eclipse", 22, y_cord - 20)
            for i in range(len(DescriptionPane.solar_attributes)):
                text(DescriptionPane.solar_attributes[i] + " " + self.current_data[i], 22, y_cord)
                y_cord += 20
        elif self.eclipse_type == "solar":
            textAlign(LEFT)
            textSize(15)
            fill(0,0,0)
            y_cord = self.y + 35
            text("Solar Eclipse", 22, y_cord - 20)
            for i in range(len(DescriptionPane.solar_attributes)):
                text(DescriptionPane.solar_attributes[i] + ": " + self.current_data[i], 22, y_cord)
                y_cord += 20
