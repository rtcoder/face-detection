import cv2
import face_recognition
import face_detector
import os
import sys

if len(sys.argv) < 2:
    print('Usage: main.py <image-to-test> [<cli-only=1>]')
    exit(1)

if len(sys.argv) == 3:
    cliOnly = int(sys.argv[2])
else:
    cliOnly = 1

filepath = sys.argv[1]

if not os.path.isfile(filepath):
    print("File not accessible")
    exit(1)

img = face_recognition.load_image_file(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceLoc = face_detector.detect_faces(img)

if cliOnly == 0:
    for loc in faceLoc:
        cv2.rectangle(img, (loc[1], loc[2]), (loc[3], loc[0]), (255, 0, 255), 1)

    cv2.imshow(filepath, img)
    cv2.waitKey(0)
else:
    print(faceLoc)
