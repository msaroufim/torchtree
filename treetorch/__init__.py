import torch

class SpatialTree():
    def __init__():
        pass

    def __split__():
        pass



class KDTree(SpatialTree):
    def __split__(self, data):
        # data is a tensor
        
        mean = data.mean(dim=1)
        std =  data.std(dim=1)

        # return the coordinate of maximum variance
        return torch.max(std, dim=1)

