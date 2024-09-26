class GoalBasedReflexAgent:
   def __init__(self, goals):
       self.internal_model = {'history': [], 'current_state': {}}
       self.goals = goals


   def perceive(self, current_state):

       self.internal_model['history'].append(current_state)
       self.internal_model['current_state'] = current_state


   def decide_action(self):

       current_state = self.internal_model['current_state']
       if 'cleanliness' in self.goals and current_state['cleanliness'] == 'dirty':
           return 'clean'
       elif 'avoid_obstacle' in self.goals and current_state['obstacle']:
           return 'avoid_obstacle'
       elif 'wait' in self.goals and current_state['occupied']:
           return 'wait'
       elif 'move_to_next_room' in self.goals:
           return 'move_to_next_room'
       else:
           return 'no_action'


   def perform_action(self, decided_action):

       print(f"Performing action: {decided_action}")



   def display_history(self):

       print("History of Room States:")
       for state in self.internal_model['history']:
           print(state)




def user_interface_goal_based_reflex_agent():
   goals = input("Enter goals (comma-separated for e.g: cleanliness,avoid_obstacle,wait): ").split(',')
   agent = GoalBasedReflexAgent(goals)


   while True:
       cleanliness = input("Is the room dirty? (clean/dirty): ")
       obstacle = input("Is there an obstacle? (yes/no): ")
       occupied = input("Is the room occupied? (yes/no): ")


       current_state = {'cleanliness': cleanliness, 'obstacle': obstacle.lower() == 'yes', 'occupied': occupied.lower() == 'yes'}
       agent.perceive(current_state)


       decided_action = agent.decide_action()
       agent.perform_action(decided_action)


       agent.display_history()


       user_input = input("Do you want to continue? (yes/no): ")
       if user_input.lower() != 'yes':
           break

user_interface_goal_based_reflex_agent()
