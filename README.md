# Class Cloud Service Platform

This project is a class cloud service platform based on xadmin, committed to providing class cadres with high-quality, fast, convenient, and digital data experience

## Notice
The class source. zip file in tagv1.0.3 is a web side file. To download this file, you don't need to make the following changes, just configure the corresponding environment and the correct environment file path in the environment file. You can also download the APK experience app




## 1. Move file

Download the files for branch retain, such as HelloWorld, classy, mycellery, etc. Place lay, layui.js, layui.all.js in the lib/layui folder, and create a new folder named static. Place CSS, fonts, images, js, lib in static. Once the file locations are correct, pull the project into the IDE









## 2.Change Configuration File

1. Open the settings. py file in the HelloWorld folder

2. Find the MySQL database configuration and change it to your own database configuration

   ![image-20231003000956402](https://github.com/MoonforDream/Xadmin-based-class-cloud-service-platform/blob/remain/image-20231003000956402.png)

3. Add sending email configuration at the end of the file

4. Open the terminal, enter Python manage. py makemigrations, Python manage. py migrate, and migrate the model layer to the database

5. Open config.py and main.py in the mycellery folder, configure the Redis configuration inside as your own, and then change the sending email address of tasks. py in the email folder to your own





## 3. Run Project
Run screenshot
![image-20231003000956403](https://github.com/MoonforDream/Xadmin-based-class-cloud-service-platform/blob/main/Snipaste_2023-10-03_18-19-07.jpg)

![image-20231003000956404](https://github.com/MoonforDream/Xadmin-based-class-cloud-service-platform/blob/main/Snipaste_2023-10-03_19-01-50.jpg)



