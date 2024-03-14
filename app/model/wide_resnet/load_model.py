""" Module to load ResNet50 instance pretrained from ImageNet
    Model selection criterion:
    In PyTorch documentation are listed every model disponible pretrained model
    with its ImageNet Top 1 Acc, Top 5 Acc and params size. The selected model is
    Wide_ResNet50_2, wich have achived 81.6% Top 1 acc, 95.76% Top 5 acc with 68.9M
    params, that is a very good accuracy for its size. Other models presents a better
    accuracy but with a larger size.
"""

from torchvision.models import wide_resnet50_2, Wide_ResNet50_2_Weights
import torch


# Asserting if cuda is avaliable (for performance improvement)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# Get inference Transforms
transforms = Wide_ResNet50_2_Weights.DEFAULT.transforms()

# Instanciating pretrained model
model = wide_resnet50_2(weights=Wide_ResNet50_2_Weights.IMAGENET1K_V2).to(device)
