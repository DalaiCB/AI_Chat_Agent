# ULTRAVOLT EFL SERIES

# ENHANCED FLOATING HOT DECK LOW-VOLTAGE POWER SUPPLIES

The UltraVolt® EFL series of floating hot deck, low voltage (LV) power supplies offers an integrated solution for systems requiring LV power and controls with high voltage isolation. Combining a highly isolated, DC-to-DC, multioutput low-voltage power supply (LVPS) with an advanced isolated digital and analog I/O topology, the EFL subsystem provides both power and controls to floating-hot deck circuitry. This solution, when combined with one or more Advanced Energy high voltage power supplies or other circuitry, can provide high performance solutions for a variety of applications.

# PRODUCT HIGHLIGHTS

- Precision analog control
- Linearity of ±0.05% and accuracy of ±0.2%
- 10 ppm temperature coefficient
- Isolated up to 15 kV or 30 kV
- Isolation resistance of 150 GΩ (15 kV) or 2 GΩ (30 kV)
- 4 regulated floating LV power outputs
- Isolated digital and analog I/O to and from floating hot deck

# AT A GLANCE

|Nominal Output Voltage|Output #1: +12/+24 VDC|
|---|---|
| |Output #2 and #4: ±15 VDC|
| |Output #3: +5.1 VDC|
|Maximum Output Power|12, 24, or 36 W|
|Isolation Voltage|15 kV or 30 kV|
|Temperature Coefficient|&lt;10 ppm/°C|

# TYPICAL APPLICATIONS

- Floating/stacked ion or e-beam biases
- Floating filament bias
- Floating pulsers and gated grids
- Floating capacitance meters
- Floating high side current monitors
- Floating leakage testers

©2022 Advanced Energy Industries, Inc.
---
# ULTRAVOLT EFL SERIES

All EFLs feature a mode control. Three different models — normal, half-quiet, and quiet — are selectable via the voltage level at the mode pin. A voltage between -1.0 and +0.8 V keeps the unit in normal mode; the up and down analog channels follow their inputs. If the mode feature is not used, the mode pin must be grounded for the EFL to operate properly. A voltage more negative than -4.0 V places the EFL in half-quiet mode. The up channels do not respond to changes in their inputs in half-quiet mode. A voltage greater than +3.75 V and less than +5.0 V places the EFL in quiet mode. In quiet mode, the up and down channels do not respond to changes in their inputs. The voltage level at the mode pin must not exceed +5.0 V at any time. Please contact Advanced Energy for an analysis of your requirements.

|+12 VDC|VPS|VPS|12/+24|
|---|---|---|---|
|1|+24| |1|
|ADC|DAC| |1|
|ADC|DAC| |1|
|DAC|ADC| | |
|DAC|ADC| | |

UltraVolt "EFL" Series

|SYSTEM|SYSTEM|SYSTEM|SYSTEM|
|---|---|---|---|
|SIGNAL|FLOATING POWER|FLOATING POWER|SIGNAL GROUND|
|CHASSIS GROUND|GROUND|GROUND|GROUND|

Note: If a voltage >0.8 V is applied to the mode pin, it must source less than 400 μA.

advancedenergy.com
---
# ULTRAVOLT EFL SERIES

# ELECTRICAL SPECIFICATIONS

|Parameter|Conditions|Models|Units|
|---|---|---|---|
|Input Voltage Range|Full Power|+12 ±5%|VDC|
|Current|Standby (Disabled)|&lt;150|mA|
|Current|No Load|&lt;0.5|A|
|Current|Max Load|&lt;2.5|A|
|AC Ripple Current|Nominal Input, Full Load|&lt;50|mA pk to pk|

Local Controls: Reference - All Types

|Output Voltage|T = +25°C, Initial Value|+5.1 ±2%|VDC|
|---|---|---|---|
|Output Impedance|T = +25°C|464 ±1%|Ω|
|Stability|Over Full Temperature Range|0.4|mV/°C|

Local Controls: Reference LVPS Enable/Disable - All Types

|Power Supply On|Open, or a Voltage Above TTL High (Isource &lt; 400 μA)|+3.2 to 5|VDC|
|---|---|---|---|
|Power Supply Off|Grounded, or a Voltage Below TTL Low|&lt; 0.8 (Isink 1 mA min)|VDC|

|Input/Output Isolation| |Models| | |Units| |
|---|---|---|---|---|---|---|
|Isolation Voltage|Continuous|15| | |kV| |
|Isolation Resistance|All Inputs to All Outputs|150| | |GΩ| |
|Leakage Capacitance|All Inputs to All Outputs|&lt;40 std, &lt;50 “-E”| | |pF| |

|Parameter|Conditions|Models|Units|
|---|---|---|---|
|Isolated Power Outputs|12 W|24 W|36 W (15 kV only)|
|Output #1 Power|Nominal Input, Max Iout|12|W|
|Output #1 Voltage|Nominal Input Voltage Range|+12 ±2%|VDC|
|Output #1 Current|Min to Max|0 to 1|A|
|Output #1 Line Regulation|Nominal Input Range, Full Load|&lt;0.1%|VDC|
|Output #1 Load Regulation|No Load to Full Load|&lt;0.25%|VDC|
|Output #1 Ripple|Full Load|&lt;2.5%|V pk to pk|
|Output #2 and #4 Voltage|Nominal Input Voltage Range|±15 ±5%|VDC|
|Output #2 and #4 Current|Min to Max|0 to 50|mA|
|Output #2 and #4 Line Regulation|Nominal Input Range, Full Load|&lt;0.3%|VDC|
|Output #2 and #4 Load Regulation|No Load to Full Load|&lt;5%|VDC|
|Output #2 and #4 Ripple|Full Load|&lt;2.5%|V pk to pk|
|Output #3 Voltage|Nominal Input Voltage Range|+5.1 ±1%|VDC|
|Output #3 Current|Min to Max|500|mA|
|Output #3 Line Regulation|Nominal Input Range, Full Load|&lt;1%|VDC|
|Output #3 Load Regulation|No Load to Full Load|&lt;1%|VDC|
|Output #3 Ripple|Full Load|&lt;4%|V pk to pk|

advancedenergy.com
---
# ULTRAVOLT EFL SERIES

|Parameter|Conditions|Models|Units|
|---|---|---|---|
|Isolated Controls: TTL Channel "Up"| |All Types| |
|Local Input|Source Voltage, Sink Current|Logic Low: ≤ 0.5 (Isink 3 mA min)|VDC|
| | |Logic High: ≥ 2.4 (300 μA max or open collector)| |
|Isolated Output|Inverted and Buffered TTL|Logic High: ≥ 2.4|VDC|
| | |Logic Low: ≤ 0.55 ± (sources 0.8 mA, sinks 3 mA)| |
|Baud Rate|Duty Cycle|&lt;15|ms|
|Isolated Controls: Analog Channel "Up"| |12 V| |
|Local Input Voltage|Range|0 to +5|VDC|
| | |0 to +10|VDC|
|Isolated Output Voltage|Range|0 to +5|VDC|
| | |0 to +10|VDC|
|Local Input Impedance| |20.0 K|Ω|
|Initial Offset Error| |&lt; ±2|mV|
|Gain Error|Full Scale|&lt; ±0.2%|VDC|
|Linearity Error|Full Scale|&lt; ±0.05%|VDC|
|Stability|30 Min Warmup, Per 8 h, per day|&lt; 0.02%|VDC|
|Temperature Coefficient|0 to +55°C|&lt; ±10|ppm/°C|
|Bandwidth|Symmetric or Asymmetric Signal|DC to 4|Hz|
|-RB’ Isolated Controls: TTL Channel "Down"| |All Types| |
|Isolated ‘Hot Deck’ Input|Source Voltage, Sink Current|Logic Low: ≤ 0.5 (Isink 1 mA Min)|VDC|
| | |Logic High: ≥ 2.4 (300 μA max or open collector)| |
|Local Output|Inverted and Buffered TTL|Logic High: &gt; 2.4 (sources 0.8 mA)|VDC|
| | |Logic Low: &lt; 0.55 (sinks 10 mA)| |
|Propagation Delay|Duty Cycle|&lt; 15|ms|

advancedenergy.com
---
# ULTRAVOLT EFL SERIES

|Parameter|Conditions|Models|Units|
|---|---|---|---|
|Isolated Controls: Analog Channels #1 and #2 "Down"|All Types| | |
|Isolated ‘Hot Deck’ +Input|Range|0 to +5 for 12 V and 0 to +10 for 24 V|VDC|
|Isolated ‘Hot Deck’ -Input|Range|0 to –5 for 12 V and 0 to -10 for 24 V|VDC|
|Isolated ‘Hot Deck’ + or -Input|Signal Source|>10|MΩ|
|Local Output +Voltage|Range|0 to +5 for 12 V and 0 to +10 for 24 V|VDC|
|Local Output -Voltage|Range|0 to –5 for 12 V and 0 to -10 for 24 V|VDC|
|Initial Offset Error|Signal Source|< ± 2|mVDC|
|Gain Error|Full Scale|< ±0.2%|VDC|
|Linearity Error|Full Scale|< ±0.05%|VDC|
|Stability|30 Min Warmup, Per 8 h, Per Day|< 0.01%/< 0.02%|VDC|
|Temperature Coefficient|-20 to +55°C|< ±10|ppm/°C|
|Bandwidth|Symmetric or Asymmetric Signal|DC to 4|Hz|
|Environmental|All Types| | |
|Operating Temperature|Full Load, Case Measurement|-20 to +55°C| |
|Storage Temperature|Non-operating, Case Measurement|-55 to +85°C| |
|Thermal Shock Temperature|Mil-Std-810, Method 503-4, Proc. II|-20 to +55°C| |
|Operating Altitude|All Operating Conditions|Sea level to vacuum| |
|Storage Altitude|Non-operating|Sea level to vacuum| |
|Shock|Mil-Std-810, Method 516.5, Proc. IV 2|20 Gs| |
|Vibration|Mil-Std-810, Method 514.5, Fig. 514.5C-3|10 Gs| |

Note: Analog channels #1 and #2 DOWN parameters are valid for outputs in the range of 10 to 100% of maximum.

advancedenergy.com 5
---
# ULTRAVOLT EFL SERIES

|MECHANICAL SPECIFICATIONS| | |
|---|---|---|
|Construction|Epoxy-filled DAP box certified to ASTM-D-5948| |
|Volume|15EFL: 181.9 cc (11.1 in3)|30EFL: 275.3 cc (16.8 in3)|
|Weight|15EFL: 377.1 g (13.3 oz)|30EFL: 569.8 g (20.1 oz)|
|Tolerance|Overall ±0.050” (1.27 mm)| |
|Pin to Pin|±0.015” (0.38 mm)| |
|15EFL mounting hole locations|±0.025” (0.64 mm)| |
|30EFL mounting hole locations|±0.76 mm (0.030")| |

Note: Pins appear shorter in the outline drawing than actual module to ease visibility of pinout numbers. Minimum pin height from the cover is 7.62 mm (0.300").

7x6 210121 '4- '38

15EFL Module
30EFL Module

advancedenergy.com
---
# ULTRAVOLT EFL SERIES

|Local Connections| |Isolated / Floating Connections| |
|---|---|---|---|
|Pin|Function|Pin|Function|
|1|Input Power Ground Return|1|Analog Down Channel 1, +|
|2|Positive Power Input|2|Analog Down Channel 1, -|
|3|LVPS Enable/Disable/Sync In|3|Analog Down Channel 2, +|
|4|TTL Up|4|Analog Down Channel 2, -|
|5|Signal Ground Return|5|+15 VDC Output|
|6|Analog Up Channel 1|6|Analog Up Channel 2|
|7|+5 V Reference Output|7|Floating TTL Input (Digital Down Channel 1)|
|8|Analog Down Channel 1, +|8|Floating Power Ground Return|
|9|Analog Down Channel 1, -|9|Floating +12 VDC or +24 VDC Output|
|10|Analog Down Channel 2, +|10|Floating -15 VCD Output|
|11|Analog Down Channel 2, -|11|Floating TTL Up|
|12|Analog Up Channel 2|12|Floating Signal Ground Return|
|13|Mode|13|Floating Analog Up Channel 1|
|14|TTL Output (Inverted Down Channel 1)|14|Floating +5.1 VDC Reference Output|

# ORDERING INFORMATION

|Type|15 kV Isolation|15EFL|
|---|---|---|
| |30 kV Isolation|30EFL|
|Input Voltage|12 VDC Nominal|12|
| |24 VDC Nominal|24|
|Power|Watts Output (12 Vin Only)|-12W|
| |Watts Output (24 Vin Only)|-24W|
| |Watts Output (15 kVout, 24 Vin Only)|-36W|
|Standard Features|(1) Digital Up Channel and (2) Analog Up Channels|-I/O|
| |(1) Digital Down Channel and (2) Analog Down Channels|-R/B|
|Options|Partial Mu-Metal Shield|-M|
|Case|Plastic Case—Diallyl Phthalate|Standard|
| |"Eared" Chassis Mounting Plate (15 kV only)|-E|
| |Example:|15EFL12-12W-I/O-RB|
---
# DS TITLE

ABOUT ADVANCED ENERGY

Since 1981, Advanced Energy (AE) — and its UltraVolt® family of products — has perfected how power performs for its customers. For both end users and OEMs, AE’s comprehensive portfolio of standard and custom high-voltage components precisely match system specifications to deliver unparalleled energy, quality, and performance. Through close customer collaboration, design expertise, application insight, and world-class support, AE creates successful partnerships and enables customers to push the boundaries of innovation and stay ahead of evolving market needs.

TRUST

Read and understand all documentation before you install, operate, or maintain Advanced Energy high voltage power supplies. Follow all safety instructions and precautions to protect against property damage and serious or possibly fatal bodily injury. Never defeat safety interlocks or grounds.

CAUTION: High Voltage

For international contact information, visit advancedenergy.com.

Contact Information:

- powersales@aei.com (Sales Support)
- productsupport.ep@aei.com (Technical Support)
- +1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2019 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE®, and Ultravolt® are U.S. trademarks of Advanced Energy Industries, Inc.

RoHS

ENG-High-Power-EFL Series-235-01 10.25.2022