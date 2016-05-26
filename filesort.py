import os

def sort():
	path = raw_input('Place path to files here:')
	directory = os.listdir(path)

	if any(".tif" in s for s in directory):
		new_tif_dir = path + '/TIFs'
		os.mkdir(new_tif_dir, 0755)
	if any(".jpg" in s for s in directory):
		new_jpg_dir = path + '/JPGs'
		os.mkdir(new_jpg_dir, 0755)
	if any(".psd" in s for s in directory):
		new_psd_dir = path + '/PSDs'
		os.mkdir(new_psd_dir, 0755)

	new_other_dir = path + '/OTHER'	
	os.mkdir(new_other_dir, 0755)


	for item in directory:
	    if ".tif" in item:
	        os.rename(path + '/' + item, new_tif_dir + '/' + item)
	    elif ".jpg" in item:
	        os.rename(path + '/' + item, new_jpg_dir + '/' + item)
	    elif ".psd" in item:
	        os.rename(path + '/' + item, new_psd_dir + '/' + item)
	    else:
	        os.rename(path + '/' + item, new_other_dir + '/' + item)

	print "Files sorted!"


sort()