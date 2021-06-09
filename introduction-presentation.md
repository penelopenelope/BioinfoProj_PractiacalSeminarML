# Introduction Presentation

## 1. Research Problem - Atrophic Gastritis Diagnosis

leading to a loss of [gastric glandular cells](https://en.wikipedia.org/wiki/Gastric_gland) and their eventual replacement by intestinal and fibrous tissues

Given this information, the motivation of this research project is that the diagnosis quality from the conventional white-light endoscopy is that

so the desired situation is that we want to develop an more sensitive and specific algorithm with low cost but still high accuracy. 

## 2. Current Situation

Aiming at this desired situation, what is the current situation of the research topic? There are some methods already really successful enough and helpful to give us some intructions. 

### 1\) Guimarães, P., Keller, A., Fehlmann, T., et al.​ 

###  Deep-learning based detection of gastric precancerous conditions

the first methods is also an inspiration to our research project, which achieved a rather high accuracy using real-world data even though the image data size and quality are limited severely. 

the first dataset is used mainly for model training and the second one is for model modification and testing. Instead of training a model from scratch and it will take a really long time on training, they used transfer learning and fine-tuned methods which save training time and also keeps the model accuracy. In fact we can see this technique is also applied in other literatures.

They selected several deep learning methods to compare their performance and turns out the best one is VGG16

### 2\) Zhang, Y., Li, F., Yuan, F., et al.​  

### Diagnosing chronic atrophic gastritis by gastroscopy using artificial intelligence​

The second methods also used transfer learning on a rather sufficient data size, and their best performance model is DenseNet121, which can also tell the different degrees of the diseace development with high accuracy. at the end of their study, they also generate heat maps to tell which image regions makes the model decision.

### 3\) Mu, G., Zhu, Y., Niu, Z., et al.​ 

### Expert-level classification of gastritis by endoscopy using deep learning: a multicenter diagnostic trial​



### 4\) Open Challenges



