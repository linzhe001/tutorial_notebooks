# Deep Learning Basics notes
This notes includes two parts: 
1. basic train and test process 
2. model architecture
## Basic train process
The following chart shows the general process:
![image](./media/CIFAR_10N_CNN%20code%20flow%20chart.png)
The 5 important components are dataloader, loss function,optimzer, training epoch and iteration, evaluation matrix.
### Dataloader
Dataloader is used to split datasets into batches, so before dataloader there is a datasets function.

**datasets function:**

> input of datasets: lots of images and labels
> 
> output of datasets: augumented and paired images and labels in trainset; paired images and labels in testset

There are two way to creat datasets class: [inherent from library]((https://colab.research.google.com/github/linzhe001/tutorial_notebooks/blob/Notes/CIFAR_10N_CNN_withNotes.ipynb#scrollTo=z4uiWMiyCkjk&line=8&uniqifier=1)); [creat a new one](https://colab.research.google.com/github/mobarakol/tutorial_notebooks/blob/main/tiny_imagenet.ipynb#scrollTo=O5IYHVb5Rukr&line=6&uniqifier=1)
