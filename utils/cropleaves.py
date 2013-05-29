from SimpleCV import *
import os

basedir = "Leaves"
cropbasedir = "Cropleaves"

if cropbasedir not in os.listdir('.'):
    os.mkdir(cropbasedir)

leaves = os.listdir(basedir)
for leaf in leaves:
    if leaf not in os.listdir(cropbasedir):
        os.mkdir(os.path.join(cropbasedir,leaf))
    imgs = ImageSet(os.path.join(basedir, leaf))
    for i in xrange(len(imgs)):
        img = imgs[i].resize(400, 300).invert().findBlobs()[-1].crop().invert()
        img.save(os.path.join(cropbasedir, leaf, str(i)+".jpg"))
        print os.path.join(cropbasedir, leaf, str(i)+".jpg"), "saved"
