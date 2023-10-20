# scara

This is the source code of a mini project I did for my second Year course project


In this Project, I built a Selective Controlled Articulated Robotic Arm (SCARA) bot, 3d printed along with an easy and intuitive user interface for everyone to easily access
the application

In typical industrial settings, programming a robot is a difficult task requiring skilled people with lots of knowledge in the domain. To overcome this challenge, I have designed a easy and intuitive interface to enhance user experience and allow even beginners to easily program a bot

# Usage

***The follwoing steps must be followed to use this Program***

1) Set the required angle for each joint
2) Send the commands to the bot to verify
3) Set the command in the buffer (Click the set button)
4) Repeat the process till all the commands are set in the buffer
5) Press **Send all** butten to send all the commands in the buffer

***To save the commands***
1) Press **Save Commands** Button
2) Save the file in the appropriate location (The file must be in .ccia extension)

***To Load the commands***
1) Press **Load Commands** Button to load the commands to the buffer
2) Select the file form the file locaion (the file must be in .ccia extension)
       * The commands are now stored in the buffer
3) Press **Send all** button to send the commands to the robot


# Robot

The robot is controlled using the Arduino UNO microcontroller. The Uno receives commands via a serial port or bluetooth module and performs the required task automatically. 

# Image of the interface

![Screenshot 2023-10-16 234707](https://github.com/sacheinn17/scara/assets/109337367/855b8ffe-dee2-416f-876b-af6b34643d87)

Note : This is the interface used for this project. However, the interface can be customized for specefic needs and may look different from this.
