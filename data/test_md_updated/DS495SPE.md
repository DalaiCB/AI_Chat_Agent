# ARTESYN DS495SPE 495 Watts Distributed Power System

Advanced Energy's Artesyn DS495SPE is housed in 1U high rack-mounting enclosures measuring just 3.4 x 7.7 inches (86.3 x 196.5 mm). This form factor is significantly shorter than that of similarly rated earlier-generation power supplies — freeing up valuable system space — and is achieved by use of the latest power switching technology and high density component packaging techniques.

# AT A GLANCE

|Front-end Bulk Power|Total Output Power|
|---|---|
|495 W continuous|Wide Input Voltage|
| |90 to 264 VAC|

# SPECIAL FEATURES

- 495 W output power
- 1U power supply
- Active power factor correction
- EN61000-3-2 harmonic compliance
- Inrush current control
- 80plus Platinum efficiency
- N+N redundant
- Hot-pluggable
- Active current sharing
- Full digital control
- PMBus compliant
- Standard airflow
- Two-year warranty

# COMPLIANCE

- Conducted/Radiated EMI Class A Limits + 6 dB margin
- EN61000-4-11

# SAFETY

- IEC62368
- UL/cUL
- Demko +CB Report
- CE Mark
- UKCA Mark
- CCC
- BSMI

&copy;2022 Advanced Energy Industries, Inc.
---
# ELECTRICAL SPECIFICATIONS

|Input| |
|---|---|
|Input range|90 to 264 VAC|
|Frequency|47 to 63 Hz|
|Efficiency|94.0% peak|
|Max input current|6.6 Arms @ 90 VAC|
|Inrush current|25 Apk|
|Conducted EMI|Class A with 6 dB margin|
|Radiated EMI|Class A with 6 dB margin|
|Power factor|>0.9 beginning at 20% load|
|ITHD|10%|
|Leakage current|1 mA|
|Hold-up time|10 ms at full load|

| |Output|Main DC Output| |Standby DC Output| | |
|---|---|---|---|---|---|---|
| |MIN|NOM|MAX|MIN|NOM|MAX|
|Nominal setting|-0.2%|12 V|0.2%|-2.5%|12 V|+2.5%|
|Total output regulation range|11.4 V|-|12.6 V|11.4 V|-|12.6 V|
|Dynamic load regulation range|11.4 V|-|12.6 V|11.4 V|-|12.6 V|
|Output ripple (peak to peak)|-|-|120 mV|-|-|120 mV|
|Output current|2.0 A1|-|41.25 A|0.0 A|-|3.0 A|
|Current sharing| |Within ±5% of full load rating| |N/A| | |
|Capacitive loading|-|-|38,000 μF|47 μF|-|4,700 μF|

1 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load.

# ELECTRICAL SPECIFICATIONS

|Protections|Main output| | | | | | |
|---|---|---|---|---|---|---|---|
| | |MIN|NOM|MAX| | | |
|Overcurrent protection|110%| |-| | |150%| |
|Overvoltage protection|13.5 V| |-| | |15.0 V| |
|Undervoltage protection|10.0 V| |-| | |11.0 V| |
|Overtemperature protection|Yes| | | | | | |
|Fan fault protection|Yes| | | | | | |

| |Standby output| | | | | |
|---|---|---|---|---|---|---|
| | |MIN|NOM|MAX| | |
|Overcurrent protection|3.6 A| |-| | |4.5 A|
|Overvoltage protection|13.5 V| |-| | |15.0 V|
|Undervoltage protection|10.0 V| |-| | |11.0 V|

1 Latch mode

2 Standby protection is auto-recovery

advancedenergy.com
---
# ORDERING INFORMATION

|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|---|---|---|---|
|DS495SPE-3|12 V @ 41.25 A|12 V @ 3 A|Standard (forward)|
|DS495SPE-3-001|12 V @ 41.25 A|12 V @ 3 A|Reverse|

# CONTROL AND STATUS SIGNALS

# Input Signals

| | |MIN|MAX|
|---|---|---|---|
|VIL|Input logic level LOW|-|0.4 V|
|VIH|Input logic level HIGH|2.06 V|3.0 V|
|ISOURCE|Current that may be sourced by this pin at low state|-|1 mA|

| | |MIN|MAX|
|---|---|---|---|
|VIL|Input logic level LOW|-|0.4 V|
|VIH|Input logic level HIGH|2.4 V|3.0 V|
|ISOURCE|Current that may be sourced by this pin at low state|-|1.0 mA|

# Output Signals

| | | |MIN| |MAX|
|---|---|---|---|---|---|
|VoL|Output logic level LOW| |-| |0.6 V|
|VoH|Output logic level HIGH| |2.0 V| |3.0 V|
|ISOURCE|Current that may be sourced by this pin| |-| |4.0 mA|

| | | | | |MIN| |MAX|
|---|---|---|---|---|---|---|---|
|VoL|Output logic level LOW| | | |-| |0.4 V|
|VoH|Output logic level HIGH| | | |2.0 V| |3.0 V|
|ISINK|Current that may be sunk by this pin| | | |-| |10.0 mA|

advancedenergy.com
---
# CONTROL AND STATUS SIGNALS (CONTINUED)

|Output Signals| | | | |
|---|---|---|---|---|
|PS_PRESENT|Signal used to indicate to the system that a power supply is inserted in the power bay. This pin is connected to the standby return in the power supply through a 220 ohm resistor. Recommended pull-up resistor to 12 VSB is 8.2k ohm with a 3.0k ohm pull-down to ground. A 100 pF decoupling capacitor is also recommended.| | | |
|PS_INTERRUPT_L|Active low signal used by the power supply to indicate to the system that a change in power supply status has occurred. This event can be triggered by faults such as OVP, OCP, OTP, and fan fault. This signal can be cleared by a CLEAR_FAULT command. Recommended pull-up resistor to 12 VSB is 8.2k ohm with a 3.0k ohm pull-down to ground. A 100 pF decoupling capacitor is also recommended.| | | |
|VoL|Output logic level LOW| |-|0.8 V|
|VoH|Output logic level HIGH| |2.0 V|3.0 V|
|ISOURCE|Current that may be sourced by this pin| |-|4 mA|
|ISINK| |Current that may be sunk by this pin at low state|-|4 mA|

Note: All signal noise levels are below 400 mVpk-pk from 0 to 100 MHz.

IC Addressing Table: Not applicable. This power supply has a fixed IC address. In order to support multiple addresses, the system will have to utilize a switcher or an IC expander.

advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS

|LED Indicators|Status LED|
|---|---|
|No AC input, with external 12 V available|Blinking GREEN (2 sec on, 1 sec off)|
|Standby mode|Blinking GREEN (2 sec on, 1 sec off)|
|Main output ON|Solid GREEN|
|Power supply failure (OCP, OVP, OTP, FAN FAULT)|Blinking AMBER (1 sec on, 1 sec off)|
|Standby fault|OFF|

|Firmware Reporting And Monitoring|Accuracy Range| | |
|---|---|---|---|
|Output loading|5 to 20%|20 to 50%|50 to 100%|
|Input voltage|±5%|±5%|±5%|
|Input current|±0.55 A fixed error|±5%|±5%|
|Input power|6.25 W|5%|5%|
|Output voltage|±2%|±2%|±2%|
|Output current|±0.7 A error|±3%|±3%|
|EIN|±15% from 10% to 20% load|±5%|±5%|
|Temperature|±5°C on the operating range| | |
|Fan speed|Actual RPM ±250 RPM| | |

|Timing Specifications|Description|Min|Max|Unit|
|---|---|---|---|---|
|Tsb_On|Delay from AC being applied to standby output being within regulation|-|1700|ms|
|TVout_Rise|Rise time of output voltage going from 10% to 90% of the nominal regulation|2|20|ms|
|Tsb_Vout|Delay from standby output to main output voltage being within regulation|-|300|ms|
|TAC_On_Delay|Delay from AC being applied to main output being within regulation|-|2000|ms|
|TPWOK_On|Delay from output voltages within regulation limits to PWOK asserted|100|500|ms|
|TACOK_PWOK_Delay|Delay from deassertion of ACOK, due loss of input, to deassertion of PWOK|4|-|ms|
|TPWOK_Hold-up|Delay from loss of AC to deassertion of PWOK|10|-|ms|
|TVout_Hold-up|Delay from loss of AC to main output being within regulation|11|-|ms|
|TVout_sb_dwell|Delay from main output going <1 V to standby voltage falling out of regulation|5|-|ms|
|TACOK_off_dwell|Duration time of ACOK deassertion when the PSU has sensed a loss of input|75|120|ms|
|Tsb_Hold-up|Delay from loss of AC to standby output being within regulation|150|-|ms|
|TPWOK_Off|Delay from deassertion of PWOK to output falling out of regulation|1|-|ms|
|TPSON_On_Delay|Delay from PSON assertion to output being within regulation|-|350|ms|

advancedenergy.com
---
# TIMING DIAGRAM

AC InputVout_stbyAcOKVout_mainPWOKPSON

# ENVIRONMENTAL SPECIFICATIONS

| | |sb_Hold-up|Vout dwell| |
|---|---|---|---|---|
| |Vout|AcOK_PwoK_Delay| | |
| | | |ACOK_ot_dwell| |
|AC_On_Delay| |Vout Hold-UP| | |
| |Vout| | | |
|Pwok| | |Pwok_Of| |
| |PWOK_Hold-up| |PSON_On_Delay| |

Operating temperature: 0°C to 55°C at 100% load;

DS495SPE-3 can operate up to 65°C at 300 W without damage

DS495SPE-3-001 can operate up to 60°C at 300 W without damage

Operating altitude: Up to 16,400 feet, with ambient temperature derated to 45°C at 10,000 feet

Operating relative humidity: 10% to 95% non-condensing

Non-operating temperature: -40°C to +70°C

Non-operating relative humidity: 10% to 95% non-condensing

Non-operating altitude: Up to 50,000 feet

Vibration and shock: Standard operating/non-operating random shock and vibration

ROHS compliance: Yes

MTBF: &gt; 900 khours at 55°C, 80% load

Operating life: &gt; 5 years at 55°C at 80% load

advancedenergy.com
---
# CONNECTOR DEFINITIONS

|Output Connector Part Number|Card-edge|
|---|---|
|Mating Connector Part Number|FCI 10107844-002LF or equivalent|

Power Supply Output Card Edge (Top Side)

Power Supply Output Card Edge (Bottom Side)Power Supply Output Card Edge (Bottom Side)  Power Supply Output Card Edge (Top Side)

| |Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Bottom Side)|Power Supply Output Card Edge (Top Side)|
|---|---|---|---|
| |S24|S13| |
|P29-P36|P21-28| | |
|P19/20| |P1-P8|P9-P18|
| | |S1|S12|

advancedenergy.com
---