ARTESYN LGA C SERIES

15 to 100 Watts ARTESYN LGAt M1OC-OOSADJJ

Advanced Energy’s Artesyn LGA C series is a non-isolated DC-DC converter that provides a cost-effective high density power solution in a low profile, surface-mount land grid array package for space sensitive applications. The converter accepts a wide range 3.4 to 14 VDC input and has a 15 to 100 watts power output rating. Its output voltage is adjustable from 0.59 to 5.1 VDC to accommodate a wide variety of silicon power needs. Standard features include remote sense, remote enable and voltage margining. LGA C series converters offer resistor-programmable undervoltage lockout, as well as non-latching short-circuit and overvoltage protection.

AT A GLANCE

|Total Power|15 to 100 W|
|---|---|
|# of Outputs|Single|

SPECIAL FEATURES

- 3, 6, 10 and 20 A output current rating
- Wide input voltage range: 3.4 to 14 V
- Adjustable output voltage: 0.59 to 5.1 V
- Excellent transient response
- High efficiency
- Output margining
- Power enable
- Minimal airflow requirement
- Termination voltage capability
- Ultra compact profile and footprint
- RoHS compliant
- Remote sense
- Termination voltage capability

SAFETY

- Designed to meet EN60950
- International Standards for Solderability: J-STD-002B
- IEC-60068-2-58

©2022 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Output| |3/6/10 A Models|20 A Model|
|---|---|---|---|
|Output voltage|See page 3| |0.59 to 5.1 V|
|Output setpoint accuracy|0.1% trim resistors| |±1.0%|
|Line regulation| | |±0.2%|
|Load regulation| | |±0.5%|
|Max power| |15/30/50 W|100 W|
|Overshoot|At turn-on| |0%|
|Undershoot|At turn-off| |0 mV|
|Ripple and noise|See note 1|20/25/30 mV|30 mV|
|5 Hz to 20 MHz|Vin = 5 V, Vout = 2.5 V| | |
|Transient response|See notes 1 and 2|100/160/160 mV|1175 mV|
| |Vin = 5 V, Vout = 2.5 V|15 μs recovery to within regulation band|15 μs recovery to within regulation band|

|Input| | | | |
|---|---|---|---|---|
|Input voltage range|See notes 3| |3.4 to 14 VDC|4.5 to 14 VDC|
|Input current|Enable on at (0 A)| | |50 mA|
| |Enable off| | |5 mA|
|Start-up time|Power up| | |3 ms|
| |Enable on/off| | |2 ms|

|General| | | |
|---|---|---|---|
|Efficiency|Vin = 5 V, Vo = 2.5 V, Iout = 50% Imax|92% typ.| |
|Switching frequency| |1 MHz|800 kHz|

|Material flammability| |UL94V-0| | |
|---|---|---|---|---|
|MTBF|12 V @ 40 °C|> 20,000,000 hours|100% load|Bellcore 332|
|Coplanarity| |150 μm| | |
|Thermal performance|Operating ambient|-40 °C to +85 °C| | |
| |Non-operating ambient|-40 °C to +125 °C| | |

|Protection| |
|---|---|
|Short circuit|Hiccup, non-latching|
|Overvoltage|Hiccup, non-latching|

|Mininum Recommended System Capacitance|3/6/10 A Model|20 A Model|
|---|---|---|
|Short circuit|1 μF|10 μF|
|Overvoltage|10 μF|50 μF|

# advancedenergy.com
---
# ORDERING INFORMATION

|Standard Model Numbers|Output Power (Max.)|Input Voltage|Output Voltage|Output Current Min|Output Current Max|Efficiency (Typical)|Regulation Min|Regulation Max|
|---|---|---|---|---|---|---|---|---|
|LGA03C-00SADJJ|15 W|3.4 to 14.0 VDC|0.59 to 5.1 VDC|0 A|3 A|92%|±0.2%|±0.5%|
|LGA06C-00SADJJ|30 W|3.4 to 14.0 VDC|0.59 to 5.1 VDC|0 A|6 A|92%|±0.2%|±0.5%|
|LGA10C-00SADJJ|50 W|3.4 to 14.0 VDC|0.59 to 5.1 VDC|0 A|10 A|92%|±0.2%|±0.5%|
|LGA20C-01SADJJ|100 W|4.5 to 14.0 VDC|0.59 to 5.1 VDC|0 A|20 A|91%|±0.2%|±0.5%|

# MODEL NUMBER SYSTEM WITH OPTIONS

|Product Family|Rated Output Current|Performance|Input Voltage|Type of Output|Options|RoHS Compliance|
|---|---|---|---|---|---|---|
|LGA|XX|C|00|SADJ|X|J|

Rated Output Current: 03 = 3 Amp, 06 = 6 Amp, 10 = 10 Amp, 20 = 20 Amp

Performance: C = Cost Optimized

Input Voltage: 00 = 3.4 to 14.0 V, 01 = 4.5 to 14.0 V

Type of Output: Single Adjustable Output

Options: X = Various Options (see Sales Rep)

RoHS Compliance: J = Pb free (RoHS 6/6 compliant)

# HEATSINK NUMBER SYSTEM WITH OPTIONS

|Product Family|Product|Purpose|Height*|
|---|---|---|---|
|LGA|XX|C|00|

Product: Land Grid Array Heatsink

Purpose: Heatsink and Adhesive

Height*: Total Height (LGA20 + Heatsink)

Height options: 045 = 0.45", 048 = 0.48", 050 = 0.50"

* Height is the total height of the LGA20C-00SADJJ with heatsink attached.

advancedenergy.com 3
---
# APPLICATION EQUATIONS

# Setting Output Voltage

Default output voltage: 0.591 V

The output voltage may be adjusted with a resistor placed between the "Trim" and "-Sense" pin.

The formula for calculating the value of this resistor is:

|Rtrim (kΩ) =|1.182|
|---|---|
| |Vout - 0.591|

See Technical Reference Note for other trimming methods.

To margin the output up, pull the margin control pin high. To margin down, pull the margin control pin low. If the pin is left floating, the feature is disabled. The maximum margining range is ±33% of the output default voltage setting, with maximum output at 5.5 V

Vmargin_up = 0.1182 * Rmargin * Rtrim + 2k / Rofs + Rtrim

Vmargin_down = 0.1182 * Rmargin * Rtrim + 2k / Rofs - Rtrim

# Setting Under Voltage Lock Out – 20 A Models

Default Turn-on voltage: 2.9 V (300 mV Hysteresis)

The Turn-on voltage may be adjusted with a resistor placed between the “Enable” and “Ground” pins.

The formula for calculating the value of this resistor is:

|Ruvlo (kΩ) =|14.81 * 6.81|
|---|---|
| |(6.81 * VTurn_on) - 18.16|

Default Turn-on voltage: 4.3 V (300 mV Hysteresis)

The Turn-on voltage may be adjusted with a resistor placed between the “Enable” and “Ground” pins.

The formula for calculating the value of this resistor is:

|Ruvlo (kΩ) =|30.1 * 4.22|
|---|---|
| |(8.577 * VTurn_on) - 34.32|

*ONLY USE WITH OPEN COLLECTOR DEVICE

*DO NOT DRIVE PIN WITH A VOLTAGE

# Notes:

1. Measured as per recommended minimum system capacitance.
2. di/dt = 10 A/ μs,12 Vin = Norm, Tc = 25 °C, load change = 50% lo 100% Imax.
3. Internal input capacitance is rated 16 Vdc maximum.

External input fusing is recommended.

advancedenergy.com
---
# REVISION RECORD

|PART NUMBER|REV|DESCRIPTION|DRAFT|DATE|
|---|---|---|---|---|
|7091323-0000|A|RELEASE FOR PRODUCTION REVISION RECORD|MATT KRETMAN|04/10/09|
|7091323-0000|REVB|UPDATE TO PARALLELISM SPEC DESCRIPTION|MATT KRETMAN DRAFT|05/26/09|
|7091323-0000|A|RELEASE FOR PRODUCTION|MATT KRETMAN|04/10/09|
|7091323-0000|B|UPDATE TO PARALLELISM SPEC|MATT KRETMAN|05/26/09|

NOTE:

1. 9300161-0000 PACKAGING AND MATERIAL HANDLING PROCEDURE.
2. COSMETIC AND WORKMANSHIP PER 9300152-0000.
3. LABEL SHOWN FOR PLACEMENT REFERENCE ONLY.

MATERIAL

1. 9300161-0000 PACKAGING AND MATERIAL HANDLING PROCEDURE. UNLESS OTHERWISE SPECIFIED EMERSON NETWORK POWER

2. COSMETIC AND WORKMANSHIP PER 9300152-0000. DIMENSIONS ARE IN INCHES EDEN PRAIRIE, MN 55433

Pin Assignments-

3. LABEL SHOWN FOR PLACEMENT REFERENCE ONLY. TOLERANCES:

2 PLACE 3 PLACE ANGLES

.03 .015 1 TITLE: PH. 952-941-1100

UNLESS OTHERWISE SPECIFIED HOLE TOLERANCE: .005 LGA 10 TLA EMERSON NETWORK POWER

MATERIAL APPROVALS DATE

FINISH- DIMENSIONS ARE IN INCHES

TOLERANCES: DRAWN DWG. NO. EDEN PRAIRIE, MN 55433

Single Output 3 PLACE ANGLES- 2 PLACE

ENGINEER

HOLE TOLERANCE: MATT KRETMAN .03 .015

.005 10APR09 10APR09 TITLE: PROJECT USED ON: 7091323-0000 B

MATT KRETMAN 10APR09 SIZE PROJECT USED ON:

THIRD B LGA10C-00SADJJ

# Recommended System Board Footprint

VoutPin 16Pin 24Pin 10Pin 9Pin 5Pin 1Module OutlineKeep Out AreaVinNC - Offset+ Offset- Sense+ SenseNCNCNCEnablePower GoodMargin ControlTrim

Tolerance Note: ±0.010 (0.25)

Recommended Solder Paste Stencil

advancedenergy.com 5