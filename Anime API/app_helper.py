from Pipeline import Pipe
import os
import pandas as pd
pipe = Pipe()

outputPath = r".\templates"
df = pd.read_csv('Anime_df.csv')
def get_image(image_path, img_name):

	
	#try:
	image, top1, top5 = pipe.process(image_path)	
	#except:
	#	print('Mother Fucker')
	
	image.save(os.path.join(outputPath, img_name))

	info = ''
	for name in top1:
		index = df['Name'][df['Name'] == name].index[0]
		orgin = df['Orgin'][index]
		gender = df['Gender'][index]
		isMain = df['IsMain'][index]
		info += 'Name:{}, From anime:{}, Sex:{}, isMain:{};\\n\\n'.format(name, orgin, gender, isMain)
	info = info[:-4]
	os.remove(image_path)
	image.close()
	del image
	return info, img_name