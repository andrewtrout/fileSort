import os


def withsubs():
	dir_to_sort = raw_input('Place path to files here:')

	directory = []
	for path, subdirs, files in os.walk(dir_to_sort):
		for name in files:
		    directory.append(os.path.join(path, name))

	if any(".tif" in s for s in directory):
		new_tif_dir = dir_to_sort + '/TIFs'
		os.mkdir(new_tif_dir, 0755)
	if any(".jpg" in s for s in directory):
		new_jpg_dir = dir_to_sort + '/JPGs'
		os.mkdir(new_jpg_dir, 0755)
	if any(".psd" in s for s in directory):
		new_psd_dir = dir_to_sort + '/PSDs'
		os.mkdir(new_psd_dir, 0755)

	new_other_dir = dir_to_sort + '/OTHER'	
	os.mkdir(new_other_dir, 0755)

	for item in directory:
		if ".tif" in item:
		    os.rename(item, new_tif_dir + '/' + os.path.basename(item))
		elif ".jpg" in item:
		    os.rename(item, new_jpg_dir + '/' + os.path.basename(item))
		elif ".psd" in item:
		    os.rename(item, new_psd_dir + '/' + os.path.basename(item))
		else:
		    os.rename(item, new_other_dir + '/' + os.path.basename(item))

	print "Files sorted!"


def without_subs():
	dir_to_sort = raw_input('Place path to files here:')
	directory = os.listdir(dir_to_sort)

	if any(".tif" in s for s in directory):
		new_tif_dir = dir_to_sort + '/TIFs'
		os.mkdir(new_tif_dir, 0755)
	if any(".jpg" in s for s in directory):
		new_jpg_dir = dir_to_sort + '/JPGs'
		os.mkdir(new_jpg_dir, 0755)
	if any(".psd" in s for s in directory):
		new_psd_dir = dir_to_sort + '/PSDs'
		os.mkdir(new_psd_dir, 0755)

	new_other_dir = dir_to_sort + '/OTHER'	
	os.mkdir(new_other_dir, 0755)

	for item in directory:
		if ".tif" in item:
		    os.rename(dir_to_sort + '/' + item, new_tif_dir + '/' + item)
		elif ".jpg" in item:
		    os.rename(dir_to_sort + '/' + item, new_jpg_dir + '/' + item)
		elif ".psd" in item:
		    os.rename(dir_to_sort + '/' + item, new_psd_dir + '/' + item)
		else:
		    os.rename(dir_to_sort + '/' + item, new_other_dir + '/' + item)

	print "Files sorted!"


def sort():


	sub = raw_input('Include all subdirectories Y/N?:')

	if sub.lower() == 'y':
		withsubs()
	elif sub.lower() == 'n':
		without_subs()
	else:
		print "Not a valid input!"
		sort()

	


sort()