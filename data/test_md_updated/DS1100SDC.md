# ARTESYN DS1100SDC-3

500W
RTN 48V
1100 Watts

Distributed Power System

Advanced Energy's Artesyn DS1100SDC-3 series bulk front end DC-DC power supply accepts a wide range -36 to -72 VDC input and provides a main 12 V output plus a 12 V standby output. It is rated at 1,100 watts. Housed in a 1U high rack-mounting enclosure with a short form factor that frees up system space, the DS1100SDC-3 has a very high power density of 24 watts per cubic inch. This series comes in two airflow versions – dc-connector to ac-connector and vice versa. The series is also in the same form factor and has the same output configuration as the DS1100PED-3.

# SPECIAL FEATURES

- 1100 W output power
- High power and short form factor
- 1U power supply
- High-density design: 24 W/in^3
- Inrush current control
- N+1 or N+N redundant
- Active current sharing
- Full digital control
- PMBus compliant
- Compatible with Artesyn’s Universal PMBus GUI
- Reverse airflow available
- Two-year warranty

# COMPLIANCE

|EMI Conducted/Radiated Class A Limits|PMRIS|
|---|---|
|UL/cUL 62368 (UL Recognized)|DEMKO+ CB Report EN62368|
|EN62368|CE Mark|
|China CCC| |

# SAFETY

- UL/cUL 62368 (UL Recognized)
- DEMKO+ CB Report EN62368
- EN62368
- CE Mark
- China CCC

©2020 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|-36 to -72 Vdc|
|Efficiency|90.0% peak|
|Max input current|37 Arms|
|Inrush current|55 Apk|
|Conducted EMI|Class A|
|Radiated EMI|Class A|
|Hold-up time|1 ms at full load|

| | |Output|Main DC Output|Standby DC Output| | |
|---|---|---|---|---|---|---|
|Nominal setting|MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting|-0.20%|12|0.20%|-1%|12|1%|
|Total output regulation range|11.4 V| |12.6 V|11.4 V| |12.6 V|
|Dynamic load regulation range|11.4 V| |12.6 V|11.4 V| |12.6 V|
|Output ripple| | |120 mVp-p| |120 mVp-p| |
|Output current|2 A| |91.76 A|0.1 A| |3.0 A|
|Current sharing| |Within ±5% of full load rating| | |N/A| |
|Capacitive loading|2000 μF| |40,000 μF|47 uF| |680 μF|
|Start-up from input to output| | |2200 ms| | |1700 ms|
|Output rise time|5 ms| |50 ms|2 ms| |60 ms|

|Protections|MIN|NOM|MAX| | |
|---|---|---|---|---|---|
|Overcurrent protection|120%| | | |150%|
|Overvoltage protection|13.5 V| | | |15.0 V|
|Undervoltage protection|10.5 V| | | |11.0 V|
|Overtemperature protection| |Yes| | | |
|Fan fault protection| |Yes| | | |

|Standby Output| | | |
|---|---|---|---|
|Overcurrent protection|120%| |150%|
|Overvoltage protection|13.5 V| |15.0 V|
|Undervoltage protection|10.0 V| |11.0 V|

1 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load.

2 Autorecovery if the overcurrent is less than 120% and last only for <500 ms

3 Standby protection is auto-recovery
---
# ELECTRICAL SPECIFICATIONS (CONTINUED)

LED Indicators

Status LEDNo DC input to PSUMain output ONStandby mode or Power supply failure (OCP, OVP, OTP, FAN FAULT:)

Firmware Reporting And Monitoring

|Accuracy Range|5 to 20%|20 to 50%|50 to 100%|
|---|---|---|---|
|Output loading|2%| | |
|Input voltage|±0.55 A fixed error|±4%| |
|Input power|±1.25 W at < 125 W input|±1.25%| |
|Output voltage| |±2%| |
|Output current|0.3 A fixed error|±2%| |
|Temperature|±5 °C on the operating range| | |
|E IN|±15% from 10% to 20% load|±5%| |
|Fan speed|Actual RPM ±250 RPM| | |

PMBus: YES

Remote ON/OFF: YES

Timing Specifications

|Description| |Min|Max|Unit|
|---|---|---|---|---|
|Tsb_On| |20|1700|ms|
|Tsb_INPUT_OK| |See note below|20|ms|
|Tsb_Vout| | |300|ms|
|T INPUT_On_Delay| | |2200|ms|
|T PWR_GOOD_On| |100|1000|ms|
|T INPUT_OK_Delay| | |6|ms|
|T PWR_GOOD_Hold-up| | |0.2|ms|
|T Vout_Hold-up| |1| |ms|
|Tsb_Hold-up| |150| |ms|
|T PWR_GOOD_Off| |1| |ms|
|T PSON_On_Delay| | |350|ms|
|T PWOK_Low| |N/A|N/A| |

Note: Tsb_hold-up: tested at 1A load on standby output. Tsb_INPUT_OK: INPUT_OK can assert earlier than the standby output

advancedenergy.com 3
---
# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|DS1100SDC-3: 1100W from 0 to 50 °C DS1100SDC-3-001: 1100W from 0 to 40 °C|
|---|---|
|Operating altitude|up to 10,000 feet with derating|
|Operating relative humidity|20% to 80% non-condensing|
|Non-operating temperature|-40 to +70 °C|
|Non-operating relative humidity|10% to 95% non-condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating/non-operating shock/vibration|
|ROHS compliance|YES|
|MTBF|200,000 hours per Telcordia Issue 2, Method 1, Case 3 at 25 °C ambient at full load|
|Operating life|Minimum of 5 years|
|Reliability|All electronic component derating analysis is done at maximum ambient, 80% of maximum rated load, nominal input line voltage.|

advancedenergy.com
---
# DS1100SDC

# CONTROL AND STATUS SIGNALS

# Input Signals

|Signal| |MIN|MAX|
|---|---|---|---|
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |2 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.5 mA|

# PSKILL_L

|Signal| |MIN|MAX|
|---|---|---|---|
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |2 mA|
|I SINK|Current that may be sunk by this pin at low state| |0.5 mA|

# Output Signals

|Signal| | |MIN| |MAX|
|---|---|---|---|---|---|
|INPUT_OK|Signal used to indicate the presence of DC input to the power supply.| | | | |
|V IL|Input logic level LOW| | | |0.6 V|
|V IH|Input logic level HIGH| |2.0 V| |5.0 V|
|I SOURCE|Current that may be sourced by this pin| | | |3.3 mA|
|I SINK|Current that may be sunk by this pin at low state| | | |0.7 mA|

# PWR_GOOD / PWOK

|Signal| | |MIN| |MAX|
|---|---|---|---|---|---|
| |Signal used to indicate that main output voltage is within regulation range.| | | | |
|V IL|Input logic level LOW| | | |0.8 V|
|V IH|Input logic level HIGH| |2.0 V| |5.0 V|
|I SOURCE|Current that may be sourced by this pin| | | |3.3 mA|
|I SINK|Current that may be sunk by this pin at low state| | | |0.7 mA|

advancedenergy.com          5
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| |
|---|---|
|PS_PRESENT_L|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is shorted to the standby return in the power supply. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.|
|PS_INTERRUPT_L|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to 12 VSB is 8.2 k with a 3.0 k pull-down to ground. A 100 pF decoupling capacitor is also recommended.|

| | |MIN|MAX|
|---|---|---|---|
|V IL|Input logic level LOW| |0.8 V|
|V IH|Input logic level HIGH|2.0 V|5.0 V|
|I SOURCE|Current that may be sourced by this pin| |4 mA|
|I SINK|Current that may be sunk by this pin at low state| |4 mA|

|BUS Signals| |
|---|---|
|ISHARE|Bus signal used by the power supply for active current sharing. All power supplies configured in the system for n+n sharing will refer to this bus voltage in order to load share.|

| | |MIN|MAX|
|---|---|---|---|
|I SHARE Voltage|Input logic level LOW|7.75|8.25|
| |Voltage at 50% load, stand-alone unit|3.85|4.15|
| |Voltage at 0% load, stand-alone unit|0|0.3|
|I SOURCE|Current that may be sourced by this pin| |160 mA|

SCL, SDAClock and data signals defined as per I C requirements. It is recommended that these pins be pulled-up to a 2.2 kohm resistor to 3.3 V and a 100 pF decoupling capacitor at the system side.

| | |MIN|MAX|
|---|---|---|---|
|VL|Input logic level LOW| |0.8 V|
|VH|Input logic level HIGH|2.0 V|5.0 V|

Note: All signal noise levels are below 400 mVpk-pk from 0 - 100 MHz.

I2C Addressing Table: Not applicable. This power supply has a fixed I2C address. In order to support multiple addresses, the system will have to utilize a switcher or an I2C expander.

advancedenergy.com
---
|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS1100SDC-3|12 V|12 V @ 3A|Std (forward)|
|DS1100SDC-3-001|12 V|12 V @ 3A|Reverse1|

1 Derating may apply

MECHANICAL DRAWING

AIRFLOW DIRECTION

Standard (Forward)

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

WATTAGE LABEL

SECTION A-A

advancedenergy.com 7
---
# Input Connector (System Side)

Molex 394210002

# PSU Side Connector Part Number

Molex 394250002


advancedenergy.com   9
---