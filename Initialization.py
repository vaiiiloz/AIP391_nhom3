import torch
import torch.nn as nn
from torchvision import transforms as T
import timm

class EffNetV2(nn.Module):
    def __init__(self,pretrained = True, labels=1) -> None:
        super().__init__()
        self.backbone = timm.create_model('tf_efficientnetv2_b3', pretrained = pretrained)
        self.backbone.classifier = nn.Linear(self.backbone.classifier.in_features,labels)
        
    def forward(self,x)->torch.Tensor:
        out = self.backbone(x)
        return out
    
class Models:
    def __init__(self, detect_model_path = 'best.pt', recog_model_path = 'Eff_anime.pt', num_labels = 1):
        self.detect_model = torch.hub.load('ultralytics/yolov5', 'custom', path= detect_model_path)
        
        
        
        self.recog_model = EffNetV2(pretrained = False, labels = num_labels)
        self.recog_model.load_state_dict(torch.load(recog_model_path))
        if torch.cuda.is_available():
            self.device = torch.device('cuda:0')
            
        else:
            self.device = torch.device('cpu')
        self.detect_model.to(self.device)
        self.recog_model.to(self.device)
        
        