# ARTESYN DS2000SPE SERIES

2000 Watts Distributed Power System

Advanced Energy's Artesyn DS2000SPE is an ultra-high density power supply providing 50W per cubic inch. The 2000 watt DS2000SPE power supply is housed in 1U high rack-mounting enclosures measuring just 3.4 x 7.7 in (86.3 x 196.5 mm). This form factor is significantly shorter than that of similarly rated earlier-generation power supplies — freeing up valuable system space — and is achieved by use of the latest power switching technology and high density component packaging techniques.

# SPECIAL FEATURES

|AT A GLANCE| |
|---|---|
|Front-end Bulk Power|Total Output Power|
|2000 W continuous at high line|90 to 140 VAC & 180 to 264 VAC operation|

# COMPLIANCE

- 80PLUS PLATINUM
- RoHS

- 2000 W output power at high line
- High power and short form factor
- 1U power supply
- High density design: 50 W/in3
- Active power factor correction
- Inrush current control
- 80PLUS platinum efficiency
- N+1 or N+N redundant
- Active current sharing
- PMBus compliant
- Two-year warranty
- Class A Conducted/Radiated EMI
- RoHS

# SAFETY

- UL/cUL 60950 (UL Recognized)
- DEMKO+ CB Report EN60950
- EN60950
- CE Mark
- UKCA Mark

©2022 Advanced Energy Industries, Inc.
---
# DS2000SPE

|ELECTRICAL SPECIFICATIONS| |
|---|---|
|Input| |
|Input voltage range|180 to 264 VAC: 2000 W|
| |90 to 140 VAC: 1000 W|
|Frequency|47 Hz to 63 Hz|
|Efficiency|94.0% peak|
|Max input current|11.5 Arms at 100/200 VAC|
|Inrush current|50 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Power factor|> 0.9 beginning at 20% load|
|ITHD|10%|
|Leakage current|1.0 mA|
|Hold-up time|11 ms at 95% load|

|ORDERING INFORMATION| | | |
|---|---|---|---|
|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|DS2000SPE-3|12.2 V @ 163.9 A|12 V @ 3.5 A|Standard (forward)|
|TBD|12.2 V @ TBD|12 V @ 3.5 A|Reverse|

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS

|Output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal setting|12.175|12.2|12.225|
|Total output regulation range|11.4 V| |12.9 V|
|Dynamic load regulation range|11.4 V| |12.9 V|
|Output ripple| | |180 mVp-p|
|Output current|5.0 A (minimum starting load for 17% transient step)| |163.9 A at high line, 82 A at low line|
|Current sharing| |Within +/-7.0 A of each other| |
|Capacitive loading|4,900 μF| |38,000 μF|
|Start-up from AC to output| | |2,300 ms|
|Output rise time| | |100 ms|

|Standby DC output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal setting|11.95|12|12.05|
|Total output regulation range|11.4 V| |12.6 V|
|Dynamic load regulation range|11.4 V| |12.6 V|
|Output ripple| | |120 mVp-p|
|Adjustment range| |N/A| |
|Output current|0.0 A| |3.5 A|
|Current sharing| |N/A| |
|Capacitive loading|1 μF| |4700 μF|
|Start-up from AC to output|20 ms| |2000 ms|

|Protections|MIN|NOM|MAX|
|---|---|---|---|
|Main Output| | | |
|Overcurrent protection|107%| |130%|
|Overvoltage protection|13.5 V| |14.5 V|
|Undervoltage Protection|10.0 V| |10.5 V|
|Overtemperature protection| |Yes| |
|Fan fault protection| |Yes| |
|Standby Output| | | |
|Overcurrent protection|110%| |150%|
|Overvoltage protection|13.5 V| |15.0 V|
|Undervoltage protection|10.0 V| |10.5 V|

1 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load.

2 Output voltage will stay within regulation during a 50% step load with a minimum starting load of 41A.

3 Latch mode

4 Auto-recovery

advancedenergy.com 3
---
# DS2000SPE

# CONTROL AND STATUS SIGNALS

|Input Signals| |MIN|MAX|
|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output.| | |
|VIL|Input logic level LOW| |0.8 V|
|VIH|Input logic level HIGH|2.0 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |1.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|PSKILL_H|First break/last mate active HIGH signal which enables/disables the main output.| | |
|VIL|Input logic level LOW. This allows for the power supply to be turned on| |0.8 V|
|VIH|Input logic level HIGH. Immediately shuts down the power supply|2.0 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| | |
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|VSENSE+, VSENSE-|VSENSE+ and VSENSE- lines are the remote sense lines for regulation. Each line will compensate for a maximum of 100 mV.| | |

|Output Signals| |MIN|MAX|
|---|---|---|---|
|ACOK|Signal used to indicate the presence of AC input to the power supply. A logic level HIGH will indicate that the AC input to the power supply is within the operating range while a logic level LOW will indicate that AC has been lost.| | |
|VOL|Output logic level LOW| |0.4 V|
|VOH|Output logic level HIGH|2.4 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |2.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of AC input or system shutdown request. More details in the Timing Section.| | |
|VOL|Output logic level LOW| |0.4 V|
|VOH|Output logic level HIGH|2.4 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |2.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|

# advancedenergy.com
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| |
|---|---|
|PS_PRESENT|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is connected to the standby return in the power supply.|
|PS_INTERRUPT|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command.|

| | |MIN|MAX|
|---|---|---|---|
|VOL|Output logic level LOW| |0.8 V|
|VOH|Output logic level HIGH|2.0 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |2.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|

|Bus Signals| | | | | |
|---|---|---|---|---|---|
|ISHARE|Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.| | | | |

| | |Min|Max|
|---|---|---|---|
|ISHARE Voltage|Voltage at 50% load, stand-alone unit|3.412|3.588|
| |Voltage at 100% load, stand-alone unit|6.912|7.088|

| | |MIN| |MAX|
|---|---|---|---|---|
|SCL, SDA|Clock, data and addressing signals defined as per IC requirements. It is recommended that these pins be pulled-up to a 2.0 kohm resistor to 3.3 V and a 100 pF decoupling capacitor at the system side.| | | |
|VL|Logic level LOW| | |0.8 V|
|VH|Logic level HIGH|2.0 V| |3.6 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 - 100 MHz.

# LED Indicators

A single bi-color LED is used to indicate the power supply status.

| |Status LED|
|---|---|
|No AC input to PSU with external 12 V|Blinking AMBER|
|Main output ON|Solid GREEN|
|Standby mode and Power supply failure (OCP, OVP, OTP, FAN FAULT)|Blinking AMBER|

advancedenergy.com          5
---
# DS2000SPE

|Description|Min|Max|Unit|
|---|---|---|---|
|Delay from AC being applied to standby output being within regulation|20|2000|ms|
|Delay from standby output to ACOK assertion|20| |ms|
|Delay from standby output to main output voltage being within regulation| |300|ms|
|Delay from AC being applied to main output being within regulation| |2300|ms|
|Delay from output voltages within regulation limits to PWOK asserted|100|1000|ms|
|Delay from loss of AC to assertion of ACOK|7| |ms|
|Delay from loss of AC to deassertion of PWOK|10| |ms|
|Delay from loss of AC to main output being within regulation|11| |ms|
|Delay from loss of AC to standby output being within regulation|150| |ms|
|* Standby output loaded at 1.0 A| | | |
|Delay from deassertion of PWOK to output falling out of regulation|1| |ms|
|Delay from PSON assertion to output being within regulation|350| |ms|
|Duration of PWOK being in deasserted state during an ON/OFF cycle of PSU|N/A|N/A| |

advancedenergy.com
---
# DS2000SPE Timing Diagram

|AC Input| |
|---|---|
|T sb_On|T sb_Hold-up|
|Vout_stby|T sb_Vout|
|T sb_ACOK|ACOK|
|T AC_On_Delay|T Vout_Hold-up|
|Vout_main| |
|T PWOK_On|TPWOK_Off|
|PWOK| |
|T PWOK_Hold-up|T PSON_On_Delay|
| |PSON|

advancedenergy.com 7
---
# DS2000SPE Mechanical Outline

| |EMI CLIP|185.4 x 0.3|14.8 x 0.3| |
|---|---|---|---|---|
|HOT SURFACE WARNING LABEL|8.8 x 0.5| | | |
|+0.44 x 0.1|-0.1| | | |
| | | |MODEL LABEL|196.5 x 0.5|
|FAN GUARD TO BE USED FOR REVERSE AIR MODELS ONLY| | | | |
|LED INDICATOR|86.3 x 0.5| | | |
| | |FORWARD AIRFLOW DIRECTION| | |
| | |REVERSE AIRFLOW DIRECTION| | |
|14 x 0.3| | | | |
|4 x 0.2| | | | |
|49.5| | | | |
|9.5| | | | |
|38.5 x 0.5| | | | |
|9.3 x 0.38| | | | |
|17.8| | | | |
|8 advancedenergy.com| | | | |
---
# CONNECTOR DEFINITIONS

|Output Connector Part Number|Card-edge|
|---|---|
|Mating Connector Part Number|FCI 10107844-002LF or any equivalent|

|Power Supply Output Card Edge (Top Side)|Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Top Side)|
|---|---|---|---|
|S24|S13| | |
|P29-P36|P21-28| | |
| |P19/20|P1-P8|P9-P18|
| | |S1|S12|

# Output Connector Pin Configuration

|S1|PS_PRESENT|S13|PS_ON_L|
|---|---|---|---|
|S2|A1|S14|PSKILL_H|
|S3|A0|S15|RESERVED|
|S4|PWR_GOOD (PWOK)|S16|RETURN|
|S5|ACOK (AC Input Present)|S17|SDA|
|S6|RETURN|S18|RETURN|
|S7|I_SHARE|S19|SCL|
|S8|RESERVED|S20|RETURN|
|S9|PS_INTERRUPT_L / ALERT|S21|REMOTE SENSE -|
|S10|RETURN|S22|RETURN|
|S11|RESERVED|S23|REMOTE SENSE +|
|S12|RESERVED|S24|A2|
|P1-P8|+12VOUT|P19-P20|+VSB|
|P9-P18|RETURN|P21-P28|RETURN|
| | |P29-P36|+12VOUT|

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|0 to 50°C, allowable up to 60°C at derated output of 2.6%/°C above 50°C|
|---|---|
|Operating altitude|16,400 ft with derated power|
|Operating relative humidity|Up to 95% non-condensing|
|Non-operating temperature|-40 to +70°C|
|Non-operating relative humidity|Up to 95% non-condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating and non-operating random shock and vibration|
|ROHS compliance|Yes|
|MTBF|900 khours Telcordia Issue 3|
|Operating life|Minimum of 5 years|

advancedenergy.com 9
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2022 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS2000SPE-235-02 4.27