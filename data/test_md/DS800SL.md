# ARTESYN DS800SL SERIES

800 Watts Bulk Front End

Advanced Energy's Artesyn DS800SL series bulk front end AC-DC power supply accepts a wide range 90–264 Vac input and provides a main 12 V output plus a 5 V standby output. Rated at 800 watts it is an 80 Plus Gold supply with a high half-load efficiency of 92%. Housed in a slimline 1U high, 2.1 inch wide rack-mounting package, the power supply is primarily designed for ‘always-on’ enterprise servers and similar space-constrained applications. This series comes in two airflow versions – dc-connector to ac-connector and vice versa.

# DATA SHEET

Total Output Power:
800 Watts +5.0 Vdc Standby

# SPECIAL FEATURES

|800 W output power|UL/cUL 60950 -1|
|---|---|
|19.05 W/cu-in|CSA 60950-1|
|1U X 54.5 mm form factor (slimline)|VDE 60950-1|
|N + 1 redundant|China CCC|
|Hot-swap|CB Scheme Report/Cert|
|Internal OR’ing| |
|5.0 V housekeeping| |
|High efficiency 92% @ 200 Vac, 50% load (Climate Savers Gold)| |
|Variable speed “smart fans”| |
|EMI Class B| |
|Available in two airflow directions| |

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range (operating)|90 - 264 Vac|
|Input range (nominal)|115 / 230 Vac|
|Frequency|47 - 63 Hz|
|Inrush current|≤ 40 A peak Either hot or cold start|
|Power factor|0.99 typical Meets EN61000-3-2|
|Harmonics|Meets IEC 1000-3-2 requirements|
|Input current|10.0 A RMS max input current At 100 Vac|
|Holdup time|10 ms minimum for main O/P At full rated load|
|Undervoltage lockout|85 ± 3.0 Vac Turn-on voltage|
| |80 ± 3.0 Vac Turn-off voltage|
|Overvoltage lockout|N/A|
|Leakage current|< 1.0 mA At 264 Vac|
|On/Off power switch|N/A|
|Power line transient|MOV directly after the fuse|

|Efficiency Curve 800 W DS Slim| |
|---|---|
|92.0%| |
|90.0%| |
|88.0%| |
|86.0%|230 Vac, 50 Hz|
|84.0%|115 Vac, 60 Hz|
|82.0%| |
|80.0%| |
|0.0 100.0 200.0 300.0 400.0 500.0 600.0 700.0 800.0 900.0|Output Power [W]|

|DS800SL-3-001 Power Derating| |
|---|---|
|820|100Vac|
|800|110Vac|
|780| |
|760| |
|740| |
|720| |
|700| |
|680| |
|660|230Vac|
|640| |
|620| |
|0 10 20 30 40 50|Ambient Temperature (degC)|

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

|Input|Output rating|Setpoint|
|---|---|---|
|12 V @ 66.7 A; 800 W|90 - 264 Vac|12.0 V|
|5.0 Vsb @ 4 A; 20 W| | |

Total regulation range

|12 V ± 1%|Line/load/transient when measured at output connector|
|---|---|
|5.0 Vsb ± 3%| |

Rated load

800 W maximum
No derating over operating temp range for forward air

Minimum load

|12 V @ 0.5 A|No load operation shall not damage the power supply|
|---|---|
|5.0 Vsb @ 0.0 A| |

Output noise (PARD)

| |120 mV Max P-P|12.0 V output|
|---|---|---|
| |100 mV Max P-P|5.0 Vsb output|
|Measured with a 0.1 uF ceramic and 10 uF tantalum capacitor on any output; 20 Mhz| | |

Output voltage overshoot

600 mV; 12 V main250 mV; 5.0 standby

Transient response

| |+/-5% of regulation range|50% load step @ 1 A/us|
|---|---|---|
| | |Step load valid between 10% to 100% of output rating|
| | |Recovery time to within 1% of set point at onset of transient|

Max units in parallel

Up to 6

Short circuit protection

>130% of rated output
Output to return

Remote sense

Compensation up to 100 mV

Output isolation

Standard per Safety Requirements

Forced load sharing

To within 10% of all shared outputs
Digital sharing control

Overload protection (OCP)

|120% to 130%|12 V output|
|---|---|
|120% to 170%|5.0 Vsb output|

Overvoltage protection (OVP)

|110% to 120%|12 V output|
|---|---|
|110% to 125%|5.0 Vsb output|

Overtemperature protection

10 - 15 ˚C above safe operating area
Both PFC and output converter monitored

advancedenergy.com
---
# Timing Diagram

|AC Input|AC On|AC On| | | |
|---|---|---|---|---|---|
|Main Vout|T AC_On_Delay|T PWOK_Off_| | | |
| |T PWOK_On| | |T PWOK_Off| |
| | |PWOK| |T PWOK_Holdup|T PWOK_On|
| | |T sb_on_delay| |T PSON_PWOK| |
|5.0 Vsb Vout|T SB_Vout| | |T PSON_On_Delay| |
|PS_ON| | |T ACOK_Delay| | |
|AC_OK|AC Input| | |PSON|ON / OFF Cycle|

advancedenergy.com
---
# OUTPUTS - ALL MODELS (CONTINUED)

|Item|Description|Min|Max|Units| |
|---|---|---|---|---|---|
|Tvout_rise|+12 Output rise time|5|300|mSec| |
|Tvout_rise|5.0 Vsb output rise time|1|50|mSec| |
|Tsb_on_delay|Delay from AC being applied to 5.0 Vsb being within regulation.| | |2000|mSec|
|Tac_on_delay|Delay from AC being applied to all output voltages being within regulation.| | |4000|mSec|
|Tvout_holdup|Time all output voltages, including 5.0 Vsb, stay within regulation after loss of AC.| | |12|mSec|
|Tpwok_holdup|Delay from loss of AC to de-assertion of PWOK.| | |5|mSec|
|Tpson_on_delay|Delay from PSON# active to output voltages within regulation limits.|5|200|mSec| |
|Tpson_pwok|Delay from PSON# de-active to PWOK being de-asserted.| | |50|mSec|
|Tacok_delay|Delay from loss of AC input to de-assertion of ACOK#.|5|12|mSec| |
|Tpwok_on|Delay from output voltages within regulation limits to PWOK asserted at turn on.|100|1000|mSec| |
|Tpwok_off|Delay from PWOK de-asserted to 12 Vdc or 5.0 Vsb dropping out of regulation limits.|1|1000|mSec| |
|Tpwok_low|Duration of PWOK being in the de-asserted state during an off/on cycle using AC or the PSON# signal.| | |100|mSec|
|Tsb_vout|Delay from 5.0 Vsb being in regulation to 12 Vdc being in regulation at AC turn on.|50|1000|mSec| |

PSON #

The PSON# signal is required to remotely turn on/off the power supply. PSON# is an active low signal that turns on the +12 Vdc power rail. When this signal is not pulled low by the system, or left open, the +12 Vdc output turns off. The Vsb output remains on. This signal is pulled to a standby voltage by a pull-up resistor internal to the power supply. The power supply fan(s) shall operate at the lowest speed.

PWOK# (Power Good)

PWOK is a power good signal and will assert HIGH when the outputs are within the regulation limits. PWOK will be pulled LOW by the power supply to indicate when either output falls below regulation limits or when AC power has been removed for a time sufficiently long so that power supply operation is no longer guaranteed. The start of the PWOK# delay time shall be inhibited as long as the +12 Vdc output is in current limit or the 5.0 Vsb output is below the regulation limit.

|PSON Signal Characteristics|PWOK Signal Characteristics|
|---|---|
|Signal Type|Accepts an open collector/drain input from the system. Pulled-up to the 5.0 Vsb located in power supply.|
|PSON# = Low|ON|
|PSON# = Open|OFF|
|Logic level low (power supply ON)|0 V - 0.8 V|
|Logic level high (power supply OFF)|2.0 V - 5.2 V|
|Source current, Vpson = low|4 mA|
|Power up delay: Tpson_on_delay|5 msec - 200 msec|
| | |
| | |
| | |
| | |

Power down delay: Tpson_off 1 msec - 1000 msec

advancedenergy.com
---
# DS800SL

# OUTPUTS - ALL MODELS (CONTINUED)

PSKILL

The +12 Vdc output only from the power supply shall be disabled if the PSKILL input is high and V Standby will continue to be provided, outputs may be enabled if this signal is low. The power supply includes a pull up to disable all outputs if this signal is open. PSKILL shall not be connected during a hot insertion before all of the other pins are connected.

AC INPUT PRESENT INDICATOR (ACOK/L)

The ACOK signal is used to indicate the presence of AC input to the power supply. This signal shall be connected to Vsb through a resistor on the host system side. A logic “Low” level on this signal shall indicate AC input to the power supply is present. A Logic “High” on this signal shall indicate a loss of AC input to the power supply.

ACOK# Signal Characteristics

|Signal Type|Pull up to 5.0 Vsb through a resistor in the host system.| |
|---|---|---|
|Present| | |
|Present = High|Present| |
|Present = Low|Not Present| |
|MIN|MAX| |
|Logic level low voltage, Isink = 4 mA|0 V|0.8 V|
|Logic level high voltage, Isink = 50 μA|2.0 V|5.2 V|
|Sink current, PRESENT# = low|4 mA| |
|Sink current, PRESENT# = high|50 μsec| |

# STATUS INDICATIONS

See table below for Summary of Status signals, Ports, and Indicators. The condition column assumes 2 or more power supplies present and ON and 5.0 Vsb shared for the management interface. On the “Fan Blocked” condition, the assumption is that all outputs are within spec and not over temperature. This would be considered a “warning” condition. On the “Standby” condition, the system differentiates this state by knowing PS_ONL in negated (requesting Standby).

|Condition| |Status Signals| |Status Register| | |Shutdown Register| | |LED’s| | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Normal Operation|ACOK/L|PWOK/H|PSON|PWOK|Fan-Fail|AC-Loss|0-Temp|0-Current|Fail|AC|DC|Fail|
|V1 12 V Overcurrent|0|0|1|0|0|0|1|1|On|Off|On| |
|AC Input Fail|1|0|1|0|0|1|0|0|1|Off|Off|Off|
|Fan Blocked or Running Under Speed. O/P’s ok|0|1|1|0|0|0|0|0|0|On|On|Off|
|UV on V1 12 V and PS Has Latched Off|0|0|1|0|0|0|0|0|1|On|Off|On|
|UV on Vsb +5.0 and PS Has Turned Off|0|0|1|0|0|0|0|0|1|On|Off|On|
|OV on V1 12V or Vsb +5.0 & PS Has Latched Off|0|0|1|0|0|0|0|0|1|On|Off|On|
|Over Temp and PS Has Turned Off|0|0|1|0|0|0|1|0|1|On|Off|On|
|Fan Below Shutdown Limit|0|0|1|0|1|0|0|0|1|On|Off|On|
|No Problems But PS is in Standby Mode|0|0|0|0|0|0|0|0|0|On|Off|Off|

advancedenergy.com
---
# OUTPUT CONNECTOR AND PIN-OUT TABLE

|Pin|Signal Name|Top Side|
|---|---|---|
|Pin 1|+12 V|S13|
|Pin 2|+12 V|S24|
|Pin 3|Ground|Ground|
|Pin 4|Ground|Ground|
|S1|+12 V Sense|S1|
|S2|+12 V RTN Sense|S12|
|S3|+12 V Current Share|Bottom Side|
|S4|SMB_ALERT/L| |
|S5|SDA| |
|S6|SCL*| |
|S7|PSKILL| |
|S8|PSON/L| |
|S9|PW_OK| |
|S10|PS_A1| |
|S11|+5.0 V_STBY| |
|S12|+5.0 V_STBY| |
|S13|Reserved| |
|S14|PRESENT/L| |
|S15|PS_A0| |
|S16|Reserved| |
|S17|Reserved for factory use| |
|S18|EEPROM_WP| |
|S19|ACOK/L| |
|S20|Not used| |
|S21|PS_A2| |
|S22|V_STBY Remote Sense| |
|S23|V_STBY| |
|S24|V_STBY| |

* Supports I2C standard mode (100 kHz) only

Note: Pin number may not necessarily match vendor’s pin number assignment. Please follow the signal and number assignment as indicated in this datasheet

advancedenergy.com 7
---
# MECHANICAL DRAWING

BURN-IN100% Burn-in at 45 °C, at 80-90% load. Duration of burn-in determined by Quality Assurance Procedures.

# MTBF

The power supply has an MTBF of >400K hours using Telcordia SR-332 at full load, and 25 °C ambient. With the power supply installed in a system in a 25 °C ambient environment and operating at full load, capacitor life shall be 5 years, minimum for ALL electrolytic capacitors contained within this power supply.

# QUALITY ASSURANCE

Full QAV testing shall be conducted in accordance with Artesyn Embedded Power Standards with reports available upon request.

# WARRANTY

Artesyn Embedded Power shall warrant the power supply to be free of defects in materials and workmanship for a minimum period of two years from the date of shipment, when operated within specifications. The warranty shall be fully transferable to the end owner of the equipment powered by the supply.

advancedenergy.com
---
About Advanced Energy

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)
productsupport.ep@aei.com (Technical Support)
+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-DS800SL-235-01 12.14