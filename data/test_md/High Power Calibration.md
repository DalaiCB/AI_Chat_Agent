# TEGAM HPC Series RF Calibration and Measurement Instruments

High Power RF Calibration System

|Model|Description|
|---|---|
|2601A|Calibrate High Power RF Sensing devices up to 100 W with uncertainty less than 1%|
|2602A|Working standards: TEGAM 2601A and 2602A|

Features:

- Calibrate High Power RF Sensing devices up to 100 W with uncertainty less than 1%
- Working standards: TEGAM 2601A and 2602A
- Through devices: Bird Wattmeters
- High Power RF Power Sensors from Bird, Keysight, R&S, and Anritsu
- 250 kHz to 3000 MHz Frequency Range
- National Lab Traceable through an AC Power Standard

The TEGAM High Power Calibration System is an automated solution for calibrating through path and terminating RF power measurement devices from multiple manufacturers. It includes the signal generation, amplification and filtering necessary to achieve or exceed the devices original specifications with the most accurate high power measurement system available.

The basis for the High Power Calibration System’s unmatched accuracy is an exclusive flow calorimeter designed to provide low uncertainties and convenient traceability. An internationally recognized AC power standard is used to calibrate the entire system in place. The AC standard can be sent to a national metrology institute to provide traceability at the highest level.

Prices and specifications subject to change without notice.
---
# High Power RF Calibration System Configurations

The High Power RF Calibration System can be configured differently depending on what you are calibrating. The two most popular configurations are shown below. Figure 1 shows the system set up to calibrate one of TEGAM’s standards, either the TEGAM 2601A or 2602A depending on the frequency band required. Figure 2 shows the calibration of a DUT using the 2601A or 2602A as the Standard.

|RF Calorimeter Working Standard Calibration|Working Std Meter| | | | |
|---|---|---|---|---|---|
| | | |Switch & Filters|Flow Calorimeter| |
|RF Signal Generator|RF Amplifier| | | | |
| | | |Component Specifications| | |

# RF Signal Generator (Minimum Requirements)

- Frequency Range: 100 kHz to 3 GHz
- Output Power: 0 dBm
- SCPI Compliant

# RF Amplifier (Minimum Requirements)

- Rated Output Power: 250 W (to achieve output power at DUT of ~100 W)
- Frequency Range: 100 kHz to 3 GHz (System Dependent)
- Harmonic Distortion: -20 dBC at 250 watts

# Lowpass Filter

- Lowpass filter designed to attenuate RF amplifier harmonics to < -50 dBC
- Frequency Selective Switch Controller

# Working Standard Meter

- TEGAM Model 1830A

# Working Standard Sensor

- TEGAM Model 2601A
- Frequency Range: 250 kHz to 1000 MHz
- Maximum Power: +54 dBm (250 W) (Calibrated up to ~100 W)
- TEGAM Model 2602A
- Frequency Range: 1000 MHz to 3000 MHz
- Maximum Power: +54 dBm (250 W) (Calibrated up to ~100 W)

# Flow Calorimeter

- TEGAM Model 1314
- Frequency Range: 50 Hz to 3000 MHz
- Maximum Power: 250 W (Typical Usable Range +10 to 250 W)
---
# HPC Series

# RF CALIBRATION AND MEASUREMENT INSTRUMENTS

Figure 2

RF Standard DUT Calibration

|RF Signal Generator|RF Amplifier|Switch & Filters|Wkg Std Sensor DUT Meter/Sensor RF Load|
|---|---|---|---|
| |Control|Component Specifications| |

RF Signal Generator (Minimum Requirements)

- Frequency Range: 100 kHz to 3 GHz
- Output Power: 0 dBm
- SCPI Compliant

RF Amplifier (Minimum Requirements)

- Rated Output Power: 250 watts (Output Power at the DUT is ~100 W)
- Frequency Range: 100 kHz to 3 GHz (System Dependent)
- Harmonic Distortion: -20 dBC at 250 watts

Lowpass Filter

- Lowpass filter designed to attenuate RF amplifier harmonics to < -50 dBC
- Frequency Selective Switch Controller

Working Standard Meter

- TEGAM Model 1830A

Working Standard Sensor

- TEGAM Model 2601A
- Frequency Range: 250 kHz to 1000 MHz
- Maximum Power: +54 dBm (250 W) (Output Power at the DUT is ~100 W)
- TEGAM Model 2602A
- Frequency Range: 1000 MHz to 3000 MHz
- Maximum Power: +54 dBm (250 W) (Output Power at the DUT is ~100 W)

RF Load

- VSWR: < 1.05
---
# HPC Series RF Calibration and Measurement Instruments

Power Cal System software controls all hardware providing an automated High Power RF Calibration System.

- Control of RF Switch bank to select correct amplifier and filter band.
- Control of RF signal generator to level power at proper frequency.
- Use of statistical analysis to determine if system is settled.
- EEPROM programming capability for Bird 4020 series (4021, 4022, 4024, and 4025) with customer supplied Bird 4421 (non-A) programming power meter with GPIB option and customer supplied Bird EEPROM adaptor.

|TEGAM|ALLO?| | | | | | |Verscn|1.045| | |
|---|---|---|---|---|---|---|---|---|---|---|---|
|RF Power Meter| | | |DUC Power Meter|Output Power| | | | | | |
| | | |Freq|Field Read|Power|Cal RF Calibrated Power| |Difference|Test Limit|Min|Burn|
| | | |32000|32002|99.822|409.077| |0.255|LC00| | |
|30000| | | |30.075|ouSt|100.032|0.269| | | | |
|25000| | | |25.148|Jo01Z0|100.067| | | | | |
|20000|20.02|99.869| | | |00.085| | | | | |
| |4000| |100.41| | | | | | | | |
|6000| |100.167|100.124| | | | | | |Pass| |
|8000| | | | |99.785|100.109| | | | | |
|10000| | | | |99.916|100.058| |0.142| | | |
|20000| | | | |100.4698|100.116| |03-S| |Pass| |
|25000| | |2,000|2169|00.218| | |0.154| | | |
|30000| | |09.067|16018| | | |0us6| | | |
| | | |32000| | | | | | | | |

Std: Deva Limit 0.05

Lcvlimo Points

| | |Test Info|Calcrmeter|RF Power lic|Senson|Genelator|Amp Selup|Control|Switch|
|---|---|---|---|---|---|---|---|---|---|
| | |3622110| |98-000 [ine] ceenuacio 52| | | |ZA-0| |

Dwell Time Remaining

Action

Calibration Test

Adjustment Test

Start Test

Save Settings

Report

Check Equipment

Save Attenuations

Accessories (Needed for Calibration of TEGAM Model 1314)

- AC Power Standards
- Radian RD-23 Dytronic Single Phase Reference Standard
- Accuracy + 0.01%
- Yokogawa WT310E

AC Power Sources (Based on Driver Availability)

- Keysight 6811B

Please contact TEGAM with any questions pertaining to specific configuration needs and hardware configuration requirements.

10 TEGAM Way • Geneva, Ohio 44041 • Phone: 440-466-6100 • Fax: 440-466-6110 • E-mail: tegamsales@aei.com • www.tegam.com