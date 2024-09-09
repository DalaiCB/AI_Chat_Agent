# SERIES ARTESYN

ARTESYN CSU1300AP

1300 Watts Distributed Power System

Advanced Energy's Artesyn CSU1300AP power supply is housed in a 1U high rack-mount enclosure measuring just 2.89 x 7.28 inches (73.5 x 185.0 mm). This form factor is significantly narrower and shorter than that of similarly rated earlier generation power supplies — freeing up valuable system space — and is achieved by use of the latest power switching technology and high density component packaging techniques. This form factor conforms to the standard market's Common Redundant Power Supplies.

# DATA SHEET

|Front-end Bulk Power| |
|---|---|
|Total Output Power:|1300 W continuous|
|Wide Input Voltage:|90 - 264 Vac; 180 - 300 Vdc|

# SPECIAL FEATURES

- 1300 W output power
- High power and short form factor
- 1U power supply
- High density design: 39 W/in 3
- Active Power Factor Correction
- EN61000-3-2 Harmonic compliance
- Inrush current control
- 80 PLUS® Platinum efficiency
- N+M redundant N+M ≤ 4
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus® compliant
- EN61000-4-5 surge level 1 kV/2 kV
- DM/CM
- Compatible with Artesyn’s Universal PMBus GUI

# COMPLIANCE

- Conducted/Radiated EMI Class A
- EN61000-4-11

# SAFETY

- UL/cUL
- UL + CB Report
- CE Mark
- CCC
- BSMI
- KC
- TÜV

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|90 - 264 Vac / 180 - 300 Vdc|
|Frequency|47 Hz to 63 Hz|
|Efficiency|80 PLUS® Platinum efficiency|
|Max input current|8.5 Arms @ 180 Vac; 12.5 Arms @ 100 Vac|
|Inrush current|25 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Power factor|>0.9 beginning at 10% load|
|ITHD|20% beginning at 10% load; 8% at 20% load|
|Leakage current|1.75 mA|
|Hold-up time|11 ms at full load|

|Output|Main DC Output|Standby DC Output|
|---|---|---|
|Nominal setting|12.1|11.9|
|(12 V / 1 A, 12 VSB / 0.1 A)|12.2|12.0|
| |12.3|12.1|
|Total output regulation range|11.8 V - 12.6 V|11.4 V - 12.6 V|
|Dynamic load regulation range|11.6 V - 12.6 V|11.4 V - 12.6 V|
|Output ripple|120 mV|120 mV|
|Output current|1 Hi line: 108.3 A Lo line: 83.3 A|0 - 3 A|
|Current sharing|beginning at 20% loading|N/A|
|Capacitive loading|2200 μF - 22000 μF|100 μF - 3100 μF|
|Start-up from AC to output|3000 ms|1500 ms|
|Output rise time|NA 25 ms|NA 70 ms|

|Protections (Main Output)|Minimum|Nominal|Maximum|Units|Comment|
|---|---|---|---|---|---|
|Peak current| |115|%| | |
|Output OCP|120|140|%| | |
|Dynamic loading setup| | |±5|%|60% rated load step, 1.0 A/μs slew rate; 2200 μF / 1 A min|
|Output OVP|13.5| |15|V|Latch|
|Output UVP|9.5| |11.0|V|Recovery|

|Standby Output| |
|---|---|
|Output OCP|4.0 - 5.0 A|
|Output OVP|13.5 - 15 V|
|Dynamic loading setup|±5 % 1 A rated load step Slew rate: 0.5 A / μs / 1000 μF|

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|LED Indicators|POWER SUPPLY CONDITION| | |LED STATE|
|---|---|---|---|---|
|Normal work| | | |GREEN|
|No AC power to all power supplies| | | |OFF|
|AC present / Only 12 VSB on (PS off) or PS in CR state| | | |1 Hz Blink GREEN|
| |AC cord unplugged; with a second power supply in parallel still with AC input power| | |RED|
| |Power supply warning events where the power supply continues to operate; high temp, high power, high current, slow| | |1 Hz Blink RED|
| |fan, input voltage lower than 90 Vac (not warning above 90 V condition, must be warning state below 85 V condition)| | | |
| |Power supply critical event causing a shutdown; failure, OCP, OVP, fan fail| | |RED|

# Firmware Reporting And Monitoring

| | |Accuracy Range| | |
|---|---|---|---|---|
|Output loading|10% to 20%|&gt; 20% to 50%|&gt; 50% to 100%| |
|READ_PIN and READ_EIN|±5 W|±2%|±2%| |
|READ_IOUT|±5%|±2%|±2%| |
|READ_TEMPERATURE|±3 °C| | | |

# TIMING SPECIFICATIONS

|Description|Min|Max|Unit|
|---|---|---|---|
|T vout_rise|12 V main output voltage rise time|5.0|25 ms|
|Tsb_on_delay|Delay from AC being applied to 12 Vsb being within regulation|NA|70 ms|
|Tsb_on_delay|Delay from AC being applied to 12 Vsb being within regulation| |1500 ms|
|Tac_on_delay|Delay from AC being applied to all output voltages being within regulation| |3000 ms|
|T vout_holdup|Time 12 VI output voltage stay within regulation after loss of AC|11|ms|
|Tpwok_holdup|Delay from loss of AC to de-assertion of PWOK|10|ms|
|Tpson_on_delay|Delay from PSON# active to output voltages within regulation limits|5|400 ms|
|Tpson_pwok|Delay from PSON# deactivate to PWOK being de-asserted|5|ms|
|Tpwok_on|Delay from output voltages within regulation limits to PWOK asserted at turn on|100|500 ms|
|Tpwok_off|Delay from PWOK de-asserted to output voltages dropping out of regulation limits|1|ms|
|Tpwok_low|Duration of PWOK being in the de-asserted state during an off/on cycle using AC or the PSON signal|100|ms|
|Tsb_vout|Delay from 12VSB being in regulation to O/Ps being in regulation at AC turn on|50|1000 ms|
|T 12VSB_holdup|Time the 12VSB output voltage stays within regulation after loss of AC|70|ms|

advancedenergy.com
---
# TIMING DIAGRAM

|AC Input|Vout|TAc|dalai|piok|pwor_off|Tsb|owok|Tpox_off| |
|---|---|---|---|---|---|---|---|---|---|
|PWOK|deliy|Tpwok| | |Tpwok|dulai|Tpson Drok| | |
|SVSB| |Tp _| |Tsb_noldup| | | | | |
|PSON#| | | | | |PSON turn on/off cycle| | | |
| | |AC turn on/off cycle| | | | | | | |

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|0 to 55 °C|
|---|---|
|Operating altitude|up to 5000 m|
|Operating humidity|+5% to +90% non-condensing|
|Storage temperature|-40 °C to +85 °C, non-condensing|
|Storage humidity|+5% to +95% non-condensing|
|Non-operating altitude|up to 15,200 meters|
|Vibration and shock|Standard operating/non-operating random shock and vibration|
|RoHS compliance|Yes|
|MTBF|250,000 hours at 40 °C ambient at full load|
---
| | |CSU1300AP|
|---|---|---|
|MECHANICAL OUTLINE|3nnw| |
| |Status LED| |
|POWER SUPPLY OUTPUT CARD EDGE| | |
| | |advancedenergy.com 5|
---
# CONNECTOR DEFINITIONS

|Output connector part number|Card-edge|
|---|---|
|Mating connector part number|2x25 pin configuration of the FCI power card connector 10035388-102LF|

# Output Connector Pin Configuration

|Pin|Name|Pin|Name|
|---|---|---|---|
|A1-A9|GND|B1-B9|GND|
|A10-A18|+12 V|B10-B18|+12 V|
|A19|SDA|B19|A0 (SMBus address)|
|A20|SCL|B20|A1 (SMBus address)|
|A21|PSON|B21|12 VSB|
|A22|SMBAlert#|B22|CR_BUS#|
|A23|-VSENSE|B23|12 V load share|
|A24|+VSENSE|B24|Present|
|A25|PWOK|B25|VIN-GOOD|

# ORDERING INFORMATION

|Model number|Airflow|Nominal Output Voltage|Regulation Band|Minimum Current|Maximum Current|Output Ripple P/P|Standby|
|---|---|---|---|---|---|---|---|
|CSU1300AP-3-600|Normal fan|12.2 Vdc|11.6 - 12.6 Vdc|1 A|Hi line: 108.3 A Lo line: 83.3 A|120 mV|12.0 V @ 3 A|

advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

Contact Information:

powersales@aei.com (Sales Support)productsupport.ep@aei.com (Technical Support)+1 888 412 7832
Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-CSU1300AP-235-01 12.09