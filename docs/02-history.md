# History of Humanoid Robotics

The quest to create artificial life is as old as engineering itself. The modern history of humanoid robotics is a journey from stiff, pre-programmed machines to dynamic, learning-based agents.

## Early Automata (Pre-20th Century)
Long before electronics, artisans built **automata**—mechanical dolls moved by cams and clockwork.
- **Karakuri puppets (Japan)**: Tea-serving dolls.
- **Jaquet-Droz automata (Europe)**: The Writer, The Draftsman, and The Musician.
*Key Takeaway:* These demonstrated that mechanical complexity could mimic life, but they lacked autonomy.

## The Dawn of Modern Robotics (1970s - 1980s)
- **WABOT-1 (1973):** Developed by Waseda University, often cited as the first full-scale humanoid. It could walk (very slowly), grip objects, and speak.
- **Static Walking:** Early robots used **static stability**. The Center of Mass (CoM) was always kept strictly within the polygon of support (the feet). If the robot froze mid-step, it wouldn't fall. This resulted in a slow, shuffling gait.

## The Honda Era & ZMP (1986 - 2000s)
Honda initiated a secret project to build a walking robot.
- **E-Series:** Experimental legs.
- **P-Series (P2, P3):** The first self-contained humanoids.
- **ASIMO (2000):** The icon of humanoid robotics. ASIMO introduced **Zero Moment Point (ZMP)** control, allowing for "dynamic walking." It could run, hop, and climb stairs.
*Limitation:* ASIMO was still largely position-controlled and stiff. It couldn't handle significant external disturbances (like being pushed hard).

## The DARPA Robotics Challenge (2012 - 2015)
Triggered by the Fukushima nuclear disaster, DARPA challenged teams to build robots that could drive cars, open doors, and turn valves.
- **The Result:** Most robots were slow and fell over frequently. It highlighted the gap between "demo" robotics and "disaster" robotics.
- **Atlas (Boston Dynamics):** Emerged as a leading platform, transitioning from hydraulic control to pure electric (later versions) and demonstrating incredible balance.

## The Modern Era: Dynamic & Learning-Based (2015 - Present)
- **Boston Dynamics Atlas:** Showcased backflips and parkour. It uses **Model Predictive Control (MPC)** and hydraulic actuation for high power-to-weight ratio.
- **The Rise of Learning:** Recently, Reinforcement Learning (RL) has moved from simulation to reality ("Sim2Real"). Robots learn to walk by trial and error in physics simulators (like Isaac Sim) and transfer that "neural network brain" to the real robot.
- **Commercial Humanoids:** Tesla Optimus, Figure, Agility Robotics (Digit), and Unitree are racing to deploy general-purpose labor robots in factories.

## Evolution of Control
1.  **Scripted:** "Move joint A to 30 degrees."
2.  **Model-Based (ZMP):** "Keep the center of pressure under the foot."
3.  **Dynamic/MPC:** "Plan forces to balance while moving fast."
4.  **Learning-Based:** "Reward the robot for staying upright; let it figure out the motor commands."