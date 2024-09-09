# ARTESYN CSU800AP 800 W Distributed Power System

Advanced Energy's Artesyn CSU800AP power supply is housed in a 1U high rack-mount enclosure measuring just 2.89 x 7.28 inches (73.5 x 185.0 mm). This form factor is significantly narrower and shorter than that of similarly rated earlier generation power supplies - freeing up valuable system space - and is achieved by use of the latest power switching technology and high density component packaging techniques. This form factor conforms to the standard market's Common Redundant Power Supplies.

# AT A GLANCE

|Front-end Bulk Power| |
|---|---|
|Total Output Power:|800 W continuous|
|Wide Input Voltage:|90 to 264 VAC; 164 to 320 VDC|

# SPECIAL FEATURES

|800 W output power|High power and short form factor| |
|---|---|---|
|1U power supply|High density design: 25 W/in3| |
|Active Power Factor Correction|EN61000-3-2 Harmonic compliance| |
|Inrush current control|80 PLUS® Platinum efficiency| |
|N+M redundant N+M ≤ 4|Hot-pluggable| |
|Active current sharing|Full digital control| |
|PMBus® compliant|Accurate input power reporting| |
|EN61000-4-5 surge level 2 kV/4 kV DM/CM|Compatible with Artesyn’s Universal PMBus GUI| |
|Reverse airflow option| | |

# COMPLIANCE

- Conducted/Radiated EMI Class A
- EN61000-4-11

# SAFETY

- IEC62368
- UL/cUL
- UL + CB Report
- CE Mark
- CCC
- BSMI
- KC
- BSMI
- KC
- TÜV

&copy;2024 Advanced Energy Industries, Inc.
---
# CSU800AP-600

# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input Range|90 to 264 VAC / 164 to 320 VDC|
|Frequency|47 Hz to 63 Hz|
|Efficiency|80 PLUS® Platinum efficiency|
|Max Input Current|11.7 Arms @ 90 VAC|
|Inrush Current|35 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Power Factor|>0.9 beginning at 10% load|
|ITHD|<10% beginning at 20% load|
|Leakage Current|1.75 mA|
|Hold-up Time|13 ms at full load|

| | |Output|Main DC Output| |Standby DC Output| |
|---|---|---|---|---|---|---|
| |MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal Setting (12.2 V / 1 A, 12 VSB / 0.1 A)|12.1 V|12.2 V|12.3 V|11.9|12.0 V|12.1 V|
|Total Output Regulation Range|11.8 V| |12.6 V|11.4 V| |12.6 V|
|Dynamic Load Regulation Range|11.6 V| |12.8 V|11.4 V| |12.8 V|
|Output Ripple| | |120 mV| | |120 mV|
|Output Current|1| |66.7 A|0| |3 A|
|Current Sharing| |Within ±5% @ full load rating| | |N/A| |
|Capacitive Loading|500 μF| |25000 μF|100 μF| |3100 μF|
|Start-up from AC to Output| | |3000 ms| | |1500 ms|
|Output Rise Time|5 ms| |70 ms|1 ms| |25 ms|

|Protections (Main Output)|Minimum|Nominal|Maximum|Units|Comment|
|---|---|---|---|---|---|
|Peak Current| |76| |A| |
|Output OCP| |76|83.6|A| |
|Dynamic Loading Setup| |±5| |%|60% rated load step, 0.25 A/μs slew rate; 2000 μF / 1 A min|
|Output OVP|13.3| |14.5|V|Latch|
|Output UVP|9.5| |11.0|V|Latch|

Overtemperature Protection: Yes

Fan Fault Protection: Yes

# Standby Output

|Output OCP|4.0| |5.0|A| |
|---|---|---|---|---|---|
|Output OVP|13.3| |14.5|V| |
|Dynamic Loading Setup| | |±5|%|50% rated load step Slew rate: 0.25 A / μs / 100 μF|

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
|Output loading|10% to 30%|&gt; 30% to 50%|&gt; 50% to 100%| |
|READ_PIN and READ_EIN|±5 W|±3%|±3%| |
|READ_IOUT|±5%|±2%|±2%| |
|READ_TEMPERATURE|±3 °C| | | |

# TIMING SPECIFICATIONS

|Description|Min|Max|Unit|
|---|---|---|---|
|Tvout_rise|12 V main output voltage rise time|5.0|70 ms|
|12 VSB output voltage rise time|1|25|ms|
|Tsb_on_delay|Delay from AC being applied to 12 Vsb being within regulation| |1500 ms|
|Tac_on_delay|Delay from AC being applied to all output voltages being within regulation| |3000 ms|
|Tvout_holdup|Time 12 VI output voltage stay within regulation after loss of AC|13|ms|
|Tpwok_holdup|Delay from loss of AC to de-assertion of PWOK|12|ms|
|Tpson_on_delay|Delay from PSON# active to output voltages within regulation limits|5|400 ms|
|Tpson_pwok|Delay from PSON# deactivate to PWOK being de-asserted|5|ms|
|Tpwok_on|Delay from output voltages within regulation limits to PWOK asserted at turn on|100|500 ms|
|Tpwok_off|Delay from PWOK de-asserted to output voltages dropping out of regulation limits|1|ms|
|Tpwok_low|Duration of PWOK being in the de-asserted state during an off/on cycle using AC or the PSON signal|100|ms|
|Tsb_vout|Delay from 12VSB being in regulation to O/Ps being in regulation at AC turn on|50|1000 ms|
|T12VSB_holdup|Time the 12VSB output voltage stays within regulation after loss of AC|70|ms|
---
# CSU800AP-600

# Environmental Specifications

|Operating Temperature|0 to 55°C, the maximum operating temperature (55°C) is to be derated by 1°C per 300 m above 2000 m|
|---|---|
|Operating Altitude|up to 5000 m|
|Operating Humidity|+5% to +85% non-condensing|
|Storage Temperature|-40 to +70°C, non-condensing|
|Storage Humidity|+5 to +95% non-condensing|
|Non-operating Altitude|up to 15,200 meters|
|Vibration and Shock|Standard operating/non-operating random shock and vibration|
|RoHS Compliance|Yes|
|MTBF|2,261,000 hours per Telcordia SR332 Issue 3, Method 1, Case 3 at 25°C ambient at full load|

# advancedenergy.com
---
CSU800AP-600MECHANICAL OUTLINELABELPOWER SUPPLY OUTPUT CARD EDGEadvancedenergy.com 5
---

# ORDERING INFORMATION

|Model number|Airflow|Output Voltage|Set Point|Regulation Band|Minimum Current|Maximum Current|Output Ripple P/P|Output Standby|
|---|---|---|---|---|---|---|---|---|
|CSU800AP-3-600|Normal fan|12.2 VDC|12.1 - 12.3 VDC|11.8 - 12.6 VDC|1 A|66.7 A|120 mV|12.0 V at 3 A|
|CSU800AP-3-601|Reverse fan|12.2 VDC|12.1 - 12.3 VDC|11.4 - 12.6 VDC|1 A|66.7 A|120 mV|12.0 V at 3 A|
---