# LGA50D Evaluation Board User Manual

Artesyn Embedded Technologies

LGA50D JJ and JSBJ
Evaluation Board User Manual

LGA50D Evaluation Board

October 2018

Page 1 of 18
---
# TABLE OF CONTENTS

GENERAL

- EQUIPMENT REQUIRED
- DEFAULT SETTINGS

COMPONENT IDENTIFICATION

OPERATION

- POWER UP SEQUENCE
- ADDITIONAL INFORMATION
- TEST FUNCTIONS

APPENDIX A – SILK-SCREEN LAYER OF THE EVALUATION BOARD.

DOCUMENT REVISION HISTORY

CONTACT FOR TECHNICAL SUPPORT AND INFORMATION

AMERICAS

ASIA

EUROPE

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 2 of 18
---
# LGA50D Evaluation Board User Manual

GENERAL

The LGA50D evaluation board (LGA50D-EVAL-KIT-JSBJ, Revision AP) allows the user to test and investigate the performance of the LGA50D non-isolated module.

Within the kit there are the following items:

The evaluation board equipped with 2 LGA50D modulesThe Artesyn PMBus interface dongleThe PMBus to USB interface cables

Embedded POWER

DigItaL

DcDc

Fig. 1 – LGA50D evaluation kit

This equipment allows you monitor and control the modules via your computer, or you can apply settings to the modules by hardware configuration.

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 3 of 18
---
# Equipment required

To run the evaluation board, the following equipment will be required to supply power to the board, apply load to the board, and to cool the dc-dc converters if the board is to be operated for long periods.

| |Recommended Test Equipment|
|---|---|
|DC Source|7~15V, 40A or above|
|Load|40A or above for Vo1 or Vo2, 80A or above for Vo3|
|Cooling Fan|Please use fan cool if operate at full load for long time|

Power cables with M6 ring terminations are required for the input and output connections to and from the evaluation board.

Test equipment that will be required will be:

- A personal computer with the LGA50D GUI software installed on it
- The GUI software is available on the Artesyn website: https://www.artesyn.com/power/LGA50D-eval-GUI
- Please refer to the GUI user manual for instructions on how to install and use this software
- Oscilloscope and associated test probes
- Digital multi-meter and associated test probes

Artesyn Embedded Technologies - LGA50D Evaluation Board - October 2018 - Page 4 of 18
---
# Default settings

The evaluation board has been supplied with the following configuration and set-up by default.

If no changes are made to the hardware and firmware configuration of the unit then, the user will see that this board is equipped with 2 LGA50D modules with the following voltage settings:

|1 module is configured for a single output|Output voltage setting is 1.2V via the dip switches on the PCB|
|---|---|
|1 module is configured for 2 independent outputs|Output A voltage is set to 1.2V via the dip switches on the PCB|
| |Output B voltage is set to 1.2V via the dip switches on the PCB|

The PCB has been equipped with the following value of capacitors. These have been selected to provide optimum performance under as many different test conditions as possible, but the user may change or optimize the values according to the specific conditions that are to be replicated:

- Input capacitance (per module)
- - Recommended:
- 1x120uF/16V polymer caps (APXS160ARA121MH 70G or equivalent) + 4 x 22uF/16V ceramic cap

Output capacitance

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 5 of 18
---
# LGA50D Evaluation Board User Manual

# COMPONENT IDENTIFICATION

The key components and connection locations are shown in the picture of the evaluation board below.

Note that the LGA50D shown at the ‘top’ of this picture is the one that is configured as the single output unit, and the ‘bottom’ converter is configured as a dual output module.

| |Vout3 Regulation Measurement Point|Vout3 Ripple Measurement Point|
|---|---|---|
|Vin2 and Vout3 Efficiency Test Point|Vout3 setting|Vout3|
|Vin2|GND|GND|
|Vini|Vout2 Regulation Measurement Point|Vout1|
| |Vout2 Ripple Measurement Point| |
|Vini, Vout1, and Vout2 Efficiency Test Point|Enable switch|I2C connector|
| |Vout2 setting|Vout1 setting|
| |Vout1 Regulation Measurement Point| |

Fig. 2 – LGA50D setup

Assumption: The user has made the power connections to and from the evaluation card. These will not be described further.

Artesyn Embedded Technologies

Page 6 of 18

LGA50D Evaluation Board

October 2018
---
# OPERATION

Here are the instructions to power up the PCB and modules.

# Power up sequence

To power up and configure the evaluation card, please follow the steps as described below.

1. # Initial set position of the enable switch

Please make sure the OUTPUT ENABLE toggle switch (S201) is in the “disable” orientation as shown below with the toggle of the switch leaning toward the modules and the output side of the PCB (and away from the input side of the board).

Fig. 3 – Initial enable switch orientation

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 7 of 18
---
# Connection and configuration

Connect the input and output cables to the M6 terminations of the PCB.

Then connect the following:

1. Connect the Vin1 and Vin2 connections to the DC power source with a voltage setting in the range of 7.5Vdc to 14Vdc
2. Connect the Vo1, Vo2 and Vo3 connections to your E-load
3. Add the enable jumpers to the En1, EN2 and EN3 locations on J203 – this will ensure that the 3 outputs will be enabled. Note these are the jumper components located next to the enable switch – they are shown below.

Fig. 4 – Enable jumper location and population
Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 8 of 18
---
# LGA50D Evaluation Board User Manual

3. Connection of the I2C dongle to IC connector2

This is the interconnect cable between your PMBus dongle and the evaluation PCB. It is polarized and will only fit into the connected in 1 orientation.

The other end of this cable should be plugged into your dongle. The dongle also has USB connections (and the cable is provided) to connect your dongle to the USB port of your computer.

4. Voltage setting

Select the suitable voltage for Vo1, Vo2, and Vo3 by the voltage selector DIP switches Vo setting. The silk screen marking shows the voltage settings that can be achieved by these switches.

|Vout2 setting|Vout1 setting|
|---|---|
| |Fig. 6 – Nominal output voltage settings by DIP switch setting|

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 9 of 18
---
# Power up sequence

To enable the DC-DC converters to work now that all connections to and from the evaluation board have been applied, take the following steps:

1. Apply the input voltage to Vin1 and Vin2
2. Operate the toggle enable switch (S201) so that the toggle is leaning toward the input connections and away from the output connections.

The LGA50D modules should now be operating and supplying power to your E-load.

|VS|VSR|V82|V85|3|9|CMI|Jrob|
|---|---|---|---|---|---|---|---|
|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|Fig. 7 – Toggle switch position to enable the outputs of the modules|

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 10 of 18
---
# 6. The Power down sequence

To disable the outputs from the evaluation board, please take the following steps:

- Toggle Enable switch to disable Vout
- Turn off main voltage to Vin1 and Vin2

Note that not following power up/down sequence may damage the evaluation board.

# Additional information

1. Initial set position of the enable switch

This demo board is designed to have two LGA50D modules which can be tested independently with 2 independent input supplies.

However, if the user wants to use one input (either Vin1 or Vin2) to power both modules, then this can be done by linking the 2 solder pads together as identified in the picture below:

|Vin2|GND|Short|
|---|---|---|
|Vin1|GND| |

Fig. 8 – Shorted pads required to use a single input to supply both LGA50D modules

The short should be removed for efficiency test, because it affects the test result.

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 11 of 18
---
# Enabling each output

The outputs of the individual converters can be enabled or disabled by populating and depopulating the enable jumpers as required.

|EN1|EN2|EN3| |
|---|---|---|---|
| |Fig. 9 – The enable jumpers – all 3 shown in place to enable all 3 outputs| | |

If the enable signal is bouncing during enable and disable, a 0.1uF 0603 capacitor can be added at C211, C212 and C213 for monotonic signal. (Refer to Appendix A for the location of the capacitors)

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 12 of 18
---
# Test functions

The evaluation board is also equipped with test points to provide easily accessible voltage measurement points.

# 1. Vin and Vout sense locations

Accurate input and output voltage measurements via pin-headers can be found on J205 and J1205.

Use J1205 for monitoring the input voltage and output voltage of the ‘top’ LGA50D (when the input connections are on the left). Note, this converter is configured for a single 50A maximum output.

| |Vin-2|Vout-3|
|---|---|---|
|Vin2 -| |Vout-1|
|Vin-1| |Vout-2|

Fig. 10 – Voltage sense locations for Vin-2 and Vout-3

Use J205 for monitoring the input voltage and output voltage of the ‘bottom’ LGA50D (when the input connections are on the left). Note that this converter is configured for 2 independent 25A maximum outputs.

| |Vin-1-rtn|Vout-2-rtn|
|---|---|---|
|Vout-1-rtn| | |

Fig. 11 – Voltage sense locations for Vin-1 and Vout-2 and Vout-1

Artesyn Embedded Technologies LGA50D Evaluation Board October 2018 Page 13 of 18
---
# Ripple and regulation measurement locations

There are 3 test points provided to give accurate measurements of the output noise and ripple from the LGA50D.

The mating connector to the SMA connector found on the Evaluation board can be defined as “A Straight Cable Mount SMA Connector, Plug, Crimp Termination type RG174U”.

|Vout3 Regulation Measurement Point|Vout3 Ripple Measurement Point|
|---|---|
|Vin2 and Vout3 Efficiency Test Point|Vout3 setting|
|Fig. 12– Ripple and regulation measurement point for Vout-3|Fig. 12– Ripple and regulation measurement point for Vout-3|

J1403 - Point of Measurement for Vout-3 ripple.

J1401 - Point of Measurement for Vout-3 regulation.

|Vout2 Regulation Measurement Point|Vout2 Ripple Measurement Point|
|---|---|
|Voutz Regulation Measurement Point|Voutz Ripple Measurement Point|
|Fig. 13– Ripple and regulation measurement point for Vout-2| |

J303 - Point of Measurement for Vout-2 ripple

J301 - Point of Measurement for Vout-2 regulation
---
# LGA50D Evaluation Board User Manual

• J403 Point of Measurement for Vout-1 ripple

• J401 Point of Measurement for Vout-1 regulation

|Vout1 Ripple Measurement Point|J1206|
|---|---|
|Enable jumper|I2C connector|
|Vout2 setting| |
|Vout1 Regulation Measurement Point| |

Fig. 14– Ripple and regulation measurement point for Vout-1

# Errata

Fig. 15 J1206 silk screen

Note: The silk screen on the demo-PCB is missing on J1206. The silk screen is shown on the right in the figure above. The J1206 is for 4 phase setting.

For any other measurements and configurations, please contact your Artesyn representative or technical support for any further configurations or evaluation parameters that you wish to investigate.

Artesyn Embedded Technologies - LGA50D Evaluation Board - October 2018 - Page 15 of 18
---
# Appendix A – Silk-screen layer of the evaluation board

| | | | | |MT| |SCPWI| | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ScaT|8| | | |Wn0| |3| | | | | |
| | | |OVP WD BQL PLOL| | |D D0| | |SCRMS| | | |
| |1 1 8| | | | |1| |107|SCRH4|8| | |
| |SCRWZ| |0 ? @|1 1| |107| | | | | | |
|01 0|8| |3|0j|1 1|D00| | |ScRNG| | | |
|'2| | | | | | | |2| |1|110 OPENIIOI|OPENI102|
|P/N:509-023316-O000| | | | | | | | | | | | |
| | | | | | |L2e| |ScRW?| | | | |
| |1| | | |2| |0! ?| | | | | |
|RedLrcANT|8 8| | | |2|07 3| | |SCRMII| | | |
| |ScaT| | |3| |8| |CPENIOI|OPENIOZ2| | | |
|:1| | | |8|1|'|L|ScRWIO| | | | |
| | | | | | |0 9 ?|2| | | | | |
| | | | |1| | | | |SCRM12| | | |
| |ScrNB| | |5| |W| | | | | | |
|1| | | | | | |3|OUTPUT ENABLE|W|W| | |
| |8| | | | | | | | | | | |
| | | | | | |Mm| |I|(D| | | |

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 16 of 18
---
# LGA50D Evaluation Board User Manual

# DOCUMENT REVISION HISTORY

|REV|DATE|DESCRIPTION|REMARKS|
|---|---|---|---|
|01|12th Nov2018|First release| |

Artesyn Embedded Technologies LGA50D Evaluation Board October 2018

Page 17 of 18
---
# Contact for Technical Support and Information

|Americas|Asia|Europe|
|---|---|---|
|Phone:|Phone:|Phone:|
|+1 888 412 7832 or|400 8899 130 (in China) and|(0) 8000 321 546 (in the UK) and|
|+1 407 241 2752|+86 29 88836505 (outside China)|+44 (0) 800 032 1546 (outside UK)|
|Email:|Email:|Email:|
|techsupport.embeddedpower@emerson.com|TSXA.embeddedpower@emerson.com|techsupport.embeddedpower@emerson.com|
|Availability:|Availability:|Availability:|
|8am to 8pm (EST)|8:30am to 5:30pm (HKT)|8am to 5pm (GMT)|

Visit us: http://www.artesyn.com/

http://www.artesyn.com/power/

Artesyn Embedded Technologies, Artesyn and the Artesyn Embedded Technologies logo are trademarks and service marks of Artesyn Embedded Technologies, Inc. All other names and logos referred to are trade names, trademarks, or registered trademarks of their respective owners. © 2016 2018 Artesyn Embedded Technologies, Inc. All rights reserved. For full legal terms and conditions, please visit www.artesyn.com/legal.

Artesyn Embedded Technologies

LGA50D Evaluation Board

October 2018

Page 18 of 18