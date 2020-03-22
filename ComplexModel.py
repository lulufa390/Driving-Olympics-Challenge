import math

def calc_centered_reward(distance_from_center, track_width):
    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    reward = 0
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.9
    elif distance_from_center <= marker_3:
        reward = 0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    return reward
    
def calc_finished_reward(steps, progress):
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 600
    CHECK_STEP_SIZE = 10 # As it is 10FPS camera
    
    # Initialize the reward with typical value 
    reward = 0.0

    # Give additional reward if the car pass every 100 steps faster than expected 
    if (steps % CHECK_STEP_SIZE) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    return reward
    
def calc_direction_reward_coe(waypoints, closest_waypoints, heading):
    DIRECTION_THRESHOLD = 15.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    if direction_diff > DIRECTION_THRESHOLD:
        return 0.8

    return 1.0
    
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

def reward_function(params):
    '''
    Penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
        
    reward = 0.0
    reward += calc_centered_reward(distance_from_center, track_width)
    reward += calc_finished_reward(steps, progress)
    
    reward *= calc_direction_reward_coe(waypoints, closest_waypoints, heading)
    reward *= calc_on_track_reward_coe(all_wheels_on_track)
    reward *= calc_steering_reward_coe(steering)

    return float(reward)
