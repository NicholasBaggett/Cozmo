import cozmo
import time
import random
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

yellow_color = cozmo.lights.Color(rgb=(255, 180, 0), name="yellow")
yellow_light = cozmo.lights.Light(yellow_color, yellow_color)
purple_color = cozmo.lights.Color(rgb=(169, 180, 0), name="yellow")
purple_light = cozmo.lights.Light(yellow_color, yellow_color)


def random_light(robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):
    rand = random.randrange(0, 5)

    cube.last_tapped_time = None

    if rand == 0:
        cube.set_lights(cozmo.lights.red_light)
    elif rand == 1:
        cube.set_lights(cozmo.lights.green_light)
    elif rand == 2:
        cube.set_lights(cozmo.lights.white_light)
    elif rand == 3:
        cube.set_lights(cozmo.lights.blue_light)
    elif rand == 4:
        cube.set_lights(purple_light)
    else:
        pass

    return rand


def light_show(robot: cozmo.robot.Robot):
    count = 0
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    cube_cooldown = 1.5
    cube1_timer = cube_cooldown
    cube2_timer = cube_cooldown
    cube3_timer = cube_cooldown
    speed = 0.1

    is_not_pushed = True
    is_counting_1 = False
    is_counting_2 = False
    is_counting_3 = False

    while is_not_pushed:
        if cube1_timer == 1.5:
            number1 = random_light(robot, cube1)
        elif cube1_timer <= 0:
            cube1_timer = 1.5
            number1 = random_light(robot, cube1)
            is_counting_1 = False

        if cube2_timer == 1.5:
            number2 = random_light(robot, cube2)
        elif cube2_timer <= 0:
            cube2_timer = 1.5
            number2 = random_light(robot, cube2)
            is_counting_2 = False

        if cube3_timer == 1.5:
            number3 = random_light(robot, cube3)
        elif cube3_timer <= 0:
            cube3_timer = 1.5
            number3 = random_light(robot, cube3)
            is_counting_3 = False

        time.sleep(speed)

        if cube1_timer == 1.5:
            if cube1.last_tapped_time is not None:
                count += 1
                cube1.set_lights_off()
                is_counting_1 = True
                if number1 == 0:
                    is_not_pushed = False

        if cube2_timer == 1.5:
            if cube2.last_tapped_time is not None:
                count += 1
                cube2.set_lights_off()
                is_counting_2 = False
                if number2 == 0:
                    is_not_pushed = False

        if cube3_timer == 1.5:
            if cube3.last_tapped_time is not None:
                count += 1
                cube2.set_lights_off()
                is_counting_3 = False
                if number3 == 0:
                    is_not_pushed = False

        if is_counting_1:
            cube1_timer -= speed
        if is_counting_2:
            cube2_timer -= speed
        if is_counting_3:
            cube3_timer -= speed

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
