Here is a **clean, professional, GitHub-ready README.md** for your project.

You can copy–paste this directly into your repository’s README.md.

---

# ⭐ Temperature-Dependent Sensible Heat Calculator (Python)

A Python-based engineering tool that calculates **sensible heat (Qₛₑₙₛ)** using **temperature-dependent heat capacity Cp(T)**.
Built using concepts from **Chemical Process Calculations (CPC)** and **Thermodynamics**.

This project integrates **Cp(T) = a + bT + cT² + dT³** polynomials and computes the exact energy required to heat a substance between two temperatures.

---

## 🔥 Features

* Temperature-dependent ideal gas heat capacity:
  [
  C_p(T) = a + bT + cT^2 + dT^3
  ]
* Exact integral calculation:
  [
  Q = m \int_{T_1}^{T_2} C_p(T), dT
  ]
* Built-in database of Cp coefficients for:

  * Elements: **Hydrogen, Carbon, Oxygen, Nitrogen**
  * Organic compounds: **Methane, Ethane, Propane, Butane**
  * Alcohols: **Methanol, Ethanol**
  * Others: **CO₂, Acetone, Benzene**
* Easy to extend — add any species from NIST WebBook
* Clean, modular code

---

## 📘 Formula Used

The ideal-gas heat capacity polynomial:

[
C_p(T) = a + bT + cT^2 + dT^3
]

Integrated to compute sensible heat:

[
Q = m \left[ a(T_2 - T_1)

* \frac{b}{2}(T_2^2 - T_1^2)
* \frac{c}{3}(T_2^3 - T_1^3)
* \frac{d}{4}(T_2^4 - T_1^4)
  \right]
  ]

Where:

* **m** = number of moles
* **T₁, T₂** = initial and final temperature (K)
* **Q** = sensible heat (J)

---

## 🧪 Example Usage

```text
Available species:
 - hydrogen
 - oxygen
 - nitrogen
 - carbon
 - co2
 - ch4
 - ethane
 - propane
 - butane
 - methanol
 - ethanol
 - acetone
 - benzene

Enter species name: ethanol
Enter number of moles: 2
Enter initial temperature (K): 300
Enter final temperature (K): 500

Sensible Heat Required (Temperature dependent): 648.32 kJ
```

---

## 🧩 Code Structure

```
.
├── qsens_temp_dependent.py   # Main calculator script
├── README.md                 # Project documentation
└── (optional) /data          # Store additional Cp datasets
```

---

## 🛠 How to Run

1. Install Python 3.7+
2. Download the `.py` file
3. Run:

```bash
python qsens_temp_dependent.py
```

4. Choose a species and enter temperatures.

---

## 📦 Extend the Database

The Cp database is stored as:

```python
cp_database = {
    "ethanol": {"a": 26.01, "b": 75.84, "c": -57.29, "d": 13.15},
}
```

To add more species, simply append new entries using Cp(T) values from the **NIST WebBook**.

---

## 📚 Sources

* NIST Chemistry WebBook (Ideal Gas Heat Capacity Polynomials)
* Standard CPC/Thermodynamics (Chemical Engineering)

---

## 🤝 Contributions

Pull requests to add more compounds, improve accuracy, or optimize the code are welcome!

---

## ⭐ Acknowledgments

This project is inspired by the desire to combine **Chemical Engineering fundamentals** with **Python programming**, creating tools useful for CPC, Thermodynamics, and process calculations.




Just tell me!
