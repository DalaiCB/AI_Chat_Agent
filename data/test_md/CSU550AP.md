# ARTESYN CSU550AP 550 Watts Distributed Power System

Advanced Energy’s Artesyn CSU550AP power supply is housed in a 1U high rack-mount enclosure measuring just 2.89 x 7.28 inches (73.5 x 185.0 mm). This form factor is significantly narrower and shorter than that of similarly rated earlier generation power supplies — freeing up valuable system space — and is achieved by use of the latest power switching technology and high density component packaging techniques. This form factor conforms to the standard market's Common Redundant Power Supplies.

# DATA SHEET

|Front-end Bulk Power| |
|---|---|
|Total Output Power:|550 W continuous|
|Wide Input Voltage:|90 - 264 Vac; 164 - 320 Vdc|

# SPECIAL FEATURES

- 550 W output power
- High power and short form factor
- 1U power supply
- High density design: 17 W/in3
- Active Power Factor Correction
- EN61000-3-2 Harmonic compliance
- Inrush current control
- 80plus Platinum efficiency
- N+M redundant N+M ≤ 4
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus compliant
- Accurate inut power reporting
- Reverse airflow option
- Conducted/Radiated EMI Class A
- EN61000-4-11

# COMPLIANCE

- SAFETY
- UL/cUL
- UL + CB Report
- CE Mark
- CCC
- BSMI
- KC
- TÜV

©2021 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|90 - 264 Vac; 164 - 320 Vdc|
|Frequency|47 Hz to 63 Hz|
|Efficiency|80plus Platinum efficiency|
|Max input current|8.0 Arms @ 90 Vac|
|Inrush current|10 Apk|
|Conducted EMI|Class A -6 dB|
|Radiated EMI|Class A -6 dB|
|Power factor|>0.89 beginning at 10% load|
|ITHD|<10% beginning at 20% load|
|Leakage current|0.85 mA|
|Hold-up time|13 ms at full load|

| | |Output|Main DC Output| |Standby DC Output| |
|---|---|---|---|---|---|---|
| |MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting|12.05|12.15|12.25|12.05|12.2|12.35|
|(12 V / 1 A, 12 VSB / 0.1 A)| | | | | | |
|Total output regulation range|11.4 V| |12.6 V|11.4 V| |12.6 V|
|Dynamic load regulation range|11.4 V| |12.6 V|11.4 V| |12.6 V|
|Output ripple| | |120 mV| |120 mV| |
|Output current|0| |45 A|0|2.5 A| |
|Current sharing| |Within ±5% @ full load rating| |N/A| | |
|Capacitive loading|500 μF| |25000 μF|100 μF|3100 μF| |
|Start-up from AC to output| | |3000 ms| |1500 ms| |
|Output rise time|5 ms| |70 ms|1 ms|25 ms| |
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|Protections (Main Output)|Minimum|Nominal|Maximum|
|---|---|---|---|
|Peak current| |54| |
|Output OCP|55| |62|
|Dynamic loading setup|11.4| |12.6|
|Output OVP|13.3| |14.5|
|Overtemperature protection|Yes| | |
|Fan fault protection|Yes| | |

|Standby Output|Peak current| | |
|---|---|---|---|
| |2.75| | |
|Output OCP|3.0| |4.5|
|Output OVP|13.3| |14.5|
|Dynamic loading setup| |±5| |

# LED Indicators

POWER SUPPLY CONDITION

- Normal work
- No AC power to all power supplies
- AC present / Only 12 VSB on (PS off) or PS in CR state
- AC cord unplugged; with a second power supply in parallel still with AC input power
- Power supply warning events where the power supply continues to operate; high temp, high power, high current, slow fan, input voltage lower than 90 Vac (not warning above 90 V condition, must be warning state below 85 V condition)
- Power supply critical event causing a shutdown; failure, OCP, OVP, fan fail

Firmware Reporting And Monitoring

|Output loading|10% to 30%|
|---|---|
|READ_PIN and READ_EIN|±6 W|
|READ_IOUT|±0.4 A|
|READ_TEMPERATURE| |

Units

|A| |
|---|---|
|A| |
|V|60% rated load step, 0.5 A/μs slew rate; 2000 μF / 1 A min|
|V|Latch|
|A| |
|A| |
|V|Load step 1A, Slew rate: 0.5 A / μs / 100 μF|
|%| |

LED STATE

|GREEN|OFF|
|---|---|
|1 Hz Blink GREEN| |
|RED|1 Hz Blink RED|
|RED| |

Accuracy Range

|> 30% to 50%|> 50% to 100%|
|---|---|
|±3%|±2%|
|±2%|±2%|
|±3 °C| |

advancedenergy.com          3
---
# TIMING SPECIFICATIONS

|Description|Min|Max|Unit|
|---|---|---|---|
|12 V main output voltage rise time|5.0|70|ms|
|12 VSB output voltage rise time|1|25|ms|
|Delay from AC being applied to 12 Vsb being within regulation| |1500|ms|
|Delay from AC being applied to all output voltages being within regulation| |3000|ms|
|Time 12 VI output voltage stay within regulation after loss of AC|13| |ms|
|Delay from loss of AC to de-assertion of PWOK|12| |ms|
|Delay from PSON# active to output voltages within regulation limits|5|400|ms|
|Delay from PSON# deactivate to PWOK being de-asserted|5| |ms|
|Delay from output voltages within regulation limits to PWOK asserted at turn on|100|500|ms|
|Delay from PWOK de-asserted to output voltages dropping out of regulation limits|1| |ms|
|Duration of PWOK being in the de-asserted state during an off/on cycle using AC or the PSON signal|100| |ms|
|Delay from 12VSB being in regulation to O/Ps being in regulation at AC turn on|50|1000|ms|
|Time the 12VSB output voltage stays within regulation after loss of AC|70| |ms|

# TIMING DIAGRAM

AC Input

Vout

PWOK

12VSB

PSON#

TAc delay

Tpwok

Tsb_noldup

Tvcu_toldup

Tp_on

Tp_off

Tsb

Tpok

Tpox_off

Tpwok_off

Tpwok_low

Tpson_on dolar

Tpson_pwok

AC turn on/off cycle

PSON turn on/off cycle
---
# CSU550AP

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|0 to 50 °C, the maximum operating temperature (50 °C) is to be derated by 1 °C per 300 m above 2000 m|
|---|---|
|Operating altitude|up to 5000 m|
|Operating humidity|+5% to +85% non-condensing|
|Storage temperature|-40 °C to +70 °C, non-condensing|
|Storage humidity|+5% to +95% non-condensing|
|Non-operating altitude|up to 15,200 meters|
|Vibration and shock|Standard operating/non-operating random shock and vibration|
|RoHS compliance|Yes|
|MTBF|250,000 hours per Telcordia Issue 2, Method 1, Case 3 at 25 °C ambient at full load|

# MECHANICAL OUTLINE

advancedenergy.com
---
# POWER SUPPLY OUTPUT CARD EDGE CONNECTOR DEFINITIONS

|Output connector part number|Card-edge|
|---|---|
|Mating connector part number|2x25 pin configuration of the FCI power card connector 10035388-102LF|

|Output Connector Pin Configuration| | | | |
|---|---|---|---|---|
|Pin|Name|Pin|Name| |
|A1-A9|GND|B1-B9|GND| |
|A10-A18|+12 V|B10-B18|+12 V| |
|A19|SDA|B19|A0 (SMBus address)| |
|A20|SCL|B20|A1 (SMBus address)| |
|A21|PSON|B21|12 VSB| |
|A22|SMBAlert#|B22|CR_BUS#| |
|A23|-VSENSE|B23|12 V load share| |
|A24|+VSENSE|B24|Present| |
|A25|PWOK|B25|Reserved| |

Note: PSON connect to GND for power up.

# ORDERING INFORMATION

|Model number|Airflow|Nominal Output Voltage|Set Point|Regulation Band|Minimum Current|Maximum Current|Output Ripple P/P|Standby Output|
|---|---|---|---|---|---|---|---|---|
|CSU550AP-3|Normal fan|12.0 Vdc|11.9 - 12.1 Vdc|11.4 - 12.6 Vdc|0 A|45 A|120 mV|12.0 V @ 2.5 A|
|CSU550AP-3-001|Reverse fan|12.0 Vdc|11.9 - 12.1 Vdc|11.4 - 12.6 Vdc|0 A|45 A|120 mV|12.0 V @ 2.5 A|

advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2021 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-CSU550AP-235-01 2.19