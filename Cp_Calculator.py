import math

# -------------------------------------------------------------
# DATABASE: Cp = a + bT + cT^2 + dT^3   (Units: J/mol·K, T in K)
# Sources: NIST Chemistry WebBook (Ideal Gas Cp Polynomials)
# -------------------------------------------------------------
cp_database = {
    "hydrogen":      {"a": 33.066178, "b": -11.363417, "c": 11.432816, "d": -2.772874},
    "oxygen":        {"a": 31.32234,  "b": -20.23531,  "c": 57.86644,  "d": -36.50624},
    "nitrogen":      {"a": 28.98641,  "b": 1.853978,   "c": -9.647459, "d": 16.63537},
    "carbon":        {"a": 21.175,    "b": -0.812,     "c": 0.049,     "d": 0},  # graphite approx
    "co2":           {"a": 24.99735,  "b": 55.18696,   "c": -33.69137, "d": 7.948387},
    "ch4":           {"a": -0.703029, "b": 108.4773,   "c": -42.52157, "d": 5.862788},
    "ethane":        {"a": -0.268,    "b": 138.42,     "c": -46.687,   "d": 4.738},
    "propane":       {"a": 4.218,     "b": 143.38,     "c": -54.15,    "d": 6.31},
    "butane":        {"a": 6.808,     "b": 162.1,      "c": -62.31,    "d": 7.465},
    "methanol":      {"a": 19.89,     "b": 52.11,      "c": -36.85,    "d": 7.47},
    "ethanol":       {"a": 26.01,     "b": 75.84,      "c": -57.29,    "d": 13.15},
    "acetone":       {"a": 16.31,     "b": 102.3,      "c": -77.74,    "d": 18.06},
    "benzene":       {"a": 19.02,     "b": 70.15,      "c": -56.2,     "d": 14.7},
}

# -------------------------------------------------------------
# Function to compute integral of Cp(T)
# -------------------------------------------------------------
def qsens_temperature_dependent(moles, T1, T2, a, b, c, d):
    Q = moles * (
        a * (T2 - T1)
        + (b/2) * (T2**2 - T1**2)
        + (c/3) * (T2**3 - T1**3)
        + (d/4) * (T2**4 - T1**4)
    )
    return Q  # J


# -------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------
print("\nAvailable species:")
for s in cp_database:
    print(" -", s)

species = input("\nEnter species name: ").lower()

if species not in cp_database:
    print("Species not found in database.")
    exit()

moles = float(input("Enter number of moles: "))
T1 = float(input("Enter initial temperature (K): "))
T2 = float(input("Enter final temperature (K): "))

# extract Cp(T) coefficients
coeff = cp_database[species]

Q = qsens_temperature_dependent(moles, T1, T2,
                                coeff["a"], coeff["b"], coeff["c"], coeff["d"])

print(f"\nSensible Heat Required (Temperature dependent): {Q/1000:.2f} kJ")
