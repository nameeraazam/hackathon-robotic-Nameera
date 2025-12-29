# AI and Machine Learning for Humanoids

The "brain" of a modern humanoid is shifting from hard-coded control theory to data-driven AI.

## The Traditional Stack vs. The AI Stack
- **Traditional:**
    1.  *Perception:* "I see a box at (x,y,z)."
    2.  *Planning:* "Plan a path to (x,y,z)."
    3.  *Control:* "Move joints to follow the path."
- **AI / End-to-End:**
    - Input: Camera pixels + Joint angles.
    - Neural Network (Policy).
    - Output: Motor torques.
    *Benefit:* The robot learns to handle noise and slip naturally, just like a human learns to walk on ice.

## Key Techniques
### 1. Reinforcement Learning (RL)
The robot treats walking like a game.
- **Reward Function:** +1 for moving forward, -10 for falling, -0.1 for using too much energy.
- Over millions of simulated steps, it discovers efficient gaits that no human could hand-code.

### 2. Sim-to-Real (Sim2Real) Transfer
Training a robot in the real world is slow and dangerous. We train in simulation (NVIDIA Isaac Sim, MuJoCo).
- **Domain Randomization:** In sim, we vary friction, robot weight, and lighting wildly. The real world just looks like "another variation" to the neural net.

### 3. Imitation Learning & Teleoperation
Instead of starting from scratch, the robot watches a human.
- **Teleoperation:** A human wears a VR headset and gloves to control the robot (like the movie *Avatar*).
- **Behavior Cloning:** The AI learns to copy the human's motions. This is crucial for complex tasks like folding laundry or making coffee.

### 4. Vision-Language Models (VLMs)
Giving the robot "Common Sense."
- Integrating models like GPT-4o or Gemini allowing us to say: "I spilled my drink."
- The robot understands:
    1.  Spilled drink = needs cleaning.
    2.  Locate sponge.
    3.  Wipe surface.