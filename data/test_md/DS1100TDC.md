# ARTESYN DS1100TDC 1100 Watts Distributed Power System

Advanced Energy's Artesyn DS1100TDC series bulk front end DC-DC power supply accepts a wide range -40 to -72 Vdc input and provides a main 12 V output plus a 3.3 V standby output. Housed in an industry standard 1U x 2.1 inch rack-mounting package and able to deliver 1,100W, the power supply is ideal for space-constrained applications. This series comes in two airflow versions – output-connector to input-connector and vice versa.

# Front-end Bulk Power

|Total Output Power:|1100 W continuous|
|---|---|
|Wide Input Voltage:|-40 to -72 Vdc|

# SPECIAL FEATURES

- 1100 W output power
- High-power and short form factor
- 1U power supply
- High density design: 26 W/in 3
- Inrush current control
- N+1 or N+N Redundant
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus compliant
- Compatible with Artesyn’s Universal PMBus GUI
- Reverse airflow option
- Two-year warranty

# COMPLIANCE

- EMI Conducted/Radiated Class ALimits + 6 dB margin PMRTS
- EN61000-4 Electro-magnetic Compatibility
- RoHS 6/6

# SAFETY

- UL/cUL 60950
- DEMKO+ CB Report
- CE Mark
- China CCC

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|-40 to -72 Vdc|
|Efficiency|90.0% typical|
|Max input current|37.0 Arms|
|Inrush current|ETSI EN 300 132-2 Limits|
|Conducted EMI|Class A +6 dB margin|
|Radiated EMI|Class A +6 dB margin|
|Hold-up time|1 ms at full load|

| | |Output|Main DC Output| |Standby DC Output| |
|---|---|---|---|---|---|---|
| |MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting|-1%|12|+1%|-2.5%|3.3|2.5%|
|Total output regulation range|11.4 V|12|12.6 V|3.14 V|3.3|3.46 V|
|Dynamic load regulation range|11.4 V| |12.6 V|3.14 V| |3.46 V|
|Output ripple| | |180 mVp-p| | |45 mVp-p|
|Output current|0.5 A| |91.6 A|0.1 A| |3.0 A|
|Current sharing|Within ±5.625A of each other from 25% to 100% load| | | |N/A| |
|Capacitive loading|500 μF| |11,000 μF|100 μF| |680 μF|
|Start-up from AC to output| | |3000 ms| | |2500 ms|
|Output rise time|5 ms| |100 ms| | |100 ms|

Note: Outputs shall be isolated from the chassis ground by at least 50 V

1 Minimum starting current for transient load response testing only. Unit is designed to operate and be within output regulation at zero load.

|Protections| |MIN|NOM|MAX| | |
|---|---|---|---|---|---|---|
|Main Output| | | | | | |
|Overcurrent protection| |107%| | | |130%|
|Overvoltage protection| |13.5 V| | | |14.5 V|
|Overtemperature protection| | | |Yes, autorecovery| | |
|Fan fault protection| | | |Yes| | |
|Standby Output| | | | | | |
|Overcurrent protection| |107%| | | |150%|
|Over-voltage protection| |3.6 V| | | |4.1V|

1 Latch mode

2 Autorecovery for 5s then latch

3 Autorecovery

advancedenergy.com
---
# DS1100TDC

# CONTROL AND STATUS SIGNALS

|Input Signals| | | | |
|---|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | |
|V IL|Input logic level LOW| | |0.8 V|
|V IH|Input logic level HIGH|2.0 V| |3.6 V|
|I SOURCE|Current that may be sourced by this pin| | |4 mA|
|I SINK|Current that may be sunk by this pin at low state| | |4 mA|
|PSKILL_H|First break/last mate active HIGH signal which enables/disables the main output. This signal will have to be pulled to ground at the system side with a 100 ohm resistor. A 100 pF decoupling capacitor is also recommended.| | | |
|V IL|Input logic level LOW| | |0.8 V|
|V IH|Input logic level HIGH|2.0 V| |3.6 V|
|I SOURCE|Current that may be sourced by this pin| | |4 mA|
|I SINK|Current that may be sunk by this pin at low state| | |4 mA|
|VSENSE+, VSENSE-|VSENSE+ and VSENSE- lines are the remote sense lines for regulation. Each line will compensate for a maximum of 200 mV.| | | |

# IC ADDRESSING

|A1 Pin|A0 Pin|PMBus (w/r)|
|---|---|---|
|0|0|B0/B1|
|0|1|B2/B3|
|1|0|B4/B5|
|1|1|B6/B7|

* For additional addressing options, please contact techsupport

# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS1100TDC-3|12 V|3.3 V @ 3 A|Std (forward)|
|DS1100TDC-3-001|12 V|3.3 V @ 3 A|Reverse|

advancedenergy.com
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| | | | | | | | |
|---|---|---|---|---|---|---|---|---|
|INPUT_OK|Signal used to indicate the presence of DC input to the power supply. A logic level HIGH will indicate that the DC input to the power supply is within the operating range while a logic level LOW will indicate that input has been lost. This is an open collector/drain output. This pin is pulled high by a 1 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 200 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | | | | | | |
|VOH|Output high voltage| | | | |MIN| |MAX|
| | | | | | |2.4 V| |3.6 V|
|VOL|Output low voltage| | | | | | |0.4 V|
|I SOURCE|Output signal source current| | | | | | |2 mA|
|I SINK|Output signal sink current| | | | | | |4 mA|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of DC input or system shutdown request. More details in the Timing Section. This is an open collector/drain output. This pin is pulled high by a 1 kohm resistor connected to 3.3 V inside the power supply. It is recommended that this pin be connected to a 100 pF decoupling capacitor and pulled down by a 100 kohm resistor.| | | | | | | |
|VOH|Output high voltage| | | | |MIN| |MAX|
| | | | | | |2.4 V| |3.6 V|
|VOL|Output low voltage| | | | | | |0.4 V|
|I SOURCE|Output signal source current| | | | | | |2 mA|
|I SINK|Output signal sink current| | | | | | |4 mA|
|PS_PRESENT|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is connected via a 220 ohm resistor to the standby return in the power supply. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | | | | | |
|PS_INTERRUPT|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to VSB is 5.1 kohms. A 100 pF decoupling capacitor is also recommended.| | | | | | | |
|VOH|Output high voltage| | | | |MIN| |MAX|
| | | | | | |2.4 V| |3.6 V|
|VOL|Output low voltage| | | | | | |0.4 V|
|I SOURCE|Current that may be sourced by this pin| | | | | | |4 mA|
|I SINK|Current that may be sunk by this pin at low state| | | | | | |4 mA|

# BUS Signals

|ISHARE| | | | | | | | |
|---|---|---|---|---|---|---|---|---|
|Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.| | | | | | | | |
|Voltage Range| | |The range of this signal for active sharing will be up to 8.0 V, which corresponds to the maximum output current.| | | | | |
|I SHARE Voltage|Input logic level LOW| | | | |MIN| |MAX|
| | | | | | |7.75| |8.25|
| |Voltage at 50% load, stand-alone unit| | | | |MIN| |MAX|
| | | | | | |3.85| |4.15|
| |Voltage at 0% load, stand-alone unit| | | | |MIN| |MAX|
| | |0| | | | | |1.0|
|I SOURCE|Current that may be sourced by this pin| | | | | | |4.0 mA|
|SCL, SDA|Clock and data signals defined as per I C requirements. These pins are pulled high internally to 3.3V by a 100kohm resistor. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 200 pF decoupling capacitor at the system side.| | | | | | | |
|VL|Input logic level LOW| | | | | | |0.8 V|
|VH|Input logic level HIGH| | | | |MIN| |MAX|
| | | | | | |2.0 V| |3.6 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 - 100 MHz.
---
# DS1100TDC

# ELECTRICAL SPECIFICATIONS

|LED Indicators|Color|Input LED|Fail LED|
|---|---|---|---|
|No input to PSU|Off|Off| |
|Input present, STBY ON, main output OFF|On|Blinking Amber, at least 1 Hz| |
|Main output ON|On|Green| |
|Power supply warning (hi-temp)|On|Blinking Amber/Green, at 2:1 ratio, at least 1 Hz| |
|Power supply warning (slow fan)|On|Blinking Amber/Green, at 1:1 ratio, at least 1 Hz| |
|Power supply failure (OVP, OTP, FAN FAULT)|On|Amber| |

# Firmware Reporting And Monitoring

|Accuracy Range|Output loading|Input voltage|Input current|Input power|Output voltage|Output current|Temperature|Fan speed|
|---|---|---|---|---|---|---|---|---|
|5% to 20%| |±5%|±0.55 A fixed error|±5 W fixed error up to 120 W input|±2%|±0.8 A fixed error|±5 °C across operating range|±250 RPM|
|20% to 50%| | |±4%| | |±5%| | |
|50% to 100%| | | | | |±2%| | |

PMBus: YES

Remote ON/OFF: YES

# Timing Specifications

|Description|Min|Max|Unit|
|---|---|---|---|
|Tsb_On| |2500|ms|
|T INPUT_OK_ON| |1500|ms|
|Tsb_Vout| |1000|ms|
|T INPUT_On_Delay| |3000|ms|
|T PWOK_On|100|1000|ms|
|T INPUT_OK_Delay| |20|ms|
|T PWOK_Hold-up| |PWOK may deassert as soon as input|ms loss is detected|
|T Vout_Hold-up| |1|ms|
|Tsb_Hold-up| |25|ms|
|T PWR_GOOD_Off|1|700|ms|
|T PSON_On_Delay| |400|ms|

advancedenergy.com
---
# DS1100TDC

|TIMING DIAGRAM| | | | |
|---|---|---|---|---|
|DC Input|Tsb_On| | | |
|Vout_stby| |Tsb_Hold-up| | |
| | |TInput_Delay| | |
|INPUT_OK|Tsb_Vout| | | |
| |TInput_On_Delay| | | |
| | | |TPWOK_Off| |
|Vout_main| | | | |
| |TPWOK_On|TPWOK_Off| | |
| |PWOK|TPWOK_Hold-up| | |
| | | |PSON|TPWSON_On_Delay|

advancedenergy.com
---
# MECHANICAL OUTLINE

|Output Connector Part Number|TEI 1926736-3|
|---|---|
|Output Mating Connector Part Number|TEI 2-1926739-5, 1892787-6 or equivalent|
|Input Mating Connector Part Number|Molex 42816-0212 or equivalent|

DS1100TDC-3 (FORWARD) - RED HANDLE

DS1100TDC-3-001 (REVERSE) - BLUE HANDLE

AIRFLOW DIRECTION

DS1100TDC-3 FORWARD AIRFLOW

DS1100TDC-3-001 REVERSE AIRFLOW

Pin 41 Pin E

advancedenergy.com
---
|Output Connector|Pin Configuration|
|---|---|
|A1|3.3 VSB Standby Output|
|B1|3.3 VSB Standby Output|
|C1|3.3 VSB Standby Output|
|D1|3.3 VSB Standby Output|
|E1|3.3 VSB Standby Output|
|A2|SGND Signal Ground|
|B2|SGND Signal Ground|
|C2|Reserved|
|D2|Reserved|
|E2|Reserved|
|A3|A2/ A_Select Optional address line 2|
|B3|A0 I C address|
|C3|SDA I2 C Data|
|D3|-Remote_Sense Wire drop compensation|
|E3|+Remote_Sense Wire drop compensation|
|A4|SCL I2 C Clock|
|B4|PSON_L Enable/Inhibit|
|C4|PS_INTERRUPT_L Alert for failure|
|D4|A1 I2 C address|
|E4|INPUT_OK Input indicator|
|A5|PSKILL_H First break/last mate pin|
|B5|ISHARE Current share bus|
|C5|PWOK Output indicator|
|D5|Reserved|
|E5|PS_PRESENT_L Power supply present|
|P1-P5|+12 V Return Main output power contact|
|P6-P10|12 V Main output return contact|
---
# DS1100TDC Environmental Specifications

|Operating temperature|DS1100TDC-3:|Full power at -5 to 50 °C, derate to 660 W at 65 °C|
|---|---|---|
| |DS1100TDC-3-001:|Full power at -5 to 45 °C, derate to 660 W at 55 °C|
|Operating altitude|Up to 10,000 feet|Up to 10,000 feet|
|Operating relative humidity|+5% to +95% non-condensing|+5% to +95% non-condensing|
|Non-operating temperature|-40 to +70 °C|-40 to +70 °C|
|Non-operating relative humidity|+5% to +95% non-condensing|+5% to +95% non-condensing|
|Non-operating altitude|Up to 50,000 feet|Up to 50,000 feet|
|Vibration and shock|Standard operating/non-operating random shock and vibration|Standard operating/non-operating random shock and vibration|

RoHS compliance: Yes

MTBF: >300,000 hours.

Operating life: Minimum of 7 years at typical operating conditions

Reliability: All electronic component derating analysis and capacitor life calculation is done at 40 °C ambient, 80% of maximum rated load, nominal input line voltage.

advancedenergy.com          9
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS1100TDC-235-01 12.14