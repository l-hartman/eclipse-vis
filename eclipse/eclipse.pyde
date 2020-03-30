def setup():
    lunar_data = load_lunar_data("../data/lunar.csv")
    solar_data = load_solar_data("../data/solar.csv")

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
                table.append(row)
            else:
                cal_date = row[1].split()
                row[1] = cal_date[0] + '-' + str(month_to_num(cal_date[1])) + '-' + str(cal_date[2])
                row[9] = lat_direction_to_degree(row[9])
                row[10] = long_direction_to_degree(row[10])
                row[14] = central_duration_clean(row[14])
                print(row)
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
                table.append(row)
            else:
                cal_date = row[1].split()
                row[1] = cal_date[0] + '-' + str(month_to_num(cal_date[1])) + '-' + str(cal_date[2])
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
    
