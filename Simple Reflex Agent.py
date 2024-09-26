class SimpleReflexAgent:
   def perceive(self, cleanliness, obstacle, occupied):
       return {'cleanliness': cleanliness, 'obstacle': obstacle, 'occupied': occupied}

   def decide_actions(self, perceived_state):
       actions = []
       if perceived_state['cleanliness']:
           actions.append('clean')
       if perceived_state['obstacle']:
           actions.append('avoid_obstacle')
       if perceived_state['occupied']:
           actions.append('wait')
       return actions

   def perform_actions(self, actions):
       for action in actions:
           if action == 'clean':
               print("Cleaning the room.")
           elif action == 'avoid_obstacle':
               print("Avoiding an obstacle.")
           elif action == 'wait':
               print("Waiting for the room to be unoccupied.")


# Interface
def main():
   agent = SimpleReflexAgent()


   cleanliness = input("Is the room dirty? (yes/no): ")
   obstacle = input("Is there an obstacle? (yes/no): ")
   occupied = input("Is the room occupied? (yes/no): ")


   try:
       perceived_state = agent.perceive(cleanliness.lower() == 'yes', obstacle.lower() == 'yes', occupied.lower() == 'yes')
   except:
       print("Invalid input. Please enter 'yes' or 'no'.")
       return


   actions = agent.decide_actions(perceived_state)
   agent.perform_actions(actions)


if __name__ == "__main__":
   main()
