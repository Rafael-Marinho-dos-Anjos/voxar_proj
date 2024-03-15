""" Module to load ResNet50 instance pretrained from ImageNet
    Model selection criterion:
    In PyTorch documentation are listed every model disponible pretrained model
    with its ImageNet Top 1 Acc, Top 5 Acc and params size. The selected model is
    Wide_ResNet50_2, wich have achived 81.6% Top 1 acc, 95.76% Top 5 acc with 68.9M
    params, that is a very good accuracy for its size. Other models presents a better
    accuracy but with a larger size.
"""

# Importing network model and weights making assignment for more
# facilities to test several different architectures avaliable
# in PyTorch
import torch
from torchvision.models import wide_resnet50_2 as net
from torchvision.models import Wide_ResNet50_2_Weights as Weights


# Asserting if cuda is avaliable (for performance improvement)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# Get inference Transforms
transforms = Weights.DEFAULT.transforms()

# Instanciating pretrained model
model = net(weights=Weights.IMAGENET1K_V2).to(device)
