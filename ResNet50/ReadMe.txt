This ReadMe file is an introduction on how to implement the models - ResNet50 and Inception V3 - to predict given image(s). The corresponding models are
named as 'ResNet50_FinalVersion_acc94.3.pth' and 'InceptionV3_FinalVersion_acc91.43.pth' in the corresponding folders. Also, a prediction script in Python is
provided named as 'Model_Prediction.py'.

Library - Pytorch

<Implementation 'Model_Prediction.py'>

python 3.7

open the script in IDE
model_path - path to the saved model

 - <predict single image>
Step 1: change the parameter 'img_path' - path to the image to predict
Step 2: Run the script

 - <predict batch images>
Step 1: change the parameter 'folder_path' - path to the images folder to predict
Step 2: Run the script

<File structure>

├── ReadMe.txt

│├── ResNet50/
│    ├── Model_Generation/
│        ├── ResNet50_FinalVersion_acc94.3.py
│    ├── Model_Performance/
│        ├── confusion_matrix.png
│        ├── model_performance.png
│        ├── Prediction-Atrophy.png
│        ├── Prediction-Non-Atrophy.png
│        ├── training_process.png
│    ├── Model_Prediction/
│        ├── Model_Prediction.py
│    ├── ResNet50_FinalVersion_acc94.3.pth

│├── InceptionV3/
│    ├── Model_Generation/
│        ├── InceptionV3_FinalVersion_acc91.43.py
│    ├── Model_Performance/
│        ├── confusion_matrix.png
│        ├── model_performance.png
│        ├── Prediction-Atrophy.png
│        ├── Prediction-Non-Atrophy.png
│        ├── training_process.png
│    ├── Model_Prediction/
│        ├── Model_Prediction.py
│    ├── InceptionV3_FinalVersion_acc91.43.pth

├── data/
│   ├── additional_test_imgs/
│        ├── test1_a.jpg
│        ├── test2_n.jpg
│        ├── atrophy_imgs/
│             ├── 4453335_corpus.dcm
│             ├── 4453335_corpus.png
│             ├── ...
│        ├── non_atrophy_imgs/
│             ├── 4439023_Corpus.dcm
│             ├── 4439023_Corpus.png
│             ├── ...
│   ├── train/
│        ├── Dysplasia/
│             ├── Dysplasia_original_D_1_1.png_050f0461-8f06-401c-878d-326b28b692df.png
│             ├── Dysplasia_original_D_1_1.png_1017738c-2e5e-4b6f-a653-53ee2b901d65.png
│             ├── ...
│        ├── Normal/
│             ├── Normal_original_N_1_1.png_0178db5a-974b-4c5e-ba3b-a01924230e36.png
│             ├── Normal_original_N_1_1.png_0e7cd4cb-c389-416e-bda6-cb1230313ee5.png
│             ├── ...
│   ├── test/
│        ├── D_1_1.png
│        ├── D_1_10.png
│        ├── ...
│        ├── N_1_1.png
│        ├── N_1_10.png
│        ├── ...
