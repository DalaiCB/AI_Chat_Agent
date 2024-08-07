# ARTESYN POWERPRO DONGLE

MODBUS RTU TO CANBUS/CANOPEN

MODBUS RTU TO PMBUS

Modbus RTU communication is suitable for long distance data transmission in electrically noisy environments. Advanced Energy's Artesyn PowerPro Dongle support Modbus RTU communication for many Artesyn power supply series, such as NeoPower, LCM10K, LCM4000HV, iTS and iHP series. It converts CANbus/CANopen and PMbus protocols to the Modbus input on the PSU.

# CONTENTS

- Ordering Part Number
- Mechanical Drawings
- Connectors and Pin Definitions
- Environment Specifications
- Regulatory Requirements

*Note: Contact AE technical support for the communication protocols documents. ©2024 Advanced Energy Industries, Inc.
---
# POWERPRO DONGLE

|Ordering Part Number|Description|
|---|---|
|83-200-001|Dongle that converts CANBUS/CANOPEN and PMBUS protocols to the ModBus protocol|

# MECHANICAL DRAWINGS

Note: The dongle comes with a RJ45 to RJ45 cable plug connected to the power supply.

# CONNECTORS AND PIN DEFINITIONS

|Back End Side|Pin 1|PSU MODBUS PORT ADDRESS SELECT|Back End Connector Description|
|---|---|---|---|
| |PSU MODBUS PORT ADDRESS SELECT|Back End Connector|RJ45 port to the power supply|
| | |ADDRESS SELECT|DIP switch to set the I2C address and CAN ID|

advancedenergy.com
---
# POWERPRO DONGLE

# CONNECTORS AND PIN DEFINITIONS (CON'T)

# PSU MODBUS PORT Connector Pin Definition

|Pin|Description|Pin|Description|
|---|---|---|---|
|1|RS485 A|5|Reserve|
|2|RS485 B|6|Communication Return|
|3|Reserve|7|+5V Logic Supply|
|4|Communication Return|8|+5V Logic Supply Return|

# Addressing Switch

|ADDRESS SELECT|DIP ADDR[0] value|DIP ADDR[1] value|DIP ADDR[2] value|DIP ADDR[3] value|
|---|---|---|---|---|
|Switch State|Position 1|Position 2|Position 3|Position 4|
|ON|Set ADDR[0] = “0”|Set ADDR[1] = “0”|Set ADDR[2] = “0”|Reserved|
|OFF|Set ADDR[0] = “1”|Set ADDR[1] = “1”|Set ADDR[2] = “1”|Reserved|

# Addressing - PMBUS

The dongle supports up to 8 unique customer facing addresses.

|Bits 7-4|Bit 3 (A2)*|Bit 2 (A1)*|Bit 1 (A0)*|Bit 0 (R/W)|Address (R/W)|
|---|---|---|---|---|---|
|1011|0|0|0|1/0|0xB1/ 0xB0|
|1011|0|0|1|1/0|0xB3/ 0xB2|
|1011|0|1|0|1/0|0xB5/ 0xB4|
|1011|0|1|1|1/0|0xB7/ 0xB6|
|1011|1|0|0|1/0|0xB9/ 0xB8|
|1011|1|0|1|1/0|0xBB/ 0xBA|
|1011|1|1|0|1/0|0xBD/ 0xBC|
|1011|1|1|1|1/0|0xBF/ 0xBE|

* DIP SWITCH ADDR [2-0] = [A2, A1, A0]

# Addressing - CANBUS

The dongle supports up to 8 unique customer facing addresses.

|Bits 10-3|Bit 2 (A2)*|Bit 1 (A1)*|Bit 0 (A0)*|Address|
|---|---|---|---|---|
|00001011|0|0|0|0x58|
|00001011|0|0|1|0x59|
|00001011|0|1|0|0x5A|
|00001011|0|1|1|0x5B|
|00001011|1|0|0|0x5C|
|00001011|1|0|1|0x5D|
|00001011|1|1|0|0x5E|
|00001011|1|1|1|0x5F|

* DIP SWITCH ADDR [2-0] = [A2, A1, A0]

advancedenergy.com 3
---
# POWERPRO DONGLE - CONNECTORS AND PIN DEFINITIONS (CON'T)

# Front End Side

|Kpin|Front End Connector Description|
|---|---|
|1|PKBUS|
|2|PMbus|
|CaNBUS:|CANBUS|
|DEBUG|PWR|

Front End Connector:

- PMBUS CANBUS-1 & PMBUS CANBUS-2: Dual RJ45 ports for daisy-chaining up to 8 dongles
- DEBUG: Dongle bootload and FRU writing (RS232 signal)
- Pin 8: ModBus daisychain (RS485 signal)

# PMBUS CANBUS-1 / PMBUS CANBUS-2 Connector Pin Definition

|Pin|Description (Left RJ45)|Description (Right RJ45)|External Resistor|
|---|---|---|---|
|1|Serial Data Signal (SDA)|Serial Data Signal (SDA)|Pull-up resistor 470 to 680 ohms, 1% tolerance|
|2|Digital Ground|Digital Ground|N/A|
|3|Serial Clock Signal (SCL)|Serial Clock Signal (SCL)|Pull-up resistor 470 to 680 ohms, 1% tolerance|
|4|Reserve|Reserve|N/A|
|5|Reserve|Reserve|N/A|
|6|SMBALERT#|SMBALERT#|Pull-up resistor 10K ohms, 1% tolerance|
|7|CANBus High|CANBus High|120 ohms, 1% tolerance resistor across CANBus|
|8|CANBus Low|CANBus Low|Low and High signals|

# Debug Connector Pin Definition

The dongle debug connector provides dongle bootload and FRU writing capability through RS232 signal and passthrough ModBus daisychain capability through RS485 signal.

|Pin|Signal|Description|
|---|---|---|
|1|RS232 TX|Dongle FW bootloading / FRU Write|
|2|GND|Ground|
|3|RS485A|Modbus passthrough from PSU|
|4|RS232 RX|Dongle FW Bootloading / FRU Write|
|5|GND|Ground|
|6|RS485B|Modbus passthrough from PSU|

RS232 serial configuration: Data Rate=9600, Data Bits=8, Parity=none, Stop Bits=1.

# PWR LED

|Color|Description|
|---|---|
|Solid Blue|Indicates dongle power on|
|Solid Amber|Indicates a dongle fault has occurred|
|Off|Indicates dongle power off|

advancedenergy.com
---
# POWERPRO DONGLE

| |Environment Specifications| |
|---|---|---|
|Operational Temperature|-40°C to 70°C| |
|Storage Temperature|-40°C to 85°C| |
|Humidity|Operating, non-condensing 10% to 95% RH| |
|EMC|Tested with compatible PSU model| |
|Shock and Vibration|TBD| |

# REGULATORY REQUIREMENTS

|Standard|Description|
|---|---|
|Safety Approvals|CE (LVD+ROHS), EN 62368-1 Listed|
|ROHS|RoHS 6 compliant|

advancedenergy.com 5
---
# ABOUT ADVANCED ENERGY

Advanced Energy (AE) has devoted more than four decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

TRUST

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2024 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE®, Evergreen™, and Vento™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-POWERPRO DONGLE 06.26.24