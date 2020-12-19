def map_rotated_location_90deg(location, width, height):
    return [
        height - location[1],
        location[0],
        height - location[3],
        location[2]
    ]


def map_rotated_location_180deg(location, width, height):
    return [
        height - location[2],
        width - location[3],
        height - location[0],
        width - location[1]
    ]


def map_rotated_location_270deg(location, width, height):
    return [
        location[1],
        width - location[0],
        location[3],
        width - location[2]
    ]

