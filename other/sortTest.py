import os

def where():
	dir_to_sort = raw_input('Place path to files here:')
	sub = raw_input('Include all subdirectories Y/N?:')

	if sub.lower() = 'y':
		file_names = []
		for path, subdirs, files in os.walk(dir_to_sort):
		    for name in files:
		        file_names.append(os.path.join(path, name))

	elif sub.lower() = 'n':
		file_names = []
		for path, files in os.walk(dir_to_sort):
		    for name in files:
		        file_names.append(os.path.join(path, name))
	else:
		print "Not a valid input!"
		where()

def sort():

	where()


	if any(".tif" in s for s in file_names):
		new_tif_dir = dir_to_sort + '/TIFs'
		os.mkdir(new_tif_dir, 0755)
	if any(".jpg" in s for s in file_names):
		new_jpg_dir = dir_to_sort + '/JPGs'
		os.mkdir(new_jpg_dir, 0755)
	if any(".psd" in s for s in file_names):
		new_psd_dir = dir_to_sort + '/PSDs'
		os.mkdir(new_psd_dir, 0755)

	new_other_dir = dir_to_sort + '/OTHER'	
	os.mkdir(new_other_dir, 0755)

	for item in file_names:
	    if ".tif" in item:
	        os.rename(item + '/' + item, new_tif_dir + '/' + item) #Remove old path from file name!
	    elif ".jpg" in item:
	        os.rename(item + '/' + item, new_jpg_dir + '/' + item)
	    elif ".psd" in item:
	        os.rename(item + '/' + item, new_psd_dir + '/' + item)
	    else:
	        os.rename(item + '/' + item, new_other_dir + '/' + item)

	print "Files sorted!"


sort()