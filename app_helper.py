from Pipeline import Pipe
import os
import pandas as pd
pipe = Pipe()
outputPath = r"\static\detect"
df = pd.read_csv('Anime_df.csv',encoding='latin-1')
if os.path.exists(outputPath):
	os.makedirs(outputPath)
def get_image(image_path, img_name):
	try:
		img, top1, top5 = pipe.process(image_path)
	except:
		pass
	img.save(os.path.join(outputPath, img_name))

	info = ''
	for name in top1:
		index = df['Name'][df['Name'] == name].index[0]
		orgin = df['Orgin'][index]
		gender = df['Gender'][index]
		isMain = df['IsMain'][index]
		info += 'Name:{}, From anime:{}, Sex:{}, isMain:{};\n\n'.format(name, orgin, gender, isMain)
	return info