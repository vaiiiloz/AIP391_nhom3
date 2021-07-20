from Pipeline import Pipe
import os
import pandas as pd
pipe = Pipe()
outputPath = r"static\detect"
for filename in os.listdir(outputPath):
	os.remove(os.path.join(outputPath, filename))
df = pd.read_csv('Anime_df.csv',encoding='latin-1')

def get_image(image_path, img_name):
	
	img, top1, top5 = pipe.process(image_path)
	
	img.save(os.path.join(outputPath, img_name))

	info = ''
	for name in top1:
		index = df['Name'][df['Name'] == name].index[0]
		orgin = df['Orgin'][index]
		gender = df['Gender'][index]
		isMain = df['IsMain'][index]
		info += 'Name:{}, From anime:{}, Sex:{}, isMain:{};\n\n'.format(name, orgin, gender, isMain)
	img.show()
	img.close()
	return info