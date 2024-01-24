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

1. Visual inspection (by Fez is ideal)
2. Dice coefficient measures
3. Communicate with people who add new models (I think this is Barry currently?) before and after testing

## Checklists
Often, itemized checklists are easier to follow and some SOPs might be better described in this form.