# ARTESYN DS750PED-3 750 Watts Distributed Power System

Advanced Energy's Artesyn DS750PED-3 series bulk front end AC-DC power supply accepts a wide range 90 to 264 VAC input and provides a main 12 V output plus a 12 V standby output. Rated at 750 watts, it is an 80 Plus Platinum power supply with a peak conversion efficiency of 94%. Housed in a 1U high rack-mounting enclosure with a short form factor that frees up system space, the DS750PED-3 has a high power density of 16 watts per cubic in. This series comes in two airflow versions – dc-connector to ac-connector and vice versa.

|SPECIAL FEATURES|SPECIAL FEATURES|
|---|---|
|750 W output power|Conducted/Radiated EMI Class A Limits + 6 dB margin|
|High-power and short form factor|EN61000-4-11|
|1U power supply|SAFETY|
|High-density design: 16.4 W/in3|UL/cUL|
|Active power factor correction|Demko +CB Report|
|EN61000-3-2 harmonic compliance|CE Mark|
|Inrush current control|UKCA Mark|
|80plus Platinum efficiency|CCC|
|N+1 or N+N redundant|BSMI|
|Hot-pluggable| |
|Active current sharing| |
|Full digital control| |
|PMBus compliant| |
|Accurate input power reporting| |
|Compatible with Artesyn’s Universal PMBus GUI| |
|Reverse airflow option| |
|Two-year warranty| |

# AT A GLANCE

Front-end Bulk Power

Total Output Power: 750 W continuous

Wide Input Voltage: 90 to 264 VAC

80 PLUS PLATINUM

RoHS

©2022 Advanced Energy Industries, Inc.
---
# DS750PED-3

# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|90 to 264 VAC|
|Frequency|47 to 63 Hz|
|Efficiency|94.0% peak|
|Max Input current|10.0 Arms @ 90 VAC|
|Inrush current|55 Apk|
|Conducted EMI|Class A with 6 dB margin|
|Radiated EMI|Class A with 6 dB margin|
|Power factor|>0.9 beginning at 20% load|
|ITHD|10%|
|Leakage current|1.75 mA|
|Hold-up time|10 ms at full load|

| | |Output|Main DC Output| |Standby DC Output| | |
|---|---|---|---|---|---|---|---|
|Nominal setting|-0.20%| |12|0.20%|-1%|12|1%|
|Total output regulation range|11.4 V| | |12.6 V|11.4 V| |12.6 V|
|Dynamic load regulation range|11.4 V| | |12.6 V|11.4 V| |12.6 V|
|Output ripple| | | |120 mVp-p| |120 mVp-p| |
|Output current|0.5 A| | |62.5 A|0.1 A| |3.0 A|
|Current sharing| | |Within ±5% of full load rating| | |N/A| |
|Capacitive loading|2000 uF| | |40000 uF|47 uF| |680 uF|
|Start-up from AC to output| | | |2200 ms| | |1700 ms|
|Output rise time|5 ms| | |50 ms|2 ms| |60 ms|

|Protections|Main Output| | | | | |
|---|---|---|---|---|---|---|
|Overcurrent protection|120%| |150%| | | |
|Overvoltage protection|13.5 V| |15.0 V| | | |
|Undervoltage protection|10.5 V| |11.0 V| | | |
|Overtemperature protection| |Yes| | | | |
|Fan fault protection| |Yes| | | | |

|Standby Output| | | | | | |
|---|---|---|---|---|---|---|
|Overcurrent protection|120%| |150%| | | |
|Overvoltage protection|13.5 V| |15.0 V| | | |
|Undervoltage protection|10.0 V| |11.0 V| | | |
|Autorecovery if the overcurrent is less than 120% and last only for <500 ms| | | | | | |
|Latch mode| | | | | | |
|Standby protection is auto-recovery| | | | | | |

advancedenergy.com
---
# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS750PED-3|12 V @ 62.5 A|12 V @ 3 A|Standard (forward)|
|DS750PED-3-001|12 V @ 62.5 A|12 V @ 3 A|Reverse|

# CONTROL AND STATUS SIGNALS

# Input Signals

PSON_L

Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output. Recommended pull-up resistor to 12VSB is 8.2 kohm with a 3.0 kohm pull-down to ground. A 100 pF decoupling capacitor is also recommended.

| | |MIN|MAX|
|---|---|---|---|
|VIL|Input logic level LOW| |0.8 V|
|VIH|Input logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |2 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.5 mA|

PSKILL_L

First break/last mate active LOW signal which enables/disables the main output. This signal will have to be pulled to ground at the system side with a 220 ohm resistor. A 100 pF decoupling capacitor is also recommended.

| | |MIN|MAX|
|---|---|---|---|
|VIL|Input logic level LOW| |0.8 V|
|VIH|Input logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |2 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.5 mA|

advancedenergy.com 3
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals|
|---|
|ACOK Signal used to indicate the presence of AC input to the power supply. A logic level HIGH will indicate that the AC input to the power supply is within the operating range while a logic level LOW will indicate that AC has been lost. This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.|
|| |MIN|MAX|
|VIL|Input logic level LOW| |0.6 V|
|VIH|Input logic level HIGH|2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| |3.3 mA|
|ISINK|Current that may be sunk by this pin at low state| |0.7 mA|

PWR_GOOD/PWOK

Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold.

This signal also gives an advance warning when there is an impending power loss due to loss of AC input or system shutdown request. More details in the Timing Section.

This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 10 kohm resistor.

| | | | |MIN| |MAX|
|---|---|---|---|---|---|---|
|VIL| |Input logic level LOW| | | |0.8 V|
|VIH| |Input logic level HIGH| |2.0 V| |5.0 V|
|ISOURCE| |Current that may be sourced by this pin| | | |3.3 mA|
|ISINK| |Current that may be sunk by this pin at low state| | | |0.7 mA|

Output Signals

PS_PRESENT

Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is shorted to the standby return in the power supply.

Recommended pull-up resistor to 12 VSB is 8.2 kohm with a 3.0 kohm pull-down to ground. A 100 pF decoupling capacitor is also recommended.

PS_INTERRUPT_L

Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to 12 VSB is 8.2 kohm with a 3.0 kohm pull-down to ground. A 100 pF decoupling capacitor is also recommended.

| | | | | |MIN|MAX|
|---|---|---|---|---|---|---|
|VIL|Input logic level LOW| | | | |0.8 V|
|VIH|Input logic level HIGH| | | |2.0 V|5.0 V|
|ISOURCE|Current that may be sourced by this pin| | | | |4 mA|
|ISINK|Current that may be sunk by this pin at low state| | | | |4 mA|

BUS Signals

ISHARE

Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.

| | | | |MIN|MAX|
|---|---|---|---|---|---|
|ISHARE Voltage|Vshare at 100% load, stand-alone unit| | |7.75|8.25|
| |Voltage at 50% load, stand-alone unit| | |3.85|4.15|
| |Voltage at 0% load, stand-alone unit|0| | |0.3|
|ISOURCE|Current that may be sourced by this pin| | | |160 mA|

SCL, SDA

Clock and data signals defined as per IC requirements. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 100 pF decoupling capacitor at the system side.

| | | | | |MIN|MAX|
|---|---|---|---|---|---|---|
|VL|Input logic level LOW| | | | |0.8 V|
|VH|Input logic level HIGH| | | |2.0 V|5.0 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 to 100 MHz.

IC Addressing Table: Not applicable. This power supply has a fixed IC address. In order to support multiple addresses, the system will have to utilize a switcher or an IC expander.

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS

LED Indicators

Status LEDNo AC input to PSUMain output ONStandby mode or Power supply failure (OCP, OVP, OTP, FAN FAULT)Off when stand-alone, blinking AMBER when in parallelSolid GREENBlinking AMBER

Firmware Reporting And Monitoring

|Accuracy Range|5 to 20%|20 to 50%| |50 to 100%|
|---|---|---|---|---|
|Input voltage| |±5%| | |
|Input current|±0.55 A fixed error| |±4%| |
|Input power|±1.25 W at <125 W input| |±1.25%| |
|Output voltage| |±2%| | |
|Output current|0.3 A fixed error| |±2%| |
|Temperature| |±5°C on the operating range| | |
|EIN|±15% from 10% to 20% load| |±5%| |
|Fan speed| |Actual RPM ± 250 RPM| | |

PMBus: YES

Remote ON/OFF: YES

Timing Specifications

|Description|Min|Max|Unit|
|---|---|---|---|
|Tsb_On|Delay from AC being applied to standby output being within regulation|20|1700 ms|
|Tsb_ACOK|Delay from standby output to ACOK assertion|See note below|20 ms|
|Tsb_Vout|Delay from standby output to main output voltage being within regulation| |300 ms|
|TAC_On_Delay|Delay from AC being applied to main output being within regulation| |2200 ms|
|TPWR_GOOD_On|Delay from output voltages within regulation limits to PWOK asserted|100|1000 ms|
|TACOK_Delay|Delay from loss of AC to assertion of ACOK|6|ms|
|TPWR_GOOD_Hold-up|Delay from loss of AC to deassertion of PWOK|10|ms|
|TVout_Hold-up|Delay from loss of AC to main output being within regulation|11|ms|
|Tsb_Hold-up|Delay from loss of AC to standby output being within regulation|150|ms|
|TPWR_GOOD_Off|Delay from deassertion of PWOK to output falling out of regulation|1|ms|
|TPSON_On_Delay|Delay from PSON assertion to output being within regulation|350|ms|
|TPWOK_Low|Duration of PWOK being in deasserted state during an ON/OFF cycle of PSU|N/A|N/A|

Note:

Tvout_hold-up: tested at 1A load on standby output

Tsb_ACOK: ACOK can assert earlier than the standby output

advancedenergy.com 5
---
# DS750PED-3

# TIMING DIAGRAM

|AC Input|Tsb_On|Tsb_Hold-up| | |
|---|---|---|---|---|
|Vout_stby|Tsb_Vout| | | |
|ACOK|TAC_On_Delay|TVout_Hold-up| | |
|Vout_main|TPWOK_On| |TPWOK_Off| |
| | |PWOK|TPWOK_Hold-up|TPSON_On_Delay|
| | | |PSON| |

# ENVIRONMENTAL SPECIFICATIONS

Operating temperature: 0 to 50°C, withstand operation up to 60°C at full power without damage

Operating altitude: up to 10,000 feet

Operating relative humidity: 20% to 80% non-condensing

Non-operating temperature: -40 to +70°C

Non-operating relative humidity: 10% to 95% non-condensing

Non-operating altitude: up to 50,000 feet

Vibration and shock: Standard operating/non-operating random shock and vibration

ROHS compliance: Yes

MTBF: 200,000 hours per Telcordia Issue 2, Method 1, Case 3 at 25°C ambient at full load.

Operating life: Minimum of 5 years

Reliability: All electronic component derating analysis and capacitor life calculation is done at maximum ambient, 80% of maximum rated load, nominal input line voltage.

advancedenergy.com
---
# DS750PED-3

86,3±0.5
38,5±0.5

# MECHANICAL OUTLINE

|17,8|9,5| |
|---|---|---|
|9,3±0.3|4±0.2|9,5|

# STD (FORWARD) AIRFLOW

8
9,4

9±0.5
196,5±0.5
1,5
40,2

# MODEL LABEL

15±0.3

190,9±0.5

202,9
61,9
0,6

14,2±0.8

advancedenergy.com 7
---
# CONNECTOR DEFINITIONS

|Output Connector Part Number|Mating Connector Part Number|Card-edge|
|---|---|---|
|Power Supply Output Card Edge (Top Side)|FCI 10107844-002LF or equivalent| |
|Power Supply Output Card Edge (Bottom Side)| | |
|Power Supply Output Card Edge (Bottom Side)| | |
|S24|S13| |
|P29-P36|P21-28| |
| | | |
|P1-P8|P9-P18| |
| | | |
|S1|S12| |

# Output Connector Pin Configuration

|S1|PS PRESENT|S13|PS_ON_L|
|---|---|---|---|
|S2|Reserved|S14|PS_KILL_L|
|S3|Reserved|S15|Reserved|
|S4|Pwr_Good (PWOK)|S16|RETURN|
|S5|ACOK (AC Input Present)|S17|SDA|
|S6|RETURN|S18|RETURN|
|S7|ISHARE|S19|SCL|
|S8|RESERVE|S20|RETURN|
|S9|PS INTERRUPT_L|S21|REMOTE SENSE-|
|S10|RETURN|S22|RETURN|
|S11|Reserved|S23|REMOTE SENSE+|
|S12|Reserved|S24|RESERVE|
|P1-P8|Vo|P19-P20|VSB|
|P9-P18|RTN|P21-P28|RTN|
| | |P29-P36|Vo|
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2022 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS750PED-235-01 5.10