
import torch.nn as nn
from torchvision.models import vgg16, VGG16_Weights

def get_dex():
    weights = VGG16_Weights.DEFAULT
    model = vgg16(weights=weights)
    dim_feats = model.last_linear.in_features
    model.last_linear = nn.Linear(dim_feats, 101)
    model.avg_pool = nn.AdaptiveAvgPool2d(1)
    return model

def main():
    model = get_dex()
    print(model)

if __name__ == '__main__':
    main()

