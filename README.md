# EAST: An Efficient and Accurate Scene Text Detector
### Description:
The motivation of this version is to build a easy-training model containing train-eval-zipfile-computeF1.
The version is ported from [argman/EAST](https://github.com/argman/EAST), from Tensorflow to Pytorch

Now, the first three of the flow is done, and some bugs exists in compute F1 score script.So you can only submit it to website

You could use zipfile ./submit/epoch_###_submit.zip to submit on [website](http://rrc.cvc.uab.es/?ch=2&com=mymethods&task=1) 

### Introduction
This is a pytorch re-implementation of [EAST: An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155v2).
The features are summarized blow:

+ Only **RBOX** part is implemented.
+ A fast Locality-Aware NMS in C++ provided by the paper's author.(g++/gcc version 6.0 + will be ok)
+ Evalution see [here](http://rrc.cvc.uab.es/?ch=4&com=evaluation&view=method_samples&task=1&m=29855&gtv=1) for the detailed results.
+ Differences from original paper
	+ Use ResNet-50 rather than PVANET
	+ Use dice loss (optimize IoU of segmentation) rather than balanced cross entropy
	+ Use linear learning rate decay rather than staged learning rate decay
	
Thanks for the author's ([@zxytim](https://github.com/zxytim)) help!
Please cite his [paper](https://arxiv.org/abs/1704.03155v2) if you find this useful.

### Contents
1. [Installation](#installation)
2. [Download](#download)
3. [Prepare dataset/pretrain](#dataset)
4. [Test](#train)
5. [Train](#test)
6. [Examples](#examples)


### Installation
1. Any version of pytorch version > 0.4.0 should be ok.

### Download
1. Pretrained model is not provided temporarily. Web site is updating now, please continue to pay attention 

### Prepare dataset/pretrain weight
1. dataset 
+ -- trainset  ./data/train/img_###.jpg 
	       ./data/test/img_###.txt 
+ -- testset   ./data/test/img_###.jpg (img only)
**Note: you can download dataset here
+ -- [ICDAR15](http://rrc.cvc.uab.es/?ch=4&com=downloads)
+ -- [ICDAR13](http://rrc.cvc.uab.es/?ch=2&com=downloads)

2. pretrained  
+ In config.py set resume True and set checkpoint path/to/weight/file



