# ARTESYN 50 V 3 kW OPEN RACK V3 PSU

For 18 kW 1OU ORV3 Power Shelves

Advanced Energy's Artesyn introduces the ORV3 3 kW PSU for use in the Open Rack V3 Power System. The PSU is a single-phase AC to DC power supply that operates from nominal input voltage from 200 to 277 VAC and produces 50 V, 60 A (3 kW) DC output. Within the ORV3 1OU Power Shelf, six of the ORV3 rectifiers operate in parallel, current sharing mode to produce 15 kW of N + 1 redundant power. The ORV3 Power System features a narrow DC voltage range to eliminate oversize design and enable high efficiency, fixed ratio downstream DC to DC conversion.

# AT A GLANCE

|Total Output Power|3 kW|
|---|---|
|Input Voltage|180 to 305 VAC|
|Output Voltage|50.5 to 51 VDC|
|Mechanical Dimensions|73.5 x 525 x 40 mm (L x W x H)|
|Operating Temperature|-5°C to 45°C|

# KEY FEATURES

- Peak efficiency 97.5%
- Efficiency greater than 96.5% for 230 VAC to 277 VAC and 30% to 100% load range
- 200 VAC to 277 VAC nominal input voltage range
- Active + Droop current sharing
- Hot swappable
- Cooling via internal fan with speed control
- Modbus/PMBus communications
- Interface for monitoring and control
- Black box fault logging

EMC / SAFETY COMPLIANCE

- IEC EN 61000-4-5 CAT A surges
- EN 61000-3-2 Class A harmonics
- CISPR and FCC Part A EMC
- UL 60950
- IEC 60950
- IEC/EN/UL 62368-1
- SEMI F47 Compliance

©2023 Advanced Energy Industries, Inc.
---
# 50 V 3 kW OPEN RACK V3 PSU

# ELECTRICAL SPECIFICATIONS

|Absolute Maximum Ratings|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|Input Voltage|AC continuous operation|180|-|305|VAC|
|Maximum Output Power| |-|-|3|kW|
|Isolation Voltage|Input to outputs|-|-|-|V|
| |Input to safety ground| | | | |
|Ambient Operating Temperature| |-5|-|45|C|
|Storage Temperature| |-40|-|85|OC|
|Humidity (non-condensing)|Operating|10|-|90|%|
| |Non-operating|5|-|93|%|
|Altitude|Operating|0|-|3050|m|
| |Non-operating|0|-|12000|m|

|Input Specifications|Conditions|Min|Typ|Max|Unit| |
|---|---|---|---|---|---|---|
|Input Voltage| |-|180|200/277|305|VAC|
|Input AC Frequency|-|47|50/60|63|Hz| |
|Input AC Start-up Voltage|-|-|178|-|VAC| |
|Input AC Undervoltage Lockout Voltage| |-|-|172|-|VAC|
|Fuse|Phase and return lines|25|-|-|kA| |
|TON_noBBU| |-|1|-|4.5|s|
|TON_BBU| |-|1|-|8|s|
|T-Max_ON_noBBU|-|6|-|7.5|s| |
|T-Max_ON_BBU|-|9.5|-|11.0|s| |
|Inrush Current| |-|-|30|A| |

|Hold Up Time1|200 to 277 VAC input|-|20|-|ms|
|---|---|---|---|---|---|
| |100% Load|5% to 10% load|-|15|%|
|iTHD|10% to 30% load|-|10|%| |
| |30% to 100% load|-|5|%| |
| |10% to 30% load VIN < 250V|0.95|-|-|%|
|Power Factor|10% to 30% load VIN > 250V|0.90|-|-|%|
| |30% to 100% load|0.98|-|-|%|

Note 1 - Refer to PSU-BBU Transition.

Note 2 - At 30% to 100% load, peak 230, 240, 277 Vac input, the minimum efficiency is 97.5%. At 30% to 100% load, 230, 240, 277 Vac input, the minimum efficiency is 96.5%. At 30% to 100% load, peak 208Vac input, the minimum efficiency is 96.5%. At 30% to 100% load, 208Vac input, the minimum efficiency is 95.5%. At 10% to 30% load, 208 to 277 Vac input, the minimum efficiency is 94%.

# advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

# ELECTRICAL SPECIFICATIONS

|Electrical Specifications|Conditions|Min|Nom|Max|Unit|
|---|---|---|---|---|---|
|Set Point|50% Load|50.625|50.750|50.875|VDC|
|Output Current| |-|-|60|A|
|Ripple & Noise|20MHz bandwidth|-|-|500|mVpp|
|VO Dynamic Response|10% min load|-|-|-| |
|VO Dynamic Response|0 to 10 mF output cap.|-|-|-| |
|Regulation and Droop characteristics|Dynamic load @ 20Hz|-|3|-|ms|
|Current Sharing Accuracy|50% Load|-5|-|+5|%|
|Output Rise Time| |-|60|-|ms|
|Short circuit protection (SCP)|If the rectifier voltage is lower than 10 V (short circuit condition), the rectifier shuts off immediately. No component will damage. The protection is hiccup mode. It tries to restart 5 times (2 second off, 200 ms on) and then locks out.| | | | |
|Overcurrent protection (OCP)|If a PSU is overloaded higher than the values listed below, it will “softly shut down”, meaning reduce its voltage by 3 V and wait for 6 ms (to give enough time for BBU to take over). If overload is still there, PSU can shut down. After an overload fault, PSUs will retry to sync together and turn on once every 5 s.| | | | |
|Overvoltage protection (OVP)|The rectifier will shut down for DC output voltage exceeding 52.5 V and the reacting time will not exceed 200 ms. For DC output voltage will never exceed 54 V (fast OVP).| | | | |
|Overtemperature protection (OTP)|The rectifier employ over temperature protection for both ambient over temperature and internal thermal temperature to protect the rectifier. The rectifier will shut down under over temperature condition and recover after certain period after the over temperature condition is removed.| | | | |

The OTP circuit incorporate built in hysteresis such that the power supply does not oscillate on and off due to temperature recovering condition. The OTP event shall be reported as a fault condition.

Note 1 - For surge current capabilities, see Pulse Load Operation.

Note 2 - Compliance will be verified using a 0.1 uF capacitor connected locally to the oscilloscope probe tips during this measurement.

advancedenergy.com 3
---
# 50 V 3 kW OPEN RACK V3 PSU

# PULSE LOAD OPERATION

PSU voltage should drop by 3V after its holdup energy is lost by 50% or 30J. Here, 24J or 40% of holdup energy is allocated for pulse power. As a result, PSU should meet the following pulse power envelope shown below without triggering BBU (reducing voltage by 3 V, which happens when holdup energy is reduced by 50%).

|Pulse step|Positive Half| |One Cycle or Period| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Allowable peak power step|40.00|20.00| | | | | | | | | | | |
|L|10.00|8.00| | | | | | | | | | | | |
| |6.00| | | | | | | | | | | | | |
| |2.00|3.00|4.00|5.00|6.00|7.00|8.00|9.00|10.00|110%|120%|130%|140%|150%|

In order to meet the Pulse power requirements as the graph above, the dc-dc converter should meet the following absolute pulse power requirement as shown below. This graph comes from the worst case of Pstart as 100%.

| | |dc-dc converter pulse power requirement| | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| |80.00| | | | | | | | |
| |60.00| | | | | | | | |
| |40.00| | | | | | | | |
| |20.00| | | | | | | | |
| |0.00|110%| |120%|130%|140%| |150%| |

advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

PSU-BBU TRANSITION

Graph below shows the PSU requirement to transition to BBU in case of AC outage. PSU voltage should drop by 3V after its holdup energy is lost by 50% or 30J.

|Load Power|Holdup Time (ms)|Time Before 3V Drop (ms)|Remaining Time After 3V Drop (ms)|
|---|---|---|---|
|100%|20.00|10.0|9.0|
|110%|18.18|9.1|8.1|
|120%|16.67|8.3|7.3|
|130%|15.38|7.7|6.7|
|140%|14.29|7.1|6.1|
|150%|13.33|6.7|5.7|

In case that AC voltage is available, but constant overload of up to 150% happens, PSUs will drop voltage by 3 V per the scheme above and share power with BBUs. PSUs will retry to sync together and increase the voltage once every 5 s.

Note1: all numbers with +/- 0.25% accuracy.

Note2: PSU and BBU voltage droop is 0.5V for 0-100% load.

Note3: BBU is triggered after Vbus is <48V for 20ms and starts up within 2ms (4ms total).

Note4: if BBU current <0.1A and Vbus >48.5V for 200ms, BBU goes to the standby mode.

Note5: PSU hold-up energy is 60J for loads up to 150%.

Note6: PSU 3V drop should occur after its hold-up energy is lost by 50%. This can be done by setting proper trigger value on the PSU PFC bulk voltage.

Note7: PSU 3V drop fall time is 1ms (3V/ms).

Per the scheme above, for the worst case that AC outage and pulse power happens at the same time (and pulse power remains constantly), PSU will transition to BBU seamlessly as calculated in the table above.

advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU PROTECTION

# Input Over Current Protection

The rectifier will incorporate primary fusing on both phase and return lines for input over-current protection to meet product safety requirements. Fuses shall be selected to prevent nuisance trips. Fuse may be internal to unit and need not be user serviceable. AC inrush current will not cause the fuse to blow under any conditions. No rectifier operating condition will cause the fuse to blow unless a component in the rectifier has failed. This includes DC output overload and short-circuit conditions. Fuse will be approved by UL for an interrupt rating of at least 25 kA.

PSU fuse will be in coordination with datacenter Tapbox breaker curve as given below.

NEC breakers are 20 and 30 A (two ac feeds go to the power shelf – one PSU per input ac phase feed).

IEC breaker is normally 32 A (one ac feed goes to the power shelf – two PSUs per input ac phase feed). (Ignore 16A breaker.)

|CURRENT IN AMPERES|Breaker Type|
|---|---|
|1000|ABB T1N|
|100|SQD QOU330|
|70-50|ABB 5203KZ0|
|Setros Ptuse|SQD C60N|
|EATON FD 30A|EATON FAZ16 pole|
|EATON FD 20A|EATON FAZ10k|

Tap Box Breakers tcc Ref: Voltage - 480V Current in Amps

# Input Over Voltage and Under Voltage Protection

The rectifier contain protection circuitry such that application of an input voltage below the minimum specified in section "Input Specification" on page 2 will not cause any damage to the rectifier and “softly shuts down” while operating. The rectifier will “softly shut down” if the input voltage is over 345 V for 20 ms or 309 V for 50 ms as shown in the graph below.

|VRMS|Time|Action|
|---|---|---|
|345|20 ms|Ok to trip|
|309|50 ms| |

advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

# PROTECTION

Output Power / Current Protection

If a PSU is overloaded higher than the values listed below, it will “softly shut down”, meaning reduce its voltage by 3 V and wait for 6 ms (to give enough time for BBU to take over and then turn off output.). If overload is still there, PSU will shut down. After an overload fault or in case of 3 V drop if there is no overload, PSUs will retry to sync together and turn on once every 5 s.

- Average power more than 3.45 kW for 10 s.
- Average power more than 3.6 kW for 100 ms.
- Repetitive pulse power more than the pulse power envelope specified (up to 150% load).

Constant Current mode will be triggered at 155% load. Output reduce voltage by 3 V if any of the conditions below are met:

- Constant current mode dwell for 10 ms.
- Output droops &lt; 48.5 V due to constant current mode.

Output Short Protection

The rectifier includes short-circuit protection to protect the rectifier and attached load in the case of an output short-circuit or other output overload condition.

If the rectifier voltage is lower than 10 V (short circuit condition), the rectifier shuts off immediately. No component damage. The protection will be implemented with a hiccup mode. it tries to restart 5 times every 5 s and then locks out. PSUs will sync using sync_start after shut down to power up together.

Over Temperature Protection

The rectifier employ over temperature protection for both ambient over temperature and internal thermal temperature to protect the rectifier. The rectifier will “softly shut down” under over temperature condition and recover after certain period after the over temperature condition is removed. The OTP circuit incorporate built in hysteresis such that the power supply does not oscillate on and off due to temperature recovering condition. The OTP event will be reported as a fault condition.

# TIMING

Random Timer and Synchronization

Under any conditions of dissipative load, capacitive load, temperature, with or without backup voltage connected to the PSU, Max time for PSU to be “power-up ready” after AC voltage starts is 2.5 s.

After “power-up ready”:

- When there is no DC voltage on the bus (first AC turn on) the power shelf will be randomized with 0 to 2 s window to give each power shelf a random turn-on time (six PSUs turn-on is synchronized).
- When there is DC voltage on the bus higher than 44 V for 0.1 second (BBU is discharging), the power shelf will be randomized with 0 to 5.5 seconds window to give each power shelf a random turn-on time (six PSU turn-on is synchronized).

The power shelf will trun on with only 1 PSU inserted into any slot.

Note: The random numbers above will be dynamically generated immediately after each AC recycle, and not generated one time and then stored in the EEPROM for future usages.

|Item|Description|Min|Max|Unit|
|---|---|---|---|---|
|T_power-up_ready|Time for PSU to be power-up ready|1.0|2.5|s|
|T_random_noBBU|0 to 2 seconds initial turn on random delay without BBU discharging|0|2.0|s|
|Ton_noBBU|Time 51 VDC turns on after shelf receives AC input without BBU discharging.|1.0|4.5|s|
|T_random_BBU|0 to 5.7 seconds turn on random delay after BBU discharging|0|5.5|s|
|Ton_BBU|Time 51 VDC turns on after shelf receives AC input with BBU discharging.|1.0|8.0|s|
|Tsync|After all PSUs in the shelf are ready to start till when 51 VDC will start|2.0|5.0|ms|
|Tmax_ON_noBBU|Max PSU turn-on time without BBU in case of sync failure|6.0|7.5|s|
|Tmax_ON_BBU|Max PSU turn-on time with BBU in case of sync failure|9.5|11.0|s|

advancedenergy.com 7
---
# TRANSITION AND SYNCHRONIZATION REQUIREMENTS

# Start-up (0 V to 51 V) Transition Procedure

|1)|Each PSU sets its uC Digital output signal (Do_SyncReady_L) to low when the PSU is ready to turn on the output.|
|---|---|
|2)|Only PSU in SLOT #1 generates random timer and set Do_SyncReady_L to low when ready and random timer is finished.|
|3)|The PSUs will turn on the output when the uC Digital input sync signal (DI_Sync_H) is high.|
|4)|If DI_Sync_H kept stuck low for 3 s more than the max random timer limit (which is 2 s without BBU and 5.5 s with BBU), the PSU will turn on immediately.|
|5)|If PSU1 is not installed or its Do_SyncReady_L stuck low, the other PSUs shall turn on when the DI_Sync_H is high. In this case random timer doesn't exist.|

Please refer to section "Pulse Load Operation" on page 4 for the timing and constant current value requirements during the cold startup.

|PSU1|High @ PSU not ready| | | | |
|---|---|---|---|---|---|
| | | | |Do_SyncReady_L|High @ start-up|
| | | | | |DI_Sync_H|
|PSUx|High @ PSU not ready| | | | |
| | | | |Do_SyncReady|High @ start-up|
| | | | | |DI_Sync_H|

# 48 V to 51 V Transition Procedure

|1)|When PSU enters 48V output mode, it sets “Do_SyncReady_L” signal to HIGH.|
|---|---|
|2)|If there is no over power or over current condition for 5s, each PSU sets “Do_SyncReady_L” signal to LOW.|
|3)|If signal “DI_Sync_H” is HIGH (HIGH when all PSUs in parallel ready to adjust), then change constant current level to 120% and adjust output from 48 V to 51 V.|
|4)|If the signal “DI_Sync_H” is stuck LOW for 5 s, the PSU shall adjust its output from 48 V to 51 V.|
|5)|If the PSU output did not reach 51 V in 5s, then it return to 48 V mode, set constant current level to 155%, and go to step 1).|

Refer to diagram below that covers both 48 V to 51 V and 51 V to 48 V transitions.
---
# 50 V 3 kW OPEN RACK V3 PSU

# TRANSITION AND SYNCHRONIZATION REQUIREMENTS

51V to 48V and 48V to 51V Transition FlowchartPSU hold-up energy is lower than 50%Average power more than 45kW for 10s51V stateConstant Current = 1559Average power more than 6kW for 100msAdjust Vout to 48VOutput able to rise regulation in less than 5s?Adjust Vout to 51VChange constant current level to 12096

# 51 V to 48 V Transition Procedure

This transition and conditions associated with it was explained in section "over power/current protection" on page 7 and section "PSU-BBU transition" on page 5. No synchronization is needed in this case. Refer to diagram above that covers both 48 V to 51 V and 51 V to 48 V transitions.

# CONTROL AND MONITORING SIGNALS

The Power shelf includes a slot for a power shelf management controller (PMC) to monitor and control various rectifier parameters. The PMC is connected to rack management controller or facility level monitoring through a monitoring & control interface.

If the PMC fails or is not provided, the power system is able to operate normally. The PMC is powered from the 48 V bus directly.

advancedenergy.com 9
---
# 50 V 3 kW OPEN RACK V3 PSU

# COMMUNICATIONS

The rectifiers can communicate on PMBus (up to 100 kbps) and ModBus (up to 115 kbps).

At default, Modbus is active and PMBus is hardware only. Contact AdvancedEnergy to switch to PMBus communication.

The software interface is operational when the AC is present or when the DC output bus is powered up by other power sources. The software provides below functions:

# Fault conditions

- Last power failure event
- Rectifier failure

# Read:

- Voltage in
- Current in
- Voltage out
- Current out
- Temperatures
- Fan speeds
- Power out
- Power in
- Position
- Serial Number
- Manufacturer part number
- Hardware revision
- Firmware revision

# Write:

- Clear faults

# Upgrades:

- Upgrade firmware image (s)

# Firmware Upgrade

The interface shall allow the user to re-flash firmware on the device. Firmware upgrade shall result in no power interruption on the shelf level (the unit being upgraded can go offline.) Upgrades can be done 1 rectifier at a time.

The PSU FW shall maintain regulation on the output during Send, Install and verification of the new FW, and only require a soft reset (that may reset the output for a short period in a few seconds).

PSU output voltage interruption due to FW upgrade will be less than 10 s.

advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

# COMMUNICATIONS

Reporting Accuracy

Accurate reporting of input power (power factor, input current, input current harmonics and voltage) and output power (output current and voltage) readings shall be reported via communication system at all rated voltage. The accuracy will be maintained across the operating temperature range and between 200 VAC and 305 VAC.

|Parameter|Load|Accuracy|
|---|---|---|
|AC Input Power|&lt;10%|±25W|
| |10% to 20%|±5%|
| |20% to 100%|±3%|
|AC Input Current|&lt;10%|±0.5A|
| |10% to 20%|±2%|
| |20% to 100%|±1%|
|AC Input Current THD (Error difference not %)|10% to 20%|±2%|
| |20% to 100%|±1%|
| |&lt;10%|±0.1|
|Power Factor (Error difference not %)|10 to 20%|±0.025|
| |20 to 100%|±0.01|
|AC Input Voltage|0 to 100%|±1%|
|Output Voltage|0 to 100%|±0.5%|
| |10 to 20%|±10%|
|Output Current|20 to 50%|±5%|
| |50 to 100%|±1%|
|Output Power|&lt;10%|±25W|
| |10 to 20%|±4%|
| |20 to 100%|±2%|

advancedenergy.com 11
---
# 50 V 3 kW OPEN RACK V3 PSU

# BLACKBOX FUNCTION

For the following section please refer to the latest Communication Specification for detailed information.

The black box function store key important data to be used when a fault occurs.

- Store data in memory and can withstand several read/write cycles
- PSU can store failure data before the PSU turns off/fails even in catastrophic failure events both on primary and secondary side. Hold up time of the blackbox microcontroller can store all the information and then shutdown.
- Last 4 events stored in memory.
- AC input current, AC input voltage, Input Power, Power factor, iTHD, DC output voltage, DC output current,
- Temperature readings, fan Speed, input voltage, output voltage, bulk voltage, various error codes from all the different converters (OTP, OVP, OCP, UVP), and warnings.
- BBU signals at time of failure (fail, charge_enable, BBU voltage, etc)
- Total run time of PSU
- Run time since last turn on
- Real time stamping
- Number of AC power cycles
- Number of AC outages (can be determined by going into backup without counting the battery test conditions)

Power supply event data is saved to the Black Box for the following events that:

- Any events that caused the Main Output to shut down:
- - Main Output over voltage fault
- Main Output under voltage fault
- Main Output over current fault
- Main Output short circuit fault
- Fan failure
- Over temperature fault

Any events that caused the AC input to be bad:

advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

|ENVIRONMENTAL SPECIFICATIONS| | |
|---|---|---|
|Temperature range|Operational: -5°C to +45°C; Non-operational: -40°C to +85°C| |
|Humidity|Operational: 10% to 90% non-condensing; Non-operational: 5% to 93% non-condensing| |
|Altitude|Operational: 3050 m; Non-operational: 12000 m| |

|Shock|EN 60068-2-6 and 60068-2-27 12g Non-Operating / 6g Operating|
|---|---|
|Vibration|EN 60068-2-6 and 60068-2-27 1g Non-Operating / 0.5g Operating|
|Fan noise|&lt; 85 dBA, 100% load|

# THERMAL

Airflow Direction: Front-to-back

Fan Speed Control: The fan speed varies depending on ambient temperature and load and is optimized to maintain a temperature difference of 22°F nominally across 30 to 85% load range and up to 35°C inlet/ambient and 3050 m (10,000 ft) above sea-level. The benefit is reduced fan power usage.

System Back-pressure: Front-to-back airflow maintain for system backpressure up to minimum 0.3 inches of water.

Fan Failure: If a fan fails, the rectifier will indicate the failure with a signal that will be reported via software as well as an LED indicator on the front panel. The rectifier will not shut down because of a failed fan and will only shut down if there is a fault, ie. over-temperature fault.

Rectifier Thermal Monitoring: Inlet temperature, exhaust temperature, fan speed and fan fail signals are reported via communications. See Communications Section for details.

advancedenergy.com 13
---
50 V 3 kW OPEN RACK V3 PSUMECHANICAL - PSUEkdS20 ,0_8LaTch To conhecToRPAODUCL LABELFOLOABLE HandLle.dDFIA 4DETAIL At2:|)35151219>10.51JiLBL WE;ahber14 advancedenergy.com
---
# 50 V 3 kW OPEN RACK V3 PSU

MECHANICAL - POWER SHELFINPUT CONNECTOR7 Pin INPUT CONNECTORPosmroxcSpjorsssinzodi-AA-2238
PRODUCT LABEL

DATATRD LABEL

SCALE US

BLOCKER

ASCETTAG

New F

SEETiaL=

DET

537 ,0.5

GEE DETAL A

Ktttp

advancedenergy.com 15
---
50 V 3 kW OPEN RACK V3 PSUMECHANICAL - PMI3450316   advancedenergy.com
---
|Pin|Name|Description|
|---|---|---|
|P1 & P2|48V positive| |
|P3 & P4|48V return| |
|LP1|Earth| |
|LP2|AC phase| |
|LP3|AC phase| |
|P1|PSU_A0|Address 0 - PSU ID A0, Internal pull up 10k to 3.3V|
|P2|PSU_A1|Address 1 - PSU ID A1, Internal pull up 10k to 3.3V|
|P3|PSU_A2|Address 2 - PSU ID A2, Internal pull up 10k to 3.3V|
|P4|PSU_A3|Address 3 - PSU ID A3, Internal pull up 10k to 3.3V|
|P5| | |
|Q1|Ground| |
|Q2|Alert|Logic “low”= Fault or Warning, Logic “High”=OK, Internal pull up 10k to 3.3V PSU Alert|
|Q3|Reset_Latch_Fault|Logic "high" for 1 to 2s = clear faults and start PSU to operate if not working due to a fault. Should be enabled by SW. Internal pull down 10k resistor.|
|Q4|RS485_addr0|Internal pull up 100k to 3.3V|
|Q5|RS485_addr1|Internal pull up 100k to 3.3V|
|U1|RS485_addr2|Internal pull up 100k to 3.3V|
|U2|BKP|No pull up or pull down, Open collector output. All PSUs Ored together.|
|U3|PSKILL (Short Pin)|Logic “Low”= Output Turn on, Logic “High”= Output Turn off Quick shut down Output, mitigate hot unplug arcing. Internal pull up 10k to 3.3V|
|U4|RS485A| |
|U5|RS485B| |
|V1|Ground| |
|V2|I2C_SDA|I2C Data|
|V3|I2C_SCL|I2C Clock|
|V4|Ground|I2C ground|
|V5|PLS (power loss siren)|No pull up or pull down, Open collector output. All PSUs Ored together.|
|Y1|ISHARE|Main Output current share bus|
|Y2|SYNC_STOP|Internal pull up 10k to 3.3V|
|Y3|SYNC_START|Synchronizing turn-on main output, Internal pull up 10k to 3.3V|
|Y4|VOUT_SEL|Logic “Low”= Set Output 48V, Logic “High”=Set Output 51V, Internal pull up 10k to 3.3V, Default Output is 51V|
|Y5|Ground| |
---
# 50 V 3 kW OPEN RACK V3 PSU

|Device|Connector|Mating Connector|Description|
|---|---|---|---|
|PSU|FCI: 10127396-01U1520LF (PwrBlade ULTRA HD)|FCI: 1027400-01U1520LF (PwrBlade ULTRA HD)|I/O Connector|

# LED

The PSU has a single blue and single amber LED mounted near the PSU handle for accessibility. Following are power supply LED states:

|LED|Status|Description| |
|---|---|---|---|
| |Blue|Blinking Blue @ 4 Hz frequency|Sync Start State, PSU is ready to turn on its output and awaiting the sync Start signal|
| |Solid Blue|51 V is ON and available| |
|Off| |51 V output off| |
| |Amber|Blinking Amber @ 4 Hz frequency:|Bootloading|
| |Solid Amber|Primary/Secondary/Fan/bootloading Failure and/or loss of DC output (refer to PSU PMbus registers for specific failures)| |
|Off| |fault NOT present/condition 1 and 2 are false| |

Note 1 - Toggling AC input power will reset the solid/blinking amber fault light but will come up again if faults re-occur.

Note 2 - Only one of the 3 conditions per LED will be applied at all time.

# ORDERING INFORMATION

|Model|Input|Output|Description|
|---|---|---|---|
|700-015234-0100|1 Phase AC, 180 to 305 VAC, 50 to 60 Hz|50 V 60 A|ACDC-ORV3-3000 W, ORV3 PSU|
|700-015746-0100|3 Phase AC, 200/480 V, 50 to 60 Hz|50 V 300 A|ACDC-ORV3-1OU-18 kW, ORV3 Power Shelf - Single Whip|
|700-015235-01001|3 Phase AC, 200/480 V, 50 to 60 Hz|50 V 300 A|ACDC-ORV3-1OU-18 kW, ORV3 Power Shelf - Dual Whip|
|700-015718-0100| | |PMI|

Note 1 - Shelves are related products (not covered by this data sheet). Refer to ORV3 power shelf data sheet.

18 advancedenergy.com
---
ABOUT ADVANCED ENERGY

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

TRUST

For international contact information, visit advancedenergy.com.

powersales@aei.com (Sales Support)

productsupport.ep@aei.com (Technical Support)

+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2023 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, AE® and Artesyn™ are U.S. trademarks of Advanced Energy Industries, Inc.

ENG-50 V 3 kW OPEN RACK V3 PSU.02.20.23