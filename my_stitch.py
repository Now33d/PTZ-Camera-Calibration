import cv2
import os

image_path = 'results/new2'
files = os.listdir(image_path)

image_names = []
for img in files:
    path = image_path + '/' + img
    image_names.append(path)
    
print(len(image_names), image_names)

images = []
for name in image_names:
    img = cv2.imread(name)
    img = cv2.resize(img, (0,0), None, 0.2,0.2)
    images.append(img)
    
stitcher = cv2.Stitcher.create()
(status, result) = stitcher.stitch(images[0:6])

if (status == cv2.STITCHER_OK):
    print('Panorama generated')
    cv2.imwrite('test_file.jpg', result)
    cv2.imshow('pano', result)
    cv2.waitKey(1)
else:
    print('Panorama generation unsuccessful')