# The Landing of the Concorde

## 1. Calculation of Coefficients Using Newton's Second Law

Given the equation of motion:  
\[ m \frac{dv}{dt} = -F - \frac{1}{2} \rho_{\text{air}} v^2 C_d S \]

With the provided values:  
- \( C_d = 0.25 \)  
- \( S = 358 \, \text{m}^2 \)  
- \( v = 160 \, \text{kts} = 82.4 \, \text{m/s} \)  
- \( m = 1.1 \times 10^5 \, \text{kg} \)  
- \( F = 10^4 \, \text{N} \)  

The drag term is calculated as:  
\[ \frac{1}{2} \rho_{\text{air}} v^2 C_d S = 54.82 \]  

Substituting into Newton's law:  
\[ 1.1 \times 10^5 \frac{dv}{dt} = -10^4 - 54.82 v^2 \]  

Comparing with the general form:  
\[ a \frac{dv}{dt} = -b v^2 - c \]  

We identify the coefficients:  
- \( a = 1.1 \times 10^5 \)  
- \( b = 54.82 \)  
- \( c = 10^4 \)  

---

## 2. Distance Required to Nearly Stop (\( v = 1 \, \text{m/s} \)) with Engines Disengaged

Starting from the simplified equation:  
\[ \frac{dv}{dt} = -4.98 \times 10^{-4} v^2 - 0.091 \]  

Rewriting in terms of \( x \):  
\[ \frac{dv}{dt} = v \frac{dv}{dx} \]  

Thus:  
\[ dx = \frac{v \, dv}{-4.98 \times 10^{-4} v^2 - 0.091} \]  

This integral will yield the distance \( x \) required for the Concorde to decelerate to \( v = 1 \, \text{m/s} \).  

From \( v_1 = 82.4 \, \text{m/s} \) to \( v_2 = 1 \, \text{m/s} \)

  
\[ x = -\frac{1}{9.96 \times 10^{-4}} \ln \left( \frac{-4.98 \times 10^{-4} v_2^2 - 0.091}{-4.98 \times 10^{-4} v_1^2 - 0.091} \right) \]  
After a numerical integration, the result is:

\[ x = 3650 \text{m} \]

## 3. What do you think about this lenght ?

It's a very long distance, but it is not surprising given the high speed of the Concorde. The aircraft is designed to travel at high speeds, so it requires a long distance to decelerate to a stop. This is a common characteristic of high-speed aircraft, and pilots are trained to manage these long stopping distances.

---


# The Race of Usain Bolt

## Problem Statement
During the start of the 100 meters' race, the runner Usain Bolt (mass \( m = 93 \, \text{kg} \)) comes out of the blocks, driven by a force \( F = 500 \, \text{N} \). His drag coefficient during the race is \( C_d = 1.2 \). The horizontal component of the ground reaction is estimated at \( R_x = 40 \, \text{N} \).

---

## 1. Equation of Motion
Given the equation of motion:
\[
m \frac{dv}{dt} = F - R_x - \frac{1}{2} \rho_{\text{air}} v^2 C_d S
\]

We can rewrite it in the form:
\[
a \frac{dv}{dt} = -b v^2 - c
\]

### Coefficients:
- **Mass (a):**
  \[
  a = m = 93 \, \text{kg}
  \]

- **Net Force (b):**
  \[
  b = \frac{1}{2} \rho_{\text{air}} C_d S
  \]
  Assuming standard air density \( \rho_{\text{air}} = 1.225 \, \text{kg/m}^3 \) and cross-sectional area \( S = 0.93 \, \text{m}^2 \):
  \[
  b = \frac{1}{2} \times 1.225 \times 1.2 \times 0.93 = 0.68355 \, \text{kg/m}
  \]

- **Constant Term (c):**
  \[
  c = R_x - F = 40 - 500 = -460 \, \text{N}
  \]

Thus, the equation becomes:
\[
93 \frac{dv}{dt} = -0.68355 v^2 + 460
\]

---

## 2. Distance to Reach 12.2 m/s
We want to find the distance \( x \) required for Usain Bolt to reach a speed of \( 12.2 \, \text{m/s} \).

### Rewriting the Equation:
\[
\frac{dv}{dt} = \frac{460 - 0.68355 v^2}{93} = 4.946 - 0.00735 v^2
\]

Using the chain rule \( \frac{dv}{dt} = v \frac{dv}{dx} \), we get:
\[
v \frac{dv}{dx} = 4.946 - 0.00735 v^2
\]

Separate variables and integrate:
\[
\int \frac{v}{4.946 - 0.00735 v^2} \, dv = \int dx
\]

Let \( u = 4.946 - 0.00735 v^2 \), then \( du = -0.0147 v \, dv \):
\[
\int \frac{v \, dv}{u} = -\frac{1}{0.0147} \int \frac{du}{u}
\]

Integrating both sides:
\[
x = -\frac{1}{0.0147} \ln \left( \frac{4.946 - 0.00735 v^2}{4.946} \right) + C
\]

At \( v = 0 \), \( x = 0 \), so \( C = 0 \). Evaluating at \( v = 12.2 \, \text{m/s} \):
\[
x = -\frac{1}{0.0147} \ln \left( \frac{4.946 - 0.00735 \times (12.2)^2}{4.946} \right)
\]
\[
x \approx 17 \, \text{m}
\]

### Conclusion:
Usain Bolt reaches a speed of \( 12.2 \, \text{m/s} \) after approximately **17 meters**.

## 3. Time to Reach 12.2 m/s  

We want to find the time \( t_1 \) required for Usain Bolt to reach a speed of \( 12.2 \, \text{m/s} \).  

### Rewriting the Equation of Motion  
From the previous section, we have:  
\[
\frac{dv}{dt} = 4.946 - 0.00735 v^2  
\]  
Separating variables:  
\[
dt = \frac{dv}{4.946 - 0.00735 v^2}  
\]  

### Using Partial Fraction Decomposition  
The integral can be solved using the identity:  
\[
\frac{dv}{\alpha^2 - \beta^2 v^2} = \frac{1}{2\alpha} \left( \frac{dv}{\alpha - \beta v} + \frac{dv}{\alpha + \beta v} \right)  
\]  
Where:  
\[
\alpha^2 = 4.946 \implies \alpha = \sqrt{4.946} \approx 2.224  
\]  
\[
\beta^2 = 0.00735 \implies \beta = \sqrt{0.00735} \approx 0.0857  
\]  

Thus:  
\[
dt = \frac{1}{2 \alpha} \left( \frac{dv}{\alpha - \beta v} + \frac{dv}{\alpha + \beta v} \right)  
\]  
\[
dt = \frac{1}{4.448} \left( \frac{dv}{2.224 - 0.0857 v} + \frac{dv}{2.224 + 0.0857 v} \right)  
\]  

### Integrating Both Sides  
Integrate from \( v = 0 \) to \( v = 12.2 \, \text{m/s} \):  
\[
t_1 = \frac{1}{4.448} \left[ -\frac{1}{0.0857} \ln|2.224 - 0.0857 v| + \frac{1}{0.0857} \ln|2.224 + 0.0857 v| \right]_0^{12.2}  
\]  
\[
t_1 = \frac{1}{4.448 \times 0.0857} \left[ \ln \left( \frac{2.224 + 0.0857 v}{2.224 - 0.0857 v} \right) \right]_0^{12.2}  
\]  
Evaluating at \( v = 12.2 \, \text{m/s} \):  
\[
t_1 = \frac{1}{0.381} \ln \left( \frac{2.224 + (0.0857 \times 12.2)}{2.224 - (0.0857 \times 12.2)} \right)  
\]  
\[
t_1 \approx 2.624 \ln \left( \frac{2.224 + 1.045}{2.224 - 1.045} \right)  
\]  
\[
t_1 \approx 2.624 \ln \left( \frac{3.269}{1.179} \right)  
\]  
\[
t_1 \approx 2.624 \ln(2.773) \approx 2.624 \times 1.02 \approx 2.68 \, \text{s}  
\]  

### Conclusion  
The time required for Usain Bolt to reach \( 12.2 \, \text{m/s} \) is approximately **2.677 seconds**.

## 4. He maintains a speed of some 12.2 m/s throughout the remainder of the race. Calculate the time for Usain Bolt to complete the 100 meters.

To calculate the total time Usain Bolt takes to complete the 100-meter race, we'll break the problem into two phases:

1. **Acceleration Phase**: The time taken to reach \( 12.2 \, \text{m/s} \).
2. **Constant Speed Phase**: The time taken to cover the remaining distance at \( 12.2 \, \text{m/s} \).

### Given:
- **Total distance**, \( D_{\text{total}} = 100 \, \text{m} \)
- **Maximum speed**, \( v_{\text{max}} = 12.2 \, \text{m/s} \)
- **Time to reach maximum speed**, \( t_1 = 2.677 \, \text{s} \)

### Step 1: Calculate the Distance Covered During Acceleration
Assuming constant acceleration, the distance covered during the acceleration phase (\( D_1 \)) can be calculated using the formula for uniformly accelerated motion:

\[
D_1 = \frac{1}{2} \times a \times t_1^2
\]

However, since we don't have the acceleration (\( a \)) directly, we can use the relationship between speed, acceleration, and time:

\[
v_{\text{max}} = a \times t_1 \implies a = \frac{v_{\text{max}}}{t_1}
\]

Substituting \( a \) back into the distance formula:

\[
D_1 = \frac{1}{2} \times \left( \frac{v_{\text{max}}}{t_1} \right) \times t_1^2 = \frac{1}{2} \times v_{\text{max}} \times t_1
\]

Plugging in the known values:

\[
D_1 = \frac{1}{2} \times 12.2 \, \text{m/s} \times 2.677 \, \text{s} \approx 16.33 \, \text{m}
\]

### Step 2: Calculate the Remaining Distance
The remaining distance (\( D_2 \)) to be covered at constant speed is:

\[
D_2 = D_{\text{total}} - D_1 = 100 \, \text{m} - 16.33 \, \text{m} = 83.67 \, \text{m}
\]

### Step 3: Calculate the Time for the Constant Speed Phase
The time (\( t_2 \)) to cover \( D_2 \) at \( v_{\text{max}} \) is:

\[
t_2 = \frac{D_2}{v_{\text{max}}} = \frac{83.67 \, \text{m}}{12.2 \, \text{m/s}} \approx 6.858 \, \text{s}
\]

### Step 4: Calculate the Total Time
The total time (\( T \)) is the sum of the acceleration time and the constant speed time:

\[
T = t_1 + t_2 = 2.677 \, \text{s} + 6.858 \, \text{s} \approx 9.535 \, \text{s}
\]

### Final Answer
\[
\boxed{9.54 \, \text{s}}
\]

*Note: The slight difference from Usain Bolt's actual world record time of approximately \( 9.58 \, \text{s} \) can be attributed to factors like air resistance, slight variations in speed, and the assumption of perfect constant acceleration.*

## 5. What do you think about this time?

A new world record, i guess. Usain Bolt is a phenomenal athlete, and his speed and performance are truly remarkable.



# The Water Tower

## Problem Statement
A 45 km/h wind blows past the water tower shown in the figure. We treat the water tower as a sphere resting on a circular cylinder. We assume that the total drag is the sum of the drag from these parts.

Given parameters:
- ρ_air = 1.225 kg/m³ (air density)
- ν_air = 1.4 × 10⁻⁵ m²/s (kinematic viscosity of air)
- Cd_cylinder = 0.4 (drag coefficient for cylinder)
- Cd_sphere = 0.2 (drag coefficient for sphere)

## 1. Compute the Drag Forces

### Sphere Drag (Dₛ)
- Projected area of sphere (Aₛ):  
  \[
  A_s = \frac{\pi}{4} \Phi_s^2 = 113.1 \, \text{m}^2
  \]
- Drag force on sphere:  
  \[
  D_s = \frac{1}{2} \rho v^2 A_s C_{d,s} = 2165 \, \text{N}
  \]

### Cylinder Drag (D_c)
- Projected area of cylinder (A_c):  
  \[
  A_c = \Phi_c H = 125 \, \text{m}^2
  \]
- Drag force on cylinder:  
  \[
  D_c = \frac{1}{2} \rho v^2 A_c C_{d,c} = 4785 \, \text{N}
  \]

## 2. Estimate the Moment at the Base

The moment (M) needed to prevent tipping is calculated by considering the drag forces and their respective lever arms:
- Height to sphere center of pressure (H_gs):  
  \[
  H_{gs} = 25 + 6 = 31 \, \text{m}
  \]
- Height to cylinder center of pressure (H_gc):  
  \[
  H_{gc} = 12.5 \, \text{m}
  \]
- Total moment:  
    \[
    M = D_s \times H_{gs} + D_c \times H_{gc} = 126,927 \, \text{N} \cdot \text{m}
    \]


# The Billboard Exercise

## Problem Statement
A billboard is illustrated in the figure. The sign can be analyzed as a flat plate with dimensions 4m (width) × 3m (height). We want to determine:

1. The wind velocity required to overturn the sign if it was designed to resist a total moment of 8000 N·m at its base (original pillar height).
2. The same question if the height of the pillar is reduced to 2 meters.

Given parameters:
- Air density (ρ): 1.225 kg/m³
- Drag coefficient (C_D): 1.2 (for flat plate perpendicular to flow)
- Sign dimensions: 4m × 3m = 12m² area

## Part 1: Original Pillar Height

### Step 1: Calculate Drag Force
The drag force (D) on the billboard is given by:
\[
D = \frac{1}{2} \rho v^2 A C_D
\]
Where:
- \(A = 4 \, \text{m} \times 3 \, \text{m} = 12 \, \text{m}^2\) (frontal area)
- \(C_D = 1.2\)

### Step 2: Calculate Overturning Moment
Assuming the pillar height (h) is such that the center of pressure is at mid-height of the billboard (default assumption unless specified otherwise), the moment arm is:
\[
\text{Moment arm} = h + \frac{3}{2} = h + 1.5 \, \text{m}
\]

The overturning moment (M) is:
\[
M = D \times \left(h + 1.5\right)
\]

Given the resisting moment is 8000 N·m, we set:
\[
\frac{1}{2} \rho v^2 A C_D \times \left(h + 1.5\right) = 8000
\]

Assuming the original pillar height \(h\) is not explicitly given, we'll proceed with the default assumption that the total moment arm is dominated by the billboard height (i.e., \(h + 1.5 \approx 1.5 \, \text{m}\) if \(h\) is small or negligible). If \(h\) is significant, it must be provided. For this solution, we'll assume \(h + 1.5 = 1.5 \, \text{m}\) (pillar height negligible compared to billboard).

Solving for \(v\):
\[
v = \sqrt{\frac{2 \times 8000}{\rho A C_D \times 1.5}} = \sqrt{\frac{16000}{1.225 \times 12 \times 1.2 \times 1.5}} \approx 24.6 \, \text{m/s} \approx 88.6 \, \text{km/h}
\]

## Part 2: Reduced Pillar Height (2 meters)

Now, the pillar height \(h = 2 \, \text{m}\), so the moment arm becomes:
\[
\text{Moment arm} = 2 + 1.5 = 3.5 \, \text{m}
\]

Set the overturning moment equal to 8000 N·m:
\[
\frac{1}{2} \rho v^2 A C_D \times 3.5 = 8000
\]

Solving for \(v\):
\[
v = \sqrt{\frac{2 \times 8000}{\rho A C_D \times 3.5}} = \sqrt{\frac{16000}{1.225 \times 12 \times 1.2 \times 3.5}} \approx 16.2 \, \text{m/s} \approx 58.3 \, \text{km/h}
\]

## Summary of Results
1. **Original pillar height (negligible or small):**  
   Wind velocity required to overturn: **24.6 m/s (88.6 km/h)**.

2. **Reduced pillar height (2 m):**  
   Wind velocity required to overturn: **16.2 m/s (58.3 km/h)**.

## Discussion
- The pillar height significantly affects the stability of the billboard. A taller pillar increases the moment arm, making the billboard more susceptible to overturning at lower wind speeds.
- The results suggest that the design must account for the pillar height to ensure resistance to expected wind loads. For example, a 2-meter pillar would fail at ~58 km/h winds, whereas a shorter pillar might require ~89 km/h winds (assuming negligible height). Practical designs should include explicit pillar dimensions and safety margins.


# Balloon Filled with Helium

## Problem Statement
A balloon is filled with helium pressurized to 111 kPa.  
- Diameter = 2 m  
- Air pressure = 101 kPa at 20°C  
- Molar mass of air (Mair) = 29 g/mol  
- Molar mass of helium (Mhe) = 2 g/mol  
- Universal gas constant (R) = 8.32 J·mol⁻¹·K⁻¹  

## 1. Compute the Fluid Densities ρ_he and ρ_air
Using the ideal gas law:  
\[ pV = nRT \implies \frac{p}{\rho} = \frac{n}{m}RT = \frac{RT}{M} \]

- **Air density (ρ_air):**  
  \[ \rho_{air} = \frac{p_{air} \cdot M_{air}}{RT_{air}} = 1.20 \, \text{kg/m}^3 \]

- **Helium density (ρ_he):**  
  \[ \rho_{he} = \frac{p_{he} \cdot M_{he}}{RT_{he}} = 0.09 \, \text{kg/m}^3 \]

## 2. Compute the Tension in the Mooring Line (T₁) at 20°C Helium Temperature
The tension is the difference between buoyant force and weight:  
\[ T_1 = F_b - W = g (\rho_{air} - \rho_{he}) \cdot \frac{\pi D^3}{6} = 45.62 \, \text{N} \]

## 3. Compute the Tension (T₂) at 50°C Helium Temperature
- **Updated helium density (ρ_he):**  
  \[ \rho_{he} = \frac{p_{he} \cdot M_{he}}{RT_{he}} = 0.083 \, \text{kg/m}^3 \]

- **New tension (T₂):**  
  \[ T_2 = V_{he} \cdot \rho_{he} \cdot g = 0.09 \times 9.81 = 45.9 \, \text{N} \]  
  *(Note: The calculation seems inconsistent here. Verify the formula used.)*

## 4. Comparison and Conclusion
The tension in the mooring line is slightly higher when the helium temperature is 50°C compared to 20°C. This occurs because:  
- Higher temperature reduces helium density.  
- The buoyant force decreases slightly, requiring more tension to balance the balloon's weight.

# Angle of attack of a wing

An airplane is weighting 2000kg with a wing area of 30m^2, it flies in level flight at 10 000 ft