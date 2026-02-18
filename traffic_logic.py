def calculate_green_time(north, south, east, west):

    total = north + south + east + west

    min_time = 20
    max_time = 90

    if total == 0:
        return (30,30,30,30)

    north_time = min_time + (north/total)*(max_time-min_time)
    south_time = min_time + (south/total)*(max_time-min_time)
    east_time  = min_time + (east/total)*(max_time-min_time)
    west_time  = min_time + (west/total)*(max_time-min_time)

    return (
        round(north_time),
        round(south_time),
        round(east_time),
        round(west_time)
    )
