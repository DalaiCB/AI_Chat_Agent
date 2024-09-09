# ARTESYN CNS650-M SERIES 650 W AC-DC Power Supplies

Advanced Energy's Artesyn CNS650-MU series of single output open-frame AC-DC power supplies are offered in 12 V, 24 V, or 48 V outputs with +15% trim range. Each power supply comes with a 12 V fan output and 5 V standby. All models feature ITE and medical safety approvals and accept a universal input of 90 to 264 VAC. Depending on operating conditions, its 4'' x 6'' x 1.54'' compact and high density "U-Channel" construction delivers up to 400 W of output power with free air convection cooling and up to 650 W with 400 LFM of forced air. These power supplies are ideal for industrial systems as well as for medical applications.

# SPECIAL FEATURES

|Designed for forced air and natural convection cooling|Medical and ITE safety approvals, 2x MOPP|
|---|---|
|PMBus® interface|Active current share with OR-ing FET|
|Dual fused|Type BF ready|
|Active Power Factor Correction, 61000-3-2 compliant|Built-in Class B EMI filter|
|Less than 1U high|4" x 6" U-channel construction (open-frame or end-fan variants available for 12 V)|
|&lt;500 mW no-load power consumption|80 PLUS® certified (-ME model)|
|Three year warranty (consult factory for extended terms)| |

# SAFETY

|UL+CUL ES 60601-1|UL 60601-1|
|---|---|
|UL 62368-1|TÜV EN 60601-1|
|DEMKO EN 62368-1|CB IEC 60950-1|
|IEC 60601-1|IEC 62368-1|
|CCC GB4943.1/GB9254|GB17625.1|
|CE LVD, RoHS|UKCA Mark|

** CNS650-M tested according to the medical standard IEC 60601-1-2 4th Edition.

©2022 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input voltage range|90 to 264 VAC or 127 to 350 VDC|
|---|---|
|Frequency|47 to 63 Hz (360 to 440 Hz with higher leakage)|
|Inrush current|50 Apk, cold start|
|Leakage current|<300 μA (using UL test method)|
|No load power|< 500 mW|

|Output| |
|---|---|
|Maximum power|650 W, forced-air cooling (750 W peak)|
| |400 W, free-air natural convection cooling (650 W peak)|
|Adjustment range|-0% to +15%|
|Holdup time|20 ms @ 400 W|
|Fan output|12 V @ 1.0 A (forced air)|
| |12 V @ 0.5 A (natural convection)|
|Standby output|5 V @ 2.0 A (forced air)|
| |5 V @ 1.0 A (natural convection)|

|Control and Protection| |
|---|---|
|Serial bus interface|PMBus®|
|Current share|Active|
|Remote sense|2-wire (+ and -)|
|Remote inhibit|Pull inhibit low = main & fan output OFF (5 V standby is ON)|
| |Pull inhibit high (or floating) = all outputs ON|
|AC OK|Active high when normal AC input is present (with internal 10 kOhm pull up to 3.3 V)|
|DC OK|Active high when main O/P is within regulation (with internal 10 kOhm pull up to 3.3 V)|
|Smart fan control|Monitor, control and override|
|Overvoltage protection|Latch (AC recyle or inhibit toggle required for PSU restart)|
|Overload protection|Auto-recovery (constant current mode down to 50% Vout)|
|Overtemperature protection|Auto-recovery with hysteresis|

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|-20 °C to +80 °C (derate at 50 °C), startup at -40 °C|
|---|---|
|Storage temperature|-40 °C to +85 °C|
|Operating humidity|5% to 95% (non-condensing)|
|Non-operating humidity|5% to 95% (non-condensing)|
|Maximum altitude|5000 m (3000 m for medical), derating may apply|
---
# OTHER SPECIFICATIONS

|Isolation|4000 VAC (input to output)|
|---|---|
| |1500 VAC (input to PE, output to PE)|
|Line harmonics|61000-3-2, Class A|
|ESD immunity|61000-4-2, ±15kV (air) / ±8kV (contact) - Criterion A|
|Conducted EMI|Level B, CISPR 22 and FCC Part 15|
|Radiated EMI|Level B, CISPR 22 and FCC Part 15 (with cover)|
|Surge immunity|61000-4-5, Level 3 - Criterion A, Level 4 - Criterion C|
|Medical EMC|60601-1-2, Edition 4 (cover maybe required for some tests)|
|MTBF|> 950 KHrs, 25 °C, 410 W natural convection|
| |(Telcordia, Issue 3, Method 1, Case 3) > 1.3 MHrs, 25 °C, 650 W forced air|

# ORDERING INFORMATION

|Model Number|Output Voltage|Output Range (-0% / +15%)|Minimum Load|Max. Continuous Load (Free Air)|Max. Load (Forced Air)|Regulation|Ripple (p-p)|
|---|---|---|---|---|---|---|---|
| | |Load|Load| | | | |
| | | |(Free Air)| |(Forced Air)| | |
| | | | | | | | |
|CNS653-ME|12 V|12 - 13.8 V|0 A|54.2 A|NA|±2%|120 mV|
|CNS653-MF|12 V|12 - 13.8 V|0 A|30.8 A|54.2 A|±2%|120 mV|
|CNS653-MU|12 V|12 - 13.8 V|0 A|33.3 A|54.2 A|±2%|120 mV|
|CNS655-MU|24 V|24 - 27.6 V|0 A|16.7 A|27.1 A|±2%|240 mV|
|CNS658-MU|48 V|48 - 55.2 V|0 A|8.3 A|13.5 A|±2%|480 mV|

1 Peak load current not to exceed 10 seconds, Ta = 50 °C.

2 Requires at least 400 LFM of airflow.

3 At 25 °C including factory setpoint, line voltage and load current variations.

4 Peak-to-peak ripple measured at the output terminal with 20 MHz bandwidth and 10 μF (tantalum capacitor) in parallel with 0.1 μF capacitor across the output.

5 Optional suffix “-ME” (end-fan) and “-MF: (open-frame) available on the 12 V output.

6 80 PLUS certified.

advancedenergy.com
---
# INPUT CONNECTIONS (-MU AND -MF SUFFIX)

|Pin|Function|Power Supply Side|System Side|
|---|---|---|---|
|TB1|PE| | |
|TB2|L2/Neutral|Dinkle EHK762V-03P|Recommended Wire Size: AWG #22 to #14 Max Torque: 4kgf-cm|
|TB3|L1/Line| | |

# INPUT CONNECTIONS (-ME SUFFIX)

|Pin|Function|Power Supply Side|System Side|
|---|---|---|---|
|IEC Inlet|Input AC|IEC 60320 C14 (Male)|IEC Cord C13 (Female)|

# OUTPUT CONNECTIONS

|Pin|Function|Power Supply Side|System Side|
|---|---|---|---|
|BAR1|-Vout| |Molex 19099-0032 or 19141-0063|
|BAR2|-Vout|Output Terminal Screw: M4X8 (4X)|for AWG #16 to #14|
|BAR3|+Vout|Max Torque: 10kgf-cm|Molex 19099-0048 or 19141-0083 for AWG #12 to #10|
|BAR4|+Vout| | |
---
# OTHER OUTPUT AND CONTROL CONNECTIONS (CONNECTOR J304)

|Pin|Designation|Description|
|---|---|---|
|1|5VSB|+5 V Standby Output|
|2|5VSB|+5 V Standby Output|
|3|5VSB_GND|+5 V Standby Output Return/Ground|
|4|SCL|Serial Clock Signal (I2C)|
|5|A0|EEPROM Address|
|6|SDA|Serial Data Signal (I2C)|
|7|I_SHARE|Active Current Share|
|8|SYS_GND|Return Ground for Signals and I2C|
|9|12VFAN|12 V Fan Output|
|10|REMOTE INHIBIT|Output Inhibit Pin (Main Output)|
|11|FAN_RTN|12 V Fan Output Return/Ground|
|12|VIN_GOOD|Input Line OK Signal|
|13|FAN_PWM1|FAN PWM|
|14|PWOK|Output Power OK Signal|
|15|FAN_TACH1|Fan1 Tacho Signal|
|16|FAN_OVERRIDE|External Fan Sensor for Override|
|17|FAN_FAIL|Fain Fail Signal|
|18|FAN_FAULT_EN|FAN Fault Enable Due to Low RPM|
|19|REMOTE_SENSE+|Positive Remote Sense|
|20|REMOTE_SENSE-|Remote Sense Return|

# FAN OUTPUT CONNECTOR FOR -MU, -MF SUFFIX (CONNECTOR J306)

|Pin|Function|Description|
|---|---|---|
|1|12VFAN|12 V fan output|
|2|FAN_RTN|12 V fan return|
|3|FAN_PWM1|Fan PWM|
|4|FAN_TACH1|Fan1 tacho signal|
---

2.5 mm max penetration depth from face of side chassis

TRIMPOT FOR OUTPUT ADJUSTABILITY

COUNTER-CLOCKWISE: INCREASE OUTPUT VOLTAGE

16.2
120

PEM F-M3-1 (4X)

3.0 MM MAX PENETRATION DEPTH FROM FACE OF BOTTOM CHASSIS

|26.2|100| |152.4|0.5|1.9 REF|
|---|---|---|---|---|---|
| | | |100 (2X)| | |

# Thermal Hot Spot Reference

|Component|Temperature Limit (-MU)|
|---|---|
|D1 (AC bridge diode)|105 °C|
|L1 (PFC choke)|115 °C|
|C40 (output cap)|100 °C|
|L-output (output choke)|125 °C|

Do not exceed indicated temperature limits to ensure operation is within the component thermal derating limits. Measure the component temperatures using K type thermocouples.

Unit weight (-MU suffix): 800 g

6 advancedenergy.com
---
INPUT CONNECTOR: DINKLE EHK762V-03P

TORQUE: 4kgf-cm MAX.

OUTPUT TERMINALS

|PE|C40|
|---|---|
|N|SCREW M4X8 (4X)|
|L-0P|TORQUE: 10kgf-cm MAX.|
|J304|20-WAY SIGNAL CONNECTOR|

FAN CONNECTOR

| |88.3|34.1|0.5|
|---|---|---|---|
|96.8|0.5|MODEL LABEL| |

Thermal Hot Spot Reference Component

|D1 (AC bridge diode)|Temperature Limit (-MF)|
|---|---|
|L1 (PFC choke)|120°C|
|C40 (output cap)|100 °C|
|L-output (output choke)|125 °C|

Do not exceed indicated temperature limits to ensure operation is within the component thermal derating limits. Measure the component temperatures using K type thermocouples.

Unit weight (-MF suffix): 650 g

advancedenergy.com
---
Figure 5. Typical Efficiency for 48 V Output

Figure 6. Estimated Product Useful Life Based on C40 Case Temperature

Figure 7. CNS653-ME (End Fan) Typical Audible Noise Level vs. Output Load at 90 VAC, ~30 °C Ambient.

advancedenergy.com 9
---
# ACCESSORIES

|Orderable Part Number|Description|Description|
|---|---|---|
|73-788-001|J304 (20 Pin) Mating Connector with 0.3 m wires attached|Description|
| | |Description|
| | |PIN 20|
| | |PIN 19|
| | |PIN 3|
| | |PIN 2|
| | |PIN 1|
| | | |
| | | |
| | |300 ± 5 mm|

|Orderable Part Number|Description|
|---|---|
|CNS-BBAR-KIT|Output Bussbar Extension Kit for Vertical Wire Interface|
|73-769-002|USB to I2C Adaptor for PMBus Communication|

advancedenergy.com
---
