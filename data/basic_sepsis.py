# Example of patient data
heart_rate = 110        # bpm
systolic_bp = 85        # mmHg
resp_rate = 24          # breaths/min
temp = 38.5             # °C
spo2 = 93               # %
wbc = 14.0              # x10^9/L
lactate = 2.3           # mmol/L

# Count abnormal findings
flags = 0

if heart_rate > 100:
    flags += 1
if systolic_bp < 90:
    flags += 1
if resp_rate > 20:
    flags += 1
if temp > 38 or temp < 36:
    flags += 1
if spo2 < 94:
    flags += 1
if wbc > 12 or wbc < 4:
    flags += 1
if lactate > 2:
    flags += 1

# Define threshold for banner
if flags >= 3:
    print("⚠️ SEPSIS ALERT: Multiple abnormalities detected.")
    print("Please complete sepsis pathway: blood cultures, urine cultures, lactate, CBC, CMP, and notify MD.")
else:
    print("Patient stable. Continue routine monitoring.")
