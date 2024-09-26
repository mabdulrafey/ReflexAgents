
# Room-Cleaning Reflex Agents

## Overview
This project demonstrates two types of reflex agents: **Goal-Based Reflex Agent** and **Simple Reflex Agent**. These agents interact with a simulated environment where they perceive the state of a room and take actions based on the state conditions like cleanliness, obstacles, and room occupancy.

The **Goal-Based Reflex Agent** makes decisions based on predefined goals, while the **Simple Reflex Agent** responds directly to the environment without consideration of any goals.

## Project Structure
- **GoalBasedReflexAgent**: An agent that keeps track of the room state and its history, making decisions based on predefined goals (cleanliness, avoiding obstacles, waiting, moving to the next room).
- **SimpleReflexAgent**: A simpler agent that takes immediate actions based on room state without using goals or history.
- **User Interface**: Interactive user inputs to simulate different room conditions for the agents.

## Features
- **Perception**: Agents perceive the current state of the room based on user input.
- **Decision Making**: The goal-based agent makes decisions based on predefined goals like cleanliness, avoiding obstacles, and occupancy. The simple agent makes decisions based solely on current conditions.
- **Action Execution**: The agents perform actions like cleaning the room, avoiding obstacles, or waiting if the room is occupied.

## How to Run the Project
1. Clone this repository:

