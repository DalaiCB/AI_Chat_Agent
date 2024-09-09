# ARTESYN DS1600SPE 1600 Watts Distributed Power System

Advanced Energy's Artesyn DS1600SPE is an ultra-high density power supply providing 35 W per cubic inch. The 1600 W DS1600SPE power supply is housed in 1U high rack-mounting enclosures measuring just 3.4 x 7.7 in (86.3 x 196.5 mm). This form factor is significantly shorter than that of similarly rated earlier-generation power supplies — freeing up valuable system space — and is achieved by use of the latest power switching technology and high density component packaging techniques.

# SPECIAL FEATURES

|1600 W output power at high line|Class A + 6 dB margin Conducted/ Radiated EMI|
|---|---|
|High power and short form factor|RoHS compliant|
|1U power supply|UL/cUL 62368 (UL Recognized)|
|High density design: 40 W/in3|NEMKO+ CB Report EN62368|
|Active power factor correction|EN62368|
|EN61000-3-2 harmonic compliance|CE Mark|
|Inrush current control|China CQC|
|80PLUS platinum efficiency|UKCA Mark|
|N+1 or N+N redundant| |
|Active current sharing| |
|Full digital control| |
|PMBus compliant| |
|Compatible with Artesyn’s universal PMBus GUI| |
|Reverse airflow option| |
|Two-year warranty| |

# AT A GLANCE

Front-end Bulk Power

Total Output Power: 1600 W continuous at high line

Wide Range Input Voltage: 90 to 264 VAC

80 PLUS PLATINUM

©2022 Advanced Energy Industries, Inc.
---
# DS1600SPE

|ELECTRICAL SPECIFICATIONS| | |
|---|---|---|
|Input| | |
|Input voltage range|180 to 264 VAC: 1600 W| |
| |90 to 140 VAC: 800 W| |
|Frequency|47 Hz to 63 Hz| |
|Efficiency|94.0% peak| |
|Max input current|10.8 Arms| |
|Inrush current|55 Apk| |
|Conducted EMI|Class A| |
|Radiated EMI|Class A| |
|Power factor|> 0.9 beginning at 20% load| |
|ITHD|10%| |
|Leakage current|1.75 mA| |
|Hold-up time|10 ms| |

# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS1600SPE-3|12 V @ 133.3 A|12 V @ 3.5 A|Standard (forward)|
|DS1600SPE-3-001|12 V @ 133.3 A|12 V @ 3.5 A|Reverse|

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS

|Output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal setting|-0.20%|12|0.20%|
|Total output regulation range|11.4 V| |12.6 V|
|Dynamic load regulation range|11.4 V| |12.6 V|
|Output ripple| | |150 mVp-p|
|Output current|2 A1| |133.33 A|
|Current sharing|Within +/-5% of full load rating| | |
|Capacitive loading|2,250 μF| |14,000 μF|
|Start-up from AC to output| | |2,300 ms|
|Output rise time|2 ms| |60 ms|

|Standby DC Output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal setting|-3%|12|3%|
|Total output regulation range|11.4 V| |12.6 V|
|Dynamic load regulation range5|11.4 V| |12.6 V|
|Output ripple| | |150 mVp-p|
|Adjustment range|N/A| | |
|Output current|0.1 A1| |3.5 A|
|Current sharing|N/A| | |
|Capacitive loading|47 μF| |1,000 μF|
|Start-up from AC to output|20 ms| |2,000 ms|
|Output rise time|2 ms| |60 ms|

|Protections| | | |
|---|---|---|---|
|Main Output| | | |
|Overcurrent protection|115%| |150%|
|Overvoltage protection|13.5 V| |15.0 V|
|Undervoltage Protection|10.5 V| |11.0 V|
|Overtemperature protection| |Yes| |
|Fan fault protection| |Yes| |
|Standby Output| | | |
|Overcurrent Protection|120%| |150%|
|Overvoltage Protection3|13.5 V| |15.0 V|
|Undervoltage Protection|10.0 V| |11.0 V|

1 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load.

2 Autorecovery if the overcurrent is less than 115% and last only for < 500 ms.

3 Latch mode

4 Standby protection is auto-recovery

5 Maximum step size of 67 A at 0.5A/μs, with a beginning load of 8 A, and 3,350 μF capacitance.

advancedenergy.com 3
---
# CONTROL AND STATUS SIGNALS

# Input Signals

|Signal|Description|MIN|MAX|
|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output. System Side pull-up resistor is not required.| | |
|VIL|Input logic level LOW| |0.8 V|
|VIH|Input logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |2 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.5 mA|
|PSKILL_H|First break/last mate active HIGH signal which enables/disables the main output. This signal will have to be pulled to ground at the system side.| | |
|VIL|Input logic level LOW. This allows for the power supply to be turned on| |0.8 V|
|VIH|Input logic level HIGH. Immediately shuts down the power supply|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |2 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.5 mA|
|VSENSE+, VSENSE-|VSENSE+ and VSENSE- lines are the remote sense lines for regulation. Each line will compensate for a maximum of 200 mV.| | |

# Output Signals

|Signal|Description|MIN|MAX|
|---|---|---|---|
|ACOK|Signal used to indicate the presence of AC input to the power supply. A logic level HIGH will indicate that the AC input to the power supply is within the operating range while a logic level LOW will indicate that AC has been lost. This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | |
|VIL|Output logic level LOW| |0.6 V|
|VIH|Output logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |3.3 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.7 mA|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of AC input or system shutdown request. More details in the Timing Section. This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 10 kohm resistor.| | |
|VIL|Output logic level LOW| |0.8 V|
|VIH|Output logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |3.3 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.7 mA|
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

Output Signals

|PS_PRESENT|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is shorted to the standby return in the power supply. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.|
|---|---|
|PS_INTERRUPT|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.|

| | |MIN|MAX|
|---|---|---|---|
|VIL|Output logic level LOW| |0.8 V|
|VIH|Output logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |4 mA|
|ISINK|Current that may be sunk by this pin at low state| |4 mA|

Bus Signals

ISHARE
Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.

| | |MIN|MAX|
|---|---|---|---|
|ISHARE Voltage|Voltage at 100% load, stand-alone unit|7.75|8.25|
| |Voltage at 50% load, stand-alone unit|3.85|4.15|
|ISOURCE|Current that may be sourced by this pin| |160 mA|

SCL, SDA, A0, A1, A2

Clock, data and addressing signals defined as per I2C requirements. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 22 pF decoupling capacitor at the system side.

| | |MIN|MAX|
|---|---|---|---|
|VL|Logic level LOW| |0.8 V|
|VH|Logic level HIGH|2.0 V|5.0 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 to 100 MHz.

# I2C Addressing Table

|A2|A1|A0|PMBus (W/R)|FRU (W/R)|
|---|---|---|---|---|
|0|0|0|B0/B1|A0/A1|
|0|0|1|B2/B3|A2/A3|
|0|1|0|B4/B5|A4/A5|
|0|1|1|B6/B7|A6/A7|
|1|0|0|B8/B9|A8/A9|
|1|0|1|BA/BB|AA/AB|
|1|1|0|BC/BD|AC/AD|
|1|1|1|BE/BF|AE/AF|

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS

|LED Indicators|Status LED|
|---|---|
|No AC input to PSU|Off|
|Main output ON|Solid GREEN|
|Standby mode and Power supply failure (OCP, OVP, OTP, FAN FAULT)|Blinking AMBER|

|Firmware Reporting And Monitoring|Accuracy Range| | | |
|---|---|---|---|---|
|Output loading|8% to 20%|20% to 50%| |50% to 100%|
|Input voltage| |±5%| | |
|Input current|±0.55A| |±5%| |
|Input power|±5 W at < 125 W input power| |±1.25%| |
|Output voltage| |±2%| | |
|Output current|±1.2 A fixed error| |±3%| |
|Temperature| |±5 degC on the operating range| | |
|EIN|±15% from 10% to 20% load| |±5%| |
|Fan speed| |±250 RPM| | |

PMBus: YES

Remote ON/OFF: YES
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

| |Description|Min|Max|Unit|
|---|---|---|---|---|
|Tsb_On|Delay from AC being applied to standby output being within regulation|20|2000|ms|
|Tsb_ACOK|Delay from standby output to ACOK assertion|See note below|20|ms|
|Tsb_Vout|Delay from standby output to main output voltage being within regulation| |300|ms|
|TAC_On_Delay|Delay from AC being applied to main output being within regulation| |2300|ms|
|TPWOK_On|Delay from output voltages within regulation limits to PWOK asserted|100|1000|ms|
|TACOK_Delay|Delay from loss of AC to assertion of ACOK|7| |ms|
|TPWOK_Hold-up|Delay from loss of AC to deassertion of PWOK|10| |ms|
|TVout_Hold-up|Delay from loss of AC to main output being within regulation|11| |ms|
|Tsb_Hold-up|Delay from loss of AC to standby output being within regulation|150| |ms|
|TPWR_GOOD_Off|Delay from deassertion of PWOK to output falling out of regulation|1| |ms|
|TPSON_On_Delay|Delay from PSON assertion to output being within regulation| |150|ms|
|TPWOK_Low|Duration of PWOK being in deasserted state during an ON/OFF cycle of PSU|N/A|N/A| |

Note:

Tsb_hold-up: tested at 1 A load on standby output

Tsb_ACOK: ACOK can assert earlier than the standby output

advancedenergy.com

7
---
|DS1600SPE| | |
|---|---|---|
|TIMING DIAGRAM| | |
|AC Input| | |
|Vout_stby|T sb_On| |
| |T sb_Hold-up| |
| |T ACOK_Delay| |
|ACOK|T sb_Vout| |
| |T sb_ACOK| |
|Vout_main|T AC_On_Delay| |
| |T Vout_Hold-up| |
|PWOK|T PWOK_On| |
| |TPWOK_Off| |
|PSON|T PWOK_Hold-up| |
| |T PSON_On_Delay| |
|advancedenergy.com| | |
---
# MECHANICAL OUTLINE

| | | |DS1600SPE| |
|---|---|---|---|---|
| |191.1±0.5| |(14.8)| |
|6±0.3| |8.8±0.5|A| |
| | | |9.3±0.4| |
|C| | | | |
|40.25±0.7| |38.5+0.9-0.5|B| |
| |196.5| |(4)| |
|C|DIM AND TOL NEED TO BE HELD AT THE EDGE OF THE STANDOFF LOCATIONS ONLY.| | | |

|MODEL|AIRFLOW DIRECTION| | | |
|---|---|---|---|---|
|DS1600SPE-3|FORWARD| | | |
|DS1600SPE-3-001|REVERSE|40.2±0.5| | |
| | |B|86.3±0.5|A|

advancedenergy.com
---
# CONNECTOR DEFINITIONS

|Output Connector Part Number|Card-edge Mating Connector Part Number|
|---|---|
|FCI 10107844-002LF or any equivalent| |

|Power Supply Output Card Edge (Top Side)|Power Supply Output Card Edge (Bottom Side)|
|---|---|
| | |
|Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Top Side)|
|S24|S13|
|P29-P36|P21-28|
|P19/20|P1-P8|
| |P9-P18|
| |S1|
| |S12|

# Output Connector Pin Configuration

|S1|PS_PRESENT|S13|PS_ON_L|
|---|---|---|---|
|S2|A1|S14|PSKILL_H|
|S3|A0|S15|RESERVED|
|S4|PWR_GOOD (PWOK)|S16|RTN|
|S5|ACOK (AC Input Present)|S17|SDA|
|S6|RTN|S18|RTN|
|S7|I_SHARE|S19|SCL|
|S8|RESERVED|S20|RTN|
|S9|PS_INTERRUPT_L|S21|REMOTE SENSE -|
|S10|RETURN|S22|RTN|
|S11|RESERVED|S23|REMOTE SENSE +|
|S12|RESERVED|S24|A2|
|P1-P8|+12VOUT|P19-P20|+VSB|
|P9-P18|RETURN|P21-P28|RETURN|
| | |P29-P36|+12VOUT|

advancedenergy.com
---
# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|DS1600SPE-3: 1600 W from 0 to 50°C, can operate up to 65°C at 2% derated power for every °C above 50°C|
|---|---|
| |DS1600SPE-3-001: 1600 W from 0 to 40°C, can operate up to 60°C at 1% derated power for every °C above 40°C|
|Operating altitude|up to 16,400 feet, derated after 10,000 feet|
|Operating relative humidity|5% to 95% non-condensing|
|Non-operating temperature|-40 to +70°C|
|Non-operating relative humidity|5% to 95% non-condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating and non-operating random shock and vibration|
|ROHS compliance|Yes|
|MTBF|1,100,000 hours using Bell Core TR-332, issue 6 specification, Method 1 Case 3 at 25°C ambient at full load.|
|Operating life|Minimum of 5 years|

advancedenergy.com 11
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2022 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS1600SPE-235-02 4.26