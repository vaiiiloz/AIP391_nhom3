from Pipeline import Pipe
import os
import pandas as pd
pipe = Pipe()
outputFile = "templates\output.jpg"
df = pd.read_csv('Anime_df.csv',encoding='latin-1')

def get_image(image_path):
	try:
		img, top1, top5 = pipe.process(image_path)
	except:
		pass
	print('Done')
	img.save(outputFile)

	info = ''
	for name in top1:
		index = df['Name'][df['Name'] == name].index[0]
		orgin = df['Orgin'][index]
		gender = df['Gender'][index]
		isMain = df['IsMain'][index]
		info += 'Name:{}, From anime:{}, Sex:{}, isMain:{};\n\n'.format(name, orgin, gender, isMain)
	return info