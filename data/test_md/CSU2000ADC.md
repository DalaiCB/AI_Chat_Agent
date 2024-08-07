# ARTESYN CSU2000ADC-3-600

2000 Watts Distributed Power System

Advanced Energy's Artesyn CSU2000ADC-3-600 is housed in the industry standard 1U x 73.5 x 185 mm form factor featuring -48 VDC input voltage. This DC/DC power supply belongs to the CRPS family of products, and matches the mechanical form and fit of Advanced Energy's AC/DC power supplies. The common form, fit, and function for all products in the family provides a path for power capacity flexibility, future-proofing your system designs.

# AT A GLANCE

|Front End Bulk Power|Total Output Power|
|---|---|
| |2000 W continuous|
| |Wide Input Voltage|
| |-40 to -72 VDC|

# SPECIAL FEATURES

- 2000 W output power
- High power and short form factor
- 1U power supply
- High density design: 62 W/in3
- Uses two-hole terminal lugs to handle high input current
- Inrush current control
- N+M redundant N+M ≤ 4
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus® compliant
- Accurate input power reporting
- Compatible with Artesyn’s Universal PMBus GUI
- Reverse airflow option

# COMPLIANCE

- Conducted/Radiated EMI Class A

# SAFETY

- IEC 60950, IEC 62368
- UL/cUL
- UL + CB Report
- CQC
- KC
- BIS
- CE Mark
- UKCA Mark

# TARGET APPLICATIONS

- Server and Storage
- Networking

©2024 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input Range|-40 to -72 VDC|
|Efficiency|94% peak|
|Max Input Current|65 A at -40 VDC input|
|Inrush Current|ETSI 300 132-2 Annex C|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Hold-up Time|2.4 ms minimum at full load|

|Output|Main DC Output|Standby DC Output|
|---|---|---|
|Nominal Setting|11.8 V|11.4 V|
| |12.2 V|12.0 V|
| |12.6 V|12.6 V|
|Total Output Regulation Range|11.6 V - 12.8 V|11.4 V - 12.6 V|
|Dynamic Load Regulation Range1|11.6 V - 12.8 V|11.4 V - 12.6 V|
|Output Ripple| |120 mV|
|Output Current|1 A - 163.9 A|0 A - 3.5 A|
|Current Sharing|Within ±6% @ full load rating|N/A|
|Capacitive Loading|2000 μF - 50000 μF|47 μF - 3100 μF|
|Start-up from AC to Output|3000 ms|1500 ms|

Note 1 - Dynamic load step for main output: 60% rated load step, 0.5 A/μs slew rate; 2000 μF / 1 A min

Dynamic load step for standby output: 50% rated load step, 0.5 A/μs slew rate; 100 μF
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|Protections (Main Output)|MIN|NOM|MAX|Units|Comment|
|---|---|---|---|---|---|
|Peak Current| |264| |A| |
|Output OCP|261| |267|A| |
|Output OVP|13.3| |14.5|V|Latch|
|Overtemperature Protection|Yes| | | | |
|Fan Fault Protection|Yes| | | | |

# Standby Output

| |MIN|NOM|MAX|Units|
|---|---|---|---|---|
|Output OCP|4.0| |5.0|A|
|Output OVP|13.3| |14.5|V|

# LED Indicators

|Power Supply Condition|LED State|
|---|---|
|Normal work|Green|
|No DC input power to all power supplies|Off|
|DC input present / Only 12 Vsb on (PS off) or PS in CR state|1 Hz Blink Green|
|DC input cord unplugged; with a second power supply in parallel still with DC input|Amber|
|power| |
|Power supply warning events where the power supply continues to operate; high temp,|1 Hz Blink Amber|
|high power, high current, slow fan| |
|Power supply critical event causing a shutdown; failure, OCP, OVP, fan fail|Amber|

# Firmware Reporting And Monitoring

| |Accuracy Range|
|---|---|
|Output Loading|2% to 7.5%|
| |> 7.5% to 15%|
| |> 15% to 100%|
|READ_PIN and READ_EIN|±10 W|
| |±10 W|
| |±2%|
|READ_IOUT|±1 A|
| |±5%|
| |±2%|
|READ_TEMPERATURE|±3°C|

advancedenergy.com
---
# TIMING SPECIFICATIONS

|ITEM|DESCRIPTION|MIN|MAX|UNITS|
|---|---|---|---|---|
|Tvout_rise|Output voltage rise time for 12 V and 12 Vsb from 10% to within regulation limits. The default rise time shall be 25 ms.|10|70|ms|
|dV/dt (new)|Output voltage dv/dt at any point of the voltage slow start when PSU is powered ON. Applies to both 12 V and 12 Vsb. This is the time the PSU must stay off when being powered off with loss of DC input.|0.5| |V/msec|
|Toff_latch|Both outputs must meet this off time; 1) whenever PWOK is de-asserted for the 12 V output; 2) whenever the 12 Vsb output drops below regulation limits|500| |ms|
|Tsb_on_delay|Delay from DC being applied to 12 Vsb being within regulation|1500|2500|ms|
|Tvin_good_high|Delay from input being applied to VIN_GOOD assertion|1800| |ms|
|Tac_on_delay|Delay from DC being applied to all output voltages being within regulation|3000| |ms5msec|
|Tvout_holdup|Time 12 V output voltage stay within regulation after loss of DC|2.4| |ms|
|Tpwok_holdup|Delay from loss of DC to de-assertion of PWOK|1| |ms|
|Tvin_good_low|Delay from loss of DC to de-assertion of VIN_GOOD|2| |ms|
|Tpson_off_delay|Delay from PSON# de-asserted to power supply turning off|5| |ms|
|Tpson_on_delay|Delay from PSON# active to output voltages within regulation limits|5|400|ms|
|Tpson_pwok|Delay from PSON# deactivate to PWOK being de-asserted|5| |ms|
|Tpwok_on|Delay from output voltages within regulation limits to PWOK asserted at turn on|100|500|ms|
|Tpwok_off|Delay from PWOK de-asserted to output voltages dropping out of regulation limits|1| |ms|
|Tpwok_low|Duration of PWOK being in the de-asserted state during an off/on cycle using DC or the PSON signal|100| |ms|
|Tsb_vout|Delay from 12 Vsb being in regulation to O/Ps being in regulation at DC turn on|50|1500|ms|
|T12VSB_holdup|Time the 12 Vsb output voltage stays within regulation after loss of DC|50| |ms|

# TIMING DIAGRAM

|Pmax peak| | |&lt; 80μsec|
|---|---|---|---|
|Pmax.app peak| | |&lt; 80μsec|
|PSU Iout| | |&lt; 20μsec|
|SMBAlert#| | | |
---
# CSU2000ADC-3-600

|ENVIRONMENTAL SPECIFICATIONS| | |
|---|---|---|
|Operating Temperature|0 to 55°C at full load| |
| |Allowable operating temperature of 65°C at 60% load| |
|Operating Altitude|up to 5000 m| |
|Operating Humidity|+5% to +95%, non-condensing| |
|Storage Temperature|-40°C to +70°C, non-condensing| |
|Storage Humidity|+5% to +95%, non-condensing| |
|Non-operating Altitude|up to 10,000 meters| |
|Vibration and Shock|Standard operating/non-operating random shock and vibration| |
|RoHS Compliance|Yes| |
|MTBF| |250,000 hours per Telcordia Issue 2, Method 1, Case 3 at 25°C ambient at full load|

# MECHANICAL OUTLINE

|185.0 ±0.5|110 ±0.5| | |
|---|---|---|---|
|L0I05FAL| |FORWARD AIRFLOW| |
| |DIRECTION| | |
|IQMX| | | |
| | |2319 REFE| |
| | | |Unit: mm|

advancedenergy.com       5
---
# POWER SUPPLY OUTPUT CARD EDGE CONNECTOR DEFINITIONS

|Reference|On Power Supply|Mating Connector|
|---|---|---|
|DC Input Connector|Terminal blocks, 1 lug for 800 W, 2 lugs for 1300 W and greater M5 X 0.85 mm hex nut|NA|
|Output Connector|Card-edge|2x25 pin configuration of the FCI power card connector 10035388-102LF or any approved equivalent|

|Pin|Name|Pin|Name|
|---|---|---|---|
|A1|GND|B1|GND|
|A2|GND|B2|GND|
|A3|GND|B3|GND|
|A4|GND|B4|GND|
|A5|GND|B5|GND|
|A6|GND|B6|GND|
|A7|GND|B7|GND|
|A8|GND|B8|GND|
|A9|GND|B9|GND|
|A10|+12V|B10|+12V|
|A11|+12V|B11|+12V|
|A12|+12V|B12|+12V|
|A13|+12V|B13|+12V|
|A14|+12V|B14|+12V|
|A15|+12V|B15|+12V|
|A16|+12V|B16|+12V|
|A17|+12V|B17|+12V|
|A18|+12V|B18|+12V|
|A19|PMBus SDA|B19|A0 (SMBus address)|
|A20|PMBus SCL|B20|A1 (SMBus address)|
|A21|PSON|B21|12Vsb|
|A22|SMBAlert#|B22|Cold Redundancy Bus|
|A23|Return Sense|B23|12V load share bus|
|A24|+12V remote Sense|B24|GND|
|A25|PWOK|B25|VIN_GOOD|

# ORDERING INFORMATION

|Model Number|Airflow|Nominal Output Voltage|Regulation Band|Minimum Current|Maximum Current|Output Ripple P/P|Standby|
|---|---|---|---|---|---|---|---|
|CSU2000ADC-3-600|Normal fan|12.2 VDC|11.8 - 12.6 VDC|1 A|163.9 A|120 mV|12.0 V @ 3.5 A|
---
ABOUT ADVANCED ENERGY
Advanced Energy (AE) has devoted more than four decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

TRUST

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2024 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-CSU2000ADC-3-600-235-01 03.18.24