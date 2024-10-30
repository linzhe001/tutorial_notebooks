# Deep Learning Basics notes
This notes includes two parts: 
1. basic [train](https://github.com/linzhe001/tutorial_notebooks/edit/Notes/Deep_Learning_Basics.md#basic-train-process) and test process 
2. model architecture
## Basic train process
The following chart shows the general process:
![image](./media/CIFAR_10N_CNN%20code%20flow%20chart.png)
The 5 important components are [dataloader](https://github.com/linzhe001/tutorial_notebooks/edit/Notes/Deep_Learning_Basics.md#dataloader), loss function,optimzer, training epoch and iteration, evaluation matrix.
### Dataloader
Dataloader is used to split datasets into batches, so before dataloader there is a datasets function.

**datasets function:**

> input of datasets: lots of images and labels
> 
> output of datasets: augumented and paired images and labels in trainset; paired images and labels in testset

There are two way to creat datasets class: [inherent from library](https://colab.research.google.com/github/linzhe001/tutorial_notebooks/blob/Notes/CIFAR_10N_CNN_withNotes.ipynb#scrollTo=z4uiWMiyCkjk&line=8&uniqifier=1); [creat a new one](https://colab.research.google.com/github/mobarakol/tutorial_notebooks/blob/main/tiny_imagenet.ipynb#scrollTo=O5IYHVb5Rukr&line=6&uniqifier=1).

They are similar but only the new datasets create mapping between ID with classes (saved in .txt).

## Model architecture

each convolution kernel (filters) can generate one channel output
**Basic input output image size calculation**

$$O = \frac{(I + 2P - K)}{S} + 1$$

where：
- $$O$$ = output image size（height or width）
- $$I$$ = input image size
- $$P$$ = padding
- $$K$$ = kernel size
- $$S$$ = stride
