""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################

def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """
    for nested_list in data:
        for data_value in range(len(nested_list)):
            if is_number(nested_list[data_value]):
                nested_list[data_value] = float(nested_list[data_value])
                if nested_list[data_value] % 1 == 0:
                    (nested_list[data_value]) = int(nested_list[data_value])
                  
            
            if nested_list[data_value] == 'True':
                nested_list[data_value] = True
            if nested_list[data_value] == 'False':
                nested_list[data_value] = False
            if (nested_list[data_value] == 'null' or nested_list[data_value] == ''):
                nested_list[data_value] = None
    
def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS) 
    ['Danforth/Coxwell', 13, 2]
    """
    i = 0
    while station_id not in stations[i]:
        i = i + 1
    return [stations[i][1], stations[i][5], stations[i][6]]



def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """
    sum_column = 0
    for stations_list in stations:
        sum_column = sum_column + stations_list[index]
    
    return sum_column


def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """

    maximus = 0
    i2 = 0
    for stations_list1 in stations:
        if stations_list1[BIKES_AVAILABLE] > maximus:
            maximus = stations_list1[BIKES_AVAILABLE]
            i2 = stations_list1[ID]
    return i2
               

def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """
    stations_with_n = []
    for i7 in range(len(stations)):
        if stations[i7][DOCKS_AVAILABLE] >= n:
            stations_with_n.append(stations[i7][ID])
    return stations_with_n

def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """
    
    i3 = 0
    while start_id != stations[i3][0]:
        i3 = i3 + 1
    i4 = 0
    while end_id != stations[i4][0]:
        i4 += 1  
    # for idx, x in enumerate(stations):
    if stations[i3][LATITUDE] > stations[i4][LATITUDE]:
        lat = 'WEST'
    elif stations[i3][LATITUDE] < stations[i4][LATITUDE]:
        lat = 'EAST'
    elif stations[i3][LATITUDE] == stations[i4][LATITUDE]:
        lat = ''
    if stations[i3][LONGITUDE] > stations[i4][LONGITUDE]:
        long = 'SOUTH'
    elif stations[i3][LONGITUDE] < stations[i4][LONGITUDE]:
        long = 'NORTH'
    elif stations[i3][LONGITUDE] == stations[i4][LONGITUDE]:
        long = ''    
    return long + lat
    
        
def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    
    i5 = 0
    while station_id != stations[i5][0]:
        i5 = i5 + 1        
    if stations[i5][BIKES_AVAILABLE] > 0 and stations[i5][IS_RENTING]:
        stations[i5][BIKES_AVAILABLE] = stations[i5][BIKES_AVAILABLE] - 1
        stations[i5][DOCKS_AVAILABLE] = stations[i5][DOCKS_AVAILABLE] + 1
        return True
    else: 
        return False

        
        
        #if station_id in station:
            #return station[1]
        #else:
            #return false

def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    i6 = 0
    while station_id != stations[i6][0]:
        i6 = i6 + 1        
    if stations[i6][DOCKS_AVAILABLE] and stations[i6][IS_RETURNING]:
        stations[i6][BIKES_AVAILABLE] = stations[i6][BIKES_AVAILABLE] + 1
        stations[i6][DOCKS_AVAILABLE] = stations[i6][DOCKS_AVAILABLE] - 1
        return True
    else: 
        return False    
    

def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """
    total_available = 0
    total_capacity = 0
    sumbikes = 0
    for station in stations:
        total_available = total_available + station[BIKES_AVAILABLE]
        total_capacity = total_capacity + station[CAPACITY]
    total_percent = total_available / total_capacity
    for station in stations:
        bikes_rented = 0
        bikes_returned = 0        
        desired_avail = round(total_percent * station[CAPACITY])
        difference = station[BIKES_AVAILABLE] - desired_avail
        if difference == 0:
            bikes_rented = 0
        elif difference / abs(difference) == 1:
            bikes_rented = difference
            if station[IS_RENTING]:
                station[BIKES_AVAILABLE] = station[BIKES_AVAILABLE] - difference
                station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE] + difference
        elif difference / abs(difference) == -1:
            bikes_returned = difference
            if station[IS_RETURNING]:
                station[BIKES_AVAILABLE] = station[BIKES_AVAILABLE] - difference
                station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE] + difference
        sumbikes = sumbikes + (bikes_rented + bikes_returned)
            
    return sumbikes 



if __name__ == '__main__':
    #pass  

    # To test your code with larger lists, you can uncomment the code below to
    # read data from the provided CSV file.
    stations_file = open('stations.csv')
    bike_stations = csv_to_list(stations_file)
    clean_data(bike_stations)

    # For example,
    print('Testing get_station_with_max_bikes: ', \
        get_station_with_max_bikes(bike_stations) == 7033)
    
   # print('Testing balance_all_bikes: ', \
   #     balance_all_bikes(bike_stations))    
    
    print('get_stations_with_n_docks: ', \
        get_stations_with_n_docks(5, bike_stations))     
    
