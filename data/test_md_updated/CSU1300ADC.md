# ARTESYN CSU1300ADC

1300 Watts Distributed Power System

Advanced Energy's Artesyn CSU1300ADC is housed in the industry standard 1U x 73.5 x 185 mm form factor featuring -48Vdc input voltage. This DC/DC power supply belongs to the CRPS family of products, and matches the mechanical form and fit of Advanced Energy's AC/DC power supplies. The common form, fit, and function for all products in the family provides a path for power capacity flexibility, future-proofing your system designs.

# AT A GLANCE

| |Front End Bulk Power|
|---|---|
|Total Output Power:|1300 W continuous|
|Wide Input Voltage:|-40 to -72 Vdc|

# SPECIAL FEATURES

- 1300 W output power
- High power and short form factor
- 1U power supply
- High density design: 39 W/in3
- Uses two-hole terminal lugs to handle high input current
- Inrush current control
- N+M redundant N+M ≤ 4
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus® compliant
- Compatible with Artesyn’s Universal PMBus GUI
- Reverse airflow option
- Conducted/Radiated EMI Class A
- Tested for ATIS 0600315

# COMPLIANCE

- UL/cUL
- UL + CB Report
- CE Mark
- CCC
- KC

# TARGET APPLICATIONS

- Server and Storage
- Networking

©2021 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|-40 to -72Vdc|
|Efficiency|94% peak|
|Max input current|50A at -40V|
|Inrush current|ETSI 300 132-2 Annex C|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Hold-up time|2.4 ms at full load|

| | |Output|Main DC Output|Standby DC Output| | |
|---|---|---|---|---|---|---|
|Nominal setting|MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting|11.8|12.2|12.6|11.4|12.0|12.6|
|Total output regulation range|11.6 V| |12.8 V|11.4 V| |12.8 V|
|Dynamic load regulation range|11.6 V| |12.8 V|11.4 V| |12.8 V|
|Output ripple| | |120 mV| |120 mV| |
|Output current|1| |106.5 A|0|3.5 A| |
|Current sharing| |Within ±5% @ full load rating| |N/A| | |
|Capacitive loading|2000 μF| |50000 μF|47 μF|3100 μF| |
|Start-up from AC to output| | |3000 ms| |1500 ms| |
|Output rise time|10 ms| |70 ms|10 ms|70 ms| |
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|Protections (Main Output)|Minimum|Nominal|Maximum|Units|Comment|
|---|---|---|---|---|---|
|Peak current| |176| |A| |
|Output OCP|132| |140|A| |
|Dynamic loading setup| | |±5|%|60% rated load step, 0.5 A/μs slew rate; 2000 μF / 1 A min|
|Output OVP|13.3| |14.5|V|Latch|
|Overtemperature protection|Yes| | | | |
|Fan fault protection|Yes| | | | |

|Standby Output|Minimum|Nominal|Maximum|Units|Comment|
|---|---|---|---|---|---|
|Output OCP|4.0| |5.0|A| |
|Output OVP|13.3| |14.5|V| |
|Dynamic loading setup| | |±5|%|50% rated load step, Slew rate: 0.5 A / μs / 100 μF|

# LED Indicators

|POWER SUPPLY CONDITION|LED STATE|
|---|---|
|Normal work|GREEN|
|No AC power to all power supplies|OFF|
|AC present / Only 12 VSB on (PS off) or PS in CR state|1 Hz Blink GREEN|
|AC cord unplugged; with a second power supply in parallel still with AC input power|RED|
|Power supply warning events where the power supply continues to operate; high temp, high power, high current, slow fan, input voltage lower than 90 Vac (not warning above 90 V condition, must be warning state below 85 V condition)|1 Hz Blink RED|
|Power supply critical event causing a shutdown; failure, OCP, OVP, fan fail|RED|

# Firmware Reporting And Monitoring

|Output loading|Accuracy Range|
|---|---|
|READ_PIN and READ_EIN|±10 W|
|READ_IOUT|±1A|
|READ_TEMPERATURE|±3 °C|

advancedenergy.com
---

# CSU1300ADC

|ENVIRONMENTAL SPECIFICATIONS| | |
|---|---|---|
|Operating temperature|0 to 55°C at full load| |
| |Allowable operating temperature of 65°C at 60% load| |
|Operating altitude|up to 5000 m| |
|Operating humidity|+5% to +95% non-condensing| |
|Storage temperature|-40 °C to +70 °C, non-condensing| |
|Storage humidity|+5% to +95% non-condensing| |
|Non-operating altitude|up to 10,000 meters| |
|Vibration and shock|Standard operating/non-operating random shock and vibration| |
|RoHS compliance|Yes| |
|MTBF| |250,000 hours per Telcordia Issue 2, Method 1, Case 3 at 25 °C ambient at full load|

# MECHANICAL OUTLINE

|185.0 ±0.5|110 ±0.5|
|---|---|
|L0I05FAL|FORWARD AIRFLOW|
|DIRECTION| |
| |NDEMCHNA|
|IQMX| |
|2319 REFE| |
| |advancedenergy.com 5|
---

# ORDERING INFORMATION

|Model number|Airflow|Nominal Output Voltage|Regulation Band|Minimum Current|Maximum Current|Output Ripple P/P|Standby|
|---|---|---|---|---|---|---|---|
|CSU1300ADC-3-100|Normal fan|12.2 Vdc|11.8 - 12.6 Vdc|1 A|106.5 A|120 mV|12.0 V @ 3.5 A|
|CSU1300ADC-3-101|Reverse fan|12.2 Vdc|11.8 - 12.6 Vdc|1 A|106.5 A|120 mV|12.0 V @ 3.5 A|
---