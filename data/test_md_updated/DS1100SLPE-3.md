# ARTESYN DS1100SLPE

# 1100 Watts Distributed Power System

Advanced Energy's Artesyn DS1100SLPE series bulk front end AC-DC power supply accepts a wide range 90–264 Vac input and provides a main 12 V output plus a 3.3 V standby output. Rated at 1,100 watts it is an 80 Plus Platinum supply with a high peak efficiency of 94%. Housed in an industry standard 1U x 2.1 inch rack-mounting package, the power supply is ideal for space-constrained applications. This series comes in two airflow versions – dc-connector to ac-connector and vice versa.

# SPECIAL FEATURES

- 1100 W output power
- High power and short form factor
- 1U power supply
- High density design: 26 W/in^3
- Active Power Factor Correction
- EN61000-3-2 harmonic compliance
- Inrush current control
- 80plus Platinum Efficiency
- N+1 or N+N Redundant
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus compliant
- Accurate input power reporting
- Compatible with Artesyn’s Universal PMBus GUI
- Reverse airflow option
- Two-year warranty

# COMPLIANCE

- EMI Conducted/Radiated Class A Limits + 6 dB margin
- EN61000-4 Electromagnetic compatibility
- RoHS 6/6

# SAFETY

- UL/cUL 62368 (UL Recognized)
- DEMKO+ CB Report EN62368
- CE Mark
- China CCC
- BSMI

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|90 - 264 Vac|
|Frequency|47 Hz to 63 Hz|
|Efficiency|94.0% peak|
|Max input current|14.5 Arms|
|Inrush current|55 Apk|
|Conducted EMI|Class A +6 dB margin|
|Radiated EMI|Class A +6 dB margin|
|Power factor|> 0.9 beginning at 20% load|
|ITHD|10%|
|Leakage current|1.75 mA|
|Hold-up time|16 ms at full load|

| | | |Output|Main DC Output| |Standby DC Output| |
|---|---|---|---|---|---|---|---|
| | |MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting| |-1%|12|+1%|-1%|3.3|1%|
|Total output regulation range| |11.64 V|12|12.36 V|3.14 V|3.3|3.46 V|
|Dynamic load regulation range| |11.64 V| |12.36 V|3.14 V| |3.46 V|
|Output ripple| | | |180 mVp-p| | |45 mVp-p|
|Output current| |0.5 A| |90.0 A|0.1 A| |3.0 A|
|Current sharing|Within ±5.625A of each other from 25% to 100% load| | | | |N/A| |
|Capacitive loading|500 μF| | |11,000 μF|20 μF| |1000 μF|
|Start-up from AC to output| | | |2200 ms| | |1700 ms|
|Output rise time| |5 ms| |50 ms|2 ms| |60 ms|

Note: Outputs shall be isolated from the chassis ground by at least 50 V.

Minimum starting current for transient load response testing only. Unit is designed to operate and be within output regulation at zero load.

|Protections|Main Output| | | | | | |
|---|---|---|---|---|---|---|---|
| | |MIN|NOM|MAX| | | |
|Overcurrent protection|107%| | | | |130%| |
|Overvoltage protection| |13.2 V| | | |15.0 V| |
|Overtemperature protection| | | |Yes, autorecovery| | | |
|Fan fault protection| | | |Yes| | | |

|Standby Output| | | |
|---|---|---|---|
|Overcurrent protection|110%| |150%|
|Overvoltage protection|3.6 V| |3.9 V|

1 Latch mode

2 No shutdown if the overcurrent is within the range and does not last for more than 200 ms, otherwise latch will occur

3 Autorecovery

advancedenergy.com
---
# DS1100SLPE

# CONTROL AND STATUS SIGNALS

|Input Signals| | | | | | |
|---|---|---|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | | | |
|V IL|Input logic level LOW| | |MIN|MAX| |
|V IH|Input logic level HIGH|2.0 V| |3.6 V| | |
|I SOURCE|Current that may be sourced by this pin| | | |2 mA| |
|I SINK|Current that may be sunk by this pin at low state| | | |0.5 mA| |
|PSKILL_H|First break/last mate active LOW signal which enables/disables the main output. This signal will have to be pulled to ground at the system side with a 220 ohm resistor. A 100 pF decoupling capacitor is also recommended.| | | | | |
|V IL|Input logic level LOW| | |MIN|MAX| |
|V IH|Input logic level HIGH|2.0 V| |3.6 V| | |
|I SOURCE|Current that may be sourced by this pin| | | |2 mA| |
|I SINK|Current that may be sunk by this pin at low state| | | |0.5 mA| |
|VSENSE+, VSENSE-|VSENSE+ and VSENSE- lines are the remote sense lines for regulation. Each line will compensate for a maximum of 100 mV| | | | | |

# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS1100SLPE-3|12 V|3.3 V @ 3 A|Std (forward)|
|DS1100SLPE-3-001|12 V|3.3 V @ 3 A|Reverse|

1 Derating may apply

# I2C ADDRESSING

|A1 Pin|A0 Pin|PMBus (w/r)|
|---|---|---|
|0|0|B0/B1|
|0|1|B2/B3|
|1|0|B4/B5|
|1|1|B6/B7|

advancedenergy.com
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| | | | |
|---|---|---|---|---|
|ACOK|Signal used to indicate the presence of AC input to the power supply. A logic level HIGH will indicate that the AC input to the power supply is within the operating range while a logic level LOW will indicate that AC has been lost. This is an open collector/drain output. This pin is pulled high by a 10 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | | |
|V IL|Input logic level LOW| | |0.6 V|
|V IH|Input logic level HIGH| |2.0 V|3.6 V|
|I SOURCE|Current that may be sourced by this pin| | |3.3 mA|
|I SINK|Current that may be sunk by this pin at low state| | |0.7 mA|

|Output Signals| | | | |
|---|---|---|---|---|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of AC input or system shutdown request. More details in the Timing Section. This is an open collector/drain output. This pin is pulled high by a 10 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | | |
|V IL|Input logic level LOW| | |0.8 V|
|V IH|Input logic level HIGH| |2.0 V|3.6 V|
|I SOURCE| |Current that may be sourced by this pin| |3.3 mA|
|I SINK| |Current that may be sunk by this pin at low state| |0.7 mA|

|Output Signals| | | | | | | |
|---|---|---|---|---|---|---|---|
|PS_PRESENT|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is shorted to the standby return in the power supply. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | | | | |
|PS_INTERRUPT|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | | | | |
|V IL|Input logic level LOW| | | | | |0.8 V|
|V IH|Input logic level HIGH| | | |2.0 V| |3.6 V|
|I SOURCE|Current that may be sourced by this pin| | | | | |4 mA|
|I SINK|Current that may be sunk by this pin at low state| | | | | |4 mA|

|BUS Signals| | | |
|---|---|---|---|
|ISHARE|Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.| | |
|Voltage Range|The range of this signal for active sharing will be up to 8.0 V, which corresponds to the maximum output current.| | |
|I SHARE Voltage|Input logic level LOW|7.75|8.25|
| |Voltage at 50% load, stand-alone unit|3.85|4.15|
| |Voltage at 0% load, stand-alone unit|0|1.0|
|I SOURCE|Current that may be sourced by this pin| |160 mA|

| | | | |
|---|---|---|---|
|SCL, SDA|Clock and data signals defined as per I2C requirements. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 100 pF decoupling capacitor at the system side.| | |
|VL|Input logic level LOW| |0.8 V|
|VH|Input logic level HIGH|2.0 V|3.6 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 - 100 MHz.
---
# ELECTRICAL SPECIFICATIONS

|LED Indicators|Status LED|Fail LED|
|---|---|---|
|Color|Green|Amber/Green|
|No input to PSU|Off|Off|
|Input present, STBY ON, main output OFF|On|Blinking Amber, at least 1 Hz|
|Main output ON|On|Green|
|Power supply warning (hi-temp)|On|Blinking Amber/Green, at 1:1 ratio, at least 1 Hz|
|Power supply warning (slow fan)|On|Blinking Amber/Green, at 1:1 ratio, at least 1Hz|
|Power supply failure (OVP, OTP, FAN FAULT)|On|Amber|

# Firmware Reporting And Monitoring

|Accuracy Range| | | |
|---|---|---|---|
|Output loading|&lt;10%|10% to 20%|20% to 100%|
|Input voltage|±5%| | |
|Input current|±1 A fixed error|±10%|±5%|
|Input power|30 W fixed error up to 120 W|±15%|±10%|
|Output voltage|±5%| |±2%|
|Output current|0.8 A fixed error|±15%|±5%|
|Temperature|±5 °C| | |
|Fan speed|Actual ±250 RPM| | |

# PMBus

YES

# Remote ON/OFF

YES

# Timing Specifications

|Description| |Min|Max|Unit|
|---|---|---|---|---|
|Tsb_On|Delay from AC being applied to standby output being within regulation| |2500|ms|
|Tsb_ACOK|Delay from standby output to ACOK assertion| |1500|ms|
|Tsb_Vout|Delay from standby output to main output voltage being within regulation| |1000|ms|
|TAC_On_Delay|Delay from AC being applied to main output being within regulation| |3000|ms|
|TPWR_GOOD_On|Delay from output voltages within regulation limits to PWOK asserted|100|1000 ms| |
|TACOK_Delay|Delay from loss of AC to assertion of ACOK| |20|ms|
|TPWR_GOOD_Hold-up|Delay from loss of AC to deassertion of PWOK|5| |ms|
|TVout_Hold-up|Delay from loss of AC to main output being within regulation|16| |ms|
|Tsb_Hold-up|Delay from loss of AC to standby output being within regulation|25| |ms|
|TPWR_GOOD_Off|Delay from deassertion of PWOK to output falling out of regulation|1|700|ms|
|TPSON_On_Delay|Delay from PSON assertion to output being within regulation| |400|ms|

advancedenergy.com
---
# TIMING DIAGRAM

|AC Input| | | | | | | |
|---|---|---|---|---|---|---|---|
|Vout_stby|T sb_On|T sb_Hold-up|T ACOK_Delay|T sb_Vout|T sb_ACOK|T AC_On_Delay|T Vout_Hold-up|
|Vout_main|T PWOK_On|TPWOK_Off| | | | | |
| |PWOK| | |T PWOK_Hold-up| |T PSON_On_Delay| |
| |PSON| | | | | | |

# MECHANICAL OUTLINE

NOTE - DIMENSIONS ARE

|33/95|4.120-50|10.170200191|129.1820 50|[12960+0.019|3.6I0 -1420.01]|14620.01s1|
|---|---|---|---|---|---|---|
|advancedenergy.com| | | | | | |
---
# DS1100SLPE

|Output Connector Part Number|TEI 2-1926736-2|
|---|---|
|Mating Connector Part Number|TEI 2-1926739-5, 1892787-6 or equivalent|

|Output Connector Pin Configuration| | |
|---|---|---|
|A1|3.3 VSB|Standby Output|
|B1|3.3 VSB|Standby Output|
|C1|3.3 VSB|Standby Output|
|D1|3.3 VSB|Standby Output|
|E1|3.3 VSB|Standby Output|
|A2|SGND|Signal Ground|
|B2|SGND|Signal Ground|
|C2|Reserved| |
|D2|Reserved| |
|E2|Reserved| |
|A3|A2/A_Select|Optional address line|
|B3|A0|I2C Address|
|C3|SDA|I2C Data|
|D3|-Remote_Sense|Wire drop compensation|
|E3|+Remote_Sense|Wire drop compensation|
|A4|SCL|I2C Clock|
|B4|PSON_L|Enable/Inhibit|
|C4|PS_INTERRUPT_L|Alert for failure|
|D4|A1|I2C Address|
|E4|ACOK|Input indicator|
|A5|PSKILL_L|First break/lastmate pin|
|B5|ISHARE|Current share bus|
|C5|PWOK|Output indicator|
|D5|Reserved| |
|E5|PS_PRESENT_L|Power supply present|

|P1-P5|+12 V Return|Main output return contact|
|---|---|---|
|P6-P10|12 V|Main output power contact|

advancedenergy.com 7
---
# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|DS1100SLPE-3|Full power at -5 to 55 °C, can operate up to 65 °C at 660 W derated power|
|---|---|---|
| |DS1100SLPE-3-001|Full power at -5 to 45 °C, can operate up to 55 °C at 660 W derated power|

- Operating relative humidity: 5% to 90% non-condensing
- Operating altitude: up to 10,000 feet
- Non-operating temperature: -40 to +70 °C
- Non-operating relative humidity: 10% to 95% non-condensing
- Non-operating altitude: up to 50,000 feet
- Storage temperature: -40 to +85 °C
- Storage relative humidity: 5% to 95% non-condensing
- Vibration and shock: Standard operating/non-operating random shock and vibration
- RoHS compliance: Yes
- MTBF: >500,000 hours using Telcordia Issue 2, Method 1 Case 1 at 40 °C ambient at full load.
- Operating life: Minimum of 7 years at typical operating conditions
- Reliability: All electronic component derating analysis and capacitor life calculation is done at 40 °C ambient, 80% of maximum rated load, nominal input line voltage.

advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS1100SLPE-235-01 12.14