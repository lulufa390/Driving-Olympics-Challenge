import math

def calc_centered_reward(distance_from_center, track_width):
    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.4 * track_width
    marker_4 = 0.5 * track_width
    reward = 0

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.9
    elif distance_from_center <= marker_3:
        reward = 0.7
    elif distance_from_center <= marker_4:
        reward = 0.4
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return reward


def calc_finished_reward(steps, progress):
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS1 = 700
    TOTAL_NUM_STEPS2 = 600
    TOTAL_NUM_STEPS3 = 500
    TOTAL_NUM_STEPS4 = 400
    CHECK_STEP_SIZE = 10  # As it is 10FPS camera

    # Initialize the reward with typical value
    reward = 0.0

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % CHECK_STEP_SIZE) == 0 and progress > (steps / TOTAL_NUM_STEPS1) * 100:
        reward += 10.0
    elif (steps % CHECK_STEP_SIZE) == 0 and progress > (steps / TOTAL_NUM_STEPS2) * 100:
        reward += 20.0
    elif (steps % CHECK_STEP_SIZE) == 0 and progress > (steps / TOTAL_NUM_STEPS3) * 100:
        reward += 30.0
    elif (steps % CHECK_STEP_SIZE) == 0 and progress > (steps / TOTAL_NUM_STEPS4) * 100:
        reward += 40.0

    return reward

def getNextNextWaypoint(waypoints, closest_waypoints):
    nxt_idx = closest_waypoints[1]
    nxt_nxt_idx = nxt_idx + 1

    if nxt_nxt_idx == len(waypoints):
        nxt_nxt_idx = 1
    return waypoints[nxt_nxt_idx]

def calc_direction_reward_coe(waypoints, closest_waypoints, heading, steering, is_left_of_center, speed):
    DIRECTION_THRESHOLD1 = 30
    DIRECTION_THRESHOLD2 = 20
    DIRECTION_THRESHOLD3 = 10

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    nxt_nxt_point = getNextNextWaypoint(waypoints, closest_waypoints)

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    next_direction = math.degrees(math.atan2(nxt_nxt_point[1] - next_point[1], nxt_nxt_point[0] - next_point[0]))

    turning_dgree = next_direction - track_direction
    if track_direction < 0 and next_direction < 0:
        pass
    elif track_direction < 0 and next_direction > 0:
        if turning_dgree > 180:
            turning_dgree = 360 - turning_dgree
    elif track_direction > 0 and next_direction < 0:
        if turning_dgree < -180:
            turning_dgree = -360 - turning_dgree
    elif track_direction > 0 and next_direction > 0:
        pass
    else:
        pass

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    headingCoe = 1
    if direction_diff > DIRECTION_THRESHOLD3 and direction_diff < DIRECTION_THRESHOLD2:
        headingCoe = 0.8
    elif direction_diff >= DIRECTION_THRESHOLD2 and direction_diff < DIRECTION_THRESHOLD1:
        headingCoe = 0.4
    elif direction_diff >= DIRECTION_THRESHOLD1:
        headingCoe = 0.1
    
    turningCoe = 1

    if turning_dgree > 2:
        # trun left
        if steering < 0:
            turningCoe = 0.5
        if not is_left_of_center and steering < 0:
            # right of track and turning right
            turningCoe = 0.2
    elif turning_dgree < -2:
        # turn right
        if steering > 0:
            turningCoe = 0.5
        if is_left_of_center and steering > 0:
            turningCoe = 0.2
    else:
        # go straight
        if steering != 0:
            turningCoe = 0.5

    speedCoe = 1
    if abs(turning_dgree) > 2:
        if speed >= 3:
            speedCoe = 0.5
    else:
        if speed < 3:
            speedCoe = 0.5
    print("track turning: " + str(turning_dgree) + " direction diff: " + str(direction_diff) + " steering: " + str(steering) + " left of track: " + str(is_left_of_center) + " speed: " + str(speed))
    return speedCoe * turningCoe * headingCoe

def calc_on_track_reward_coe(all_wheels_on_track):
    if not all_wheels_on_track:
        return 0.5
    return 1.0


def calc_steering_reward_coe(steering):
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        return 0.8
    return 1.0

def cal_speed_reward_coe(steering, speed):
    speed_threshold = 3
    if steering != 0:
        if speed > speed_threshold:
            return 0.5
    return 1

def reward_function(params):
    '''
    Penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])  # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']

    reward = 0.0
    reward += calc_centered_reward(distance_from_center, track_width)
    reward += calc_finished_reward(steps, progress)

    reward *= calc_direction_reward_coe(waypoints, closest_waypoints, heading, steering, is_left_of_center, speed)
    reward *= calc_on_track_reward_coe(all_wheels_on_track)
    # reward *= calc_steering_reward_coe(steering)

    return float(reward)
