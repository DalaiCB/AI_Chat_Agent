# ARTESYN INTELLIGENT TRANSFER SWITCH

Up to 24000 Watts

Designed for any application needing power switched to different loads during a 24 hour period (i.e. Horticulture, Burn-in, Test and Measurement, etc.) Advanced Energy’s Intelligent Transfer Switch has a built-in PSU to supply power to the relays and MCU module. It is designed to operate with 90 to 264 VAC standard phase input.

# AT A GLANCE

|Total Power|Up to 24 KW|
|---|---|
|Input Voltage|90 to 264 VAC Single Phase|
|# of Outputs|Up to 8|

# SPECIAL FEATURES

- 5 years manufacturer’s warranty
- Modular 8 channel A:B switch
- Standard 19” rack
- Reversible mounting tabs
- Designed for use with iHP and LCM4000 product families
- 100% digital control
- Intelligent zero current switching when used with Artesyn devices
- Digital communication via RS485 (Modbus-RTU)
- Cloud based User configurable GUI
- Natural convection cooled (No Fan)
- Field upgradeable firmware
- Up to 16 racks are addressable from one control node
- Configurable baud rate
- MTBF 400K hours per Telecordia SR-332 Method 1 Case 3, Part Stress
- Product lifetime 10 years minimum

# SAFETY

- EN62368-1
- UL/CSA62368-1
- IEC62368-1/60601-1

# TARGET APPLICATIONS

- Horticulture
- Industrial
- Burn-in

Typical Multi-Channel LED’s ON 12 hours iTS Application On / Off 12 hours

|LED’s ON|Grow Room # 1|
|---|---|
|LED’s OFF|Grow Room # 2|

©2022 Advanced Energy Industries, Inc.
---
# ITS ELECTRICAL SPECIFICATIONS – HOUSEKEEPING POWER SUPPLY MODULE

|Parameter|Value|
|---|---|
|AC Input Voltage|90 to 264 Vac|
|AC Input Frequency|50/60 Hz Nominal|
|AC Input Fusing|Included for both input AC lines (not user serviceable)|
|AC Inrush Current|Upon start-up from a “cold start”, the maximum AC input current shall NOT exceed 50 Amps at 264 VAC 25 degC|
|Output to Relay Module|12V @1A per module; 3V3 as reference voltage +/-1%|

# ITS ELECTRICAL SPECIFICATIONS – RELAY MODULE

|Parameter|Value|
|---|---|
|The relay is double break, capable for 25A max continuous operation. Both output lines, positive and return, are switched. To prevent arcing, the relay is only switched when zero voltage / zero current is flowing through the contacts (Provided by master software control of the power source and Relay MCU.)| |
|The relay module will support iHP modules with nominal voltage rating of 125VDC, 200VDC and 250VDC along with 250VDC of the LCM4000HV. iHP modules connected in series for higher voltage output is allowed, but the load maybe derated so as not to exceed the switching power rating of the relay.| |
|# Inputs|One per relay module, up to 8 can be loaded in a single 2U rack|
|Nominal Input Voltage|90V – 264VAC|
|Input Current Max|25A|
|Input current Fault|>28A|
---
# DIGITAL INPUT AND OUTPUT SIGNALS

|Signal Name|Signal Description|
|---|---|
|PRESENT(OUTPUT)|Low asserted, to be used by MCU module to denote which slot have available relay module. To be connected ground (SGND) in relay module|
|Drive_A (INPUT)|High asserted, to drive relay for output A. Minimum drive strength of 8mA is required|
|Drive_B (INPUT)|High asserted, to drive relay for output B. Minimum drive strength of 8mA is required|
|FAULT_1 (OUTPUT)|Low asserted, to trigger fault if relay coil voltage drop is >5VDC on the active relay. And if input source is turned on and both Relay A and B are off|
|FAULT_2 (OUTPUT)|Low asserted, to trigger fault if both output A and B are active (note: in the event of only relay drive active but other relay is welded/shorted). And if either output A or B is active but there is no active drive|
|SGND (OUTPUT)|Digital ground reference of MCU module and relay module|

Note: FAULT_1 and FAULT_2 should trigger a response from MCU module to shutdown iHP or LCM4000HV PSU output designated to the relay module with fault.

# EMC/IMMUNITY

|Parameter|All Models (Unless otherwise specified)|
|---|---|
|Power Frequency Magnetic Field|EN61000-4-8|
|Voltage Dips, Short Interruptions and Voltage Variations|EN 61000-4-34|

# Electromagnetic Compatibility

|Category|Standard|Frequency|Level / Limits|PSU Performance Criteria1|
|---|---|---|---|---|
|Radiated Emissions|EN 55011/CISPR11|30M -1GHz|Class A|5dB Margin|
|Radiated Emissions|FCC CFR 47, Part 15, Subpart B|>1GHz (see standard)|Class A|5dB Margin|
|Conducted Emissions|EN 55011/CISPR11|150k-30MHz|Class A|5dB Margin|
|Power Line Harmonics|EN 61000-3-12|See standard|See standard| |
|Voltage Fluctuations2|EN 61000-3-11|See standard|See standard| |
|Radiated Immunity|EN 61000-4-3|80M-2GHz|10 V/meter|A|
|ESD|EN 61000-4-2| |8 KV contact, 15 KV Air|A|
|Electrical Fast Transient|EN 61000-4-4| |+/- 4 KV|A|
|Surge AC|IEEE C62.41| |6 KV, CM & DM|Fail Safe|
|Conducted Susceptibility|EN 61000-4-6|150 KHz – 80 MHz|10Vrms|A|

Notes:

1. Performance Criteria as defined by EN 300 386 V1.3.3
2. Applies to AC power supplies only (includes all categories and parameters).

advancedenergy.com
---
# ENVIRONMENTAL OPERATING CONDITIONS

|Operating Temperature|0°C to +50°C at 100% rated load|
|---|---|
|Storage Temperature|-40°C to +85°C|
|Operating Humidity|20% - 90% non-condensing|
|Storage Humidity|10% - 95% non-condensing|
|Vibration|Reference Standard Relay Specification|
|Shock|Reference Standard Relay Specification|
|Shipping and Handling|NSTA for <100 lbs|
|Cooling and Audible Noise|<45 dBA using convection cooling|
|Ingress Protection|IP20|
|Pollution Degree|2|
|RoHS Compliance|See Note Below|

Production Hipot

| |Zone|Hipot Voltage|Trip Current|Arc Detect|Ramp|Test Time|
|---|---|---|---|---|---|---|
|Primary-to-EARTH| |2500Vdc|5mA|Medium or 5mA|500V/s|2s|
|Primary-to-Secondary| |2500Vdc|5mA|Medium or 5mA|500V/s|2s|
|Secondary-to-EARTH| |2500Vdc|5mA|Medium or 5mA|500V/s|2s|

Note: The Artesyn Technologies, Inc. “Products” meet the generally accepted RoHS 6/6 specification. Compliance with this specification includes all the components, parts, assemblies, and packaging of this product. Restricted Materials are not contained in the product or used in the manufacturing of this product or its components above the designated thresholds.

# SIGNAL TIMING DIAGRAM

|ITEM|DESCRIPTION|MIN|MAX|
|---|---|---|---|
|T_on_delay (t1)|Delay from driving the relay to the voltage being present at the output|100ms|-|
|T_off_delay (t2)|Delay from output voltage loss to the relay drive deactivation|-|2s|
|T_transfer delay (t3)|Delay from deactivation of relay activation of adjacent relay.|-|2s|
---
# MECHANICAL REQUIREMENTS

|Mechanical Drawing|Rack Size|Relay module Size|
|---|---|---|
|Height = 81mm (2U)|Height = 76.8 mm| |
|Width = 447mm|Width = 44.4 mm| |
|Depth = 320.1mm|Depth= 301.3 mm| |



advancedenergy.com
---
# Rack Mounting Ears

Rack Mounting Ears are detachable and can be placed in either the front or backside of the shelf.

