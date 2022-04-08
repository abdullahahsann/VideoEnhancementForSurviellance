#  Realtime Video Enhancement For Surviellance using Machine Learning
 
## Table of Contents
- [Introduction](#introduction)
- [Problem Solution](#problem-solution)
- [Advantages of proposed system](#advantages-of-proposed-system)
- [Results](#results)
- [Desktop Application](#desktop-application)
- [How to test yourself](#how-to-test-yourself)
- [Papers that have helped me a lot](#papers-that-have-helped-me-a-lot)
- [Code](#code)
  
## 
Special thanks to my supervisors: DR. Syed Sohaib Ali & Dr. Akber Abid Gardezi without whose guidance this wouldn't had been possible.
## Introduction
Under bad weather conditions, such as fog and haze, the quality of images degrades severely due to the inﬂuence of particles in the atmosphere. Suspended particles will scatter light and result in attenuation of reﬂected light from the scene and the scattered atmospheric light will also mix with the light received by the camera and change the image contrast and color. In surveillance systems this can obstruct the whole feed in weathers as such, and infiltrations can be done by potential intruders, using this to their advantage. And we are not just referring to home surveillance, but on industry level. Clear video feed will help in smooth running of operations even during the worst of weathers.

In production there aren’t any specific surveillance products that offer such functionality. Or an all-around solution for all the bad weather conditions that might happen. Our software will provide all the functionalities in one package and in real time. Thus, providing a clean video feed no matter the condition of the weather.  Along with this our model will also have an autonomous security system that will notify the user about any intrusion or unwanted activity that it detects during the time that the user specifies. 

## Problem Solution

For our enhanced video output feed, we are providing three different Machine Leaning models:
  1. Image Dehazing
  2. Image Deraining
  3. Low Light Image Enhancement
 
 We have a desktop application system (coded in PyQt) for the user through which they’ll be getting the video feed of their surveillance camera. The user will have options to apply any of the filter using our models to enhance the output quality in bad weather conditions. The history of the video will also be saved. And user will have access to it and can go back and review the past footage. And if needs be, apply any filter during any point in time of the video.
 
 For ouR automated security surveillance, the user will define which camera feeds need to be checked for any unusual activity. And from the choice of filters: Human detection or Movement detection, pick one. And based on the user’s choice the AI will detect any human related activity, or any activity at all whatsoever. And if anything is detected will instantly report to the user.
 
 ## Advantages of proposed system
 
 The product will help in many computer vision related tasks. It can be deployed in any field that requires clearer images/video outputs in such bad weather condition. The uses can range from being used in a cars ADAS system to being used by firefighters for a clearer video feed.We implement the model in CCTV, which can drastically enhance the work performance capacity even in the worst of weathers and increase security alongside it.
 
 The product will work not in just one, but all of the most worst weather conditions possible, being: Hazy, fogy, raining. And our low light enhancement model will make the CCTV work just as perfectly even in the darkest of night scenarios. It can help in smooth running of operations, that require overlooking, even when the weather is not favorable. It can be installed in remote areas where humans cannot reach. 
 
 Along with that the intruder detection (object detection) module can enhance the security aspect of a CCTV system, and that combined with a clearer video feed, even during bad weather or nighttime, can greatly increase the security system.
 
 ## Results
 
 These all results also work on real time, videos will be uploaded soon.
 
 ### Low Light Enhancement
![image](https://user-images.githubusercontent.com/62840383/136186439-6778036e-4cd7-4c7f-8d24-212484d73152.png)

![image](https://user-images.githubusercontent.com/62840383/136186349-c16e0ac6-7f29-4962-befd-54d638cbbc52.png)

 
 ### Dehazing
 TEST SET:
 ![Screenshot from 2021-07-11 19-28-33](https://user-images.githubusercontent.com/62840383/125199229-aa8c2500-e27e-11eb-92a6-da1998455778.png)
 
 
![Screenshot from 2021-07-11 19-28-45](https://user-images.githubusercontent.com/62840383/125199235-ac55e880-e27e-11eb-9776-33c42374f632.png)

 
 IMAGES FROM GOOGLE:
 
 ![Screenshot from 2021-07-11 19-27-19](https://user-images.githubusercontent.com/62840383/125199189-7add1d00-e27e-11eb-89d4-a11858bd9a00.png)
![Screenshot from 2021-07-11 19-26-51](https://user-images.githubusercontent.com/62840383/125199198-829cc180-e27e-11eb-81e2-8f61cecf530b.png)
![Screenshot from 2021-07-11 19-26-06](https://user-images.githubusercontent.com/62840383/125199201-84668500-e27e-11eb-925a-63ca47833a55.png)
![Screenshot from 2021-07-11 19-27-45](https://user-images.githubusercontent.com/62840383/125199207-8defed00-e27e-11eb-95f2-3839d547ed5a.png)

## Desktop Application
### Main Menu

![Capdcdcdcdture](https://user-images.githubusercontent.com/62840383/146819162-cbaa496c-c9a2-4d6a-98b1-135a4edd0fa1.PNG)

### Camera Feeds - (LLE Model in action, it works in real time)

![1](https://user-images.githubusercontent.com/62840383/146819175-aab193bd-633c-4f01-a3e4-cd815e8fb75e.PNG)
![2](https://user-images.githubusercontent.com/62840383/146819185-ddfff96f-582b-4fc4-b0a1-b68e8eaf11db.PNG)


### Human/Movement Detection

![Capturddddde](https://user-images.githubusercontent.com/62840383/146819206-b410e7bc-1282-4206-a4e1-92c1e433a8d9.PNG)
![Capddddture](https://user-images.githubusercontent.com/62840383/146819217-c2de0041-3e22-4fa0-903c-e4c62eb58ac3.PNG)
![Captcccccccure](https://user-images.githubusercontent.com/62840383/146819225-c6690a5a-f104-4849-a77a-5d491d9c7955.PNG)
![WhatsApp Image 2021-12-21 at 00 04 27](https://user-images.githubusercontent.com/62840383/146819286-bef459f3-e310-494f-93d0-b3bdb169a122.jpeg)


### Video Player
 ![Captdfdfdfdure](https://user-images.githubusercontent.com/62840383/146819321-dd898505-4741-4e01-b2c6-e593aa1678db.PNG)

 ## How to test yourself
 If you want to test the model. The simplest way is to run the Desktop application , as it will run in real time. Simply run the main.py file in that folder. You might have to change the values of cv2.VideoCapture. If you want to procecss a custom video, put it in the same directory and put the name of that video inside brackets with " ".
 
   For testing the dehazer, LLE or derainer model independently. You can run the evaluation.py file in the Evaluation directory in their respective folders. I've made functions to evaluate video, custom video or a set of images. Just run the appropriate function and it'll give the result.
   If there's any issue at all or you just wanna ask something do let me know :D.
   
   I'll soon add a whole tutorial detailing how i coded all of this, what libraries, api's, datasets used to train the models etc were used and a basic changes section to have the application up and running in no time.

 ## Papers that have helped me a lot
 
  1. An All-in-One Network for Dehazing and Beyond (https://arxiv.org/abs/1707.06543)
  2. Generic Model-Agnostic Convolutional Neural Network for Single Image Dehazing (https://arxiv.org/abs/1810.02862)
  3. Low-Light Image and Video Enhancement Using Deep Learning: A Survey (https://arxiv.org/abs/2104.10729)
  4. A great resource for Low Light models: (https://github.com/cxtalk/You-Can-See-Clearly-Now)
  5. A great resource for deraining models: (https://github.com/nnUyi/DerainZoo)
 
 ## Other Great Resources 
   1. Learning PyQt: (https://www.youtube.com/c/SpinnTV) - best place to learn pyqt
   2. Deep Learning: (https://www.coursera.org/specializations/deep-learning) - best courser to start ML journey
   3. Deep Learning Concepts: (https://www.youtube.com/c/deeplizard) - best place for ML DL Concepts 
   4. Deep Learning Practical: (https://www.youtube.com/c/sentdex/featured) - the person who started it all for me :D 

 
 ## Code
   Code for the Desktop Application as well as the ML models can be requested.
   Kindly reach me on my email :D.

