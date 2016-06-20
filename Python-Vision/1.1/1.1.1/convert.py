from PIL import Image
import os
#Try to convert an image to .jpg
#if can't do it,print an error msg.
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
	    Image.open(infile).save(outfile)
	except IOError:
	    print "cannot convert",infile

