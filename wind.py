def wind_direction(degrees):
    """Return wind direction based on https://www.windfinder.com/wind/windspeed.htm"""
    # degrees = round(degrees / 22.5) * 22.5
    degrees = round(degrees / 45) * 45
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
    """Return wind speed description based on https://www.windfinder.com/wind/windspeed.htm"""
    return {
        speed <= 0.3: 'Calm',
        0.3 < speed <= 1.6: 'Light Air',
        1.6 < speed <= 3.4: 'Light Breeze',
        3.4 < speed <= 5.5: 'Gentle Breeze',
        5.5 < speed <= 8.0: 'Moderate Breeze',
        8.0 < speed <= 10.8: 'Fresh Breeze',
        10.8 < speed <= 13.9: 'Strong Breeze',
        13.9 < speed <= 17.2: 'Near Gale',
        17.2 < speed <= 20.8: 'Gale',
        20.8 < speed <= 24.5: 'Severe Gale',
        24.5 < speed <= 28.5: 'Strong storm',
        28.5 < speed <= 32.7: 'Violent Storm',
        32.7 < speed: 'Hurricane'
    }[True]
