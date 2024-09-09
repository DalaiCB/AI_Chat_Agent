# ARTESYN DS2400SPE SERIES

2400 W Distributed Power System

Advanced Energy's Artesyn DS2400SPE series power supply features an input range of 90 to 140 VAC, and 180 to 264VAC. It employs active power factor correction to minimize input harmonic current distortion and to ensure compliance with the international EN61000-3-2 standard - they have a power factor of 0.99 at full load. The power supplies also feature active AC inrush control, to automatically limit inrush current at turn-on to 45 A maximum.

# SPECIAL FEATURES

|AT A GLANCE|COMPLIANCE|
|---|---|
|Front-end Bulk Power|80PLUS PLATINUM|

2400 W continuous at high line

90 to 140 VAC & 180 to 264 VAC Operation

- 2400 W output power at high line
- High power and short form factor
- 1U power supply
- High density design: 62 W/in3
- Active power factor correction
- Inrush current control
- 80plus platinum efficiency
- N+1 or N+N redundant
- Active current sharing
- PMBus compliant
- Two-year warranty

SAFETY

- UL/cUL 60950 (UL Recognized)
- IEC 62368-1
- DEMKO+ CB Report EN60950
- EN60950
- CE Mark
- UKCA Mark
- BIS, BSMI, KC, EAC

©2024 Advanced Energy Industries, Inc.
---
# DS2400SPE

|ELECTRICAL SPECIFICATIONS| | |
|---|---|---|
|Input| | |
|Input Voltage Range|180 to 264 VAC: 2400 W| |
| |90 to 140 VAC: 1400 W| |
|Frequency|47 Hz to 63 Hz| |
|Efficiency|94.0% peak| |
|Max Input Current|16 A| |
|Inrush Current|50 Apk| |
|Conducted EMI|Class A| |
|Radiated EMI|Class A| |
|Power Factor| |> 0.9 beginning at 20% load|
|ITHD|10%| |
|Leakage Current|0.57 mA| |
|Hold-up Time|11 ms at 95% load| |
|AC input can be re-applied after the amber light stops flashing| | |

|ORDERING INFORMATION| | | |
|---|---|---|---|
|Model Number|Nominal Main Output|Standby Output|Airflow Direction|
|DS2400SPE-3|12.2 V @ 196.72 A|12 V @ 3.5 A|Standard (forward)|
|DS2400SPE-3-001|12.2 V @ 196.72 A|12 V @ 3.5 A|Reverse|

advancedenergy.com
---
# DS2400SPE

# ELECTRICAL SPECIFICATIONS

|Output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal Setting|12.175 V|12.20 V|12.225 V|
|Total Output Regulation Range|11.6 V| |12.9 V|
|Dynamic Load Regulation Range|11.6 V| |12.9 V|
|Output Ripple| | |180 mVp-p|
|Output Current|8.0 A (minimum starting load for a 20% transient step)| |196.72 A at high line, 114.75 A at low line|
|Current Sharing| |Within +/-8.0 A of each other| |
|Capacitive Loading|4,900 μF| |38,000 μF|
|Start-up from AC to output| | |2,300 ms|
|Output Rise Time| | |100 ms|

|Standby DC Output|MIN|NOM|MAX|
|---|---|---|---|
|Nominal Setting|11.95 V|12.00 V|12.05 V|
|Total Output Regulation Range|11.4 V| |12.6 V|
|Dynamic Load Regulation Range|11.4 V| |12.6 V|
|Output Ripple| | |120 mVp-p|
|Adjustment Range| |N/A| |
|Output Current|0.0 A| |3.5 A|
|Current Sharing| |N/A| |
|Capacitive Loading|1 μF| |4700 μF|
|Start-up from AC to Output|20 ms| |2000 ms|

|Protections|MIN|MAX|
|---|---|---|
|Main Output| | |
|Overcurrent Protection|107%|130%|
|Overvoltage Protection|13.5 V|14.5 V|
|Undervoltage Protection|10.0 V|10.5 V|
|Overtemperature Protection|Yes| |
|Fan Fault Protection|Yes| |
|Standby Output| | |
|Overcurrent Protection|110%|150%|
|Overvoltage Protection|13.5 V|15.0 V|
|Undervoltage Protection|10.0 V|10.5 V|

1 Minimum current for transient load response testing only. Unit is designed to operate and be within output regulation range at zero load

2 Output voltage will stay within regulation during a 50% step load with a minimum starting load of 10A. Current slew rate is 1A/uS

3 Latch mode

4 Auto-recovery

advancedenergy.com 3
---
# DS2400SPE

# CONTROL AND STATUS SIGNALS

|Input Signals| | | |
|---|---|---|---|
|PSON_L|Active LOW signal which enables/disables the main output. Pulling this signal LOW will turn-on the main output.| | |
|VIL|Input logic level LOW| |0.8 V|
|VIH|Input logic level HIGH|2.0 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |1.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|PSKILL_H|First break/last mate active HIGH signal which enables/disables the main output.| | |
|VIL|Input logic level LOW. This allows for the power supply to be turned on| |0.8 V|
|VIH|Input logic level HIGH. Immediately shuts down the power supply|2.0 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| | |
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|VSENSE+, VSENSE-|VSENSE+ and VSENSE- lines are the remote sense lines for regulation. Each line will compensate for a maximum of 100 mV.| | |

|Output Signals| | | |
|---|---|---|---|
|ACOK|Signal used to indicate the presence of AC input to the power supply. A logic level HIGH will indicate that the AC input to the power supply is within the operating range while a logic level LOW will indicate that AC has been lost| | |
|VOL|Output logic level LOW| |0.4 V|
|VOH|Output logic level HIGH|2.4 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |2.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|
|PWR_GOOD / PWOK|Signal used to indicate that main output voltage is within regulation range. The PWR_GOOD signal will be driven HIGH when the output voltage is valid and will be driven LOW when the output falls below the under-voltage threshold. This signal also gives an advance warning when there is an impending power loss due to loss of AC input or system shutdown request. More details in the Timing Section.| | |
|VOL|Output logic level LOW| |0.4 V|
|VOH|Output logic level HIGH|2.4 V|3.6 V|
|ISOURCE|Current that may be sourced by this pin| |2.0 mA|
|ISINK|Current that may be sunk by this pin at low state| |4.0 mA|

advancedenergy.com
---
# DS2400SPE

# CONTROL AND STATUS SIGNALS (CONTINUED)

# Output Signals

# LED Indicators

A single bi-color LED is used to indicate the power supply status.

Status LEDNo AC input to PSU with external 12VMain output ONPower supply failure (OCP, OVP, OTP, FAN FAULT)

advancedenergy.com 5
---
# DS2400SPE

# ELECTRICAL SPECIFICATIONS

|Description|Min|Max|Unit|
|---|---|---|---|
|Delay from AC being applied to standby output being within regulation|20|2000|ms|
|Delay from standby output to ACOK assertion|20| |ms|
|Delay from standby output to main output voltage being within regulation|300| |ms|
|Delay from AC being applied to main output being within regulation|2300| |ms|
|Delay from output voltages within regulation limits to PWOK asserted|100|1000|ms|
|Delay from loss of AC to assertion of ACOK|7| |ms|
|Delay from loss of AC to deassertion of PWOK|10| |ms|
|Delay from loss of AC to main output being within regulation|11| |ms|
|Delay from loss of AC to standby output being within regulation|150| |ms|
|* Standby output loaded at 1.0 A| | | |
|Delay from deassertion of PWOK to output falling out of regulation|1| |ms|
|Delay from PSON assertion to output being within regulation|350| |ms|
|Duration of PWOK being in deasserted state during an ON/OFF cycle of PSU|N/A|N/A| |

advancedenergy.com
---
|DS2400SPE TIMING DIAGRAM| | |
|---|---|---|
|AC Input| | |
|Vout_stby|T sb_On| |
| |T sb_Hold-up| |
| |T ACOK_Delay| |
| |ACOK|T sb_Vout|
| |T sb_ACOK| |
|Vout_main|T AC_On_Delay| |
| |T Vout_Hold-up| |
|PWOK|T PWOK_On| |
| |TPWOK_Off| |
| |T PWOK_Hold-up| |
| | |T PSON_On_Delay|
| |PSON| |
| |advancedenergy.com 7| |
---
# DS2400SPE

# ENVIRONMENTAL SPECIFICATIONS

|Operating temperature|Forward air: 0 to 50°C, allowable up to 60°C at 1800 W|
|---|---|
| |Reverse air: 0 to 40°C, allowable up to 50°C at 1700 W|
|Operating altitude|16,400 ft with derated power|
|Operating relative humidity|Up to 95% non-condensing|
|Non-operating temperature|-40 to +70°C|
|Non-operating relative humidity|Up to 95% non-condensing|
|Non-operating altitude|up to 50,000 feet|
|Vibration and shock|Standard operating and non-operating random shock and vibration|
|ROHS compliance|Yes|
|MTBF|900 khours Telcordia Issue 3|
|Operating life|Minimum of 5 years|
