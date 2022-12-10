# ME495 Embedded Systems Homework 4
Author: James Oubre
## For manual operation:
* Use `ros2 launch nubot_nav manual_explore.launch.xml ` to open the simulation and have the robot spawn in Gazebo
* In a separate terminal, run `ros2 run teleop_twist_keyboard teleop_twist_keyboard` and drive the robot around to create a map

### Video

https://user-images.githubusercontent.com/46512429/206826980-dd02de71-338a-4846-827d-ec6705dda41a.mp4

## For autonomous operation:
* Use `ros2 launch nubot_nav explore.launch.xml ` to open the simulation
* Just wait until the robot explores the entire area to get a map
* The robot explores autnomously by subscribing to the `/pose` topic to get its current position. A random
value between 10 and -10 is then added to that positon and sent to the robot as a goal pose. This 
makes the robot drive around the area randomly.

### Video (5x Speed)

https://user-images.githubusercontent.com/46512429/206827010-58f4429a-410d-43fb-beea-8e5912d93229.mp4

### Map

![Screenshot from 2022-12-09 21-26-54](https://user-images.githubusercontent.com/46512429/206826951-90d4092e-48d3-457e-a54d-187642271e41.png)

### People I worked with:
Worked With: Liz Metzger, Dilan Wijesinghe, Meg Sindelar, Marno Nel, Katie Hughes, Ava Zahedi , Rintaroh Shima, Nicolas Morales