def wind_direction(degrees):
    degrees = round(degrees / 22.5) * 22.5
    if degrees == 360:
        degrees = 0

    match degrees:
        case 0:
            direction = 'North'
        case 22.5:
            direction = 'North-Northeast'
        case 45:
            direction = 'Northeast'
        case 67.5:
            direction = 'East-Northeast'
        case 90:
            direction = 'East'
        case 112.5:
            direction = 'East-Southeast'
        case 135:
            direction = 'Southeast'
        case 157.5:
            direction = 'South-Southeast'
        case 180:
            direction = 'South'
        case 202.5:
            direction = 'South-Southwest'
        case 225:
            direction = 'Southwest'
        case 247.5:
            direction = 'West-Southwest'
        case 270:
            direction = 'West'
        case 292.5:
            direction = 'West-Northwest'
        case 315:
            direction = 'Northwest'
        case 337.5:
            direction = 'North-Northwest'

    return direction


def wind_speed(speed):
    # TODO
    return f"{speed}"
