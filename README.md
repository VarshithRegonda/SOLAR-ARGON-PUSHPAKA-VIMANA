# 🛸 PROJECT BLUEPRINT: SOLAR-ARGON PUSHPAKA VIMANA
**Scale:** 1:10 Micro-Prototype | **Build Timeline:** 60 Days | **Lead Inventor:** Varshith Regonda

---

## 1. Project Introduction
The **Pushpaka** project is a high-efficiency micro-UAV designed for dusty, high-insolation environments. It utilizes **biomimetic surface textures** to repel dust, **selective gold plating** for zero-resistance electrical paths, and a **Tesla Fluid Machine** (bladeless turbine) propulsion system simulating ionized Argon plasma.

---

## 2. Engineering Formulas & Geometric Physics
Use these calculations to verify the prototype's performance:

### ☀️ Solar Harvesting ($P_{sol}$)
$$P_{sol} = A \cdot I \cdot \eta \cdot f_{dust}$$
* **$I$**: $1000 W/m^2$ (Avg. Irradiance)
* **$\eta$**: $0.20$ (Cell Efficiency)
* **$f_{dust}$**: $0.95$ (Textured skin factor)

### 🌪️ Tesla Turbine Geometry
To maintain the **Boundary Layer Effect** with Argon gas, the disc gap ($b$) must be corrected:
$$b \approx 2 \cdot \sqrt{\frac{\nu}{\omega}}$$
* **Correction:** For micro-scale discs (10cm), maintain a gap of **0.5mm – 1.0mm** to prevent fluid slip.

### 🚀 Thrust Simulation ($T$)
$$T = \dot{m} \cdot (v_e - v_0)$$
* **Target:** Thrust-to-weight ratio of **1.5:1** for stable hover.

---

## 🛠️ 60-Day Step-by-Step Build Details

### Phase 1: Procurement (Weeks 1-2)
* **Action:** Source components from Indian vendors (Robu.in, Quartz Components, or Koti market).
* **Key Items:** FlySky FS-i6X Remote, 8520 Coreless Motors, LW-PLA Filament, and 1N5817 Schottky Diodes.

### Phase 2: Structural Assembly (Weeks 3-4)
* **The Spine:** Construct a triangular frame using **1mm Carbon Fiber rods**.
* **The Skin:** 3D print the "Peacock Head" and "Motor Shroud" using **Fuzzy Skin** settings (Thickness: 0.125mm, Density: 10.0mm⁻¹) to create a hydrophobic/dust-repellent surface.



### Phase 3: Wiring & Gold Junctions (Weeks 5-6)
* **Connections:** Use **Gold-Plated pins** for all junctions to prevent oxidation.
* **Argon Glow:** Solder Blue LEDs in parallel with the turbine motor to sync light intensity with throttle.
* **Solar Path:** Connect Solar Strips $\rightarrow$ 1N5817 Diode $\rightarrow$ Supercapacitor Bank/Charger.



### Phase 4: Final Testing (Weeks 7-8)
* **Static Test:** Verify turbine RPM and "Argon" LED activation.
* **Range Test:** Ensure 2.4GHz signal penetrates the gold-layered frame.
* **Maiden Flight:** Controlled indoor hover test.

---

## 🕹️ Remote Control (FlySky FS-i6X) Settings
* **CH 3 (Throttle):** Controls motor thrust and Blue LED brightness.
* **Switch A (SwA):** Safety "Kill Switch."
* **Elevon Mix:** Enabled for dual-flap pitch/roll control.

---

## ⚠️ Maintenance & Troubleshooting
* **Dust Protocol:** Use a dry anti-static brush only.
* **Heat Check:** Avoid operation if ambient temperature exceeds **40°C** to protect the electronics.
* **Motor Jitter:** Re-examine gold-plated junctions for cold solder joints.

---
**License:** [Apache 2.0](LICENSE) | **Author:** Varshith Regonda
