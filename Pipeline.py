import torch
from torchvision import transforms as T
from Initialization import Models
from PIL import Image, ImageDraw, ImageFont
class Pipe:
    def __init__(self, labels_path = 'labels.txt'):
        f = open(labels_path)

        a = f.readline()
        a = a.replace('[','').replace(']','').replace("'",'')
        self.labels = [name for name in a.split(', ')]
        self.val_aug = T.Compose([
        T.Resize((224,224)),
        T.ToTensor(),
        T.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
    ])
        self.Models = Models(num_labels = len(self.labels))
    
    def process(self, img_path):
        img = Image.open(img_path).convert('RGB')
        draw = ImageDraw.Draw(img)
        face_locations = self.detect_face(img)
        top1, top5 = self.recognition_face(img, draw, face_locations)
        del draw
        return img, top1, top5
    
    def detect_face(self, img):
        result = self.Models.detect_model(img)
        result.xyxy[0]  # img1 predictions (tensor)
        results = result.pandas().xyxy[0]
        return results
    
    def recognition_face(self, img, draw, face_locations):
        self.Models.recog_model.eval()
        top5 = []
        top1 = []
        for col,row in face_locations.iterrows():
            xmin = row['xmin']
            ymin = row['ymin']
            xmax = row['xmax']
            ymax = row['ymax']
            mask = img.crop((xmin-30, ymin-30, xmax+30, ymax+30))
            inputs = self.val_aug(mask).unsqueeze_(0)
            outputs = self.Models.recog_model(inputs)
            pre = outputs.topk(5, 1, True, True)[1]
            top5.append([self.labels[i] for i in pre[0].tolist()])

            idx = torch.max(outputs,1)[1]
            pre = torch.max(outputs,1)[0]
            if pre.item()>1:
                name = self.labels[idx.item()]
                box = name.split()
                if len(box)>2:
                    name = box[0]+' '+box[1]
            else: 
                name = 'Unknow'
            top1.append(name)
            left, top, right, bottom = int(xmin),int(ymin), int(xmax), int(ymax)

            draw.rectangle(((left, top),(right, bottom)), outline = (0,0,0))
            fontsize = self.create_font(name, right-left)
            font = ImageFont.truetype("arial.ttf", fontsize)
            text_width, text_height = draw.textsize(name, font = font)
            
#             if text_width>right-left+10:
# #                 name = name.replace(' ','\n')
# #                 text_width, text_height = draw.textsize(name)
# #             if top-text_height-10<0:
#                 name = name.split(' ')[0]
#                 text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom+text_height+10),(right, bottom)), outline = (0,0,0))

            draw.text((left+6,bottom+5),name, fill=(255,0,0,0), font = font)
        return top1, top5
    def create_font(self, txt, img_size, img_fraction = 1):
        fontsize = 1
        font = ImageFont.truetype("arial.ttf", fontsize)
        while font.getsize(txt)[0] < img_fraction*img_size:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype("arial.ttf", fontsize)

        # optionally de-increment to be sure it is less than criteria
        fontsize -= 1
        return fontsize