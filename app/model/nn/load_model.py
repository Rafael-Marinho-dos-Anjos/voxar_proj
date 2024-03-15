""" Module to load ResNet50 instance pretrained from ImageNet
    Model selection criterion:
    In PyTorch documentation are listed every model disponible pretrained model
    with its ImageNet Top 1 Acc, Top 5 Acc and params size. The selected model is
    Swin_V2_S, wich have achived 83.7% Top 1 acc, 96.36% Top 5 acc with 49.7M
    params, that is a very good accuracy for its size. Other models presents a better
    accuracy but with a larger size.
"""

# Importing network model and weights making assignment for more
# facilities to test several different architectures avaliable
# in PyTorch
import torch
from torchvision.models import swin_v2_s as net
from torchvision.models import Swin_V2_S_Weights as Weights


# Asserting if cuda is avaliable (for performance improvement)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# Get inference Transforms
transforms = Weights.DEFAULT.transforms()

# Instanciating pretrained model
model = net(weights=Weights.IMAGENET1K_V1).to(device)
