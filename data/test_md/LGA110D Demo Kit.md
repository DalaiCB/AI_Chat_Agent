# Energy Advanced TECHNICAL REFERENCE NOTE

ARTESYN LGA110-EVAL-KIT Evaluation Test Board

# PRODUCT DESCRIPTION

Advanced Energy’s Artesyn LGA110D Evaluation Test Board is designed to have two LGA110D non-isolated modules. It allows the user to test and investigate the performance of modules. Total Power: 350 Watts per Module. Input Voltage: 0.5 to 5 Vdc. # of Outputs: Dual or Single.

This document is a reference guide for the evaluation test board. It provides output terminals, test points to power signals, control signals and communication interface via I2C bus. Refer to the technical reference note of the power supply for more information about the specifications and the signal definitions.

# CONTENTS

- Overview
- Pin Assignment
- Test Point Introduction
- Test Set Up
- Operation
- Supported Models
- Schematic
- PCB Layout

©2021 Advanced Energy Industries, Inc.
---
# Overview

Default Settings:

Module1 is configured as 2 phase 2 output (Vo1, Vo2)

Module2 is configured as 2 phase 1 output (Vo3)

The key components and connection locations are shown in the picture of the evaluation board below.

| |GND|Vin1| |Vin2|GND|
|---|---|---|---|---|---|
|Module1| | | | |Module2|
|Efficiency| | | | |Efficiency|
|Measurement| | | | |Measurement|

Enable Jumper

Enable Switch

SYNC Jumper

I2C Connector

| |Vo3|
|---|---|
|Enable Setting| |
|Module2 2phase 1output| |

|Vo2 Setting|Module1 2phase 2output|
|---|---|
|Vo1 Setting| |

Vout1
Vout2
GND
Vout3

Figure 1. Evaluation Test Board for LGA110D

Rev. 01.17.22_#1.0 advancedenergy.com 2
---
# PIN ASSIGNMENT

|Item|Pin Number|Designation|Function|
|---|---|---|---|
| |BUSB101|VIN1|Input Terminal|
| |BUSB102|VIN1_GND|Input Return Terminal|
| |BUSB1101|VIN2|Input Terminal|
| |BUSB1102|VIN2_GND|Input Return Terminal|
| |BUSB105|VO1|Output Terminal|
| |BUSB106|VO1_GND|Output Return Terminal|
| |BUSB103|VO2|Output Terminal|
|Test Point|BUSB104|VO2_GND|Output Return Terminal|
| |BUSB1105|VO3|Output Terminal|
| |BUSB1106|VO3_GND|Output Return Terminal|
| |BUSB1103|VO3|Output Terminal|
| |BUSB1104|VO3_GND|Output Return Terminal|
| |J205|VIN1, VO1& VO2|Module1 Efficiency Measurement|
| |J1205|VIN2& VO3|Module2 Efficiency Measurement|
| |J203|Enable Jumper|Output Enable|
| |J1206|SYNC Jumper|Clock Synchronization|
| |S201|Enable Switch|Output Enable|
| |S601|VO1|VO1 Setting|
| |S602|VO2|VO2 Setting|
| |S603|VO3|VO3 Setting|
| |J204|I2C Connector J206|I2C Communication|

Rev. 01.17.22_#1.0 advancedenergy.com 3
---
# LGA110-EVAL-KIT

# TEST POINT INTRODUCTION

|LGA110D Output Enable Connection (S201, J203)|OUTPUT ENABLE|
|---|---|
|J203|R21I|
|J203|R212|
|J203|R213|
|J203|R882|

|LGA110D I2C Connection (J204, J206)| | | | | | |
|---|---|---|---|---|---|---|
| |Pin1|Pin9| | | | |
|Pin5|Pin3|Pin1| | | | |
|Pin6|Pin4|Pin2| | | | |

I2C connector

READ DIGITAL DATA

Rev. 01.17.22_#1.0

advancedenergy.com
---
# LGA110-EVAL-KIT

# TEST POINT INTRODUCTION

| |LGA110D SYNC Connection (J1206: SYNC1, SYNC2)|PHASES CONNECTOR| | | | |
|---|---|---|---|---|---|---|
|521| |SHARE?|J1206 [451 814343-0002]|J1206 SHARE3| | |
| | |EN2|J1206 [451884878-0002]|J1206 EN3| | |
| |SYNC1|J1206 [451-884878-0002]|J1206 SYNC2| | | |
| | |PG2|J1206 [451-884890-0002]|J1206 PG3| | |
| | |VS2+|J1206 [451-88HR80-0002]|J1206 VS3+| | |
| | |VS2 =|J1206 [451- -884850-e082]884870-8802]|J1206 VS3 =| | |
| | |DDC2|J1206 [451 -|J1206 DDC3| | |

|LGA110D Voltage Setting (S601, S602, S603 & S604)| | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| |ON|R601 (309K)|VSEL/SA1|0.5V| | | | |
| | | | | | | | |1.0V|
| | | | | | | | |1.8V|
| | | | | | | | |2.5V|
| | | | | | | | |3.3V|
| |5.0V| | | | | | | |
| | | | | | | | |GND|

|ON|DIP|8| | | | | | |
|---|---|---|---|---|---|---|---|---|
|R631 (392K)|VSEL/SA2| | | | | | |0.5V|
| | | | | | | | |1.0V|
| | | | | | | | |1.8V|
| | | | | | | | |2.5V|
| | | | | | | | |3.3V|
| |5.0V| | | | | | | |
| | | | | | | | |GND|

3647 7 RSak 7 3541 7 3538 7 BS35 7 3833

Rev. 01.17.22_#1.0 advancedenergy.com
---
# LGA110-EVAL-KIT

TEST POINT INTRODUCTION

| |V1p53|
|---|---|
|(5n604scttingS604 5604 (5160) _Vo}SETTING3333 56086u3w [ 86g3w (Ox6E) VSELLSA?|Vo3 SETTING|
|8 84 %8 8 S603 063w i% i% 063w @VS S603| |
|ON DIP ON DIP C1v0 0.5V1.@V| |
|2 34 5 6 C 1V8 1.8V| |
|C2V5 2.5V| |
|C 3v3 3.3v| |
|CSVA 5.0V| |
|Eek3w 063w MPSL GND|Vo4 SETTING|
| | |
|AV5 5684 0.5v| |
|Jvd 1.0v| |
|DIVS 1.8V| |
|DVS 2.5V| |
|Bu1 3.3v| |
|D5MA 5.0v| |
|88517| |
|84063w 82674| |
|8.063w 33671| |
|izo63w 68528063w83625| |
|8.063w Eeez Refdes start from 161X| |

# LGA110D Vout Ripple Measurement Point (J303, J403, J1403)

|J303 (Vout2)|R301|
|---|---|
|Voniz|e24 8603|
|J303| |
|(301 (302| |
|8e85 je83| |
|R3e4| |
|8 0663| |
|J403 (Vout1)|R401|
|Voii|8146 091 0603 4e}|
|faei| |
|dBe5 {883(402| |
|1206 340t| |
|%3w 0503| |

Rev. 01.17.22_#1.0 advancedenergy.com 6
---
# LGA110-EVAL-KIT

TEST POINT INTRODUCTION

| |R1404| |9Rw 5%|{881|C14ez8683|J1403|
|---|---|---|---|---|---|---|
|J1403 (Vout3)|R1405|0805|Biw 5%| | | |

LGA110D PG Measurement Point (J210, J211, J1210)

| |R214| |LED202|PG1|
|---|---|---|---|---|
| |R215| |LED203|PG2|
| | |8603| |PG1|

|J210 (PG1)|J211 (PG2)|J1210 (PG3)| | |
|---|---|---|---|---|
| |R1216| |LED1204|PG LEDPGZ|
| |R1215| | |SYNC2|

Rev. 01.17.22_#1.0 advancedenergy.com 7
---
# LGA110-EVAL-KIT

# TEST POINT INTRODUCTION

| |LGA110D Efficiency & Regulation Measurement (J205, J1205)| | | | |
|---|---|---|---|---|---|
|REGULATION|V02|VIM GND|J205|J205|VINI SENSE|
|Vout2|IGNDI|VQUTI GND|J205|J205|VOuTI_SENSE|
|REGULATIONVOUTI| | |VouTI GND| | |
|1 2 SENSE3 SENSE|IGNDI|Yoxd|VouTZ GND| | |
| | | |VouTI GND REGULATION R216|J205| |
|% 0 SENSE|J205|VOUIZ GND_REGULATIOM|10R|R218 J205|J205 R219 10R VOUIZ_REGULATIQN|
| | | | |10R| |

Module1 Efficiency Measurement (Vo1&Vo2)

|VIN2 GND|J1205|J1205|VINZ_SENSE|
|---|---|---|---|
|VOUI3_GND_SENSE|J1205|J1205|VouI3_SENSE|
|VouT?_GND_REGULATION R1204|J1205|J1205|R1205 VOuT3_REGULATION|
|Rpw|J1205|J1205|'88|

MEASUREMENT Efficiency

Module2 Efficiency Measurement (Vo3)

Note: The efficiency test point is Vout sense; The regulation test point is Vout regulation.

Rev. 01.17.22_#1.0 advancedenergy.com 8
---
# TEST SET UP

# Hardware Test Setup

The LGA110D can be connected with the E-load via the Vout and Return terminals, and communicates with LGA110D GUI by the I2C connector J204.

Example:

|LGA110D|LGA110D|VIN2_GND| | | |
|---|---|---|---|---|---|
| | |VO3Setting|VO3| |+|
| |-|E-load|-| | |
|DC Source| |Vout|-| | |
|+ Module2| | | |VO3|VO3_GND|
|VIN2| | | | | |
| |VIN1| | | | |
|+ Module1| | |VO2|VO2_GND| |
|-| | | |VO1|VO1_GND|

Enable Switch

VIN1_GND

Enable Jumper J204

|1|9|
|---|---|
|2|10|

LGA110D GUI

Adapter

Figure 2. Hardware Interface Setup

Rev. 01.17.22_#1.0 advancedenergy.com 9
---
# LGA110-EVAL-KIT

# TEST SET UP

Software Test Setup
The LGA110D has an evaluation software, LGA110D GUI, designed to make the unit accessible to the user. It is intended to
control and monitor the LGA110D units as they would be used in an application.

|Mini USB Cable| |I2C Cable| |
|---|---|---|---|
|Computer|Intersil Adapter|Evaluation Test Board|LGA110D|

Figure 3. Software Interface Setup

The LGA110D GUI must be installed on a PC before using of all of the functions of this program. Please refer to the Figure 4.

Navigator 5
View    Option   Utilities Help
Part Library =                            Power Map      Roll Scope  Sequencing                                Monitor View *  Fault Status
Part Library                               Power Map                                           100 %            Monitor
Generic                                                                                                     Rail 1
Digital, Integrated FET                   Source
Digital, POL Single Phase                                             1800V 159.7504
1SL63316                            Power Good
Digital, POL Dual Phase
Digital, Multichase 1st Gen
Digital, Module                                                                                              PMBus Enable
Digital; Power Monitor                                                                                      Immediate Off
Power Management IC                                                                                        Margin Nominal
Automotive                                                                                                  Output Voltage
1.800 V
Input Voltage
11.656 V
Output Current
199.750 A
Input Current
Messjec                                                                                 Nvm Tool X
SL68316-2

Figure 4. LGA110D GUI (Power Navigator)

Rev. 01.17.22_#1.0                                                     advancedenergy.com     10
---
# TEST SET UP

|Programming Sequence|Stan|
|---|---|
|Connect HW and start GUI|Wait for GUI to detect all converters|
|Configure power architecture using the GUI|Wait for GUI to refresh the architecture display|
|Configure converter module(s)| |
|Recycle input power and restart GUI| |
|Enable some or all converter module(s) as per document|Need to change module settings|
|Monitor working behavior of converter module(s)|Need to change power architecture|
|If settings are configured, need to restore to factory defaults|Need to restore to factory defaults|
|End| |

Figure 5. Programming Sequence

Rev. 01.17.22_#1.0 advancedenergy.com 11
---
# TEST SET UP

Test Setup Example

The setup example is shown in figure 5. It contains the input cord, LGA110D, evaluation test board, intersil adapter and computer.

The adapter is required to connect the unit to the computer.

Figure 6. Setup Example

Rev. 01.17.22_#1.0 advancedenergy.com 12
---
# OPERATION

Power Up/Down Sequence

1. Please make sure the OUTPUT ENABLE toggle switch (S201) is disabled.
2. Connect the input and output cables to the bus-bars.
- Vin1 and Vin2 connect to the main DC source
- Vo1, Vo2 and Vo3 connect to the E-load
- Add SYNC jumper to J1206 (SYNC1 to SYNC2)
- Add Enable jumper to short EN1, EN2, EN3 and Switch-EN on J203. If only Vo1 and Vo2 are needed, then jumper is only needed to put at EN1, EN2 and Switch-EN.

Rev. 01.17.22_#1.0 advancedenergy.com 13
---
# LGA110-EVAL-KIT

OPERATION

Power Up/Down Sequence Con’t

1. If I2C communication is needed, connect I2C dongle to I2C connector (J204 or J206).
2. Select the suitable voltage for Vo1, Vo2 and Vo3 by switches (S601, S602, S603 & S604). Default setting is Pin2 on and the Vout=1V. Use the PMBus command to change the Vout setting.

| |ON|DIP|8|5604 (5160)|56|
|---|---|---|---|---|---|
| |3|g|43823|Vout setting 38333;|SETTING2 =|
| |8|2 3| |DIP| |
| |ON|DIP|ON| | |
| |3| |2 3| | |

Power up sequence.
- a. Apply main voltage to Vin1 and Vin2. Vin1 is for module1 (Vo1 & Vo2), Vin2 is for module2 (Vo3).
- b. Toggle Enable switch (S201) to enable LGA110D Vout.

Power down sequence.
- a. Toggle Enable switch to disable LGA110D Vout.
- b. Turn off main voltage to Vin1 and Vin2.

Warning: Not follow power up/down sequence may damage the demo board.

Rev. 01.17.22_#1.0 advancedenergy.com 14
---
# LGA110-EVAL-KIT

# OPERATION

Additional information:

1. EN1, EN2 and EN3 can control Vo1, Vo2 and Vo3 individually.
2. This demo board is designed to have two LGA110D modules which can be tested efficiency independently. If the user wants to use only one module, need to follow below steps to measure the efficiency.

For module1 (2phase 2output) efficiency measurement:

1. Please make sure the OUTPUT ENABLE toggle switch (S201) is disabled.

Hardware change:

|a. Separate the input|b. Remove the SYNC jumper on J1206|
|---|---|
|c. Remove the bias resistor R201|d. Add 5V bias to the PINL207 & PINL209|
|e. Remove module2 PMBus resistors R1201, R1202, R1203| |

Rev. 01.17.22_#1.0 advancedenergy.com 15
---
# LGA110-EVAL-KIT

OPERATION

1. Configuration file changed to ‘1+1’ by GUI.
2. Power up sequence.
1. Apply 5V bias voltage.
2. Apply main voltage to Vin1.
3. Toggle Enable switch (S201) to enable LGA110D Vout.
3. Power down sequence
1. Toggle Enable switch to disable LGA110D Vout.
2. Turn off main voltage to Vin1.
3. Turn off bias 5V voltage.

Warning: Not follow power up/down sequence may damage the demo board.

For module2 (2phase 1output) efficiency measurement:

1. Please make sure the OUTPUT ENABLE toggle switch (S201) is disabled.

Rev. 01.17.22_#1.0     advancedenergy.com  16
---
# LGA110-EVAL-KIT

# OPERATION

2. Hardware change:

a. Separate the inputb. Remove the SYNC jumper on J1206c. Remove the bias resistor R201d. Add 5V bias to the PINL207 & PINL209e. Remove module1 PMBus resistors R1211, R1212, R1213

3. Configuration file changed to ‘2’ by GUI.

4. Power up sequence:

a. Apply 5V bias voltage.b. Apply main voltage to Vin2.c. Toggle Enable switch (S201) to enable LGA110D Vout.

5. Power down sequence:

a. Toggle Enable switch to disable LGA110D Vout.b. Turn off main voltage to Vin2.c. Turn off bias 5V voltage.

Warning: Not follow power up/down sequence may damage the demo board.

Rev. 01.17.22_#1.0     advancedenergy.com  17
---
|Part Number|Description|
|---|---|
|LGA110D-01DADJJ|Dual O/P Non-isolated 110 A Digital DC/DC Converter|
---
| | |LGA110-EVAL-KIT|
|---|---|---|
|Schematic| | |
|33| | |
| |Cc Lold| |
| |Rev. 01.17.22_#1.0|advancedenergy.com 19|
---
|LGA110-EVAL-KIT|LGA110-EVAL-KIT| |
|---|---|
|Schematic| |
|Rev. 01.17.22_#1.0|advancedenergy.com 20|
---
# LGA110-EVAL-KIT

|Silkscreen|V8u582806|vo8yeacs|voutipuosBUSBI|
|---|---|---|---|
|VCUI)|VoJZ|VOJi|5601|
| | | |VCUn?|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
|36|F4|DJ|544"|
|Jior| | |VCUTI|
|L|CI?|CizC|cMM|
|CIO| | |Ci2o|
| | | |Cio7|
|7s6| | | |
|EJa|#| |DYNAMIC LOAD|
|TLaSO| | | |
|8 282|933333SETTINJ5603|03|Mila|
|E4| |0J|83|
|P/n:SC8-024199 -000?| | | |
| | | |T|
| | |J2i0|Jzu|
| | |Ji2Io| |
|Efficrenent| | | |
|BUS340]|BUSB100| |3USB[02|
| | | | |
|Rev. 01.17.22_#1.0| | |advancedenergy.com 21|
---
# LGA110-EVAL-KIT

# PCB LAYOUT

Top Copper

Rev. 01.17.22_#1.0    advancedenergy.com  22
---
# LGA110-EVAL-KIT

# PCB LAYOUT

|Layer|2 Copper|
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
---
# LGA110-EVAL-KIT

# PCB LAYOUT

Layer3 Copper

Rev. 01.17.22_#1.0    advancedenergy.com  24
---
|LGA110-EVAL-KIT|LGA110-EVAL-KIT| |
|---|---|
|PCB LAYOUT| |
|Layer4 Copper|10|
|Rev. 01.17.22_#1.0|advancedenergy.com 25|
---
# LGA110-EVAL-KIT

# PCB LAYOUT

|Layer|5 Copper| | |
|---|---|---|---|
|Rev.|01.17.22_#1.0|advancedenergy.com|26|
---
# LGA110-EVAL-KIT

# PCB LAYOUT

|Layer|6 Copper| | |
|---|---|---|---|
|Rev.|01.17.22_#1.0|advancedenergy.com|27|
---
|LGA110-EVAL-KIT|LGA110-EVAL-KIT| |
|---|---|
|PCB LAYOUT| |
|Layer7 Copper| |
|Rev. 01.17.22_#1.0|advancedenergy.com 28|
---
# LGA110-EVAL-KIT

# PCB LAYOUT

Bottom Copper

Rev. 01.17.22_#1.0    advancedenergy.com  29
---
# LGA110-EVAL-KIT

|Issue|Date|Description|Originators|
|---|---|---|---|
|1.0|01.17.2022|First Issue|J. Ma|
---
# LGA110-EVAL-KIT

ABOUT ADVANCED ENERGY

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

Contact Information:

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, and AE® are U.S. trademarks of Advanced Energy Industries, Inc.

LGA110-EVAL-KIT - Rev.01.17.22_#1.0