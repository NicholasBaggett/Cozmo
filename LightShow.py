import cozmo
import time
import random
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


def random_light(robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):
    rand = random.randrange(0, 4)

    cube.last_tapped_time = None

    if rand == 0:
        cube.set_lights(cozmo.lights.red_light)
    elif rand == 1:
        cube.set_lights(cozmo.lights.green_light)
    elif rand == 2:
        cube.set_lights(cozmo.lights.white_light)
    elif rand == 3:
        cube.set_lights(cozmo.lights.blue_light)
    else:
        pass

    return rand


def light_show(robot: cozmo.robot.Robot):
    count = 0
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    is_not_pushed = True

    while is_not_pushed:
        number1 = random_light(robot, cube1)
        number2 = random_light(robot, cube2)
        number3 = random_light(robot, cube3)
        time.sleep(0.1)

        if cube1.last_tapped_time is not None:
            count += 1
            if number1 == 0:
                is_not_pushed = False
        if cube2.last_tapped_time is not None:
            count += 1
            if number2 == 0:
                is_not_pushed = False
        if cube3.last_tapped_time is not None:
            count += 1
            if number3 == 0:
                is_not_pushed = False

    cube1.set_lights_off()
    cube2.set_lights_off()
    cube3.set_lights_off()

    robot_message1 = "Good Job!"
    robot_message2 = "Better Luck Next Time"
    robot_message3 = "Oof"

    if count <= 4:
        robot.say_text("Your score was " + str(count) + " " + robot_message1)
    elif count <= 8:
        robot.say_text("Your score was " + str(count) + " " + robot_message2)
    elif count > 8:
        robot.say_text("Your score was " + str(count) + " " + robot_message3)
    else:
        print("Error")


cozmo.run_program(light_show)
