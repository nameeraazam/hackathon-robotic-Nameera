# Key Components of Humanoid Robots

Building a humanoid is a systems engineering challenge. It requires tight coupling between hardware and software.

## 1. Perception (Sensors)
Sensors are the robot's window to the world.
### Exteroceptive (External World)
- **Cameras (RGB-D):** The primary sensor. Depth (D) is crucial for understanding 3D space.
- **LiDAR:** Uses laser pulses to create precise 3D maps (Point Clouds).
- **Microphones:** For voice commands and sound localization.
### Proprioceptive (Internal State)
- **IMU (Inertial Measurement Unit):** The "inner ear." Measures acceleration and rotation. Essential for balance.
- **Encoders:** Measure the precise angle of every joint.
- **Force/Torque Sensors:** Located in the feet (to detect ground contact) and wrists (to feel manipulation forces).

## 2. Actuation (Muscles)
Actuators convert energy into motion.
- **Electric Motors:**
    - *High Gear Ratio:* Precise but stiff (e.g., ASIMO). Hard to interact with safely.
    - *Quasi-Direct Drive (QDD):* Low gear ratio. "Back-drivable" (you can push the limb and it moves). Used in modern quadrupeds and humanoids like Tesla Optimus for safety and efficiency.
- **Hydraulics:** Used in Boston Dynamics' Atlas. Incredible power density (can do backflips) but leaky, loud, and inefficient.
- **Series Elastic Actuators (SEA):** A spring is placed between the motor and the load. Absorbs shocks and allows for force control.

## 3. Computation (The Brain)
- **Low-Level Control:** Microcontrollers (running at 1000Hz+) that control currents to motors. Real-time constraints are strict (hard real-time).
- **High-Level Planning:** Powerful GPUs (e.g., NVIDIA Jetson Orin) processing vision, path planning, and AI models. Often runs at lower frequencies (30Hz - 100Hz).

## 4. Power & Structure
- **Battery:** The bottleneck. Humanoids are energy-hungry. Operating times are typically 1-4 hours.
- **Structure:** Carbon fiber, aluminum, and magnesium alloys to minimize weight (inertia) while maintaining stiffness.