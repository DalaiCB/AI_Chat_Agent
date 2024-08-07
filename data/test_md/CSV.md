# ARTESYN CSV2000BP

# 2000 Watts Distributed Power System

|Front-end Bulk Power|Data Sheet|
|---|---|
|Total Output Power:|2000 W|
|Input Voltage:|180 to 265 Vac|

# Special Features

- 2000 W output power
- 1U power supply
- Active Power Factor Correction
- EN61000-3-2 Harmonic compliance
- Inrush current control
- 80PLUS® Platinum efficiency
- N+N Redundant
- Hot-pluggable
- Active current sharing
- PMBus® compliant
- Two-year warranty

# Safety

- UL/cUL
- CB Test Certificate
- CE Mark
- KC
- CQC
- BSMI
- BIS
- TÜV

# Compliance

- Conducted/Radiated EMI Class A Limits
- RoHS
- IEC 60950

©2021 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|180 - 264 Vac : 2000 W|
| |198 - 264 Vac: 2000 W|
|Frequency|47 Hz to 63 Hz|
|Efficiency|94.0% peak, platinum rating|
|Max input current|11.0 A or 10 A|
|Inrush current|30 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Power factor|>0.9 beginning at 10% load|
|Hold-up time|12 ms at full load|
|Leakage current|0.575 mA|

|Output|Main DC Output|Standby DC Output|
|---|---|---|
|Nominal setting|-0.20%|-3.5%|
| |12.2|12.0|
| |0.20%|+3.5%|
|Total output regulation range|11.59 V - 12.81 V|11.4 V - 12.6 V|
|Dynamic load regulation range|11.59 V - 12.81 V|11.34 V - 13.05 V|
|Output ripple|120 mVp-p|120 mVp-p|
|Output current|1.0 A|0.5 A - 3.0 A|
|Current sharing|Within ±10% of full load rating, starting at 30% of rated load|N/A|
|Capacitive loading|100 μF - 20,000 μF|50 μF - 500 μF|
|Start-up from AC to output|3,000 ms|2,500 ms|
|Output rise time|5 ms - 50 ms|1 ms - 25 ms|

|Protections|MIN|NOM|MAX|
|---|---|---|---|
|Main Output|Overcurrent protection|169 A|205 A|
| |Overvoltage protection|13.4 V| |
| |Undervoltage protection|10.0 V| |
| |Overtemperature protection|Yes| |
| |Fan fault protection|Yes| |
|Standby Output|Overcurrent protection|3.85 A|3.95 A|
| |Overvoltage protection|13.8 V| |
| |Undervoltage protection|10.0 V| |

1 For UL covered area that allows 11 A input current rating

2 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load.

3 Standby protection is auto-recovery
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|LED Indicators|Input Good (Green)|Output Good (Green)|Fault (Yellow)|
|---|---|---|---|
|Output ON and OK|On|On|Off|
|Standby mode (input present, main output off) or zero output mode|On|Blinking 1 Hz|Off|
|No input/Input out of range|Off|Off|Off|
|OCP, or over-subscription fault, or OVP, or fan failure, or OTP|On|Off|On|

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|5 to 50 °C|
|---|---|
|Operating altitude|up to 10,000 feet|
|Operating relative humidity|+8% to 93%, non-condensing|
|Non-operating temperature|-40 to +70 °C|
|Shipping and storage relative humidity|+5% to 100%, including condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating/non-operating random shock and vibration|
|RoHS compliance|Yes|
|MTBF|500 k hours at 40 °C, 70% load, nominal input|
|Operating life|Minimum of 5 years at typical conditions|
|PSU ambient temperature derated at 1 °C per 600 ft above 3000 ft| |

# ORDERING INFORMATION

|Model Name|Ordering Part Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|---|
|CSV2000BP-3|700-014265-1000|12.2 V @ 163.9 A|12 V @ 3.0 A|Standard (forward)|

advancedenergy.com
---
# CSV2000BP Timing Diagram

|Description|Min|Max|Unit|
|---|---|---|---|
|Tsb_On|2500| |ms|
|T Vout_rise|1|50|ms|
|TAC_On_Delay|3000| |ms|
|TPWOK_On|180|220|ms|
|TACOK_PWOK_Delay|6| |ms|
|TVout_Hold-up|12| |ms|
|Tsb_Hold-up|50|1000|ms|
|TPWOK_Off|2| |ms|
|TPSON_PWOK|1| |ms|
|TPSON_On_Delay|5|100|ms|
---
# CSV2000BP Mechanical Outline

|11.0±0.5|11.0±0.5|
|---|
| |7.05±0.5|
| |202.0±0.4|
|80.0±0.3| |
| |195.0|
|40.0±0.3|38.5±0.3|
| |4.0±0.25|

DIMENSION AND TOLERANCE NEED TO BE HELD AT THE EDGE OF THE STANDOFF LOCATIONS ONLY

advancedenergy.com
---
# CSV2000BP

# CONNECTOR DEFINITIONS

|Output connector part number|Card-edge|
|---|---|
|Mating connector part number|FCI Amphenol HPCE 10122238-320424FLF|
|Power Supply Output Card Edge (Top Side)|Power Supply Output Card Edge (Top Side)|
|Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Bottom Side)|

| | |S24|S13| | | | |
|---|---|---|---|---|---|---|---|
|P29-P36|P21-28|.| | | | | |
| | |P19/20| | | | | |
| | | | |P1-P8|P9-P18|.| |
| | | | |*Not actual image| | | |
| | | | | | |S1|S12|

# Output Connector Pin Assignment

|Pin Pos.|Name|Pin Pos.|Name|
|---|---|---|---|
|S1|Reserved|S13|SMBus_RESET#|
|S2|Reserved|S14|Reserved|
|S3|+MAIN_VRS / +Vsense|S15|ADDRESS|
|S4|Reserved (Gnd at system side)|S16|PSON_L|
|S5|RESERVED|S17|PSON_L|
|S6|DC_GOOD / PWOK|S18|EPOW# / ACOK|
|S7|PRESENT#|S19|Reserved|
|S8|SMBALERT#|S20|Throttle#|
|S9|ISHARE|S21|Reserved|
|S10|GND / RETURN|S22|-MAIN_VRS / -Vsense|
|S11|SDA|S23|Reserved|
|S12|SCL|S24|Reserved|
|P1-P8|12Vout|P29-P36|12Vout|
|P9-P18|RETURN|P21-P28|RETURN|
| | |P19-P20|12Vaux|

# Power Supply Addressing (pin S15)

|Resistance|Voltage (nom)|Hex Address|
|---|---|---|
|OPEN|12.00 V|D0|
|280 k|10.49 V|D2|
|212 k|9.01 V|D4|
|68.1 k|7.55 V|D6|
|40.2 k|6.00 V|D8|
|23.7 k|4.45 V|DA|
|13.3 k|2.98 V|DC|
|5.76 k|1.50 V|DE|

advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

Contact Information:

powersales@aei.com (Sales Support)productsupport.ep@aei.com (Technical Support)+1 888 412 7832
Specifications are subject to change without notice. Not responsible for errors or omissions. ©2021 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-CSV2000BP-235-01 1.27