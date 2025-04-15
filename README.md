# Poultry Disease Classification Using Deep Learning

## Project Overview
This project aims to classify poultry diseases using deep learning techniques. We've developed and trained models to accurately identify various poultry diseases from images, which can help in early detection and treatment, reducing economic losses in the poultry industry.

## Dataset
The dataset consists of images of poultry with different disease conditions:
- Healthy poultry
- Salmonella infection
- New Castle
- Coccidiosis 

The data is organized into training and validation sets, with augmented images to improve model generalization.

## Model Performance
Our best model achieved **95.36%** validation accuracy using an iterative training approach:

| Iteration | Validation Accuracy | Improvement |
|-----------|-------------------|-------------|
| 1         | 82.44%            | -           |
| 2         | 89.74%            | +7.30%      |
| 3         | 95.56%            | +5.62%      |


## Implementation Details
- **Base Architecture**: EfficientNet-B3 (pretrained)
- **Training Strategy**: 2-stage training with gradual unfreezing
- **Optimization**: Mixed precision training using PyTorch's AMP
- **Data Augmentation**: Multiple augmentation techniques employed

## Requirements
- PyTorch
- torchvision
- efficientnet_pytorch
- thop (for model profiling)
- NumPy, Pandas
- Matplotlib

## Training Process
The model was trained in three iterations, each consisting of two stages:
1. **Stage 1**: Train only the final layers while keeping pretrained weights frozen
2. **Stage 2**: Fine-tune the entire network with a lower learning rate

Each iteration built upon the previous one, with adjustments to hyperparameters based on validation results.

## Future Improvements
- Try more advanced architectures (EfficientNetV2, ConvNeXt)
- Implement more sophisticated data augmentation techniques
- Explore ensemble methods for improved accuracy
- Deploy model as a lightweight application for field use


## License
This project is licensed under the MIT License - see the LICENSE file for details.