import cv2
import face_recognition
import rotate_utils


def rotate_and_detect_faces(image):
    height, width, channels = image.shape
    locations = []

    image_rotated_90degrees = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    face_loc_90 = face_recognition.face_locations(image_rotated_90degrees)

    for location in face_loc_90:
        new_location = rotate_utils.map_rotated_location_90deg(location, width, height)
        locations.append(new_location)

    image_rotated_180degrees = cv2.rotate(image_rotated_90degrees, cv2.cv2.ROTATE_90_CLOCKWISE)
    face_loc_180 = face_recognition.face_locations(image_rotated_180degrees)

    for location in face_loc_180:
        new_location = rotate_utils.map_rotated_location_180deg(location, width, height)
        locations.append(new_location)

    image_rotated_270degrees = cv2.rotate(image_rotated_180degrees, cv2.cv2.ROTATE_90_CLOCKWISE)
    face_loc_270 = face_recognition.face_locations(image_rotated_270degrees)

    for location in face_loc_270:
        new_location = rotate_utils.map_rotated_location_270deg(location, width, height)
        locations.append(new_location)

    return locations


def detect_faces(image):
    face_loc = face_recognition.face_locations(image)
    if len(face_loc) == 0:
        face_loc = rotate_and_detect_faces(image)

    return face_loc
