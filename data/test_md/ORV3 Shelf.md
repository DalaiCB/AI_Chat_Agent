# ARTESYN 50 V, 18 KW, 1OU OPEN RACK POWER SHELVES

15 kW (N + 1) and 9 kW (N + N)

Advanced Energy's Artesyn introduces a 1OU, ORV3 compliant shelf that utilizes single or dual cords. Converting incoming supply voltage into a 50 VDC output with a total power capability of 18 kW. It accommodates 6x3 kW hot-swappable single phase PSU modules. Power Shelf input(s) are universal 7 pin connector which can be configured as star, delta or single phase. It includes a hot-pluggable Shelf Controller for monitoring and control over Ethernet (DMTF Redfish® compatible) management networks. This power shelf is typically used for compute and storage applications which require reliable power and optional battery backup.

# AT A GLANCE

|Total Output Power|Input Voltage|
|---|---|
|Single Whip Shelf: 18 kW, 15 kW (N + 1)|Nominal Ranges: 346 to 480 VAC 3 phase 5 wire Wye (3ph + N + E) 200 to 277 VAC 3 phase 4 wire Delta (3ph + E)|
|Dual Whip Shelf: 18 kW, 15 kW (N + 1) or 9 kW (N + N)| |

# KEY FEATURES

- 15 kW at 50 V with N + 1 redundancy or 9 kW at 50 V with N + N redundancy (dual feed shelf)
- Highly accurate droop + active current sharing
- Houses 6 x 3000 W power modules and a removable shelf controller
- Very high efficiency
- Accepts 3 types of input configurations (3P Delta 4 W, 3P Wye 5 W, 3 x of 1P)

# COMPLIANCE

- EN 61000-4-2 Cat-A for surges
- EN 61000-3-2 Class-A for harmonics
- EN55022, FCC Part 15, CISPR 22, Class-A for EMC

# SAFETY

- UL 60950
- IEC 60950
- EN 62368-1
- UL 62368-1
- IEC 62368-1
- SEMI F47 Compliance

Output Voltage: 50.5 VDC

Mechanical Dimensions: 720 x 537 x 46 mm (L x W x H)

Operating Temperature: -5ºC to +45ºC

©2023 Advanced Energy Industries, Inc.
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# ELECTRICAL SPECIFICATIONS

|INPUT|MIN|NOM|MAX|UNIT|
|---|---|---|---|---|
|Input Voltage (3 phase Delta 4 wire)|180|200/277|305|VAC|
|Input Voltage (3 phase Wye 5 wire)|360|380/480|528|VAC|
|Input Voltage (3 x of 1 phase)|180|200/277|305|VAC|

|OUTPUT|MIN|NOM|MAX|UNIT|
|---|---|---|---|---|
|Set Point VDC (50% Load)|50.625|50.750|50.875|VDC|
|Output Current|-|-|300|A|
|Ripple & Noise (@ 20 MHz BW)1|-|-|500|mVpp|

Note 1: Measured with a 0.1 mF capacitor connected to the probe tip

# POWER SHELF OPTION

The following power shelves are introduced on this specsheet according to the following application:

Power Shelf Option 1 - 6 x 3 kW PSU with dual cord (2 x 20 A NEC breaker upstream) - 700-015235-0100

1OU shelf with two AC power input

6 x 3 kW rectifier slots

Output power: 15 kW with N + 1 and dual cords or 9 kW N + N

Direct connect to tap-boxes/facility – no intermediate PDU.

| |AC In| |AC In| | |
|---|---|---|---|---|---|
| |Chassis| | | | |
| |3|3|3|3|2|

Power Shelf Option 2 - 6 x 3 kW PSU with single cord (32 A IEC breaker upstream) - 700-015746-0100

1OU shelf with one AC power input

6 x 3 kW rectifier slots

Output power: 15 kW with N + 1 and single cord

Direct connect to tap-box / facility - no intermediate PDU

2 advancedenergy.com
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# POWER SHELF OPTION

|AC In|Chassis|
|---|---|
|3|3|
|3|3|
|3|3|
|3|3|
|3|3|

Monitoring & Control Interface

The power shelf includes a slot for a power shelf management controller (PMC) to monitor and control various rectifier parameters. The PMC is connected to rack management controller or facility level monitoring through a monitoring & control interface. If the PMC fails or is not provided, the power system is able to operate normally. The PMC is powered from the 48 V bus directly.

FRU

FRU data is stored in an EEPROM on the power shelf PCB and can be accessed from an I2C line by the PMC. The FRU format follows "IPMI Platform Management FRU Information Storage Definition 1.0, Version 1.3". FRU will support two-byte address and FRU content will start from 0x0000. The FRU template is listed in table below. The detailed FRU information will be made available prior to the build for approval data.

|Organization|String|Example|
|---|---|---|
|Board Info Area|Language Code|19h (English)|
| |Board Mfg Date|[Generate build time]|
| |Board Mfg|Defined by vendor|
| |Board Product|Project Code Name 'ORv3 Shelf'|
| |Board Serial Number|Defined by vendor|
| |Board Part Number|Defined by vendor|
| |Custom Field 1| |
| |Custom Field 2| |
|Product Info Area|Language Code|19h (English)|
| |Product Manufacturer|Defined by vendor|
| |Product Name|Defined by vendor|
| |Part/Model Number|Defined by vendor|
| |Product Version|Defined by vendor|
| |Product Serial Number|Defined by vendor|
| |Product Asset Tag|Defined by vendor|
| |Product Build|EVT (or DVT, PVT)|

advancedenergy.com 3
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# MECHANICAL

ORV3 Rack Mounting Features

These power shelves are designed for front mounting into Open Rack V3 racks on OU pitch rails (please refer to the Open Rack V3 specifications for more details on the design). The design of the 48 V output connector allows it to be placed in any location in the rack. Rack mounting features are crucial in the power shelf design as they help constrain the power shelf in X, Y, and Z directions and ensure solid electrical contact with the 48 V busbar.

Front Latch & Bumper

Please refer to the mechanical CAD for the locations of the front latch and bumper. Note that these serve separate functions and should not be a single part.

Rear Stop

Please refer to the mechanical CAD for the geometry of the rear stop. This is necessary to interface properly with the ORV3 rack.

Connector Details

|AC Input Connector| | |
|---|---|---|
|The power shelf has either one or two AC input connectors, right only in the case of the single whip shelf PN. 700-015746-0100, or left and right in the case of the dual whip shelf PN. 700-015235-0100.|Left|Right|
|Pin| |Pin|

advancedenergy.com
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# MECHANICAL

|AC Input Connector Wiring|5-Wire Plug|7-Pin Conn|AC Pair|4-Wire Plug|7-Pin Conn|AC Pair| |
|---|---|---|---|---|---|---|---|
|L1- W| | |AC Pair 1|L1-W|AC Pair 1| | |
|L2-X| | |AC Pair 2|L2-X|AC Pair 2| | |
|NEUTRAL| | |AC Pair 3|NEUTRAL|AC Pair 3| | |
| |2-Wire Plug|7-Pin Conn|AC Pair| | | | |
| |Li-W| | |AC Pair 1| | | |
|L2-X| | |AC Pair 2| | | | |

# DC Output Connector

The shelf DC output connector is a floating blind mate connector that mates with ORV3 busbars in an ORV3 rack. This gives the flexibility for:

- Placing power and battery shelves any desirable location on the rack
- Increasing power and energy by adding more power and/or battery shelves in the rack

Rack Busbar Assembly

DC Output Connector

# Power Supply Connector

The shelf contains the 6 blind mate mating connectors for the 6 ORV3 PSUs. Amphenol 10127400-01U1520LF or equivalent. This is a R/A receptacle, PwrBlade ULTRA HD connector with 3 low power pins, 25 signal pins, and 4 high power pins. Rectifiers plug into the power shelf directly, and they are hot swappable while the rack is powered. Please refer to "ARTESYN 50 V 3 kW OPEN RACK V3 PSU" datasheet for pinout details.

# PMC/PMI Connector

The PMC is a blind-mate module with a 2C card edge connector. The PMC plugs into the power shelf directly, and is hot swappable while the rack is powered. Please refer to "ARTESYN ORV3 STANDARD PMC" datasheet for pinout details.

Note 1: Measured with a 0.1 mF capacitor connected to the probe tip

advancedenergy.com 5
---
# POWER SHELVES

# POWER SHELF MECHANICAL OUTLINE

|Single Whip Shelf| | | | |
|---|---|---|---|---|
|CONNECTOR|10156974-06077H9F| | | |
|7 PIN INPUT CONNECTOR POSITION| | | | |
|PRODUCT LABEL -| | | | |
|GR COOExxXXXX| | | | |
| | |SEE TABLE| | |
|CHIP|LOLP.SECURITY BLOCKER| | | |
| | |SCALE NS| | |
| |Mewa| | | |
| | |SEE TABLE| | |
|DETAIL| | |201245| |
|SCALE(1:1)|DETAIL:1| | | |
| |537 ,0 5| | | |
| |St DEAL| | | |
|[99 05 MECHANICAL LATCH STOP| | | | |
|EWBOSS DEPTH| | | | |

|Dual Whip Shelf| | | | | | | |
|---|---|---|---|---|---|---|---|
|7 PIN INPUT CONNECTOR POSITION|POSIRONIC Spi0rsss142001-44-2268| | | | | | |
|PRODUCT LABEL| | | | | | | |
| | | | |SEE TABLE| | | |
|VIEW| | | | | | | |
| | | | |SEE TABLE| | | |
|DETAIL| | | | | | | |
| |37+03| | | | | | |
|SEE DETAIL| | | | | |29{TYp| |
|629.0 $ VERTICAL LATCH TO STOP| | | | | | | |
|JUN CONTROLLER| | | | | | | |
|AMMIVUV 04| | | | | | |Unit: mm|

advancedenergy.com
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# MATING CONNECTOR INFORMATION

|DEVICE|CONNECTOR|MATING CONNECTOR|
|---|---|---|
|Shelf|Input Connector: POSITRONIC SP10RSSS48RM220A1-AA-2269|POSITRONIC SP10RSSS1F0W01/AA-2268|
| |Output Connector: FCI BarKlip BK500 Cable 10156914-3D6077HF|ORV3 Busbars|

# THERMAL DESIGN

- Sensor accuracy: For discrete and critical sensors (such as ambient temperature) have an accuracy of ±2°C
- Back-pressure: The shelf is designed to accommodate compliance requirements while ensuring reasonable impact to upstream components. A back-pressure of ≤0.15 inches of water is targeted.
- <li Bbus-bar power or DC output connection assembly: Cables external to the shelf as well as the clip/connector (to the rack bus-bar) mounting at the rear panel are designed to ensure adequate cooling for compliance requirements (temperature difference as a function of current draw).
- Surface temperature: To make the shelf safe for handling in-operation, accessible surfaces should not exceed a temperature of 70°C.

# ENVIRONMENTAL COMPLIANCE

- Gaseous contamination: Severity Level G1 per ANSI/ISA 71.04-1985
- Ambient operating temperature range: -5°C to +45°C
- Operating and storage relative humidity: 10% to 90% (non-condensing)
- Storage temperature range: -40°C to +70°C
- Transportation temperature range: -55°C to +85°C (short-term storage)
- Operating altitude with no de-ratings: 3,050 m (10,000 feet)
- Acoustic noise: Target sound pressure should not exceed 85 dBA when fan modules are running at full speed and operating within the defined environmental envelope

# Vibration and Shock (Non-packaged)

The “power shelf with PSUs inside” meet vibration and shock test per EN 60068-2-6 and 60068-2-27, respectively, for both non-operating and operating condition, with the specifications listed below.

During operating vibration and shock tests, the PSU will exhibit full compliance to the specification without any electrical discontinuities.

During the non-operating tests, no damages of any kinds (included physical damages) should occur and they should not corrupt the functionalities of the PSU per the specifications.

# Vibration Non-Operating:

- Excitation Mode: Sinusoidal
- Test Frequency: 5 to 500 Hz (5 to 9 Hz) 6 mm peak to peak, (9 to 500 Hz) 1 g
- Amplitude: 1 g
- Frequency Change Rate: 1 octave / min
- Test Directions: 3 directions in space (x, y, z)
- Duration: 10 sweep cycles for each direction (2 hours 13 minutes)
- Test Temperature: Room temperature
- Electrical Work: None

advancedenergy.com 7
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# ENVIRONMENTAL COMPLIANCE

|Shock Non-Operating:| |
|---|---|
|Shock Pulse:|Half sinusoidal|
|Shock Duration:|11 ms|
|Shock Amplitude:|12 g|
|Test Directions:|6 directions|
|Number of Shocks:|60 (10 per each direction)|
|Test Temperature:|Room temperature|
|Electrical Work:|None|

|Vibration Operating:| |
|---|---|
|Excitation Mode:|Sinusoidal|
|Test Frequency:|5 to 500 Hz|
| |(5 to 9 Hz) 6 mm peak to peak|
| |(9 to 500 Hz) 1 g|
|Amplitude:|0.5 g|
|Frequency Change Rate:|1 octave / min|
|Test Directions:|3 directions in space (x, y, z)|
|Duration:|10 sweep cycles for each direction (2 hours 13 minutes)|
|Test Temperature:|Room temperature|
|Electrical Work:|Power supply in operation|

|Shock Operating:| |
|---|---|
|Shock Pulse:|Half sinusoidal|
|Shock duration:|11 ms|
|Shock Amplitude:|6 g|
|Test Directions:|6 directions|
|Number of Shocks:|30 (5 per each direction)|
|Test Temperature:|Room temperature|
|Electrical Work:|Power supply in operation|

Package Vibration, Drop and Compression

The power shelves (without PSUs) in their shipping package meet the following requirements:

|Package Vibration:|1.146 g, 2 to 200 to 2 Hz, all three axes, random vibe ISTA 3E 06-06|
|---|---|
|Package Drop:|8-inch drop ISTA 3E 06-06|
|Package Compression:|Maximum compression loading on a bulk pack ASTM D 642-94|

advancedenergy.com
---
# 50 V 18 kW 1OU ORV3 POWER SHELVES

# EMC, SAFETY AND ENVIRONMENTAL COMPLIANCE

The power supply shelf is designed for compliance to allow worldwide deployment.

# Safety Standards

The product is to be designed to comply with the latest edition, revision, and amendment of the following standards. The product is designed such that the end user could obtain the safety certifications: UL 62368-1, IEC 62368-1 and EN 62368-1; hazard-based performance standard for Audio video, IT & Communication Technology Equipment

- UL or an equivalent NRTL for the US with follow-up service (e.g. UL or CSA)
- CB certificate and test report issued by CSA, UL, VDE, TUV or DEMKO
- CE marking for EU

# Component Safety requirements

Following are the safety compliances for major components:

- All fans have the minimum certifications: UL and TUV or VDE.
- All current limiting devices have UL and TUV or VDE certifications and are suitable rated for the application where the device in its application complies with IEC/UL 62368-1.
- All printed wiring boards are rated UL94V-0 and sourced from a UL approved printed wiring board manufacturer.
- All connectors are UL recognized and have a UL flame rating of UL94V-0.
- All wiring harnesses are sourced from a UL approved wiring harness manufacturer. SELV cable to be rated minimum 80 V, 130°C.
- Product safety label will be printed on UL approved label stock and printer ribbon. Alternatively, labels can be purchased from a UL approved label manufacturer.
- The product will be marked with the correct regulatory markings to support the certifications that are specified in this document.

# EMC Requirements

The power shelf meets the following requirements in the latest edition of standards when operating under typical load conditions and with all ports fully loaded. The Power supply integrated into the shelf is called the component power supply. The power shelf will have minimum 6dB margin from the Class A limit for the radiated and conducted emissions.

The following EMC Standards (the latest version) are applicable to the product:

- FCC /ICES-003
- CISPR 32/EN55032
- CISPR 35/EN55035 - Immunity
- EN61000-3-2 - Harmonics
- EN61000-3-3 - Voltage flicker
- VCCI
- KN 32 and KN35

Each individual basic standard for immunity test has the following minimum passing requirement. Higher level of passing criteria may be applied depending on the system manufacturer’s design goals and business needs.

- EN61000-4-2 Electrostatic Discharge immunity
- Contact discharge: &gt; 5.6 kV
- Air discharge: &gt; 11.2 kV
- EN61000-4-3 Radiated immunity
- &gt; 3 V/m
- EN61000-4-4 Electrical Fast Transient immunity
- AC power line: &gt; 1 kV
- Signal line: &gt; 0.5 kV
- EN61000-4-5 Surge
- AC power line: &gt; 2 kV (Line-to-line), &gt; 4 kV (Line-to-earth)
- Signal port: &gt; 1 kV

advancedenergy.com 9
---
# EMC, SAFETY AND ENVIRONMENTAL COMPLIANCE

|EN61000-4-6 Immunity to conducted disturbances|DC power line: &gt; 3 Vrms|
|---|---|
|EN61000-4-8 Power frequency magnetic field immunity, when applicable|&gt; 1 A/m|
|EN61000-4-11 Voltage dip and sag| |

Environmental Compliance

The power shelf (including all components inside) complies with the following minimum environmental requirements:

- RoHS Directive (2011/65/EU and 2015/863/EU)
- REACH Regulation (EC) No 1907/2006;
- Halogen Free: IEC 61249-2-21, Definition of Halogen Free, 900 ppm for Br or Cl, or 1500ppm combined
- US SEC conflict mineral regulation to source mineral materials from socially responsible countries, if applicable
- Waste Electrical and Electronic Equipment (“WEEE”) Directive (2012/19/EU) if applicable;
- Product does not contain any substances regulated by EPA 40 CFR751

# ORDERING INFORMATION

|Model|Description|
|---|---|
|700-015746-0100|Standard ORV3 Power Shelf - Single Whip|
|700-015235-0100|Standard ORV3 Power Shelf - Dual Whip|

|Model|Description|
|---|---|
|700-015234-0100|Standard ORV3 PSU|
|700-015798-0000|Standard ORV3 Management Controller|
|700-015718-0000|Standard ORV3 PMI|

advancedenergy.com
---
ABOUT ADVANCED ENERGY
Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

TRUST

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2023 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-50V 1OU ORV3-235-01 06.01.23