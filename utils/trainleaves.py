from SimpleCV import *
import os

basedir = "Leaves"
cropbasedir = "Cropleaves"

leaves = os.listdir(cropbasedir)
imgs = []
labels = []
for leaf in leaves:
    img = ImageSet(os.path.join(cropbasedir, leaf))
    imgs += img
    labels += [leaf]*len(img)

print len(imgs), len(labels)

f = FaceRecognizer()
f.train(imgs, labels)
f.save("fullLeavesdata.xml")