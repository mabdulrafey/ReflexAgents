internal_model = {'history': [], 'current_state': {}}

def perceive(room_state, internal_model):
    internal_model['history'].append(room_state)
    internal_model['current_state'] = room_state

def decide_action(internal_model):
    current_state = internal_model['current_state']
    history = internal_model['history']

    if current_state['occupied']:
        return 'wait'
    elif current_state['obstacle']:
        return 'avoid_obstacle'
    elif current_state['cleanliness'] == 'dirty':
        return 'clean'
    elif len(history) > 1 and history[-2]['cleanliness'] == 'dirty':
        return 'move_to_next_room'
    else:
        return 'wait'

def perform_action(action, internal_model):
    current_state = internal_model['current_state']

    if action == 'clean':
        print("Cleaning the room.")
    elif action == 'avoid_obstacle':
        print("Avoiding the obstacle.")
    elif action == 'wait':
        print("Waiting for the room to be unoccupied.")
    elif action == 'move_to_next_room':
        print("Moving to the next room.")


cleanliness_1 = input("Is the room 1 clean or dirty? (clean/dirty): ")
obstacle_1 = input("Is there an obstacle in room 1? (True/False): ")
occupied_1 = input("Is room 1 occupied? (True/False): ")

room_state_1 = {'cleanliness': cleanliness_1, 'obstacle': obstacle_1.lower() == 'true', 'occupied': occupied_1.lower() == 'true'}


perceive(room_state_1, internal_model)
action_1 = decide_action(internal_model)
perform_action(action_1, internal_model)


cleanliness_2 = input("Is the room 2 clean or dirty? (clean/dirty): ")
obstacle_2 = input("Is there an obstacle in room 2? (True/False): ")
occupied_2 = input("Is room 2 occupied? (True/False): ")

room_state_2 = {'cleanliness': cleanliness_2, 'obstacle': obstacle_2.lower() == 'true', 'occupied': occupied_2.lower() == 'true'}


perceive(room_state_2, internal_model)
action_2 = decide_action(internal_model)
perform_action(action_2, internal_model)
