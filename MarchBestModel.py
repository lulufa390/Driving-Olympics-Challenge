import math

WAY_POINTS = [
    (4.503267526626587, 0.18162955343723297),
    (4.351881504058838, 0.18078652024269104),
    (4.2004945278167725, 0.17995046079158783), 
    (4.049107313156128, 0.17926649749279022), 
    (3.897720456123352, 0.17851226031780243), 
    (3.7463330030441284, 0.1778719425201416), 
    (3.594948410987854, 0.17678216099739075), 
    (3.443572998046875, 0.1747940480709076), 
    (3.2921979427337646, 0.17274996638298035), 
    (3.1408510208129883, 0.16922733187675476), 
    (2.989630937576294, 0.1621338129043579), 
    (2.8387175798416138, 0.1501728594303131), 
    (2.6882164478302, 0.13382109999656677), 
    (2.5378719568252563, 0.11607888340950012), 
    (2.3876891136169434, 0.09693804383277893), 
    (2.2398264408111572, 0.06467685103416443), 
    (2.0999500155448914, 0.007101342082023621), 
    (1.9749209880828857, -0.07807904481887817), 
    (1.8698190450668333, -0.18691920489072836), 
    (1.7844924926757812, -0.3118980135768652), 
    (1.716057002544403, -0.44688156247138977), 
    (1.6662879586219788, -0.5898111313581467), 
    (1.6331714987754822, -0.7375103533267975), 
    (1.6094949841499329, -0.8870322704315186), 
    (1.589421033859253, -1.0370839834213261), 
    (1.57127046585083, -1.1873815059661865), 
    (1.5570560097694397, -1.3380975127220154), 
    (1.548179030418396, -1.4892249703407288), 
    (1.5471194386482239, -1.640607476234436), 
    (1.5627354383468628, -1.7911434769630432), 
    (1.6028565168380737, -1.9370014667510986), 
    (1.670343041419983, -2.0723835825920105), 
    (1.7655785083770752, -2.1899534463882446), 
    (1.8833510279655457, -2.2848815321922302), 
    (2.0170934796333313, -2.355597496032715), 
    (2.1611530780792236, -2.4020034670829773), 
    (2.3102940320968637, -2.4277615547180176), 
    (2.4611040353775024, -2.4408985376358032), 
    (2.612364530563354, -2.4471455216407776), 
    (2.763711929321289, -2.450609564781189), 
    (2.915081501007079, -2.44837349653244), 
    (3.065185070037842, -2.4293185472488403), 
    (3.20912504196167, -2.3827560544013977), 
    (3.3394370079040527, -2.305922508239746), 
    (3.4519286155700684, -2.2047539949417114), 
    (3.550142049789429, -2.0895690321922293), 
    (3.6425764560699467, -1.969667494297027), 
    (3.738682985305786, -1.8527005314826965), 
    (3.8468880653381348, -1.7469245195388794), 
    (3.9716144800186157, -1.6612989902496338), 
    (4.110928416252136, -1.6022544503211975), 
    (4.2592151165008545, -1.572363018989563), 
    (4.410504102706909, -1.5731670260429382), 
    (4.55877161026001, -1.6032885313034058), 
    (4.697690010070801, -1.663228988647461), 
    (4.8225414752960205, -1.7486644387245178), 
    (4.931865453720093, -1.8533075451850891), 
    (5.0285844802856445, -1.9697644710540771), 
    (5.120867013931274, -2.0897814631462097), 
    (5.219902992248535, -2.204228460788727), 
    (5.33541202545166, -2.301969051361084), 
    (5.469343900680542, -2.372236490249634), 
    (5.61554741859436, -2.4109965562820435), 
    (5.766258478164673, -2.424979031085968), 
    (5.91764235496521, -2.4268020391464233), 
    (6.0689918994903564, -2.423553466796875), 
    (6.220280647277832, -2.4180500507354736), 
    (6.371399164199829, -2.4089885354042053), 
    (6.522143125534058, -2.395046055316925), 
    (6.671403408050537, -2.369912028312683), 
    (6.815991163253784, -2.325380504131317), 
    (6.948606014251709, -2.252537965774536), 
    (7.058701992034912, -2.1489095091819763), 
    (7.136504650115967, -2.019335448741913), 
    (7.180192470550537, -1.8744999766349792), 
    (7.198908090591431, -1.7242890000343323), 
    (7.212253093719482, -1.573472023010254), 
    (7.241801500320435, -1.4250845313072205), 
    (7.299700021743774, -1.2853389978408813), 
    (7.387287378311157, -1.1619877219200134), 
    (7.497623920440674, -1.0584836602210999), 
    (7.623191833496094, -0.9740366339683533), 
    (7.759784460067748, -0.9088748842477804), 
    (7.902036190032959, -0.8570685535669327), 
    (8.045245409011843, -0.8079827874898904), 
    (8.183710098266602, -0.7468995600938797), 
    (8.309013843536377, -0.6621100902557373), 
    (8.411710977554321, -0.551131941378115), 
    (8.487078428268433, -0.42001823335886), 
    (8.53602123260498, -0.2767772451043129), 
    (8.566099166870117, -0.1284301243722452), 
    (8.586333751678467, 0.02160128578543663), 
    (8.60134220123291, 0.1722424551844597), 
    (8.612728118896484, 0.3232016563415503), 
    (8.621081829071045, 0.4743591994047165), 
    (8.626728057861328, 0.6256424188613909), 
    (8.630242347717285, 0.7769904434680939), 
    (8.632472515106201, 0.9283629357814777), 
    (8.633815288543701, 1.0797455310821533), 
    (8.635576248168945, 1.2311235070228577), 
    (8.638143062591553, 1.3824909925460815), 
    (8.640675067901611, 1.5338580012321472), 
    (8.642788887023926, 1.6852355003356934), 
    (8.64233684539795, 1.836618959903717), 
    (8.636707305908203, 1.9879145622253418), 
    (8.622458457946777, 2.138630509376526), 
    (8.59438180923462, 2.287396550178528), 
    (8.54852294921875, 2.431663990020752), 
    (8.482813835144043, 2.5680400133132935), 
    (8.397138833999634, 2.6927855014801025), 
    (8.29281234741211, 2.8023595809936523), 
    (8.169153213500977, 2.8895115852355957), 
    (8.031305313110352, 2.951951026916504), 
    (7.885217666625977, 2.9914629459381104), 
    (7.735015869140625, 3.0097254514694214), 
    (7.583784580230713, 3.0038909912109375), 
    (7.434887409210205, 2.9766730070114136), 
    (7.290818452835083, 2.930327534675598), 
    (7.155501842498779, 2.8626550436019897), 
    (7.0358195304870605, 2.7701019048690796), 
    (6.937677621841431, 2.6548640727996826), 
    (6.863694190979004, 2.5228474140167236), 
    (6.813917636871338, 2.379943609237671), 
    (6.785369396209717, 2.2313055992126465), 
    (6.771535873413086, 2.080568552017212), 
    (6.767365455627441, 1.9292324781417847), 
    (6.768065452575684, 1.7778465151786804), 
    (6.771385908126831, 1.6264939904212952), 
    (6.7752039432525635, 1.4751539826393127), 
    (6.776884078979492, 1.323775053024292), 
    (6.773577928543091, 1.1724279522895813), 
    (6.7624146938323975, 1.0214507281780243), 
    (6.739289283752441, 0.8718497455120087), 
    (6.698439121246338, 0.7260171473026276), 
    (6.6353583335876465, 0.5883599668741226), 
    (6.548041105270386, 0.46465345472097397), 
    (6.437201976776123, 0.36163509637117386), 
    (6.307543516159058, 0.28358694911003113), 
    (6.165451526641846, 0.2315782606601715), 
    (6.016722679138184, 0.20362405478954315), 
    (5.865716457366943, 0.1930065006017685), 
    (5.71434211730957, 0.19065430760383606), 
    (5.562954425811768, 0.1899629533290863), 
    (5.411574602127075, 0.18836215138435364), 
    (5.260190486907959, 0.1871441900730133), 
    (5.108808517456055, 0.1857307404279709), 
    (4.9574244022369385, 0.18456879258155823), 
    (4.8060386180877686, 0.18362654745578766), 
    (4.8060386180877686, 0.18362654745578766), 
    (4.654654026031494, 0.18250980973243713), 
    (4.503267526626587, 0.18162955343723297)
    ]

def find_waypoint_index(current_point):
    eps = 1e-8
    for i in range(len(WAY_POINTS)): 
        point = WAY_POINTS[i]
        if abs(current_point[0] - point[0]) < eps and abs(current_point[1] - point[1]) < eps:
            return i
    return -1

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
        reward = 0.7
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return reward

def calc_speed_reward(closest_waypoints, speed):
    breakpoints = [0, 17, 30, 48, 85, 120, 160, 200, 240, len(WAY_POINTS)]
    idx = find_waypoint_index(WAY_POINTS[closest_waypoints[1]])
    for i in range(len(breakpoints)):
        if idx >= breakpoints[i] and idx < breakpoints[i + 1]:
            # i % 2 == 0 means should be high-speed
            if bool(i % 2 == 0) != bool(speed > 2.5):
                return 0.0
            else:
                return 5.0


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
        return 0.3
    return 1.0


def calc_steering_reward_coe(steering):
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

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
    steering = abs(params['steering_angle'])  # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']

    reward = 0.0
    reward += calc_centered_reward(distance_from_center, track_width)
    reward += calc_finished_reward(steps, progress)
    reward += calc_speed_reward(closest_waypoints, speed)

    reward *= calc_direction_reward_coe(waypoints, closest_waypoints, heading)
    reward *= calc_on_track_reward_coe(all_wheels_on_track)
    reward *= calc_steering_reward_coe(steering)

    return float(reward)
