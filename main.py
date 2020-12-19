import cv2
import os
import sys
import face_recognition
import face_detector
import help
import arguments

if len(sys.argv) < 2:
    print('Usage: main.py <file>')
    print('Use: -h or --help for more information')
    exit(1)

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    help.print_help()

filepath = sys.argv[1]
options = sys.argv[2:]
cliOnly = arguments.is_cli_only(options)
rotateAndDetect = arguments.rotate_image(options)

if not os.path.isfile(filepath):
    print("File " + filepath + " not accessible")
    exit(1)

img = face_recognition.load_image_file(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceLoc = face_detector.detect_faces(img, rotateAndDetect)

if cliOnly == 0:
    for loc in faceLoc:
        cv2.rectangle(img, (loc[1], loc[2]), (loc[3], loc[0]), (255, 0, 255), 1)

    cv2.imshow(filepath, img)
    cv2.waitKey(0)

print(faceLoc)
