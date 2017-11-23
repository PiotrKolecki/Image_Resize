# # # # # # # # # # # # # # # #
# 			jpg image resizer				#
# 			by  Piotr Kolecki					#
# 					v. 0.1						#
# # # # # # # # # # # # # # # #
from PIL import Image																		# Pillow package - not in standard library
import sys																						# handling arguments
import os.path																					# to check whether file exists

# initialization
keep_ratio = False
# check for name
if len(sys.argv) > 1:																			# *.py [file]
	file_name = sys.argv[1]
	if not os.path.exists(file_name):
		print('\n* * ERROR * *\nfile not found\naborting')
		sys.exit()
	# check for sizes																			# -=- may make it like: one size means keep ratio -=-
	if len(sys.argv) > 3:
		if sys.argv[2] == 'ratio':															# *.py [file] ratio [value]
			keep_ratio = True																	# ^ [value] is longest side of image ^
		else:																						# *.py [file] [width] [height]
			output_width = int(sys.argv[2])
			if output_width < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
			output_height = int(sys.argv[3])
			if output_height < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
	else:																							# no sizes or missing one
		output_width = int(input('type in output image width '))
		if output_width < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
		output_height = int(input('type in output image length '))
		if output_height < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
else:																								# no arguments - get it now
	file_name = input('type in file name ')
	if not os.path.exists(file_name):
		print('\n* * ERROR * *\nfile not found\naborting')
		sys.exit()
	if input('do you want to keep ratio? (y/n) ') == 'y':
		temp_size = int(input('type in image longest side '))					#have to temp it cuz idk if its horizontal/vertical
		if temp_size < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
		keep_ratio = True
	else:
		output_width = int(input('type in output image width '))
		if output_width< 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
		output_height = int(input('type in output image length '))
		if output_height < 1:
				print('\n* * ERROR * *\nbad size\naborting')
				sys.exit()
# open image and get some info
input_image = Image.open(file_name)
input_width, input_height = input_image.size
image_extension = input_image.format												# -=- not used currently -=-
# keeping ratio - calculate sizes
if keep_ratio:
	if input_width > input_height:														# image is horizontal
		if len(sys.argv) > 3: 
			output_width = int(sys.argv[3])
		else:
			output_width = temp_size
		ratio = output_width / input_width
		output_height = int(input_height * ratio)
	else:																							# image is vertical (or square)
		if len(sys.argv) > 3:
			output_height = int(sys.argv[3])
		else:
			output_height = temp_size
		ratio = output_height / input_height
		output_width = int(input_width * ratio)
# resize and save
output_image = input_image.resize((output_width, output_height))
output_name = input('type in output file name (enter for default name) (extension will be added) ')
if not output_name:
	output_name = 'resized'																	# default name
if os.path.exists(output_name + '.jpg'):												# check if there is file named like that
	if input('File exists. Do you want to overwrite it? (y/n) ') == 'y':
		output_image.save(output_name + '.jpg', "JPEG")
else:
	output_image.save(output_name + '.jpg', "JPEG")