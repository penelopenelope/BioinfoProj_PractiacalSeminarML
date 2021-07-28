# Final Presentation

## ResNet50

Although in a common sence that deeper network will get more detailed features from the input, people also find that when networks reach certain layer number, the accuracy does not increase any more instead the errors increasing. 

Facing this degradation problem, a solution is proposed based on the plain VGG networks, named as deep residual learning framework. An identity mapping is added, so that the new output feature mapping is converted to the residual between the original feature mapping and the inputs. 

this small change improves the model performance a lot. It allows deeper networks to be trained without hurting performance as some layers can be skipped, and the model gets easier to optimized

## Our ResNet50 model

based on this ResNet structure, we generate our model based on a pretrained ResNet model...

.. we also investigate the impacts of each parameter on the model performance...

## learning rate schedule

three types - time-based, step-based and exponential. although we use a consistent learning rate during our training process.

## Precision, Recall, F1 score

Precision - how many actual positive are predicted as positive among prediction positive - TP/PP

Recall/Sensitivity - how many actual positive are predicted as positive among actual positive - TP/P

## Epoch, Batch, Iteration

In most cases, it is not possible to feed all the training data into an algorithm in one pass. This is due to the size of the dataset and memory limitations of the compute instance used for training. There is some terminology required to better understand how data is best broken into smaller pieces.  

An **epoch** elapses when an entire dataset is passed forward and backward through the neural network exactly one time.  If the entire dataset cannot be passed into the algorithm at once, it must be divided into **mini-batches**.  **Batch size** is the total number of training samples present in a single min-batch.  An **iteration** is a single gradient update \(update of the model's weights\) during training.  The number of iterations is equivalent to the number of batches needed to complete one epoch.  

So if a dataset includes 1,000 images split into mini-batches of 100 images, it will take 10 iterations ****to complete a single epoch.





































### 

