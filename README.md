# TreeTorch Trees

Spatial trees are essential to speed up nearest neighbor search for high dimensional data. They work by recursively partitioning the space via some rule.

Each rule describes a different algorithm and SpaceTorch currently provides support for
* KD-trees
* Random Projection trees
* PCA trees

It's easy to support new algorithms by following the Spatial Tree interface


## Installation

```
pip install treetorch
```

## Usage
Build a tree

Perform nearest neighbor search

## Requirements
Depends on how you're storing data
* numpy 
* Pytorch
* Vanilla Python lists

## Next steps

## References
* http://mlwiki.org/index.php/Metric_Trees#Spill-Trees
* https://arxiv.org/abs/1507.03338
* https://github.com/bmcfee/spatialtree
* https://github.com/scipy/scipy/blob/v0.14.0/scipy/spatial/kdtree.py