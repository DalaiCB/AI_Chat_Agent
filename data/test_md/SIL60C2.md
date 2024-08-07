# ARTESYN SIL60C2

Dual Row Pins; 60 Amps

Advanced Energy's Artesyn SIL60C2 series 60 amp DATA SHEET non-isolated DC-DC converter is designed for cost- and space-sensitive applications. It is available in a through-hole vertically mounting configuration with dual rows of pins. The Total Power is 240 Watts. The converter accepts a wide range 4.5 to 13.8 Vdc input and provides an output that is adjustable from 0.8 to 4.0 Vdc to accommodate a wide variety of silicon power needs. Rated at 240 watts, the SIL60C2 is capable of delivering up to 60 amps; it has a typical efficiency of 89% and no minimum load requirement. Standard features include differential remote sense, remote On/Off and remote ‘power good’ indication. This converter also supports phase shedding to save power under light load conditions, and its output voltage can be adjusted to within 1% by a 2-bit VID signal.

# SPECIAL FEATURES

- Two bit VID adjustable output voltage
- Phase shedding for power saving during light loads
- High power density design means reduced board space requirement
- Power good output signal
- Operating ambient temperature up to +70 °C with suitable derating and forced air cooling
- Remote ON/OFF (active high)
- 0 A minimum load
- Input under-voltage lockout
- EU directive 2002/95/EC compliant for RoHS
- Designed to meet EN60950 when used in end-use equipment

# SAFETY

©2020 Advanced Energy Industries, Inc.
---
# SIL60C2

# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input voltage range|4.5 - 13.8 Vdc|
|Input current (max.)|Minimum load: 65 mA|
| |Remote ON/OFF: 20 mA|
|Input current (max.)|20.0 A @ lo max.|
|Start-up time|Power up: <20 ms|
| |Remote ON/OFF: <20 ms|

|Output| |
|---|---|
|Output voltage|See Note 5: 0.8 - 4.0 V|
|Output setpoint accuracy|with VID: 1.0%|
|Line regulation|Low line to high line: ±0.3%|
|Load regulation|Full load to min. load: ±0.2%|
|Load line|0.225 μΩ|
|Min/Max load|0 A/60 A|
|Overshoot|At turn-on: 2% max.|
|Ripple and noise|<40 mV, 5 Hz to 20 MHz, Vin = 12 V, Vout = 1.5 V|
|Transient|Deviation (dependent on output capacitance): 20 μs recovery to within regulation band|

|Output| |
|---|---|
|Efficiency|Vi = 12 V, Vo = 1.5V, Iout = 60 A: 89%|
|Switching frequency|Fixed/ph: 300 kHz|
|Material flammability|UL94V-0|
|Weight|TBD|
|MTBF|12 V @ 40 °C, 100% load: >5,000,000 hours, Bellcore 332|

# ENVIRONMENTAL SPECIFICATIONS

|Thermal performance|Operating ambient temperature: -0 °C to +70 °C|
|---|---|
| |Non-operating ambient temperature: -40 °C to +125 °C|

|Protection| |
|---|---|
|Over temperature protection|Hiccup, non-latching|
|Short-circuit|Hiccup, non-latching|
|Overvoltage protection|Latching|

|Recommended System Capacitance| |
|---|---|
|Input|Ceramic: 3x22 μF|
|Output|1,500 μF|

advancedenergy.com
---
# ORDERING INFORMATION

|Model Number (3,5)|Output Power (Max.)|Input Voltage|Output Voltage|Output Current (Min.)|Output Current (Max.)|Efficiency (Typical)|Regulation Line|Regulation Load|Orientation|
|---|---|---|---|---|---|---|---|---|---|
|SIL60C2-00SADJ-VDJ|240 W|4.5 - 13.8 Vdc|0.8 - 4.0 V|0 A|60 A|89%|±0.3%|±0.5%|Vertical|

# PART NUMBER SYSTEM WITH OPTIONS

|Product Family|Rated Output Current|Performance|Generation|Input Voltage|Output Voltage|Mounting Option|Pins|RoHS Compliance|
|---|---|---|---|---|---|---|---|---|
|SIL|60|C|2|00|SADJ|X|D|J|
|SIL = Single In Line|60 = 60 Amps|C = Cost Optimized|2 = Increased current density|00 = 4.5-13.8 V|Single Adjustable Output|V = Vertical|D = Dual row|J = Pb free (RoHS 6/6 compliant)|

# SETTING OUTPUT VOLTAGE

Default output voltage is set with the 2 bit VID as follows:

|Vid1|Vid0|Vout|
|---|---|---|
|1|1|0.8 V|
|1|0|1.0 V|
|0|1|1.2 V|
|0|0|1.4 V|

The output voltage may be optionally adjusted with a resistor placed in the series with the sense line, from 0.8 V to 4.0 V.

To trim the output voltage, place a resistor in series with pin 6 (RS+). The formula for calculating the value of this resistor is:

Rtrim = 2000 X (Vout - VID_SET)

When trimming output voltage, always choose the nearest VID Vout setting. (VID_SET)

Notes:

1. Measured as per recommended system capacitance.
2. di/dt = 10 A/ μs, Vin = Nom, Tc = 25 ˚C, load change = 0.50 lo max. and vice versa.
3. External fusing is recommended.
4. Measured with external filter.
5. Uses external resistor from trim pin to (-) trim pin.
6. Airflow dependent, 300 LFM minimum required.
7. No capacitor needed for ripple current capability.
8. No capacitor needed for stability.
9. NOTICE: Some models do not support all options. Please contact your local Artesyn Embedded Power representative or use the on-line model number search tool at http://www.artesyn.com to find a suitable alternative.

advancedenergy.com
---
# MECHANICAL DRAWINGS

|HEATSINK ASSEMBLY NOTES| | |
|---|---|---|
|APPLY GAPFILLER 13.92 MAX|ON BACKSIDE OF IC 548 MAX|TO FILL BETWEEN HEATSINK AND PCB|
| | |PCB REF APPLY LIQUIBOND BETWEEN THESE SEMICONDUCTORS AND HEATSINK SURFACES, STENCIL APPLICATION ACCEPTABLE.|
|50.29±0.51|1.980±.020|7.20 MAX|
|1.57±0.15|HEATSINK AND PCB REF|5 MAX|
|.062±.006| |.197 MAX|
| | | |
|19.81±0.51|.780±.020|REF 37 LABEL|
|15.88±0.25|.625±.010|REF 38|
|2.29|0.64±0.03|.118|
|.090|.025±.001 SQ PIN|3.05|
|2.54|.100 TYP|2.54|
| | | |
|NOTE: 1. 9300161-0000 PACKAGING AND MATERIAL HANDLING PROCEDURE.| | |
|2. COSMETIC AND WORKMANSHIP PER 9300152-0000.| | |
|3. LABEL SHOWN FOR REFERENCE PLACEMENT ONLY.| | |
| | | |
|MATERIAL UNLESS OTHERWISE SPECIFIED DIMENSIONS ARE IN INCHES|ARTESYN TECHNOLOGIES|EDEN PRAIRIE, MN 55433|
|NA TOLERANCES: 2 PLACE 3 PLACE ANGLES|.03 .015 1 TITLE:|TOMAHAWK, TLA, VERTICAL|
|RECOMMENDED MOTHERBOARD FOOTPRINT| | |
|2.080| |FINISH MODULE OUTLINE 28AUG06 NA ENGINEER DRAWN D. TETZLAFF DWG. NO. 7091153-JPLUTO|
|7001153-JPLUTO| |D. TETZLAFF 28AUG06 SIZE PROJECT USED ON: DELL TOMAHAWK|
|DETACHED LIST| | |
| | | |

# Pin Assignments

|Pin|Function|Pin|Function|Pin|Function|
|---|---|---|---|---|---|
|1|VID0|14|Vin|27|Vout|
|2|Viout*|15|Ground|28|Vout|
|3|VID1|16|Ground|29|Ground|
|4|Power Good|17|Vout|30|Ground|
|5|RS-|18|Vout|31|Ground|
|6|RS+|19|Vout|32|Ground|
|7|Open|20|Vout|33|Vout|
|8|Enable|21|Ground|34|Vout|
|9|Ground|22|Ground|35|Vout|
|10|Ground|23|Ground|36|Vout|
|11|Vin|24|Ground|37|Ground|
|12|Vin|25|Vout|38|Ground|
|13|Vin|26|Vout| | |

*Viout is a current monitoring pin. 31 mV / A, ±15% tolerance.

4 advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-SIL60C2-235-01 12.30