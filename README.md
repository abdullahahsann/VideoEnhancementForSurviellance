#  Realtime Video Enhancement For Surviellance using Machine Learning
 
*This is, for the moment, 40% implementation of the project for my BCS in Computer Science's Final Year Project.*
*As of now it includes the Dehazer-Model along with a simple Desktop Application (coded in pyQt) in which the model has been implemented along with an open-cv simple object detection model*
## Table of Contents
- [Introduction](#introduction)
- [Problem Solution](#problem-solution)
- [Advantages of proposed system](#advantages-of-proposed-system)
- [Results](#results)
- [How to test yourself](#how-to-test-yourself)

  
## Introduction
Under bad weather conditions, such as fog and haze, the quality of images degrades severely due to the inﬂuence of particles in the atmosphere. Suspended particles will scatter light and result in attenuation of reﬂected light from the scene and the scattered atmospheric light will also mix with the light received by the camera and change the image contrast and color. In surveillance systems this can obstruct the whole feed in weathers as such, and infiltrations can be done by potential intruders, using this to their advantage. And we are not just referring to home surveillance, but on industry level. Clear video feed will help in smooth running of operations even during the worst of weathers.

In production there aren’t any specific surveillance products that offer such functionality. Or an all-around solution for all the bad weather conditions that might happen. Our software will provide all the functionalities in one package and in real time. Thus, providing a clean video feed no matter the condition of the weather.  Along with this our model will also have an autonomous security system that will notify the user about any intrusion or unwanted activity that it detects during the time that the user specifies. 

## Problem Solution

For our enhanced video output feed, we are providing three different Machine Leaning models:
  1. Image Dehazing
  2. Image Deraining
  3. Low Light Image Enhancement
 
 We’ll have a web-based system for the user through which they’ll be getting the video feed of their surveillance camera. The user will have options to apply any of the filter using our models to enhance the output quality in bad weather conditions. The history of the video will also be saved. And user will have access to it and can go back and review the past footage. And if needs be, apply any filter during any point in time of the video.
 
 For out automated security surveillance, the user will define which camera feeds need to be checked for any unusual activity. And from the choice of filters: No activity or No Human activity, pick one. And based on the user’s choice the AI will detect any human related activity, or any activity at all whatsoever. And if anything is detected will instantly report to the user.
 
 ## Advantages of proposed system
 
 The product will help in many computer vision related tasks. It can be deployed in any field that requires clearer images/video outputs in such bad weather condition. The uses can range from being used in a cars ADAS system to being used by firefighters for a clearer video feed.We implement the model in CCTV, which can drastically enhance the work performance capacity even in the worst of weathers and increase security alongside it.
 
 The product will work not in just one, but all of the most worst weather conditions possible, being: Hazy, fogy, raining. And our low light enhancement model will make the CCTV work just as perfectly even in the darkest of night scenarios. It can help in smooth running of operations, that require overlooking, even when the weather is not favorable. It can be installed in remote areas where humans cannot reach. 
 
 Along with that the intruder detection (object detection) module can enhance the security aspect of a CCTV system, and that combined with a clearer video feed, even during bad weather or nighttime, can greatly increase the security system.
 
 ## Results
 
 VALIDATION SET:
 ![Screenshot from 2021-07-11 19-28-33](https://user-images.githubusercontent.com/62840383/125199229-aa8c2500-e27e-11eb-92a6-da1998455778.png)
![Screenshot from 2021-07-11 19-28-45](https://user-images.githubusercontent.com/62840383/125199235-ac55e880-e27e-11eb-9776-33c42374f632.png)

 
 
 IMAGES FROM GOOGLE:
 
 ![Screenshot from 2021-07-11 19-27-19](https://user-images.githubusercontent.com/62840383/125199189-7add1d00-e27e-11eb-89d4-a11858bd9a00.png)
![Screenshot from 2021-07-11 19-26-51](https://user-images.githubusercontent.com/62840383/125199198-829cc180-e27e-11eb-81e2-8f61cecf530b.png)
![Screenshot from 2021-07-11 19-26-06](https://user-images.githubusercontent.com/62840383/125199201-84668500-e27e-11eb-925a-63ca47833a55.png)
![Screenshot from 2021-07-11 19-27-45](https://user-images.githubusercontent.com/62840383/125199207-8defed00-e27e-11eb-95f2-3839d547ed5a.png)

 
 ## How to test yourself
 If you want to test the model. The simplest way is to run the Desktop application (though it's still not refined), as it will run in real time. Simply run the main.py file in that folder. You might have to change the value of cv2.VideoCapture in the ui_main.py file at line 745. Change the 1 to 0 or 2 and try again if you are not getting any video feed. If you want to procecss a custom video, put it in the same directory and put the name of that video inside brackets with " ".
 
   For testing the dehazer model independently. You can run the evaluation.py file in the Evaluation directory in the Dehazer folder. I've made functions to evaluate video, custom video or a set of images. Just run the appropriate function and it'll give the result.
   If there's any issue at all or you just wanna ask something do let me know :D.
