# Final Presentation

## ResNet50

Although in a common sence that deeper network will get more detailed features from the input, people also find that when networks reach certain layer number, the accuracy does not increase any more instead the errors increasing. 

Facing this problem, a solution is proposed based on the plain VGG networks, named as deep residual learning framework. An identity mapping is added, so that the new output feature mapping is converted to the residual between the original feature mapping and the inputs. 

this small change improves the model performance a lot. It allows deeper networks to be trained without hurting performance as some layers can be skipped.

## Our ResNet50 model



### 4\) Open Challenges

As a conclusion of our literature review, we found some challenges still exist in this research topic. most literature can only execute focal detections on some regions like cardia, fundus and stomach angle, a more complete algorithm is needed in practical clinical application to detect the entire gastric mucosa.

Further more, scientists also want to tell the different etiologies of atrophic gastritis from the endoscopy images, which also need more exploratioin. 

