import numpy as np

class my_conv(object):
    def __init__(self, input_data, weight_data, stride, padding = 'SAME'):
        self.input = np.asarray(input_data, np.float32)
        self.weights = np.asarray(weight_data, np.float32)
        self.stride = stride
        self.padding = padding

    def my_conv2d(self):

        [c, h, w] = self.input.shape
        [kc, k, _] = self.weights.shape

        assert c == kc #如果输入的channel 与卷积核的channel不一致则报错

        if self.padding  == "SAME":
            pad_h = (self.stride * (h - 1) + k - h ) // 2
            pad_w = (self.stride * (w - 1) + k - w) // 2
            rs_h = h
            rs_w = w

        elif self.padding == "VALID":
