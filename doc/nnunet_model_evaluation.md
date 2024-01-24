# Creating a nnU-Net model using SynthSeg

## Introduction
BIBSNet uses a nnU-Net model as its core component.  The data set for training a nnU-Net model consists of MRI images and synthetic MRI images created by SynthSeg.

Research professionals creating a nnU-Net model from new data should find this a helpful document.
## Scope
In this document, we cover the creation of synthetic data,  validation of model data (natural and synthetic), model training, model quality evaluation, and who to contact to add the model to BIBSNet.

## Contacts
You should contact []()[Paul Reiners](mailto:reine097@umn.edu) if you have any questions or run into any problems.

## Glossary
* *BIBSNet*: This BIDS App provides the utility of creating a nnU-Net anatomical MRI segmentation and mask with a infant brain trained model for the purposes of circumventing JLF within Nibabies.
* *[nnU-Net](https://github.com/MIC-DKFZ/nnUNet)*: nnU-Net is a semantic segmentation method that automatically adapts to a given dataset. It will analyze the provided training cases and automatically configure a matching U-Net-based segmentation pipeline. No expertise required on your end! You can simply train the models and use them for your application.
* *[SynthSeg](https://github.com/BBillot/SynthSeg)*: The first deep learning tool for segmentation of brain scans of any contrast and resolution

## Step-by-step process

1. Download the new data set of segmented MRI images.
2. Visual inspection (by Fez is ideal) of the data set.
3. [Run SynthSeg](https://github.com/BBillot/SynthSeg/blob/master/scripts/tutorials/2-generation_explained.py) to create synthetic images.
4. [Create nnU-Net model](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/how_to_use_nnunet.md).
5. After the model is created, for a sanity check you should [run Dice coefficient measures](https://github.com/DCAN-Labs/SynthSeg/blob/ade17f53285e8932a47ba91bba1f93a40874cc20/ext/neuron/metrics.py#L97) using the model and make sure the Dice coefficient is reasonable (at least 0.80, and, preferably, 0.90 or 0.95).
6. Communicate with [Tim Hendrickson](mailto:hendr522@umn.edu), who adds new models, before and after testing
