# ARTESYN LGA80D SERIES

Dual O/P Non-isolated 80 A Digital DC/DC Converter

DATA SHEET

|Total Current:|80 A (single)|
|---|---|
| |40 A (dual)|
|Input Voltage:|7.5 - 14 Vdc|
|Variable Output:|0.6 - 5.2 V|

# SPECIAL FEATURES

- Two-phase design
- Dual or single output configuration possible
- High efficiency up to 95.5%
- Small size 1” x 0.5” x 0.48” (LxWxH)
- Supports PMBus
- No minimum load requirement
- Wide operating temperature range
- Exceptional power density
- Automatic loop compensation
- Excellent transient response
- Analog or digital control
- IPC9592B compliant
- Tape and reel packaging
- Reflow compatible
- Possible to stack up to 8 phases for 320 A
- Two year warranty (Consult factory for extended terms)

# SAFETY

Designed to meet IEC62368

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input voltage range|7.5 -14 Vdc|
|---|---|
|Max input current @ 7.5 V|33 A|
|Input capacitor (internal)|120 μF|

# Environmental and General Information

|Operating ambient temperature|-40 °C to +85 °C|
|---|---|
|Storage temperature|-40 °C to +125 °C|
|Switching frequency (RSYNC = 23.7 Kohm)|457 kHz typical (can be configured)|
|CMTBF Telcordia SR-332, Issue 3, Method 1 Case 1|50 MHours|

# Protection

|Overcurrent protection|Refer to application note for detail|
|---|---|
|Overvoltage protection|110% Vo nominal|
|Overtemperature protection (controller temperature)|120 °C nominal|

# Output*

|Independent output 1 and 2| | |
|---|---|---|
| |0.6 V to 1 V|40 A|
| |1.8 V|35 A|
| |2.5 V|32.5 A|
| |3.3 V|30 A|
| |5 V|20 A|
|Combined output 1 and 2| | |
| |0.6 V to 1 V|80 A|
| |1.8 V|70 A|
| |2.5 V|65 A|
| |3.3 V|60 A|
| |5 V|40 A|

*Output @ Vin = 12 V, Ta = 25 °C, unless otherwise noted

|Parameter|Conditions|Min|Nom|Max|
|---|---|---|---|---|
|Line regulation|Measured at remote sense| | | |
| |0.6 ~ 1.0 V| |2 mV| |
| |1.0 ~ 5.0 V| |0.2%| |
|Load regulation|Measured at remote sense| | | |
| |0.6 ~ 1.0 V| |5 mV| |
| |1.0 ~ 5.0 V| |0.5%| |
|Output capacitor per output|2 x 220 μF / 6.3 V polymer tan caps| |740 μF| |
| |(external minimum)| | | |
| |(6TPF220M5L or equivalent| | | |
| |3 x 100 μF / 6.3 V ceramic caps| | | |
|Ripple and noise|One module one output| | | |
| |(with minimum caps) 5 Hz to 20 MHz| |15 mV| |
| |0.6 to 1.8 V| |25 mV| |
| |2.5 V to 3.3 V| |40 mV| |
| |5.0 V| | | |
|Ripple and noise|One module two outputs| | | |
| |(with minimum caps) 5 Hz to 20 MHz| |18 mV| |
| |0.6 to 1.8 V| |35 mV| |
| |2.5 V to 3.3 V| |50 mV| |
| |5.0 V| | | |

advancedenergy.com
---
# ORDERING INFORMATION

|Model Number|Input Voltage|Output Voltage Set Point|Output Current|Efficiency|
|---|---|---|---|---|
|LGA80D-00DADJJ|7.5 - 14 Vdc|See table|80 A max|See table|

# BLOCK DIAGRAM - ONE MODULE ONE OUTPUT

|GND|CuD|
|---|---|
|ENZ| |
|EYNC|LGABOD|
|SHARE|VS2 -|
|CDDR|VS2|
|CL|Vtrim2|
|SDA|VS1 -|
|SALERT|SGND|
|ASCR|CFG|
| |Vtrimi|
| |33|

advancedenergy.com
---
# BLOCK DIAGRAM - ONE MODULE TWO OUTPUTS

| | | | | | |
|---|---|---|---|---|---|
| | |GND| |Vout2| |
|GND|CuD| |GND|GND| |
| | |LGABOD| |Vout1| |
| |YNC|SHARE| | | |
|~DDR|CL|SDA| | | |
|SALERT|SGND|ASCR|CFG|Vtrim1| |
| | | |VS1-| | |

# BLOCK DIAGRAM - TWO MODULES ONE OUTPUT

| | | | | |
|---|---|---|---|---|
|GND| |Vo2| |Vout|
|GND| | |Vo2| |
| |PG1| |Vo1|GND|
| |PG2| | | |
| | |LGABOD| | |
|SYNC|SHARE| |VS2-| |
|~DDR|SCL| |Vtrim2| |
|FDA|SALERT|SGND|ASCR|CFG Vtrim1|
| | | |VS1-| |
| | |Vo2| | |
|GND| |Vo2| | |
| |PG1| | | |
| |PG2| | | |
| | |LGABOD| | |
|YNC|SHARE| |VS2-| |
|CDDR|SCL| |Vtrim2| |
|SDA|FALERT|SGND|ASCR|CFG Vrim1|
| | | |VS1-| |

advancedenergy.com
---
| |Vout Setting|Address Setting| |
|---|---|---|---|
|RVtrim (kΩ)|Vout (V)|RADDR (kΩ)|SMbus ADDRESS|
|LOW|1|LOW|40h|
|OPEN|1.2|OPEN|42h|
|HIGH|0.9|10|41h|
|10|0.6|11|43h|
|11|0.65|12.1|44h|
|12.1|0.7|13.3|45h|
|13.3|0.75|14.7|46h|
|14.7|0.8|16.2|47h|
|16.2|0.85|17.8|48h|
|17.8|0.9|19.6|49h|
|19.6|0.95|21.5|4Ah|
|21.5|1|23.7|4Bh|
|23.7|1.05|26.1|4Ch|
|26.1|1.1|28.7|4Dh|
|28.7|1.15|31.6|4Eh|
|31.6|1.2|34.8|4Fh|
|34.8|1.25|42.2|51h|
|38.3|1.3|46.4|52h|
|42.2|1.4|51.1|53h|
|46.4|1.5|56.2|54h|
|51.1|1.6|61.9|55h|
|56.2|1.7|68.1|56h|
|61.9|1.8|75|57h|
|68.1|1.9|82.5|58h|
|75|2|90.9|59h|
|82.5|2.1|100|5Ah|
|90.9|2.2|110|5Bh|
|100|2.3|121|5Ch|
|110|2.5|133|5Dh|
|121|2.8|147|5Eh|
|133|3|162|5Fh|
|147|3.3|178|60h|
|162|4| | |
|178|5| | |
---
# MECHANICAL DRAWINGS

| | | |Pin Assignments Single Output| |
|---|---|---|---|---|
| | | |Pin #|Function|
| |1| | |Vin|
| | | |2|GND|
| | | |3|PG1|
| | | |4|PG2|
|5| | | |EN1|
| | | |6|EN2|
| | | |7|SYNC|
| | | |8|SHARE|
| | |9| |ADDR|
| | | |10|SCL|
| | | |11|SDA|
| | | |12|SALERT|
| | |13| |SGND|
| | | |14|ASCRCFG|
| | | |15|CFG|
| | | |16|Vtrim|
| | | |17|VS1+|
| | | |18|VS1-|
| | | |19|Vtrim2|
| | | |20|VS2-|
| | | |21|VS2+|
| | | |22|Vo1|
| | | |23|Vo1|
| | | |24|GND|
| | | |25|Vo2|
| | | |26|Vo2|
| | | |27|GND|
| | | |28|Vin|

# RECOMMENDED PAD LAYOUT (FOOTPRINT)

Notes:

Dimensions are in millimeters and (inches)

Tolerance: X.X mm ±0.5 mm (X.XX in. ±0.02 in.)

X.XX mm ±0.25 mm (X.XXX in. ±0.010 in.)

advancedenergy.com
---
# MECHANICAL DRAWINGS (CONTINUED)

1.60 (9X)6.803.3022.3521.50 (4X)20.5518.7516.9515.1513.3511.559.757.956.153.502.140.65 (2X)0.13 (0.005")

1 2 3 4 5 6 7 8 9 10 11 12 13 SIDE VIEW

| | | | | | |1.30 (12X)|28|
|---|---|---|---|---|---|---|---|
| | | | |2.35| | | |
| | | | | |4.15|27| |
|1.50 (19X)|16| | | | | | |
|5.95|26| | | | | | |
|7.75| | | | | | | |
| |2.30 (9X)| | | | | | |
| |0.35| | | | | | |
| | | | | |0.80 (19X)| | |
| |3.25|12.20 (0.48")| | | | | |
| |6.50|1.60 (0.063")| | | | | |
| | | |9.75| | | | |
| | | |13.00| | | | |
| | | |15.65| | | | |
| | | |17.40| | | | |
| | | |19.15| | | | |
| | | |20.90| | | | |
| | | | |22.65| | | |

# FOOTPRINT DRAWING OF METAL PINS (BOTTOM VIEW)

Notes:

Dimensions are in millimeters and (inches)

Tolerance: X.X mm ±0.5 mm (X.XX in. ±0.02 in.)

X.XX mm ±0.25 mm (X.XXX in. ±0.010 in.)

advancedenergy.com 7
---
ABOUT ADVANCED ENERGY

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-LGA80D-235-01 12.28