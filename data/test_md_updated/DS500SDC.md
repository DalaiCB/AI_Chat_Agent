# ARTESYN DS500SDC 500w RTN 48V

500 Watts Distributed Power System

Advanced Energy's Artesyn DS500SDC-3 series bulk front end DC-DC power supply accepts a wide range -36 to -72 VDC input and provides a main 12 V output plus a 12 V standby output. It is rated at 500 watts. Housed in a 1U high rack-mounting enclosure with a short form factor that frees up system space, the DS500SDC-3 has a power density of 10.9 watts per cubic inch. This series comes in two airflow versions – dc-connector to ac-connector and vice versa. The series is also in the same form factor and has the same output configuration as the DS500SPE-3.

|SPECIAL FEATURES|COMPLIANCE|
|---|---|
|500 W output power|UL/cUL 60950 (UL Recognized)|
|High power and short form factor|DEMKO+ CB Report EN60950|
|1U power supply|EN60950|
|High-density design: 12 W/in 3|CE Mark|
|Inrush current control|China CCC|
|N+1 or N+N redundant| |
|Active current sharing| |
|Full digital control| |
|PMBus compliant| |
|Compatible with Artesyn’s Universal PMBus GUI| |
|Reverse airflow available| |
|Two-year warranty| |
|EMI Conducted/Radiated Class A Limits| |

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|-36 to -72 Vdc|
|Efficiency|90.0% peak|
|Max input current|17.5 Arms|
|Inrush current|55 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Hold-up time|1 ms at full load|

| | |Output|Main DC Output| |Standby DC Output| | |
|---|---|---|---|---|---|---|---|
| |MIN| |NOM|MAX|MIN|NOM|MAX|
|Nominal setting| |-0.20%|12|0.20%|-1%|12|1%|
|Total output regulation range| |11.4 V| |12.6 V|11.4 V| |12.6 V|
|Dynamic load regulation range| |11.4 V| |12.6 V|11.4 V| |12.6 V|
|Output ripple| | | |120 mVp-p| |120 mVp-p| |
|Output current|2 A| | |41.67 A|0.1 A| |3.0 A|
|Current sharing| | |Within ±5% of full load rating| | |N/A| |
|Capacitive loading| |2000 μF| |40,000 μF|47 uF| |680 μF|
|Startup from AC to output| | | |2200 ms| | |1700 ms|
|Output rise time|5 ms| | |50 ms|2 ms| |60 ms|

|Protections|MIN|NOM|MAX| | |
|---|---|---|---|---|---|
|Main Output| | | | | |
|Overcurrent protection|120%| | | |150%|
|Overvoltage protection|13.5 V| | | |15.0 V|
|Undervoltage protection|10.5 V| | | |11.0 V|
|Overtemperature protection| |Yes| | | |
|Fan fault protection| |Yes| | | |

|Standby Output| | | |
|---|---|---|---|
|Overcurrent protection|120%| |150%|
|Overvoltage protection|13.5 V| |15.0 V|
|Undervoltage protection|10.0 V| |11.0 V|

1 Latch mode

2 Autorecovery if the overcurrent is less than 120% and last only for &lt;500 ms

3 Standby protection is auto-recovery
---
# Electrical Specifications (Continued)

LED Indicators

| |Status LED|
|---|---|
|No DC input to PSU|Off|
|Main output ON|Solid GREEN|
|Standby mode or Power supply failure (OCP, OVP, OTP, FAN FAULT:)|Blinking AMBER|

Firmware Reporting And Monitoring

|Accuracy Range|5 to 20%|20 to 50%|50 to 100%|
|---|---|---|---|
|Output loading|±2%|±4%| |
|Input voltage|±0.55 A fixed error| | |
|Input power|±1.25 W at < 125 W input|±1.25%| |
|Output voltage| |±2%| |
|Output current|0.3 A fixed error|±2%| |
|Temperature| |±5 °C on the operating range| |
|E IN|±15% from 10% to 20% load|±5%| |
|Fan speed| |Actual RPM ±250 RPM| |
|PMBus| |YES| |
|Remote ON/OFF| |YES| |

Timing Specifications

|Description| |Min|Max|Unit|
|---|---|---|---|---|
|Tsb_On|Delay from DC input being applied to standby output being within regulation|20|1700 ms| |
|Tsb_INPUT_OK|Delay from standby output to INPUT_OK assertion|See note below|20 ms| |
|Tsb_Vout|Delay from standby output to main output voltage being within regulation|300 ms| | |
|T INPUT_On_Delay|Delay from DC input being applied to main output being within regulation|2200 ms| | |
|T PWR_GOOD_On|Delay from output voltages within regulation limits to PWOK asserted|100|1000 ms| |
|T INPUT_OK_Delay|Delay from loss of DC input to assertion of INPUT_OK|6 ms| | |
|T PWR_GOOD_Hold-up|Delay from loss of DC input to deassertion of PWOK|0.1|0.2 ms| |
|T Vout_Hold-up|Delay from loss of DC input to main output being within regulation|1 ms| | |
|Tsb_Hold-up|Delay from loss of DC input to standby output being within regulation|150 ms| | |
|T PWR_GOOD_Off|Delay from deassertion of PWOK to output falling out of regulation|1 ms| | |
|T PSON_On_Delay|Delay from PSON assertion to output being within regulation|350 ms| | |
|T PWOK_Low|Duration of PWOK being in deasserted state during an ON/OFF cycle of PSU|N/A|N/A| |

Note: Tsb_hold-up: tested at 1A load on standby output, and 0A load on main output. Tsb_INPUT_OK: INPUT_OK can assert earlier than the standby output

advancedenergy.com 3
---
# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|DS500SDC-3: 500 W from 0 °C to 50 °C DS500SDC-3-001: 500 W from 0 °C to 40 °C|
|---|---|
|Operating altitude|up to 10,000 feet with derating|
|Operating relative humidity|10% to 80% non-condensing|
|Non-operating temperature|-40 °C to +70 °C|
|Non-operating relative humidity|10% to 95% non-condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating/non-operating shock/vibration|

ROHS compliance: YES

MTBF: 1,000,000 hours per Telcordia Issue 3, Method 1, Case 3 at 50 °C at full load.

Operating life: Minimum of 5 years

Reliability: All electronic component derating analysis is done at maximum ambient, 80% of maximum rated load, nominal input line voltage.

# TIMING DIAGRAM

| |DC Input| | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Tsb_On|Tsb_Hold-up|TInput_Delay|Vout_stby|Tsb_Vout|Tsb_INPUT_OK|INPUT_OK|TInput_On_Delay|TPWOK_Off|Vout_main|TPWOK_On|TPWOK_Off|PWOK|T PWOK_Hold-up|TPSON_On_Delay|PSON|

advancedenergy.com
---
# CONTROL AND STATUS SIGNALS

# Input Signals

|Signal|Description|MIN|MAX|
|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.| | |
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |2 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.5 mA|
|PSKILL_L|First break/last mate active LOW signal which enables/disables the main output. This signal will have to be pulled to ground at the system side with a 220 ohm resistor. A 100 pF decoupling capacitor is also recommended.| | |
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |2 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.5 mA|

# Output Signals

|Signal|Description|MIN|MAX|
|---|---|---|---|
|INPUT_OK|Signal used to indicate the presence of DC input to the power supply. A logic level HIGH will indicate that the DC input to the power supply is within the operating range while a logic level LOW will indicate that DC input has been lost. This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | |
|V IL|Input logic level LOW| |0.6 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |3.3 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.7 mA|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of DC input or system shutdown request. More details in the Timing Section. This is an open collector/drain output. This pin is pulled high by a 1.0 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 10 kohm resistor.| | |
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |3.3 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.7 mA|

advancedenergy.com
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| | | | | | |
|---|---|---|---|---|---|---|
|PS_PRESENT_L|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is shorted to the standby return in the power supply. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.| | | | | |
|PS_INTERRUPT_L|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.| | | | | |
|V IL|Input logic level LOW| | | | |0.8 V|
|V IH|Input logic level HIGH| | | |2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| | | | |4 mA|
|I SINK|Current that may be sunk by this pin at low state| | | | |4 mA|
|BUS Signals| | | | | | |
|ISHARE|Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.| | | | | |
|Voltage Range| | |The range of this signal for active sharing will be up to 8.0 V, which corresponds to the maximum output current.| | | |
|I SHARE Voltage|Input logic level LOW| | | |7.75|8.25|
| |Voltage at 50% load, stand-alone unit| | | |3.85|4.15|
| |Voltage at 0% load, stand-alone unit|0| | | |0.3|
|I SOURCE|Current that may be sourced by this pin| | | | |160 mA|
|SCL, SDA|Clock and data signals defined as per I C requirements. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 100 pF decoupling capacitor at the system side.| | | | | |
|VL|Input logic level LOW| | | | |0.8 V|
|VH|Input logic level HIGH| | | |2.0 V|5.0 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 - 100 MHz.

I2C Addressing Table: Not applicable. This power supply has a fixed I2C address. In order to support multiple addresses, the system will have to utilize a switcher or an I2C expander.

advancedenergy.com
---
# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS500SDC-3|12 V|12 V @ 3A|Std (forward)|
|DS500SDC-3-001|12 V|12 V @ 3A|Reverse|

1 Derating may apply

# MECHANICAL DRAWING

AIRFLOW DIRECTION

Standard (Forward)

WATTAGE LABEL

SECTION A-A

advancedenergy.com 7
---
# CONNECTOR DEFINITIONS

|Output Connector Part Number|Card-edge Mating Connector Part Number|
|---|---|
|Power Supply Output Card Edge (Top Side)|FCI 10107844-002LF or equivalent|
|Power Supply Output Card Edge (Bottom Side)|Molex 394210002|
|Power Supply Output Card Edge (Bottom Side)|Molex 394250002|

# OUTPUT CONNECTOR PIN CONFIGURATION

|S1|PS PRESENT|S13|PS_ON|
|---|---|---|---|
|S2|Reserved|S14|PS_KILL|
|S3|Reserved|S15|Reserved|
|S4|Pwr_Good|S16|RTN|
|S5|ACOK (AC Input Present)|S17|SDA|
|S6|RTN|S18|RTN|
|S7|I-SHARE|S19|SCL|
|S8|RESERVE|S20|RTN|
|S9|PS INTERRUPT_L|S21|REMOTE SENSE-|
|S10|RTN|S22|RTN|
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

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS500SDC-235-01 12.10