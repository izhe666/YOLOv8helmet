#导入这两个模块
import my1_3_CBAM, my1_2_SKNets
import torch
import torch.nn as nn
import torch.nn.functional as F


class ASAM (nn.Module):
    def __init__(self, input_channels, output_channels):
        super().__init__()
        self.cbam = my1_3_CBAM.my1_3_CBAM(input_channels)
        self.ska = my1_2_SKNets.my1_2_SKNets(channel = input_channels , reduction = 16)

    def forward(self , x ):
        input = x
        out = self.ska(input)
        out = self.cbam(input)
        return out

