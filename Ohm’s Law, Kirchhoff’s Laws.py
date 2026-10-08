# Ohm-s-Law-Kirchhoff-s-Laws
Sure. Here are simple Python programs for **Ohm’s Law, KCL, and KVL**.

### 1\. Ohm’s Law

```
V = float(input("Enter Voltage: "))
I = float(input("Enter Current: "))

R = V / I

print("Resistance =", R, "Ohms")
```

### 2\. Kirchhoff’s Current Law (KCL)

```
I1 = float(input("Enter current entering: "))
I2 = float(input("Enter another current entering: "))

I3 = I1 + I2

print("Current leaving =", I3, "A")
```

### 3\. Kirchhoff’s Voltage Law (KVL)

```
V = float(input("Enter supply voltage: "))
V1 = float(input("Enter first voltage drop: "))

V2 = V - V1

print("Second voltage drop =", V2, "V")
```

### 4\. All in One Program

```
print("Electrical Calculator")
print("1. Ohm's Law")
print("2. KCL")
print("3. KVL")

choice = int(input("Enter your choice: "))

if choice == 1:
    V = float(input("Enter Voltage: "))
    I = float(input("Enter Current: "))
    print("Resistance =", V / I, "Ohms")

elif choice == 2:
    I1 = float(input("Enter current I1: "))
    I2 = float(input("Enter current I2: "))
    print("Current leaving =", I1 + I2, "A")

elif choice == 3:
    V = float(input("Enter Supply Voltage: "))
    V1 = float(input("Enter Voltage Drop V1: "))
    print("Voltage Drop V2 =", V - V1, "V")

else:
    print("Invalid choice")
```
