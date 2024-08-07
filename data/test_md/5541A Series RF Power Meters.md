# GEMINI 5541A RF POWER METER

Operation Manual

rev AB

Manual Part Number: 5541A-900, Rev. AB

Published November 2023, Geneva, OH

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# NOTICES

Copyright Notice

© Copyright 2023 Advanced Energy Industries, Inc. All rights reserved. No part of this manual may be reproduced in any form or by any means (including electronic storage and retrieval or translation into a foreign language) without prior agreement and written consent from TEGAM, Inc. as governed by United States and international copyright laws.

Trademark Acknowledgments

This Manual

|Part Number:|5541A-900|
|---|---|
|Revision:|AB, November 2023|
|Supersedes:|AA|
|Published by:|TEGAM, Inc.|
| |10 TEGAM Way|
| |Geneva, OH 44041|
| |United States|

Disclaimer and Manual Revisions:

THE MATERIAL CONTAINED IN THIS USER MANUAL, AND ANY COMPUTER SOFTWARE ASSOCIATED WITH THIS USER MANUAL OR THE PRODUCTS COVERED BY IT, ARE PROVIDED AS IS, AND ARE SUBJECT TO CHANGE, WITHOUT NOTICE, IN FUTURE REVISIONS.

This User Manual was current at the time of publication. However, TEGAM is dedicated to a process of continual product improvement, and the products covered by this User Manual, and any associated computer software, are subject to periodic functional and design updates. Please visit tegam.com for the most current product documentation.

U.S. Government Rights

This computer software and/or technical data is TEGAM proprietary information developed exclusively at private expense. Computer software and technical data rights granted to the federal government include only those rights customarily provided to the public, pursuant to FAR 12.211 (Technical data) and FAR 12.212 (Computer software) for the federal government, and DFARS 252.227-7015 (Technical data – Commercial items) and DFARS 227-7202-3 (Rights in commercial computer software or commercial computer software documentation) for the Department of Defense. Except as explicitly permitted by the foregoing, reproduction for non-governmental use of the information or illustrations contained in this computer software and technical data is not permitted.

Compliance

- EN 61326-1:2013
- CE, (2014/30/EU)
- RoHS 3 Directive, 2015/863/EU Compliant
- REACH

Safety Notice Symbols and Terms

Safety Notices denote hazards. They indicate an operating procedure, instruction, or practice that, if not correctly performed or followed, could result in damage to equipment, or injury or death to personnel. Do not proceed beyond a Safety Notice until all conditions and instructions are fully understood and complied with.

Safety Notices Symbols:

- WARNING denotes an imminent hazard that could result in injury to personnel or death.
- CAUTION denotes a hazard that could result in damage to the unit or other equipment.
- REMINDER denotes important information about instrument functions, menus, and measurements.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Table of Contents

|1. Instrument Description|1-1|
|---|---|
|Specifications|1-1|
|2. Preparation for Use|2-3|
|General Information|2-3|
|Feature Overview|2-4|
|Safety Notices and Information|2-5|
|Unpacking and Inspection|2-7|
|Included With the GEMINI RF Power Meter|2-7|
|Model Number Configuration|2-7|
|3. Theory of Operations|3-1|
|Traceability|3-1|
|Measurement Theory|3-1|
|VSWR Calculation|3-1|
|Maximum Rated Power|3-1|
|4. Operating Instructions|4-2|
|Warm-Up Time|4-2|
|Instrument Overview|4-2|
|Instrument Power and Communication|4-3|
|Digital Display|4-3|
|Ports and Connectors|4-3|
|5. Connecting to the 5541A|5-5|
|IP Address|5-5|
|Connection using Custom Software|5-5|
|6. GEMINI Tools™ Application|6-6|
|Installation|6-6|
|Configuration Options|6-7|
|Operation|6-7|
|Measurement Data Files|6-7|
|Demo Mode|6-8|
|Snapshot|6-8|
|7. Programming Command Reference|7-9|
|Syntax|7-9|
|8. Service Information|8-1|
|Inspection and Cleaning|8-1|
|Functional Verification|8-1|
|Troubleshooting|8-2|
|Preparation for Calibration or Repair Service|8-2|
|Expedite Repair & Calibration Form|8-4|
|Warranty|8-5|
|Warranty Limitations|8-5|
|Statement of Calibration|8-5|

A. Calibration Options

B. Expanded Instrument Uncertainties

C. Power and Frequency Limits

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Preparation for Use

# 1. INSTRUMENT DESCRIPTION

|Specifications| |
|---|---|
|GENERAL SPECIFICATIONS:| |
|Measurement Ranges| |
|Frequency (MHz)|0.2 to 200|
|Forward Power (W)|3 to 5,000 (Connector dependent)|
|Reverse Power (W)|3 to 250|
|Basic Power Accuracy|± (0.5% of Rdg + 0.5 W) at the calibrated frequencies (2σ, approx. 95% confidence)|
|Measurements|Forward Power, Reverse Power, VSWR, and Frequency|
|Impedance|50 Ω|
|Directivity|>= 28 dB (Typical)|
|VSWR|Better than 1.05 : 1 below 60 MHz|
|Insertion Loss|< 0.05 dB with QC Type N connectors|
|Connector Type|Specified by customer at time of purchase. Available connectors: N, HN, LC, 7/16 DIN, 7/8 EIA, and QDS-UL|
|Display|6-Digit Auto-Resolution OLED Display|
|Display Resolution|Up to 6 digits (2 digits past decimal point)|
|Power / Data Connector|IEEE 802.3af PoE (Power over Ethernet)|
|Compliance|CE (2014/30/EU) / RoHS (2015/863/EU) / REACH IEC 61326-1 / 61326-2|
|Operating Temperature|+18 to +28 °C (+64.4 to +82.4 °F)|
|Storage Temperature|-40 to +71 °C (-40.0 to +159.8 °F)|
|Warranty|1-year Parts & Workmanship|
|Recommended Calibration Interval|12 months|
|Approximate Dimensions (W x H x D, including Type N connectors)|132 x 92 x 64 mm (5.2 x 3.6 x 2.5 in)|
|Weight|1103 g (2.44 lbs)|

1 Maximum power is limited by the measurement frequency and instrument connector types. See Appendix C for power and frequency limits.

2 Specifications valid only when used with the connectors in-place at time of calibration. Removal or changing of connectors will void calibration data.

3 See Appendix B for expanded measurement uncertainty data.

4 For reference use only.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
|PRODUCT|MODEL|DESCRIPTION|
|---|---|---|
|Calibration PNs|5541A-CAL-xxxx|See Appendix A|
|Connector Configurations|See Appendix C for connector limits and configurations| |
|Transport Case|1500-910|Transport Case|
|Ethernet Cable|XX-37|IEEE 802.3af PoE (Power over Ethernet) Cable|
|Quick Start Guide|5541A-901|GEMINI 5541A GEMINI RF Power Meter Quick Start Guide|
|Printed Manual|5541A-900|GEMINI 5541A Operation Manual|
|Service Options|See Appendix A|17025 Accredited Calibration with Data|

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Preparation for Use

# 2. PREPARATION FOR USE

General Information

This manual provides operating instructions and maintenance information for the GEMINI 5541A RF Power Meter.

This instrument is a high-performance directional RF power meter capable of measuring up to 5000 W at frequencies from 200 kHz to 200 MHz. Its 2σ accuracy of ±(0.5% of rdg + 0.5 W) provides repeatable and reliable measurement results across many applications.

The meter is self-contained, bringing the sensor, display, communication port, and measurement circuits together into a single instrument with a compact footprint.

Other features such as fast response times, data collection software available at the TEGAM website, and straightforward programming protocols for customized applications, propel the GEMINI RF Power Meter into a class of its own. Whether in the semiconductor, communication, or medical industries, the GEMINI RF Power Meter will meet your demands with a bit of room to spare.

This manual describes the GEMINI RF Power Meter, important safety precautions, meter operation, and programming. It is recommended that you read this manual thoroughly, especially the sections on safety, prior to operating these instruments.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Preparation for Use

# Feature Overview

1. Designed for convenience and versatility in a compact arrangement that includes the sensor, display, and all measurement circuits, all in the space of a typical sensor in multi-instrument power meter systems.

2. Connect the sensor and start making measurements – no settings to manage, and automated data collection software makes recording simple.

3. Reliable and repeatable measurements across a range of frequency and power bands. The GEMINI RF Power Meter can be calibrated at key industry frequencies and power levels. (See Appendix C for more information.) When measurement requirements change, simply select a different calibration option.

4. Ethernet connection via the on-board IEEE 802.3af PoE port makes integration with custom applications painless.

5. The GEMINI Tools™ RF Power Meter Application is available for download to all GEMINI RF Power Meter users. This easy-to-use application automatically connects to up to five (5) GEMINI RF Power Meters and begins collecting measurements at the click of a button.

6. Lower cost of ownership over the lifetime of the instrument, even as your measurement needs change. By implementing a single sensor that can measure multiple frequency bands, and with a recommended calibration interval of one (1) year, the GEMINI RF Power Meter saves money and time.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Preparation for Use

Safety Notices and Information

Read this Operation Manual thoroughly before using the instrument to become familiar with its operations and capabilities.

Visually inspect instrument before using. Do not use if unit or any connector appears damaged, or with any part of the case removed.

WARNING

MAINTENANCE INSTRUCTIONS WITHIN THIS MANUAL ARE FOR USE BY QUALIFIED SERVICE PERSONNEL ONLY. DO NOT ATTEMPT TO SERVICE THIS UNIT UNLESS YOU ARE QUALIFIED TO DO SO.

High voltage, current, and RF power are present in the system during use. This instrument and related equipment should be operated only by qualified personnel sufficiently trained in the safe operation of high voltage, current, and RF power systems. Failure to follow these precautions may result in death or bodily injury, or equipment damage.

Install proper safety equipment such as fuses, breakers, and interlock devices as necessary whenever working with high-power RF sources, loads, filters, and meters. Failure to follow these precautions may result in death or bodily injury, or equipment damage.

Never apply RF power to an unterminated power meter, transmission lines, or other feedthrough equipment such as filters. Before applying RF power to the measurement system, ensure the power path terminates into an appropriately rated RF load. Do not disconnect transmission lines or the GEMINI RF Power Meter while RF power is active in the system. Failure to follow these precautions may result in death or bodily injury, or equipment damage.

Never apply RF power at levels greater than the rated maximum power of the instrument. Rated power is dependent upon not only the instrument, but connectors, transmission lines, and other equipment in the measurement system. Ensure all system components are rated appropriately for the expected RF power levels.

Always follow generally accepted safe maintenance practices.

All personnel working in and around RF power should be trained in the administration of basic first aid and resuscitation.

The GEMINI RF Power Meter should be serviced by qualified personal only. Never attempt to open the instrument casing, disconnect transmission lines, or otherwise service the meter while RF power is applied to the system.

2-5

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
Preparation for Use

CAUTION

RISK OF INCORRECT READING

Always use a load rated appropriately for the applied RF power and frequency. The GEMINI RF Power Meter requires a load with VSWR better than 2.0:1 to perform within published specifications. Failure to follow these precautions could result in incorrect readings from the equipment.

Always apply the source RF power to the instrument INPUT. Incorrect readings may occur if RF power is applied to the output port of the instrument.

2-6

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Preparation for Use

# Unpacking and Inspection

Each instrument is electrically and mechanically inspected before shipment. Upon receiving your new TEGAM RF Power Meter, unpack all items from the shipping container and inspect the items for any obvious damage that may have occurred during transit. Notify TEGAM immediately if damage, dents, or other irregularities are found. Use the original packing materials if reshipment is necessary.

# Included With the GEMINI RF Power Meter

Each GEMINI 5541A RF Power Meter is shipped with:

GEMINI 5541A RF Power Meter, with input and output connectors as specified by customer at time of purchaseXX-37, Ethernet Cable1500-910, Transport Case5541A-901, GEMINI 5541A RF Power Meter Quick Start GuideCalibration Certificate and Documentation

# Model Number Configuration

Each GEMINI RF Power Meter is configurable with various connector combinations to meet measurement system requirements. A part number identifying the base model of the instrument and its connector configuration is found on the calibration label and calibration certificate.

The part number takes the form of [BASE MODEL]-[INPUT CONNECTOR TYPE][input connector gender]-[OUTPUT CONNECTOR TYPE][output connector gender]. For instance, a model 5541A with Type N female connectors on both the input and output ports will be numbered 5541A-Nf-Nf.

Note: Changing the connector configuration in place at the time of calibration will invalidate the calibration data and certification and may impact maximum rated input power. If different connector types or genders are required, contact TEGAM for connector replacement and recalibration in the new configuration.

2-7

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

# 3. THEORY OF OPERATIONS

Traceability

The GEMINI RF Power Meter is traceable to the International System of Units (SI) through the National Institute of Standards and Technology (NIST) or other recognized National Metrology Institutes. This is accomplished through comparison to TEGAM’s high-power RF calorimetric system maintained in TEGAM’s laboratories, itself traceable to the SI.

Measurement Theory

The GEMINI RF Power Meter is based on custom-designed directional power sensors coupled to a high-frequency, high-power transmission line internal to the instrument. Forward and reverse couplers react to the power flowing in the corresponding direction in the transmission line. This measurement data is used to calculate forward and reverse power. A third coupler is used to determine the frequency.

VSWR Calculation

VSWR is calculated from the forward and reverse power measurements. It should only be used for reference. As power is proportional to the voltage squared, VSWR can be derived from these power measurements with the following formula:

Where either the forward or reverse power readings are outside the dynamic range of the instrument, the display will indicate INVALID for VSWR.

Maximum Rated Power

The GEMINI RF Power Meter maximum rated power is frequency and connector dependent. See Appendix C for typical power limits of various connector configurations. For specific power levels and calibration frequency points, see the Certificate of Calibration for the particular GEMINI RF Power Meter.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●tegamsales@aei.com
---
# Operating Instructions

# 4. OPERATING INSTRUCTIONS

Warm-Up Time

If the GEMINI RF Power Meter has recently been exposed to ambient temperatures beyond its specified operating temperature of 18 to 28 °C, allow the instrument to acclimate in the laboratory environment for at least 24 hours prior to use.

Once properly acclimated to the laboratory environment and powered on, the GEMINI RF Power Meter requires at least 10 minutes to stabilize.

Instrument Overview

|Component|Description|
|---|---|
|OLED Display|Realtime display of measurements and reference calculations (See Section 4.4 for more information).|
|POE Connection (On side of unit)|Connection for IEEE 802.3af PoE (Power over Ethernet)|
|RF INPUT (On side of unit)|Input connector for RF Signal under test.|
|RF OUTPUT (On side of unit)|Output connector for RF Signal under test.|

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

Instrument Power and Communication

Input power is applied via the IEEE 802.3af PoE port on the side of the instrument. This port also serves as the communication port for remote monitoring and data collection.

The GEMINI RF Power Meter can be powered from any IEEE 802.3af PoE power source.

Manual Operation

Connect the GEMINI RF Power Meter to any IEEE 802.3af PoE source.

Communication and Data Collection

To remotely monitor the GEMINI RF Power Meter and perform automated data collection operations, the instrument must be connected via the IEEE 802.3af PoE interface.

|Digital Display|Incident Power|
|---|---|
|FWD PWR: 100.90 W|Reflected Power|
|REV PWR: 0.04 W| |
|VSWR 01|VSWR (Reference)|
|FREQ 13.56 MHz|Frequency (Reference)|

Overview

The GEMINI RF Power Meter digital direct-reading display provides forward and reverse power measurements, VSWR, and frequency. These readings are indicated on the display by the designators FWD PWR, REV PWR, VSWR, and FREQ respectively. Units of measurement are displayed on the right side of the display. The displayed measurement data is updated three (3) times per second.

Note: For traceable frequency measurements, use appropriate instruments.

Measurement Range Limitations

Display parameters will indicate INVALID when a measurement result is beyond the usable power or frequency range of the instrument. Similarly, if any measurement required to calculate a displayed result is not within the instrument range, INVALID will be displayed for that result.

For instance, a valid VSWR result requires that both Forward and Reverse Power readings be within the instrument’s usable power measurement range. If either reading is outside that range, VSWR will indicate INVALID.

Ports and Connectors

Input and Output Ports

Before connecting your GEMINI RF Power Meter to any RF power source, identify the INPUT and OUTPUT ports. The INPUT port and power flow direction are designated by the symbol on the instrument housing.

4-3

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

The GEMINI RF Power Meter may be calibrated to either the INPUT or OUTPUT port. However, the RF power source must always be connected to the INPUT port regardless of which port is calibrated. Refer to the Certificate of Calibration for port calibration information.

WARNING: Never apply RF power to an unterminated power meter, transmission line, or other feedthrough equipment such as filters. Before applying RF power to the measurement system, ensure the power path terminates into an appropriately rated RF load. Do not disconnect transmission lines or the GEMINI RF Power Meter while RF power is active in the system. Failure to follow these precautions may result in death or bodily injury, or equipment damage.

# Connection to Measurement System

Connect the GEMINI RF Power Meter OUTPUT port to an appropriate load using torque techniques appropriate for the connector type. Next, connect the instrument INPUT port to the RF power source, again following proper connection and torque techniques for the connector types being used.

# Adapters

Adapters may be used when necessary for compatibility with the measurement system. However, adapters can limit the maximum rated power of the measurement system and measurement uncertainty. Verify that any adapters used in the system are appropriate for the RF source power and frequency. See the adapter manufacturer’s technical specifications for further information.

# Taking a Reading

Measurements are read directly from the digital display. After applying RF power, allow sufficient time for the displayed measurements to stabilize before taking a reading.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●
tegamsales@aei.com
---
# Operating Instructions

5. CONNECTING TO THE 5541A

The 5541A connects via an IEEE 802.3af PoE (Power over Ethernet) connection. Once it is connected to the same network as the host computer and powered on, it is recognized automatically by TEGAM Gemini Tools. Contact TEGAM for the latest version of Gemini Tools.

IP Address

If a DHCP server is active on the network, the 5541A is assigned a dynamic IP by the DHCP server. If there is no DHCP server in the network, the unit temporarily switches to 192.168.100.100 until the next power cycle.

Connection using Custom Software

The current IP address of any recognized 5541A on the network can be found in TEGAM Gemini Tools (See Figure 1).

|Configuration|Available Meters|
|---|---|
|192.168.10.76|5541|

Figure 1: 5541A IP Address in Gemini Tools

Using the IP address, a connection to the device can be opened using port 1002. Once the connection is established, the syntax in Section 7.1 can be used to issue commands to the device manually or via software.

5-5

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

6. GEMINI TOOLS™ APPLICATION

The TEGAM GEMINI Tools™ RF Power Meter Application allows for data collection from any GEMINI RF Power Meter. Measurement data is automatically saved in delimited text file format. It provides real-time data visualization on the connected PC and saves the displayed data to a data file for additional analysis or future reference.

# Installation

Download the application at www.tegam.com/geminitools. GEMINITools.msi file and follow the onscreen prompts.

GEMINI RF Power Meter and 'Log Toola Contumbon

Figure 2: GEMINI Tools power meter application main window

To install, launch the GEMINI Tools application.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

# Configuration Options

Users can configure certain application parameters to meet their requirements. To access these parameters, click Tools -&gt; Configuration. In the Configuration Parameters window, choose a Data File Directory, Sample Interval Default in seconds, and assign a Data File Delimiter. Once each parameter is set as desired, click Save to enable the new parameter values.

| |Configuration Parameters|
|---|---|
|User Configuration| |
|Data File Directory|JSERPROFILE" DccumentsITEGAMIGEMINI Toolsi|
|Sample Interval Default (s)| |
|Data File Delimiter|Comma|

Figure 3: Configuration Parameters window

The default Data File Delimiter is set to the comma (,) character. For computer systems whose localization settings assign the period (.) as the numeric decimal separator, file import tasks will operate as expected using the comma delimiter. However, on computer systems whose localization settings use a comma character as the decimal separator, import tasks may fail or cause corruption of the imported data. Users in locales that use a comma as the numeric decimal separator should consider selecting the tab or semicolon (;) delimiter options to prevent these import errors.

# Operation

The application automatically detects GEMINI RF Power Meters connected to the local network. Once found, the IP Address, Model, and Serial Number are displayed in the Available Meters group.

Select the desired unit (multiple units can be selected by holding the CTRL key) in the Available Meters group, set a sample interval between 1 and 3600 seconds, then click START Data Acquisition to begin collecting data. Real-time charts will display live readings from the instrument.

Click Zoom to display a new chart window in which the mouse can be used to zoom in on data points of interest. Click and drag to create a square around the data. Release the mouse button and the window will zoom to the selected data.

# Measurement Data Files

The measurement data files can be found by clicking the Open Data Directory button. By default, measurement data files are found in %USERPROFILE%\Documents\TEGAM\GEMINI Tools\Data, or in the directory path defined in the Configuration Parameters.

Program log files are in %USERPROFILE%\Documents\TEGAM\GEMINI Tools\Log.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

Demo Mode

The GEMINI Tools power meter application includes a Demo mode which can be used to test
the application when no meter is available. Click Tools -&gt; Demo Mode to load the simulated
GEMINI RF Power Meters, then follow the instructions above. All application features are
available in Demo mode.

NOTE: Do not use demo mode for production data collection.

Snapshot

The Snapshot feature is used for diagnostic purposes only. It provides a data set of values
related to the current state of the instrument and the active measurement. For troubleshooting
or questions about particular measurement results, use the Snapshot feature and forward the
*.csv file to TEGAM.

To take a Snapshot:

1. Click STOP Data Acquisition to end any active data collection sessions. Do not
alter the test setup, and do not turn off the RF power source.
2. Click Snapshot.
3. In the Snapshot Parameters window, enter the expected Power (in Watts) and
Frequency (in Hz) readings.
4. Click Take Snapshot.
5. Navigate to %USERPROFILE%\Documents\TEGAM\GEMINI Tools\Snapshot\ to find
the Snapshot data file. The filename will be in the format
[TIMESTAMP]_5541_[SERIAL NUMBER].
6. Forward the appropriate Snapshot file to TEGAM, along with a detailed description
of the issue and expected results, for analysis and assistance.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●
tegamsales@aei.com
---
# Operating Instructions

# 7. PROGRAMMING COMMAND REFERENCE

Users may also develop custom applications purpose-built for their own applications. The instrument syntax and commands are discussed below.

# Syntax

The GEMINI RF Power Meter command set is straightforward and will be familiar to those who have worked with other serial instruments. It uses the GET &lt;Variable Name&gt; command format. Variable Names are described in Table 1 below.

|VARIABLE NAME|RETURN STRINGS|
|---|---|
|MODEL_NUMBER|&lt;error&gt;:&lt;unit model number&gt;|
|SERIAL_NUMBER|&lt;error&gt;:&lt;unit serial number&gt;|
|VERSION|&lt;error&gt;:&lt;firmware revision number&gt;|
|READINGS|&lt;error&gt;:FORWARD_POWER, REVERSE_POWER, VSWR, FREQUENCY|
|FORWARD_POWER|&lt;error&gt;:&lt;forward power in Watts&gt;|
|REVERSE_POWER|&lt;error&gt;:&lt;reverse power in Watts&gt;|
|VSWR|&lt;error&gt;:&lt;connection VSWR&gt;|
|FREQUENCY|&lt;error&gt;:&lt;source frequency in Hz&gt;|

Table 1: GEMINI RF Power Meter Variable Names and Return Strings

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Operating Instructions

Each GET command will result in a response. The response will be in the format &lt;error code&gt;:&lt;command response&gt;. Error responses are described in Table 2 below.

|ERROR CODE|DESCRIPTION|
|---|---|
|00|No error|
|01|Invalid command|
|02|Invalid value|
|03|Unit not in calibration mode|
|04|Invalid mode for command|
|05|Command not available on this unit|
|06|Invalid calibration file for serial number|
|07|No frequency detected - readings are invalid|

Error Code 07 will always be generated when no power is applied to the instrument.

Table 2: GEMINI RF Power Meter error response codes

# 7.1.1 Timing

The GEMINI RF Power Meter has no triggers or reading clock and cannot deliver precisely timed readings. GET, when applied to instrument readings, does not trigger a new reading. Instead, the instrument immediately transmits the last-available values. The GEMINI RF Power Meter always free-runs and produces approximately three readings per second on the display. Effectively, GET transmits the displayed value.

# 7.1.2 Note for Users of LabVIEW™ Software

The GEMINI RF Power Meter requires a terminating character at the end of any command string. When using LabVIEW software to develop a custom program, the write buffer constant must be modified to include a \n at the end of the command string. Figure 4 illustrates this requirement.

Figure 4: Sample VI for LabVIEW software, showing the GET FORWARD POWER command string.

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Service Information

# 8. SERVICE INFORMATION

Inspection and Cleaning

To extend the life of the instrument, inspect and clean the instrument regularly. Inspect the instrument for any significant abrasions, cuts, cracks, dents, or other signs of damage on the case, connectors, and display lens. Inspect the connectors for breaks, dirt, or corrosion. Ensure all screws are securely fastened.

With all screws securely fastened and the instrument disconnected from input power and any RF source, use a damp cloth or towel to wipe down the instrument. Use care to avoid scratching the display lens. Mild, non-abrasive detergents may be used providing the instrument is then wiped down with a clean damp cloth or towel.

Functional Verification

The Gemini 5500 Series are tested and inspected meticulously before shipment.

The following functional verification process is provided to verify the unit is operating properly, such as after shipment or accidental mishandling. For statements of accuracy, refer to the calibration certificate that was provided with your 5541A.

1. Attach unit INPUT to known signal source, such as a calibrated signal generator.
2. Attach unit OUTPUT to a calibrated 50Ω load.
3. Apply a power level and frequency within the range of the signal source and unit.
- See Certificate of Calibration for reference
4. Verify that the unit reads expected values.
5. If the unit does not behave as expected, contact TEGAM.

8-1

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
# Service Information

# Troubleshooting

TEGAM’s RF Power Meters are designed and built to provide years of uninterrupted use. In the event the instrument malfunctions or does not perform as expected, helpful troubleshooting tips are provided below. Figure 5 below lists some of the more common issues and their resolutions.

|Symptom|Description|Resolution|
|---|---|---|
|Harmonics will register power| |Filter harmonics or use a cleaner source|
|Unexpected or Erroneous Measurement|Frequency outside of calibrated range|Check certificate and ensure unit is being operated within calibrated frequency range|
| |Power level outside of calibrated range|Check certificate and ensure unit is being operated within calibrated frequency range|
|RF power not applied to 5541A input port| |Check cables, connections, and input source Check orientation of 5541A input and output ports|
|“Error Code 7” response from software|No frequency detected|Check that the signal source output is ON|

Figure 5: Common Troubleshooting Issues

# Preparation for Calibration or Repair Service

Once you have verified that the cause of the malfunction cannot be solved in the field and the need for repair and calibration service arises, contact TEGAM customer service to obtain an RMA (Returned Material Authorization) number. You can contact TEGAM customer service via the TEGAM website, www.tegam.com or by calling 440-466-6100 (All Locations) or 800-666-1010 (United States Only).

The RMA number is unique to your instrument and will help us identify your instrument and to address the particular service request by you which is assigned to that RMA number.

Of even greater importance, a detailed written description of the problem should be attached to the instrument. Many times, repair turnaround is unnecessarily delayed due to a lack of repair instructions or a detailed description of the problem.

This description should include information such as measurement range and other instrument settings at the time of the malfunction, type of components being tested, frequency of the

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
Service Information

symptoms (intermittent or continuous), conditions that may cause the symptoms, changes to
the test setup or operating environment that may affect the instrument, etc. Any detailed
information provided to our technicians will assist them in identifying and correcting the
problem in the quickest possible manner. Use a copy of the Repair and Calibration Service form
provided on the next page.

Once this information is prepared and sent with the instrument to our service department, we
will do our part to make sure that you receive the best possible customer service and
turnaround time possible.

8-3

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●
tegamsales@aei.com
---
# Service Information

Expedite Repair & Calibration Form

Use this form to provide additional repair information and service instructions. The completion
of this form and including it with your instrument will expedite the processing and repair
process.

|RMA#:|Instrument Model #:|
|---|---|
|Serial Number:|Company:|
|Technical Contact:|Phone Number:|
|Additional Contact Info:| |

Service Instructions:

- Evaluation
- Calibration Only
- Repair Only
- Repair & Calibration
- ISO 17025 Calibration with Data

Detailed Symptoms:

Include information such as measurement range, instrument settings, type of components
being tested, is the problem intermittent? When is the problem most frequent?, has anything
changed with the application since the last time the instrument was used?, etc.

8-4

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●

tegamsales@aei.com
---
# Service Information

# Warranty

TEGAM, Inc. warrants this product to be free from defects in material and workmanship for a period of one (1) year from the date of shipment. During this warranty period, if a product proves to be defective, TEGAM Inc., at its option, will either repair the defective product without charge for parts and labor, or exchange any product that proves to be defective.

TEGAM, Inc. warrants the calibration of this product for a period of one (1) year from date of shipment. During this period, TEGAM, Inc. will recalibrate any product, which does not conform to the published accuracy specifications.

In order to exercise this warranty, TEGAM, Inc., must be notified of the defective product before the expiration of the warranty period. The customer shall be responsible for packaging and shipping the product to the designated TEGAM service center with shipping charges prepaid. TEGAM Inc. shall pay for the return of the product to the customer if the shipment is to a location within the country in which the TEGAM service center is located. The customer shall be responsible for paying all shipping, duties, taxes, and additional costs if the product is transported to any other locations. Repaired products are warranted for the remaining balance of the original warranty, or 90 days, whichever is greater.

# Warranty Limitations

The TEGAM, Inc. warranty does not apply to defects resulting from unauthorized modification or misuse of the product or any part. This warranty does not apply to fuses, batteries, or damage to the instrument caused by battery leakage.

The foregoing warranty of TEGAM is in lieu of all other warranties, expressed or implied. TEGAM specifically disclaims any implied warranties of merchantability or fitness for a particular purpose. In no event will TEGAM be liable for special or consequential damages. Purchaser’s sole and exclusive remedy in the event any item fails to comply with the foregoing express warranty of TEGAM shall be to return the item to TEGAM; shipping charges prepaid and at the option of TEGAM obtain a replacement item or a refund of the purchase price.

# Statement of Calibration

This instrument has been inspected and tested in accordance with specifications published by TEGAM, Inc.

TEGAM, Inc. certifies the above listed instrument has been inspected and calibrated and meets or exceeds all published specifications and has been calibrated using standards whose accuracies are traceable to the International System of Units (SI) through the National Institute of Standards and Technology (NIST) or other recognized National Metrology Institutes.
---
|CALIBRATION|FREQUENCIES (MHZ)|POWER LEVELS (W)|
|---|---|---|
|5541A-CAL-0001|12.89, 13.56, 14.23|FWD 3-5000, REV 3-250|
|5541A-CAL-00025|2.0-30.0|5-250|
|5541A-CAL-0003|1.8, 2, 2.2|FWD 3-5000, REV 3-250|
|5541A-CAL-0004|57.0, 60.0, 63.0|FWD 3-5000, REV 3-250|
|5541A-CAL-0006|0.9, 1.0, 1.1|FWD 3-5000, REV 3-250|
|5541A-CAL-0007|25.764, 27.12, 28.476|FWD 3-5000, REV 3-250|
|5541A-CAL-0008|0.18, 0.20, 0.22|FWD 3-2500, REV 3-250|
|5541A-CAL-0009|0.38, 0.40, 0.42|FWD 3-5000, REV 3-250|

Accuracy derated to ± (3.0%rdg + 0.1W)

A-i

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
B. EXPANDED INSTRUMENT UNCERTAINTIES10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
|Freq (MHz)|Type|N|HN|IC|7/16" DIN|7/8" EIA|
|---|---|---|---|---|---|---|
|0.4| |9.74|10.00|10.00|10.00|10.00|
| | |9.74|10.00|10.00|10.00|10.00|
| | |9.74|10.00|10.00|10.00|10.00|
|13.56| |8.34|8.90|8.90|8.90|8.00|
|27.12| |5.87|6.19|6.19|6.19|6.19|
|40.68| |4.77|5.01|5.01|5.01|5.01|
|60| |3.92|4.09|4.09|4.09|4.09|
|200| |2.13|2.18|2.18|2.18|2.00|

Figure 6: Power Limitations by Connector Type (kW)

*Power limited by 5541A to 5kW

A-iii

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ● tegamsales@aei.com
---
TEGAM INC.

10 TEGAM WAY

GENEVA, OHIO 44041

CAGE Code: 49374

WEB: http://www.tegam.com

10 TEGAM WAY ● GENEVA, OHIO 44041 ● 440-466-6100 ● FAX 440-466-6110 ●

tegamsales@aei.com
---
