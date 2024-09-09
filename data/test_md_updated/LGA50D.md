# ARTESYN LGA50D STANDARD PROFILE SERIES

Dual O/P Non-isolated 50 A Digital DC/DC Converter
LGA50D-01DADJJ
LGA50D-01DADJSBJ

Advanced Energy's Artesyn LGA50D is a non-isolated DC-DC converter that is designed for cost and space sensitive applications.

This non-isolated unit offers two independent and configurable 25 amp, 50 watt outputs, which can also be combined to a single configurable 50 amp, 100 watt output.

With a footprint of 1 x 0.5 inches or 25.4 x 12.5 mm.

# SPECIAL FEATURES

- Two-phase design
- Dual or single output configuration possible
- High efficiency up to 95.5%
- Small size 1” x 0.5” x 0.48” (LxWxH)
- No minimum load requirement
- Wide operating temperature range
- Exceptional power density
- Analog or digital control
- Automatic loop compensation
- IPC9592B compliant @ Vin = 12 Vdc
- Tape and reel packaging
- Reflow compatible
- Possible to stack up to 4 for 200 A
- I-mon and T-mon supported
- Two (2) variants supported:
- Block pin termination
- Solder bump termination
- Two year shelf life

# SAFETY

Designed to meet IEC62368-1

©2020 Advanced Energy Industries, Inc.
---
# LGA50D-JJ_JSBJ

ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input voltage range|7.5 - 14 Vdc (0.6 Vo ≤ Vo ≤ 3.3 Vo)|
| |10 - 14 Vdc (3.3 Vo < Vo ≤ 5.0 Vo) @ 800 KHz|
|Max input current|20 A|
|Input capacitor (internal)|28.2 μF|
|Input capacitor (external) minimum|88 μF (See Note 1, Page 2)|
|Input capacitor (external)|208 μF (See Note 1, Page 2)|

|Output| | | |
|---|---|---|---|
|Independent output 1 and 2| |Standard profile| |
| |0.6 - 1 V - 25 A| | |
| |1.8 V - 22.5 A| | |
| |2.5 V - 20 A| | |
| |3.3 V - 17.5 A| | |
| |5.0 V - 12 A| | |
|Combined output 1 and 2| |Standard profile| |
| |0.6 - 1 V - 50 A| | |
| |1.8 V - 45 A| | |
| |2.5 V - 40 A| | |
| |3.3 V - 35 A| | |
| |5.0 V - 24 A| | |
|Efficiency| |Standard profile| |
| |@ Vin=12 V, Freq=571 KHz & Ta=25 °C| | |
| |Min - Nom| | |
| |1.0 V - 87.5% - 88.2%| | |
| |1.8 V - 91% - 92.2%| | |
| |2.5 V - 92.5% - 93.7%| | |
| |3.3 V - 93.5% - 94.6%| | |
| |5.0 V - 94% - 95.5%| | |
|Max output power| |120 W| |
|Output capacitor (external) required| |2,200 μF, dual O/P mode Vo1 & Vo2| |
| | |2,400 μF in single O/P mode (See Note 2, Page 2)| |

|Control and ambient temperatures| |
|---|---|
|Operating ambient temperature|-40 °C to +85 °C|
|Storage temperatures|-40 °C to +125 °C|
|Switching frequency|JJ&JSBJ: 571 KHz @ 0.6 Vo ≤ Vo ≤ 3.3 Vo|
| |800 KHz @ 3.3 Vo < Vo ≤ 5 Vo|

Note 1:

Minimum: 4 x 22 μF/16 V ceramic cap (C2012X6S1C226M125AC or equivalent)

Recommended: 1 x 120 μF/16 V polymer caps (APXS160ARA121MH 70G or equivalent) + 4 x 22 μF/16 V ceramic cap (C2012X6S1C226M125AC or equivalent)

Note 2:

Dual mode (2 outputs): 2 x 680 μF/6.3 V Polymer Tan caps (T530X687M006ATE010 or equivalent) + 8 x 100 μF/6.3 V ceramic caps (GRM32EC80J107ME20L or equivalent) + 4 x 10 μF/10 V ceramic caps (GRM31CR71A106KA01L or equivalent)

Single mode (1 output): 2 x 680 μF/6.3 V Polymer Tan caps (T530X687M006ATE010 or equivalent) + 10 x 100 μF/6.3 V ceramic caps (GRM32EC80J107ME20L or equivalent) + 4 x 10 μF/10 V ceramic caps (GRM31CR71A106KA01L or equivalent)

advancedenergy.com
---
# MODEL NUMBERS

|Model Number|Input Voltage|Output Voltage Set Point|Output Current|Efficiency|
|---|---|---|---|---|
|LGA50D-01DADJJ|7.5 - 14 Vdc|0.6 - 5.0 V|50 A max|See table|
|LGA50D-01DADJSBJ|7.5 - 14 Vdc|0.6 - 5.0 V|50 A max|See table|

# ORDERING INFORMATION

|Product Family|Rated Output Current|Performance|Input Voltage|Number of Outputs|Output Type|Pin Termination Type|
|---|---|---|---|---|---|---|
|LGA Series|50 A|D|01|D|ADJ|Blank, SB|

Protection Mode: Blank

Compliance: J

RoHS: Pb free (RoHS 6/6 compliant)

advancedenergy.com 3
---
# BLOCK DIAGRAMS

|Single Unit, Single O/P Configuration|Single Unit, Single O/P Configuration|
|---|
|Vin|Vout|
|Vin|Vo2|
|GND|Voz|
|GND|Ceu|
|PG1|GND|
|PG2|GND|
|EN1|Vot|
|EN2|Vot|
|SYNC|Vot|
|SHARE|VS2 +|
|ADDR|VS2 -|
|SCL|Vinm2|
|SDA|VS1 -|
|SALERT|VSI +|
|RSYNC|RADDR|
|SGND|RASCR|
| |RCFG|
| |Rvtrmi|

|Single Unit, Dual O/P Configuration|Single Unit, Dual O/P Configuration|
|---|
|Vin|Voutz|
|Vin|Voz|
|GND|Voz|
|GND|GND|
|PCI|Voz|
|PG2|GND|
|EN1|Coct|
|EN2|Vo1|
|SYNC|Vo1|
|SHARE|VS2 +|
|ADDR|VS2 -|
|SCL|Vtnmz|
|SDA|VS -|
|SALERT|VSI +|
|RSYNC|RDoR|
|SGND|RASCR|
| |RCFG|
| |Vinmi|
---
# BLOCK DIAGRAMS (CONTINUED)

Two Units, Single O/P Configuration

|Pin #|Function|Pin #|Function|
|---|---|---|---|
|1|Vin|15|CFG|
|2|GND|16|Vtrim1|
|3|PG1|17|VS1+|
|4|PG2|18|VS1-|
|5|EN1|19|Vtrim2|
|6|EN2|20|VS2-|
|7|SYNC|21|VS2+|
|8|SHARE|22|Vo1|
|9|ADDR|23|Vo1|
|10|SCL|24|GND|
|11|SDA|25|Vo2|
|12|SALERT|26|Vo2|
|13|SGND|27|GND|
|14|ASCRCFG|28|Vin|

advancedenergy.com 5
---
# MECHANICAL DRAWINGS

|Side view of standard profile metal-block pin termination type (LGA50D-01DADJJ)|3|
|---|---|
|0.13|(FOR METAL PINS ONLY)|

Side view of standard profile solder bump termination type (LGA50D-01DADJSBJ)

6    advancedenergy.com
---
# MECHANICAL DRAWINGS (CONTINUED)

For standard metal-block pin termination (LGA50D-01DADJJ)LJUL 602235{Q (XS14335S1.9S1/6.1523 TYPST0 35 0 B0IP 1{S1} 3.2561} 6.1915
FOOTPRINT DRAWING OF METAL PINS (BOTTOM VIEW)

Dimensions are in millimeters

Tolerances: Decimal .XX ±0.25

advancedenergy.com 7
---
# MECHANICAL DRAWINGS (CONTINUED)

| |For standard solder bump termination (LGA50D-01DADJSBJ)| | |
|---|---|---|---|
| | |25.40|25|
| | |12.35|21.50|
|20.55| |18.75| |
| | |16.95| |
| | |15.15| |
| |6.15| | |
|1|2|48IYP,51,0.35|0.96 TYP 4|
| | |13.00| |
| | |15.65| |
| | |19.15| |
| | |20.90| |

FOOTPRINT DRAWING OF SOLDER BUMP (BOTTOM VIEW)

Dimensions are in millimeters

Tolerances: Decimal .XX ±0.25

advancedenergy.com
---
# MECHANICAL DRAWINGS (CONTINUED)

Proposed solder pad macros (TBC after Artesyn Internal qualification) for standard solder bump termination (LGA50D-01DADJSBJ). It is adopted for standard metal-block pin termination (LGA50D-01DADJJ)

| | | | |20.90|
|---|---|---|---|---|
| | |19|15| |
| |140| | | |
|15.65| | | | |
|13.00| | | | |
|975| | | | |
|325| | | |313|
|2.90 TYP| | | | |
|3| | | | |
|2| | | | |
|2|2.14|350| |8|
| |9.75| | |JQIOX|
| |13.35| | | |
|1515| | | | |
|16.95| | | | |
|18.75| | | | |
|2055| | | | |
|22|17 (AXL| | | |
| |22.35| | | |

# PROPOSED PAD LAYOUT

Dimensions are in millimeters

Tolerances: Decimal .XX ±0.25

Dotted line represents LGA50D module outline

advancedenergy.com   9
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-LGA50D-JJ_JSBJ-235-01 12.28