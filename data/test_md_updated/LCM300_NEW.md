# Energy Advanced TECHNICAL REFERENCE NOTE

# ARTESYN LCM300 SERIES 300 Watts Bulk Front End

PRODUCT DESCRIPTION

Advanced Energy’s Artesyn LCM300 series provide for a very wide range of AC-DC embedded power requirement. Featuring high build quality with robust screw terminals, long life, and typical full-load efficiency of greater than 91%, these units are ideal for use in industrial and medical applications. They are backed by a comprehensive set of industrial and medical safety approvals and certificates. Variable-speed ‘Smart Fans’ draw on software controls developed by Advanced Energy to match fan speed to the unit’s cooling requirement and load current. Slowing the fan not only saves power but also reduces wear, thus extending its life.

SPECIAL FEATURES

- 310W output power (360W at 45OC for 24V and 36V models)
- Low cost
- 1.61” x 4.0” x 7.0”
- 7.1 watts per cubic inch
- Industrial/medical safety
- -40 OC to +70 OC with derating
- Optional 5V@2A housekeeping
- High efficiency: 91% @ 230Vac
- Variable speed “smart fans”
- DSP controlled
- PMBus compliant
- Conformal coat optional
- ±20% adjustment range
- Margin programming
- OR-ing FET
- EMI class B
- EN61000 Immunity

COMPLIANCE

- EMI Class B
- EN61000 Immunity
- RoHS 3
- PMBus

SAFETY

- UL 62368-1
- TUV 62368-1
- CSA 62368-1
- China CCC
- CB Report
- UKCA Mark

# AT A GLANCE

|Total Power|300 Watts|
|---|---|
|Input Voltage|90 to 264 Vac|
|# of Outputs|Single|
|Power Management|PMBus|

©2024 Advanced Energy Industries, Inc.
---
# MECHANICAL SPECIFICATIONS

|MODEL NUMBERS|Standard Output Voltage|Minimum Load|Maximum Load|Adjustment Range|Maximum Power|
|---|---|---|---|---|---|
|LCM300L|12Vdc|0A|25.0A|9.6-14.4V|310W|
|LCM300N|15Vdc|0A|20.0A|14.25-19.5V|310W|
|LCM300Q|24Vdc|0A|14.5A|19.2-28.8V|360W|
|LCM300U|36Vdc|0A|9.7A|28.8-43.2V|360W|
|LCM300W|48Vdc|0A|6.3A|43.0-60.0V|310W|

Note 1 - When operating temperature does not exceed 45°C, the power supply can continuously deliver up to 360W, includes 5V@2A standby power if the optional standby output is available.

# Options

Ordering information about LCMXXXXY-A-B-C-###:

A- Input Termination(T - Terminal Block)

B- Acoustic Noise(Blank = Standard)

C- Option Codes:

Blank = No options

1 = Conformal coat

4 = 5V Standby

5 = Opt 1 + 4

Rev. 06.26.24_#3.2

advancedenergy.com
---
# MECHANICAL SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

**Absolute Maximum Ratings**
|Parameter|Model|Symbol|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Input Voltage|All models|VIN,AC|90|-|264|Vac|
| |All models|VIN,DC|127|-|374|Vdc|
|Maximum Output Power (Main + Stand-by)|LCM300L|PO,max|-|-|310|W|
| |LCM300N|PO,max|-|-|3101|W|
| |LCM300Q|PO,max|-|-|3601|W|
| |LCM300U|PO,max|-|-|360|W|
| |LCM300W|PO,max|-|-|310|W|
|Isolation Voltage(Qualification)|All models| |-|-|4000|Vac|
| |All models| |-|-|2500|Vdc|
| |All models| |-|-|500|Vdc|
|Isolation Voltage(Production)|All models| |-|-|1800|Vac|
| |All models| |-|-|1800|Vac|
| | | |-|-|200|Vac|
|Ambient Operating Temperature|All models|TA|-40|-|+702|OC|
|Storage Temperature|All models|TSTG|-40|-|+85|OC|
|Humidity (non-condensing)|All models| |20|-|90|%|
| |All models| |10|-|95|%|
|Altitude|All models| |-|-|10,000|feet|
| |All models| |-|-|30,000|feet|

Note1 - Deliver up to 360 watts when operating temperature does not exceed 45OC

Note2 - Line derating each output at 2.5% per degree C from 50OC to 70OC.

Rev. 06.26.24_#3.2 advancedenergy.com 3
---
# ELECTRICAL SPECIFICATIONS


|Parameter|Condition|Symbol|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Operating Input Voltage, AC|All|VIN,AC|90|115/230|264|Vac|
|Input AC Frequency|All|fIN,AC|47|50/60|63|Hz|
|Maximum Input Current|VIN,AC = 100Vac|IIN,max|-|-|5|A|
|No Load Input Current|VIN,AC = 90Vac|IIN,no-load|-|-|100|mA|
|No Load Input Power|VIN,AC = 90Vac|PIN,no-load|-|-|6|W|
|Harmonic Line Currents|All|THD|Per IEC1000-3-2| | | |
|Power Factor|IO = IO,max VIN,AC = 110Vac|PF|-|0.98|-| |
|Startup Surge Current (Inrush) @ 25OC|VIN,AC = 264Vac|IIN,surge|-|-|20|APK|
|Input Fuse|Internal, L and N 8A,250Vac rated|-|-|8|A| |
|Input AC Low Line Start-up Voltage|IO = IO,max|VIN,AC-start|80|-|90|Vac|
|Input AC Undervoltage Lockout Voltage|IO = IO,max|VIN,AC-stop|75|-|85|Vac|
|PFC Switching Frequency|All|fSW,PFC|64|-|76|KHz|
|Efficiency|VIN,AC = 230Vac IO = IO,max TA = 25OC, forced air cooling|η|-|91|-|%|
|Turn On Delay|VIN,AC = 90Vac IO = IO,max Resistive Load IEC test method|tTurn-On|-|-|3|Sec|
|Leakage Current to safety ground|UL test method|IIN,leakage|-|-|0.3|mA|

Rev. 06.26.24_#3.2 advancedenergy.com 4
---
# ELECTRICAL SPECIFICATIONS

# Output Specifications

|Parameter| |Condition|Symbol|Min|Typ|Max|Unit| |
|---|---|---|---|---|---|---|---|---|
|Factory Set Voltage|LCM300L|IO = 0A|VO,Factory|23.88|24|24.12|V| |
|Output Adjust Range|LCM300Q|IO = 0A|VO|19.2|-|28.8|V| |
|Total Regulation|Inclusive of line, load temperature change, warm-up drift and dynamic load| |%VO|-2.0|-|+2.0|%| |
|Output Ripple, pk-pk|LCM300Q|See note 1, note 2 and note 3|VO| |-|-|240 mVPK-PK| |
|Output Current|LCM300Q| |IO|0|-|12.5|A| |
|Maximum Output Power, continuous|LCM300Q|All|PO,maxCC|0|-|360|W| |
|Ripple Switching Frequency| |All|fSW,DC-DC|115|-|125|KHz| |
|Hold Up Time| |See note 4|tHold-Up|20|-|-|mSec| |
|Dynamic Response - Peak Deviation|50% to 100% of IO,max load change| |±%VO|-|-|2|%| |
|Dynamic Response - Setting Time| |Slew rate = 1A/μs|ts|-|-|300|μSec| |
|Load Capacitance|Start up| |VO|0|-|1500|μF| |
|Load Capacitance|Start up| |VSB|0|-|270|μF| |
|Number of Parallel Units| |All| |-|-|-|10|Units|

Note 1 - Measure with a 0.1μF ceramic capacitor in parallel with a 10μF tantalum capacitor using a 20MHz bandwidth limited oscilloscope.

Note 2 - In case if voltage is adjusted above nominal setting, ripple expected is 1% of output voltage.

Note 3 - Ripple noise at extreme low temperature (below 0°C) is expected higher until unit get stabilized due to ESR change of the E‐Caps.

Note 4 - Adjusting the output to higher tolerance (i.e. 28.8V which is the +20% adjustment range of 24V Nominal) will give a typical hold up of 10msec.

Rev. 06.26.24_#3.2 - advancedenergy.com
---
# ELECTRICAL SPECIFICATIONS


|Label|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|T1|Delay from AC Input being applied to main output voltages being within regulation.|-|-|3000|mSec|
|T2|There is a continuous ramp of output voltage from 10% to 95% of its final set point within the regulation band, while loaded.|-|-|300|mSec|
|T3|Delay from main output within regulation to G_DCOK_C signal assertion (going low).|-|-|500|mSec|
|T4|Delay from loss of AC input to G_ACOK_C going to high.|-|-|10|mSec|
|T5|Hold up time - time all output voltages, including VSB, stay within regulation after loss of Input AC. Main output set at nominal voltage setting.|20|-|-|mSec|
|T6|Delay from G_DCOK_C signal de-assertion (going high) to main output dropping to less than the lower trimming range (-20% of the nominal output).|1|-|-|mSec|
|T7|Delay from INH_EN active to output voltages within regulation limits.|-|2000|-|mSec|
|T8|Delay from INH_EN de-active to G_DCOK_C de-asserted (going high).|-|-|2|mSec|

Rev. 06.26.24_#3.2 advancedenergy.com 6
---
# LCM300

# ELECTRICAL SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

# System Timing Diagram

|AC Input|AC on/off cycle|
|---|---|
|ACOK_C|-PSON on/off cycle - PSON on/off cycle|
|INH EN|T1 7 T2 4 ~T5|
|DCOK_C| |

Rev. 06.26.24_#3.2 advancedenergy.com 7
---
# ELECTRICAL SPECIFICATIONS

|LCM300L Performance Curves|LCM300L Turn-on delay via AC mains|LCM300L Turn-on delay via INH_EN|
|---|---|---|
|Vin = 90Vac Load: IO = 25A (12V), ISB = 2A (5V)|Vin = 90Vac Load: IO = 25A (12V), ISB = 2A (5V)| |
|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: INH_EN Ch 3: VO Ch 4: G_DCOK_C| |

|LCM300L Hold-up Time|LCM300L Hold-up Time|
|---|---|
|Vin = 90Vac / 47Hz / 0O Load: IO = 25A (12V), ISB = 2A (5V)|Vin = 264Vac / 60Hz / 0O Load: IO = 25A (12V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|

|LCM300L Output Voltage Startup Characteristic|LCM300L Turn Off Characteristic via INH_EN|
|---|---|
|Vin = 90Vac Load: IO = 25A (12V), ISB = 2A (5V)|Load: IO = 25A (12V), ISB = 2A (5V)|
|Ch 1: VO Ch 2: G_DCOK_C|Ch 1: INH_EN Ch 2: VO Ch 3: G_DCOK_C|

Rev. 06.26.24_#3.2 advancedenergy.com 8
---
# LCM300 Electrical Specifications

|Efficiency (%)|Output Voltage (V)|
|---|---|
| |LCM300|

# LCM300L Performance Curves

Figure 7: LCM300L Transient Response - VO Deviation

- 50% to 100% load change
- 1A/uS slew rate Vin = 230Vac
- Ch 1: VO
- Ch 2: IO

Figure 8: LCM300L Transient Response - VO Deviation

- 100% to 50% load change
- 1A/uS slew rate Vin = 230Vac
- Ch 1: VO
- Ch 2: IO

# LCM300L Efficiency Curves

Output Current (A)02.557.51012.51517.52022.525

Figure 9: LCM300L Efficiency Curve @ 25OC

Figure 10: LCM300L Ripple and Noise Measurement

- Vin = 90Vac
- Load: IO = 25A (12V), ISB = 2A (5V)
- Ch 1: VO

# LCM300L Vprog Curves

Prog Voltage (V)123456

Figure 11: LCM300L Output Voltage Adjustment by Vprog @ 25OC

- 115Vac
- Loading: Io = 0A (12V), ISB = 0A (5V)

Rev. 06.26.24_#3.2 advancedenergy.com 9
---
# ELECTRICAL SPECIFICATIONS

|Figure 12: LCM300N Turn-on delay via AC mains|Figure 13: LCM300N Turn-on delay via INH_EN|
|---|---|
|Vin = 90Vac Load: IO = 20A (15V), ISB = 2A (5V)|Vin = 90Vac Load: IO = 20A (15V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: INH_EN Ch 3: VO Ch 4: G_DCOK_C|

|Figure 14: LCM300N Hold-up Time|Figure 15: LCM300N Hold-up Time|
|---|---|
|Vin = 90Vac / 47Hz / 0O Load: IO = 20A (15V), ISB = 2A (5V)|Vin = 264Vac / 60Hz / 0O Load: IO = 20A (15V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C|

|Figure 16: LCM300N Output Voltage Startup Characteristic|Figure 17: LCM300N Turn Off Characteristic via INH_EN|
|---|---|
|Vin = 90Vac Load: IO = 20A (15V), ISB = 2A (5V)|Load: IO = 20A (15V), ISB = 2A (5V)|
|Ch 1: VO Ch 2: G_DCOK_C|Ch 1: INH_EN Ch 2: VO Ch 3: G_DCOK_C|

Rev. 06.26.24_#3.2 advancedenergy.com 10
---
# LCM300

# ELECTRICAL SPECIFICATIONS

Efficiency (%)
Output Voltage (V)

# LCM300N Performance Curves

|Figure 18: LCM300N Transient Response - Vo Deviation|Figure 19: LCM300N Transient Response - Vo Deviation|
|---|---|
|50% to 100% load change 1A/uS slew rate Vin = 230Vac Ch 1: VO Ch 2: IO|100% to 50% load change 1A/uS slew rate Vin = 230Vac Ch 1: VO Ch 2: IO|

# LCM300N Efficiency Curves

| |Output Current (A)|
|---|---|
|Figure 20: LCM300N Efficiency Curve @ 25OC| |
|x 90Vac 115Vac 230Vac 264Vac| |
|Loading: IO_main = 10%IO,max increment to 20A, ISB = 0A (5V)| |

# LCM300N Vprog Curves

| |Prog Voltage (V)|
|---|---|
|Figure 22: LCM300N Output Voltage Adjustment by Vprog @ 25OC x 115Vac| |
|Loading: IO = 0A (15V), ISB = 0A (5V)| |

Rev. 06.26.24_#3.2 advancedenergy.com 11
---
# ELECTRICAL SPECIFICATIONS

|LCM300Q Performance Curves|T-Fed|~Fed|
|---|---|---|
| |16.52|2.00|
|3.28|OC|2998 IS/s|
|216.38 ns|1 1.6214 Iiz|50 kS/s|
|DC 3.6 V| |DC 12.8|
|STOPPED| |STOPPED|

Figure 23: LCM300Q Turn-on delay via AC mains

Vin = 90Vac Load: IO = 12.5A (24V), ISB = 2A (5V)

Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C

| |LCM300Q Turn-on delay via INH_EN| | |
|---|---|---|---|
|Vin = 90Vac|Load: IO = 12.5A (24V), ISB = 2A (5V)| | |
|Ch 1: AC Mains|Ch 2: INH_EN|Ch 3: VO|Ch 4: G_DCOK_C|

| |LCM300Q Hold-up Time| | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
|Vin = 90Vac / 47Hz / 0O| | |Load: IO = 12.5A (24V), ISB = 2A (5V)| | | | | | |
|Ch 1: AC Mains|Ch 2: VSB|Ch 3: VO|Ch 4: G_DCOK_C| | | | | | |

Figure 25: LCM300Q Hold-up Time

Vin = 264Vac / 60Hz / 0O Load: IO = 12.5A (24V), ISB = 2A (5V)

Ch 1: AC Mains Ch 2: VSB Ch 3: VO Ch 4: G_DCOK_C

|LCM300Q Output Voltage Startup Characteristic|Figure 28: LCM300Q Turn Off Characteristic via INH_EN|
|---|---|
|Vin = 90Vac Load: IO = 12.5A (24V), ISB = 2A (5V)|Load: IO = 12.5A (24V), ISB = 2A (5V)|
|Ch 1: VO Ch 2: G_DCOK_C|Ch 1: INH_EN Ch 2: VO Ch 3: G_DCOK_C|

Rev. 06.26.24_#3.2 advancedenergy.com 12
---
# LCM300

ELECTRICAL SPECIFICATIONS

LCM300Q Performance Curves

|Figure 29: LCM300Q Transient Response - VO Deviation|Figure 30: LCM300Q Transient Response - VO Deviation|
|---|---|
|50% to 100% load change 1A/uS slew rate Vin = 230Vac Ch 1: VO Ch 2: IO|100% to 50% load change 1A/uS slew rate Vin = 230Vac Ch 1: VO Ch 2: IO|

LCM300Q Efficiency Curves

|95.00|239mv|
|---|---|
|90.00| |
|85.00| |
|80.00| |
|75.00| |
|70.00|10 Av : 50 kS/s STOPPED|
|0|Output Current (A)|

Figure 31: LCM300Q Efficiency Curve @ 25OC
Figure 32: LCM300Q Ripple and Noise Measurement Vin = 90Vac Load: IO = 12.5A (24V), ISB = 2A (5V) Ch 1: VO

LCM300Q Vprog Curves

29272523211917

Figure 33: LCM300Q Output Voltage Adjustment by Vprog @ 25OC x 115Vac Loading: IO = 0A (24V), ISB = 0A (5V)

Rev. 06.26.24_#3.2 advancedenergy.com 13
---
# ELECTRICAL SPECIFICATIONS

|Figure 34: LCM300U Turn-on delay via AC mains|Figure 35: LCM300U Turn-on delay via INH_EN|
|---|---|
|Vin = 90Vac Load: Io = 8.4A (36V), ISB = 2A (5V)|Vin = 90Vac Load: Io = 8.4A (36V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: INH_EN Ch 3: Vo Ch 4: G_DCOK_C|

|Figure 36: LCM300U Hold-up Time|Figure 37: LCM300U Hold-up Time|
|---|---|
|Vin = 90Vac / 47Hz / 0O Load: Io = 8.4A (36V), ISB = 2A (5V)|Vin = 264Vac / 60Hz / 0O Load: Io = 8.4A (36V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|

|Figure 38: LCM300U Output Voltage Startup Characteristic|Figure 39: LCM300U Turn Off Characteristic via INH_EN|
|---|---|
|Vin = 90Vac Load: Io = 8.4A (36V), ISB = 2A (5V)|Load: Io = 8.4A (36V), ISB = 2A (5V)|
|Ch 1: Vo Ch 2: G_DCOK_C|Ch 1: INH_EN Ch 2: Vo Ch 3: G_DCOK_C|

Rev. 06.26.24_#3.2 advancedenergy.com 14
---
# LCM300

# ELECTRICAL SPECIFICATIONS

Efficiency (%)
Output Voltage (V)

# LCM300U Performance Curves

|Figure 40: LCM300U Transient Response - Vo Deviation|Figure 41: LCM300U Transient Response - Vo Deviation|
|---|---|
|50% to 100% load change Ch 1: Vo LCM300U Efficiency Curves|100% to 50% load change Ch 1: Vo LCM300U Efficiency Curves|
|1A/uS slew rate Vin = 230Vac Ch 2: Io|1A/uS slew rate Vin = 230Vac Ch 2: Io|

LCM300U Efficiency Curves95.0090.0085.0080.0075.0070.0065.0060.000 1 2 3 4 5 6 7 8 9Output Current (A)

|Figure 42: LCM300U Efficiency Curve @ 25OC|Figure 43: LCM300U Ripple and Noise Measurement|
|---|---|
|x 90Vac 115Vac 230Vac 264Vac Loading: Io_main = 10%Io,max increment to 8.4A, ISB = 0A (5V) Ch 1: Vo|Vin = 90Vac Load: Io = 8.4A (36V), ISB = 2A (5V) Ch 1: Vo|

LCM300U Vprog Curves454239363330271 2 3 4 5 6Prog Voltage (V)

Figure 44: LCM300U Output Voltage Adjustment by Vprog @ 25OCx 115Vac
Loading: Io = 0A (36V), ISB = 0A (5V)

Rev. 06.26.24_#3.2 advancedenergy.com 15
---
# ELECTRICAL SPECIFICATIONS

|Figure 45: LCM300W Turn-on delay via AC mains|Figure 46: LCM300W Turn-on delay via INH_EN|
|---|---|
|Vin = 90Vac Load: Io = 6.3A (48V), ISB = 2A (5V)|Vin = 90Vac Load: Io = 6.3A (48V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: INH_EN Ch 3: Vo Ch 4: G_DCOK_C|

|Figure 47: LCM300W Hold-up Time|Figure 48: LCM300W Hold-up Time|
|---|---|
|Vin = 90Vac / 47Hz / 0O Load: Io = 6.3A (48V), ISB = 2A (5V)|Vin = 264Vac / 60Hz / 0O Load: Io = 6.3A (48V), ISB = 2A (5V)|
|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|Ch 1: AC Mains Ch 2: VSB Ch 3: Vo Ch 4: G_DCOK_C|

|Figure 49: LCM300W Output Voltage Startup Characteristic|Figure 50: LCM300W Turn Off Characteristic via INH_EN|
|---|---|
|Vin = 90Vac Load: Io = 6.3A (48V), ISB = 2A (5V)|Load: Io = 6.3A (48V), ISB = 2A (5V)|
|Ch 1: Vo Ch 2: G_DCOK_C|Ch 1: INH_EN Ch 2: Vo Ch 3: G_DCOK_C|

Rev. 06.26.24_#3.2 advancedenergy.com 16
---
# LCM300

# ELECTRICAL SPECIFICATIONS

Efficiency (%)
Output Voltage (V)

# LCM300W Performance Curves

|Figure 51: LCM300W Transient Response - Vo Deviation|Figure 52: LCM300W Transient Response - Vo Deviation|
|---|---|
|50% to 100% load change 1A/uS slew rate Vin = 230Vac Ch 1: Vo Ch 2: Io|100% to 50% load change 1A/uS slew rate Vin = 230Vac Ch 1: Vo Ch 2: Io|

# LCM300W Efficiency Curves

| |Output Current (A)|
|---|---|
|95.00|0 1 2 3 4 5 6 7|

Figure 53: LCM300W Efficiency Curve @ 25OC

Figure 54: LCM300W Ripple and Noise MeasurementVin = 90Vac Load: Io = 6.3A (48V), ISB = 2A (5V) Ch 1: Vo

# LCM300W Vprog Curves

| |Prog Voltage (V)|
|---|---|
|65|1 2 3 4 5 6|

Figure 55: LCM300W Output Voltage Adjustment by Vprog @ 25OC x 115Vac Loading: Io = 0A (48V), ISB = 0A (5V)

Rev. 06.26.24_#3.2 advancedenergy.com 17
---
# ELECTRICAL SPECIFICATIONS

# Protection Function Specifications

Input Fuse

LCM300 series are equipped with an internal non-user serviceable 8A High Rupturing Capacity (HRC) 250 Vac fuse to IEC 127 for fault protection in both the Line and Neutral input.

Over Voltage Protection (OVP)

The power supply latches off during output overvoltage with the AC line recycled to reset the latch.

|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|
|VO Output Overvoltage|125|/|145|% Vo|
|VSB Output Overvoltage|110|/|125|% Vo|

Over Current Protection (OCP)

LCM300 series include internal current limit circuitry to prevent damage in the event of overload or short circuit. Recovery must be automatic when the overload is removed more than 20secs, if the output current is larger than or equal to 105% of rated load, it will go to hiccup mode. OCP fault on 5V standby output can cause the main output shutdown.

|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|
|VO Output Overcurrent|105|/|145|%IO, max|
|VSB Output Overcurrent|120|/|170|%ISB, max|

Short Circuit Protection (SCP)

A short circuit is defined as less than 0.03 ohm resistance between the output terminals. All outputs shall be protected against short circuit to ground or other outputs. No damage shall result. In the event of short circuit, the power supply must shut down and it will automatically retry within 25 secs. Also, INH_ENA can be used for manual recycle to remove the fault condition and reset the power supply. In the event of short circuit on the optional 5V standby, the whole PSU, including the main output, must shut down. There is automatic recovery within 20secs after fault removal or the input AC can be recycled manually to reset the power supply and remove the fault condition.

Over Temperature Protection (OTP)

The power supply is internally protected against over-temperature conditions. When the OTP circuit is activated, the power supply will shut off and will auto-recover once the OTP condition is gone. OTP trip-point at full load is set at a nominal of 55 to 65OC Ambient Temperature.

Rev. 06.26.24_#3.2 advancedenergy.com 18
---
# LCM300

# MECHANICAL SPECIFICATIONS

|Mechanical Outlines (unit: mm)|PN 602-000180-0000|
|---|---|
|INPUT TERMINAL BLOCK TRIM POT|SCR-PP MC M-XO.7|
|LED (AC OK)|WIE-T-W|
|LED (DC OKIFAIL)|Pos SKA|
|SK2 SIGNAL CONNECTOR-ZOWAY|-NEG SkS|
|AIR FLOW DIRECTION|PRODUCT LABEL|

| |177.8+0.5| |
|---|---|---|
|1|148.7+0.5|1|
|M3-OZI (8 PLACES)| | |
|2X129.4+0.5|2X449.6+0.5| |
|Rev. 06.26.24_#3.2|advancedenergy.com 19| |
---
# ELECTRICAL SPECIFICATIONS

# MECHANICAL SPECIFICATIONS

# Connector Definitions

AC Input Connector - SK1L - LiveN - NeutralNL - Ground

# Output Connector – SK4&SK5

SK4 – + Main Output (Vo)SK5 – Main Output Return

# Output Connector – SK2

|Pin 1 – A2|Pin 2 – -VPROG|
|---|---|
|Pin 3 – A1|Pin 4 – -VSense|
|Pin 5 – ISHARE| |
|Pin 6 – A0| |
|Pin 7 – SDA1| |
|Pin 8 – +VPROG| |
|Pin 9 – SCL1| |
|Pin 10 – +Vsense| |
|Pin 11 – 5VSB| |
|Pin 12 – GND| |
|Pin 13 – 5VSB| |
|Pin 14 – G_DCOK_C| |
|Pin 15 – GPIOA6| |
|Pin 16 – G_DCOK_E| |
|Pin 17 – GND| |
|Pin 18 – G_ACOK_C| |
|Pin 19 – INH_EN| |
|Pin 20 – G_ACOK_E| |

Rev. 06.26.24_#3.2 advancedenergy.com 20
---
# ELECTRICAL SPECIFICATIONS

# MECHANICAL SPECIFICATIONS

# Power / Signal Mating Connectors and Pin Types

|Reference|On Power Supply|Mating Connector or Equivalent|
|---|---|---|
|AC Input Connector|DINKLE|M3.5 screw|
| |(PN: DT-4C-B14W-03)| |
| |LANDWIN|(LWE PN: 2050S2000) Housing|
|SK2|CVILUX|(LWE PN: 2053T021V) Contact|
| |(PN: CI0120P1HD0-LF)| |
| |CVILUX|(CX PN: CI0120SD000) Housing|
| | |(CX PN: CI01TD21PE0) Contact|
|SK4, SK5|500-006274-0001|M4 screw|
| | |Spade Terminal - Molex BB-124-08 (19141-0058)|

Accessories for SK2:

1. Order kit part number 73-788-001 for control connector interface with .3m wires attached
2. Order kit part number 73-788-002 for control connector interface with unloaded housing and 20 pins

Rev. 06.26.24_#3.2 advancedenergy.com 21
---
# LCM300

# ELECTRICAL SPECIFICATIONS

LED Indicator Definitions

# MECHANICAL SPECIFICATIONS

|LED (AC OK|LED (DC OK/FAIL| |
|---|---|---|
|Conditions|Conditions| |
|Two user-friendly LEDs for status and diagnostics show status of input power, output power and alarm condition valuable troubleshooting aid to reduce system downtime.| | |

|LED Status|LED Status|
|---|---|
|ACOK LED|DCOK/FAIL LED|
|AC present / Output On|Green|
|No AC power to PSU|OFF|
|Standby mode/main output off|Green|
|Power supply failure|Green|

Rev. 06.26.24_#3.2   advancedenergy.com  22
---
# LCM300

|ELECTRICAL SPECIFICATIONS|MECHANICAL SPECIFICATIONS|
|---|---|
|Weight|The LCM300 series weight is 1.76lbs (0.8kg) maximum.|

Rev. 06.26.24_#3.2 advancedenergy.com 23
---
# ELECTRICAL SPECIFICATIONS

# ENVIRONMENTAL SPECIFICATIONS

|Document|Description|
|---|---|
|EN55022|Conducted and radiated EMI limits|
|EN61000-3-2|EMC limits for Harmonic|
|EN61000-3-3|Voltage Fluctuations|
|EN61000-4-2|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Electrostatic Discharge Immunity test. +/-15KV air, +/-8KV contact discharge|
|EN61000-4-3|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Radiated, Radio-frequency, Electromagnetic Field Immunity test. 80MHz – 2.7GHz,10V/m, 80%, AM, 1KHz sine wave|
|EN61000-4-4|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Electrical Fast Transient / Burst Immunity test. +/-2KV for AC power port|
|EN61000-4-5|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Surge test. 2KV common mode and 1KV differential mode for AC ports|
|EN61000-4-6|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Radio Frequency Common Mode|
|EN61000-4-8|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Power Freq Magnetic|
|EN61000-4-11|Electromagnetic Compatibility (EMC) - Testing and measurement techniques - Voltage Dips and Interruptions. 30% reduction for 500mS- Criteria B>95% reduction for 10mS, Criteria A, >95% reduction for 5000mS, Criteria C|
|EN55024: 1998|Information Technology Equipment - Immunity Characteristics, Limits and Method of Measurement|
---
# ELECTRICAL SPECIFICATIONS

# ENVIRONMENTAL SPECIFICATIONS

|Standard|File#|Description|
|---|---|---|
|UL 62368-1 2nd Edition|E186249-A267-UL-X9|US Requirements|
|CSA 22.2 No. 60950-1| |Canada Requirements|
|EN62368-1|E186249-A6001-CB-1|European Requirements|
|UL60601|E182560-A42-UL|Medical Electrical Equipment|
|China CCC Approval|2013010907615591|China Requirements|
|CB Certificate and Report|DK-70362-UL|(All Cenelec Countries)|
|UKCA Mark| |UK Requirements|

Rev. 06.26.24_#3.2 advancedenergy.com 25
---
# ELECTRICAL SPECIFICATIONS

|EMI Emissions|ENVIRONMENTAL SPECIFICATIONS|
|---|---|
|The LCM300 series has been designed to comply with the Class B limits of EMI requirements of EN55022 (FCC Part 15) and CISPR 22 (EN55022) for emissions and relevant sections of EN61000 (IEC 61000) for immunity. The unit is enclosed inside a metal box, tested at 300W using resistive load with cooling fan. Conducted Emissions The applicable standard for conducted emissions is EN55022 (FCC Part 15). Conducted noise can appear as both differential mode and common mode noise currents. Differential mode noise is measured between the two input lines, with the major components occurring at the supply fundamental switching frequency and its harmonics. Common mode noise, a contributor to both radiated emissions and input conducted emissions, is measured between the input lines and system ground and can be broadband in nature. The LCM300 series power supplies have internal EMI ensure the convertors’ conducted EMI levels comply with EN55022 (FCC Part 15) Class B and EN55022 (CISPR22) Class B limits. The EMI measurements are performed with resistive loads at maximum rated loading. Sample of EN55022 Conducted EMI Measurement at 100Vac input Note: Red Line refers to Artesyn Quasi Peak margin, which is 6dB below the CISPR international limit. Pink Line refers to the Emerson Average margin which is 6dB below the CISPR international limit.| |

|Parameter|Model|Symbol|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|FCC Part 15, class B|All|Margin|-|-|6|dB|
|CISPR 22 (EN55022) class B|All|Margin|-|-|6|dB|

Radiated Emissions

Unlike conducted EMI, radiated EMI performance in a system environment may differ drastically from that in a stand-alone power supply. The shielding effect provided by the system enclosure may bring the EMI level from Class A to Class B. It is thus recommended that radiated EMI be evaluated in a system environment. The applicable standard is EN55022 Class A (FCC Part 15). Testing ac-dc convertors as a stand-alone component to the exact requirements of EN55022 can be difficult, because the standard calls for 1m leads to be attached to the input and outputs and aligned such as to maximize the disturbance. In such a set-up, it is possible to form a perfect dipole antenna that very few ac-dc convertors could pass. However, the standard also states that ‘an attempt should be made to maximize the disturbance consistent with the typical application by varying the configuration of the test sample.

Rev. 06.26.24_#3.2 - advancedenergy.com
---
# Output Power (W)

|Output Power (W)|Output Power (W)|Output Power (W)|Output Power (W)|
|---|---|---|---|
|LCM300| | | |

# ELECTRICAL SPECIFICATIONS

Operating Temperature

The LCM300 series maximum output power (300W) can be loaded up to an ambient temperature of +50°C. Only 50% (150W) of the maximum output power can be loaded at an ambient temp of +70°C. Linear derating to 50% nominal output power starts from +50°C to 70°C. The elapsed time between the application of input power and the attainment steady state values requires 5 minutes warm up for -20°C to -40°C operation.

Output power vs operating temperature

|Power Derating|Power Derating|Power Derating|Power Derating|
|---|---|---|---|
|400| | | |
|350| | | |
|300| | | |
|250| | | |
|200|LCM300Q Peak Power| | |
|150|Output Power| | |
|100| | | |
|50| | | |
|0| | | |

Forced Air Cooling

The LCM300 series power supplies included internal cooling fans as part of the power supply assembly to provide forced air-cooling to maintain and control temperature of devices and ambient temperature in the power supply to appropriate levels. The standard direction of airflow is from the fan side to the AC connector end of the power supply. The cooling fan is a variable speed fan. Fan is smart based on internal temperature. Fan noise less than 45 dBA with 80% load @ 30°C.

Rev. 06.26.24_#3.2 advancedenergy.com 27
---
# ELECTRICAL SPECIFICATIONS

|Storage and Shipping Temperature|The LCM300 series power supplies can be stored or shipped at temperatures between –40 OC to +85 OC and relative humidity from 20% to 90% non-condensing.|
|---|---|
|Altitude|The LCM300 series are operate within specifications at altitudes up to 16,405 feet above sea level. The power supply will not be damaged when stored at altitudes of up to 30,000 feet above sea level.|
|Humidity|The LCM300 series are operate within specifications when subjected to a relative humidity from 20% to 90% non-condensing. The LCM300 series can be stored in a relative humidity from 10% to 95% non-condensing.|
|Vibration|The LCM300 series will pass the following vibration specifications:|

# Non-Operating Random Vibration

|Acceleration|1.87 gRMS|
|---|---|
|Frequency Range|10-500 Hz|
|Duration|30 Mins|
|Direction|3 mutually perpendicular axis|

| | |FREQ (Hz)|SLOPE (db/oct)|PSD (g²/Hz)| |
|---|---|---|---|---|---|
| | |10-190| | |0.009|
| | |190-210|-2.66| |0.009|
| | |210-500| | |0.004|

# Operating Random Vibration

|Acceleration|0.153 gRMS|
|---|---|
|Frequency Range|5-100 Hz|
|Duration|30 Mins|
|Direction|3 mutually perpendicular axis|

| | | |FREQ (Hz)|SLOPE (db/oct)|PSD (g²/Hz)| |
|---|---|---|---|---|---|---|
| | | |5-10|11| |0.00003|
| | | |10-50| | |0.004|
| | | |50-100|-10| |0.00003|

Rev. 06.26.24_#3.2 advancedenergy.com 28
---
# ELECTRICAL SPECIFICATIONS

|Shock|Non-Operating Half-Sine Shock| | |
|---|---|---|---|
|Acceleration|30 G|Duration|18 mSec|
|Pulse|Half-Sine|Number of Shock|3 shock on each of 6 faces|
|Operating Half-Sine Shock| | | |
|Acceleration|4 G|Duration|22 mSec|
|Pulse|Half-Sine|Number of Shock|3 shocks in each of 6 faces|

Rev. 06.26.24_#3.2 advancedenergy.com 29
---
# ELECTRICAL SPECIFICATIONS

POWER AND CONTROL SIGNAL DESCRIPTIONS

|AC Input Connector|This connector supplies the AC Mains to the LCM300 series.|
|---|---|
| |L – L1|
| |N – L2|
| |– Earth Ground|

|Output Connectors- SK4&SK5|These pins provide the main output for the LCM300 series. The + Main Output (VO) and the Main Output Return pins are the positive and negative rails, respectively, of the VO main output of the LCM300 power supply. The Main Output (VO) is electrically isolated from the power supply chassis.|
|---|---|
| |SK4 – + Main Output (Vo)|
| |SK5 – Main Output Return|

Control Signals - SK2
The LCM300 series SK2 contains 20 pins control signal header providing analogy control interface, standby power and i2C interface.

A0, A1, A2-(Pin 6, Pin3, Pin1)

A0, A1, A2-(Pin 6, Pin3, Pin1)

A0, A1, A2- (Pin 6, Pin3, Pin1)

A0, A1, A2 -(Pin 6, Pin3, Pin1)

Please refer to “Communication Bus Descriptions” section.

-VPROG, +VPROG

-VPROG, +VPROG-(Pin2, Pin8)

-VPROG, +VPROG --(Pin2, Pin8)

-VPROG, +VPROG - (Pin2, Pin8)(Pin2, Pin8)

Positive and return connection of external supply for Margin Programming. The power supplies have a “margin” pin which will accept a 1-6Vdc signal referenced to a floating return that will program the output the entire adjustment range. –VPROG pin need to connect the main output/standby GND. Applying voltage greater than 6V may result to damage of PSU internal circuit.

-Vsense, +Vsense

-Vsense, +Vsense--(Pin 4, Pin10)

-Vsense, +Vsense -

-Vsense, +Vsense- (Pin 4, Pin10)(Pin 4, Pin10)

(Pin 4, Pin10)

This remote sense circuit is designed to compensate for a power path drop around the entire loop of 0.5 volt. These pins should be connected as close to the loading as possible, If left open, the power supply will regulate the voltage at its output terminals but the voltage level at the load may go lower than the guaranteed spec.

ISHARE

ISHARE

ISHARE

ISHARE -(Pin 5)-(Pin 5)

-(Pin 5)

- (Pin 5)

The main output have active load sharing. The output share within 10% at full load. All current sharing functions are implemented internal to the power supply by making use of the ISHARE signal. The system connects the ISHARE lines between the power supplies. The supplies are able to load share with up to 10 power supplies in parallel. The I2C Line should be connected separately when the number of units in parallel is more than 8.

SDA1, SCL1, GND-(Pin 7, Pin9, Pin17)

SDA1, SCL1, GND-(Pin 7, Pin9, Pin17)

SDA1, SCL1, GND- (Pin 7, Pin9, Pin17)

SDA1, SCL1, GND -(Pin 7, Pin9, Pin17)

Please refer to “Communication Bus Descriptions” section.

5VSB, GND

5VSB, GND

5VSB, GND

5VSB, GND -(Pin11, Pin12, Pin13)-(Pin11, Pin12, Pin13)

-(Pin11, Pin12, Pin13)

- (Pin11, Pin12, Pin13)

The LCM300 series power supply provides a regulated 5 volt 2 amp auxiliary output voltage to power critical circuitry that must remain active regardless of the on/off status of the power supply’s main output. The standby voltage is available whenever a valid AC input voltage is applied to the unit.

Rev. 06.26.24_#3.2  advancedenergy.com          30
---
# ELECTRICAL SPECIFICATIONS

# POWER AND CONTROL SIGNAL DESCRIPTIONS

|G_DCOK_C, G_DCOK_E-(Pin14, Pin16)| | | |
|---|---|---|---|
|G_DCOK_C is a power good signal and is pulled Low by the power supply to indicate that both the outputs are above the regulation limits of the power supply. When any output voltage falls below regulation limits or when AC power has been removed for a time sufficiently long so that power supply operation is no longer guaranteed, G_DCOK_C is de-asserted to a High state. Connect 4.7K resistor on G_DCOK_C to PSU’s standby.| | | |

GPIOA6--(Pin15)EEPROM Write Protect

|G_ACOK_C, G_ACOK_E--(Pin18, Pin20)| | | |
|---|---|---|---|
|G-ACOK_C signal is used to indicate presence of AC input to the power supply. A logic “Low” level on this signal will indicate AC input to the power supply is present. A Logic “High” on this signal will indicate a loss of AC input to the power supply. Connect 4.7K resistor on G_ACOK_C to external standby.| | | |

|INH_EN–(Pin19)| | | |
|---|---|---|---|
|This signal is required to remotely turn on/off the power supply. When INH_EN is shorted to secondary common, the PSU main output shall turn OFF, otherwise the main output is ON.| | | |

Rev. 06.26.24_#3.2 advancedenergy.com 31
---
# ELECTRICAL SPECIFICATIONS

# COMMUNICATION BUS DESCRIPTIONS

I2C Bus Signals

The LCM300 series contains enhanced monitor and control functions implemented via the I2C bus. The LCM300 series I2C functionality (PMBusTM and FRU data) can be accessed via the output connector control signals. The communication bus is powered either by the internal 3.3V supply or from an external power source connected to the Standby Output (ie: accessing an unpowered power supply as long as the Standby Output of another power supply connected in parallel is on). If units are connected in parallel or in redundant mode, the Standby Outputs must be connected together in the system. Otherwise, the I2C bus will not work properly when a unit is inserted into the system without the AC source connected. Note: PMBusTM functionality can be accessed only when the PSU is powered-up. Guaranteed communication I2C speed is 100KHz.

SDA1, SCL1 (I2C Data and Clock Signals)SDA1, SCL1 (I2C Data and Clock Signals) - (pin7, pin 9)SDA1, SCL1 (I2C Data and Clock Signals) - (pin7, pin 9)SDA1, SCL1 (I2C Data and Clock Signals) - (pin7, pin 9)External 2.2K ohm pull up on SCL, SDA line on system side to meet I2C rise/fall time specs.I2C serial data and clock bus - these pins are internally pulled up to internal 3.3V supply with a 4.7K resistor. Recommended

A0, A1, A2 (I2C Address BIT 0, BIT1, BIT2 Signals)A0, A1, A2 (I2C Address BIT 0, BIT1, BIT2 Signals) - (pin6, pin3, pin1)A0, A1, A2 (I2C Address BIT 0, BIT1, BIT2 Signals) - (pin6, pin3, pin1)A0, A1, A2 (I2C Address BIT 0, BIT1, BIT2 Signals) - (pin6, pin3, pin1)A0, A1, A2 (I2C Address BIT 0, BIT1, BIT2 Signals) - (pin6, pin3, pin1)

These three input pins are the address lines A0, A1, and A2 to indicate the slot position the power supply occupies in the power bay and define the power supply addresses for FRU data and PMBusTM data communication. This allows the system to assign different addresses for each power supply. During I2C communication between system and power supplies, the system is the master and power supplies are slaves. They are internally pulled up to internal 5V supply with a 2K resistor and voltage limited to 2.7V with zener diodes.

I2C Bus Communication Interval

The interval between two consecutive I2C communications to the power supply should be at least 50ms to ensure proper monitoring functionality.

I2C Bus Signal Integrity

The noise on the I2C bus (SDA, SCL lines) due to the power supply is less than 500mV peak-to-peak. This noise measurement should be made with an oscilloscope bandwidth limited to 100MHz. Measurements should be made at the power supply output connector with 4.7K ohm resistors pulled up to StandBy Output and 20pf ceramic capacitors to StandBy Output Return. The noise on the address lines A0 and A1 is less than 100mV peak-to-peak. This noise measurement should be made at the power supply output connector.

Rev. 06.26.24_#3.2 advancedenergy.com 32
---
# ELECTRICAL SPECIFICATIONS

# COMMUNICATION BUS DESCRIPTIONS

|SYSTEM|BACKPLANE|POWER SUPPLY SIDE|
|---|---|---|
| |3.3V Supply|5V Supply|

|A0|A1|A2|
|---|---|---|
|PSU Monitor| |Function|

|SDA|100|SDA|4.7K|Backplane PSU Micro Controller|
|---|---|---|---|---|
| |SCL| |SCL|2.7V Z-Diode|
| |GND|2K|Interconnect|FRU DATA EEPROM|

# I2C Bus - Recommended external pull-ups

Electrical and interface specifications of I2C signals (referenced to standby output return pin, unless otherwise indicated):

|Parameter|Condition|Symbol|Min|Type|Max|Unit|
|---|---|---|---|---|---|---|
|SDA, SCL internal pull-up resistor| |Rint| |4.7| |Kohm|
|SDA, SCL internal bus capacitance| |Cint| |0| |pF|
|Recommended external pull-up resistor|1 to 10 PSU| | |2.2| |Kohm|

Rev. 06.26.24_#3.2 advancedenergy.com 33
---
# ELECTRICAL SPECIFICATIONS

# COMMUNICATION BUS DESCRIPTIONS

|Logic Levels| |
|---|---|
|Logic High|5.1V nominal (Spec is 2.1V to 5.5V)**|
|Logic Low|500mV nominal (Spec is 800mV max)**|
|**Note: Artesyn 73-769-001 I2C adapter was used.| |

# Timings

|Parameter|Symbol|Actual Measured|Unit|Min|Max|
|---|---|---|---|---|---|
|SCL clock frequency|fSCL|96|KHz|10|100|
|Hold time (repeated) START condition|tHD;STA|4.0|uS|4.0|4.6|
|LOW period of SCL clock|tLOW|4.7|uS|4.7|4.7|
|HIGH period of SCL clock|tHIGH|4.0|uS|4.0|4.7|
|Setup time for repeated START condition|tSU;STA|4.7|uS|4.7|4.9|
|Data hold time|tHD;DAT|0.8|uS|0|3.45|
|Data setup time|tSU;DAT|3850|nS|250| |
|Rise time|tr|SCL =900 SDA =925|nS|-|600|
|Fall time|tf|SCL =285 SDA =288|nS|-|300|
|Setup time for STOP condition|tSU;STO|6|uS|4.0| |
|Bus free time between a STOP and START condition|tBUF|65***|uS|4.7| |
|***Note: Artesyn 73-769-001 I2C adapter (USB-to-I2C) and Universal PMBusTM GUI software was used.| | | | | |

Rev. 06.26.24_#3.2 advancedenergy.com 34
---
# ELECTRICAL SPECIFICATIONS

# COMMUNICATION BUS DESCRIPTIONS

Device Addressing

The LCM300 series will respond to supported commands on the I2C bus that are addressed according to pins A0, A1 and A2 of the output connector.

Address pins are held HIGH by default via pulled up to internal 5V supply with a 2K resistor. To set the address as “0”, the corresponding address line should be pulled down to logic ground level. Below tables show the address of the power supply with A0, A1 and A2 pins set to either “0” or “1”:

|PSU Slot|A2|A1|A0|PMBusTM Address|
|---|---|---|---|---|
|1|0|0|0|B0|
|2|0|0|1|B2|
|3|0|1|0|B4|
|4|0|1|1|B6|
|5|1|0|0|B8|
|6|1|0|1|BA|
|7|1|1|0|BC|
|8|1|1|1|BE*|

* Default PMBusTM address is BE

Rev. 06.26.24_#3.2 advancedenergy.com 35
---
# ELECTRICAL SPECIFICATIONS

# COMMUNICATION BUS DESCRIPTIONS

I2C Synchronization

The LCM300 series power supply might apply clock stretching. An addressed slave power supply may hold the clock line (SCL) low after receiving (or sending) a byte, indicating that it is not yet ready to process more data. The system master that is communicating with the power supply will attempt to raise the clock to transfer the next bit, but must verify that the clock line was actually raised. If the power supply is clock stretching, the clock line will still be low (because the connections are open-drain). The maximum time out condition for clock stretching for LCM300 series power supply is 100 msec.

|SDA|MSB|MSB|acknowledgement|acknowledgement|
|---|---|---|---|
|SCL|LL|3 -|ACK|ACK|
|repeated STARTSTART or condition|acknowledgement signab from slave byte complete, interrupt within slave clock line held low while interrupts are serviced|acknowledgement signab from slave byte complete, interrupt within slave clock line held low while interrupts are serviced|acknowledgement signab from slave byte complete, interrupt within slave clock line held low while interrupts are serviced|acknowledgement signab from slave byte complete, interrupt within slave clock line held low while interrupts are serviced|
|repeated STARTSTOP condition|Rev. 06.26.24_#3.2 advancedenergy.com 36|Rev. 06.26.24_#3.2 advancedenergy.com 36|Rev. 06.26.24_#3.2 advancedenergy.com 36|Rev. 06.26.24_#3.2 advancedenergy.com 36|
---
# LCM300 PMBusTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

The LCM300 series is compliant with the industry standard PMBusTM protocol for monitoring and control of the power supply via the I2C interface port.

# LCM300 Series PMBusTM General Instructions

Equipment Setup

The following is typical I2C communication setup:

|I2C Master|I2C Adaptor|LCM300|E-Load|
|---|---|---|---|
|Voltmeter| | |AC Source|

PMBusTM Writing Instructions

When writing to any PMBusTM R/W registers, ALWAYS do the following:

- Disable Write Protect (command 10h) by writing any of the following accordingly:
- Levels: 00h - Enable writing to all writeable commands
- 20h - Disables write except 10h, 01h, 00h, 02h and 21h commands
- 40h - Disables write except 10h, 01h, and 00h commands
- 80h - Disable write except 0x00h

To save changes on the USER PMBusTM Table:

Use send byte command: 15h STORE_USER_ALL

Wait for 5 seconds, turn-off the PSU, wait for another 5 seconds before turning it on.

Rev. 06.26.24_#3.2 advancedenergy.com 37
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|00h|PAGE|
|01h|OPERATION|
|02h|ON_OFF_CONFIG|
|03h|CLEAR_FAULTS|
|10h|WRITE_PROTECT|
|15h|STORE_USER_ALL|
|19h|CAPABILITY|
|1Ah|QUERY|
|20h|VOUT_MODE|
|21h|VOUT_COMMAND|
|24h|VOUT_MAX|
|30h|COEFFICIENTS|
|35h|VIN_ON|
|36h|VIN_OFF|
|3Ah|FAN_CONFIG_1_2|
|3Bh|FAN_COMMAND_1|
|40h|VOUT_OV_FAULT_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|00|R|1|Bitmapped|
|80|R/W|1|Bitmapped Used to Turn the unit ON/OFF in conjunction with the input CONTROL pin. 80h-turn on 40h-turn off|
|1E|R|Bitmapped|Configures the combination of CONTROL pin and serial communication commands needed to turn the Unit ON/OFF.|
|-|S|0|-|
|80|R/W|1|Used to Control Writing to the PMBus Device|
|-|S|0|-|
|90|R|1|Bitmapped Provides a way for the hosts system to determine some key capabilities of a PMBus device.|
|BC|BW-BR-PC|1/1|Bitmapped|
|17|R|1|Linear Specifies the mode and parameters of output voltage related Data Formats|
|12.158|R|2|Linear Set output voltage at 12V. Valid Range:9.6-14.4V|
|14.398|R|2|Sets the max adjustable output voltage limit.|
|-|BW|2/5|Raw Hex m = 1, b = 0, R = 0|
|82.5|R|2|Sets the value of input, in volts, at which the unit should start. AC GOOD 82.5 Vac|
|74.5|R|2|Sets the value of input, in volts, at which the unit should stop power conversion. AC BAD 74.5 Vac|
|90|R|1|Bitmapped Read only to reflect setting of Fans|
|0|R/W|2|Linear Adjusts the operation of the Fans. The device may override the command, if it requires higher value, to maintain proper device temperature. Duty cycle Control – Commands Speeds from 0 to 100%|
|15.6|R|2|135% of VOUT_COMMAND value Writeable in factory configuration mode for testing only, max value is 16.2V|

Rev. 06.26.24_#3.2 advancedenergy.com 38
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|41h|VOUT_OV_FAULT_RESPONSE|
|42h|VOUT_OV_WARN_LIMIT|
|43h|VOUT_UV_WARN_LIMIT|
|44h|VOUT_UV_FAULT_LIMIT|
|45h|VOUT_UV_FAULT_RESPONSE|
|46h|IOUT_OC_FAULT_LIMIT|
|47h|IOUT_OC_FAULT_RESPONSE|
|4Ah|IOUT_OC_WARN_LIMIT|
|4Fh|OT_FAULT_LIMIT|
|50h|OT_FAULT_RESPONSE|
|51h|OT_WARN_LIMIT|
|55h|VIN_OV_FAULT_LIMIT|
|56h|VIN_OV_FAULT_RESPONSE|
|59h|VIN_UV_FAULT_LIMIT|
|5Ah|VIN_UV_FAULT_RESPONSE|
|5Eh|POWER_GOOD_ON|
|5Fh|POWER_GOOD_OFF|
|60h|TON_DELAY|
|61h|TON_RISE|
|64h|TOFF_DELAY|
|6Ah|POUT_OP_WARN_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|80|R|1|Bitmapped Unit Latches OFF. Resets on PSON or CONTROL pin recycle or AC recycle.|
|12.398|R|2|Linear 102% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|11.92|R|2|Linear 98% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|10.34|R|2|Linear 85% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only. @12V,10.2V|
|80|R|1|Bitmapped Turn PSU OFF|
|28.438|R|2|Linear Support read only.|
|FA|R|1|Bitmapped OCP ride through. If OCP persists.|
|25.594|R|2|Linear Support read only 90% of IOUT_OC_FAULT_LIMIT value|
|131|R|2|Linear Secondary ambient temperature Fault threshold, in degree C.|
|78|R|1|Bitmapped Turn PSU OFF and will retry indefinitely. Supported enable/disable of protection and recoverability.|
|100|R|2|Linear Secondary ambient temperature warning threshold|
|290|R|2|Sets input over-voltage threshold. (270Vac) Valid Range: 264 to 300 Vac|
|F8|R|1|Bitmapped Default: 80 Vac Valid Rang: 70 to 90 Vac|
|11.92|R|2|Linear 98% of VOUT_COMMAND value|
|11.67|R|2|Linear 98% of VOUT_COMMAND value|
|0|R|2|Sets the time (sec), from start condition (Power ON) until the output starts to rise.|
|33|R|2|Sets the time (ms), for the output rises from 0 to regulation. (33ms)|
|3.801|R|2|Sets the time (ms), from a stop condition (Power OFF) until the output starts to drop (converter OFF).(2.8ms)|
|356.5|R|2|Vout_Cmd*Iout_OCP_level*1.03|

Rev. 06.26.24_#3.2 advancedenergy.com 39
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|78h|STATUS_BYTE|00|R|1|Returns the summary of critical faults: - b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred
- b0 – NONE OF THE ABOVE: A Fault Warning not listed in bits[7:1] has occurred
|
|78h|STATUS_WORD|0000|R|2|Summary of units Fault and warning status: - b15 – VOUT: An output voltage fault or warning has occurred
- b14 – IOUT/POUT: An Output current or power fault or warning has occurred
- b13 – INPUT: An input voltage, current or power fault or warning has occurred
- b12 – MFR: A manufacturer specific fault or warning has occurred
- b11 – POWER_GOOD#: The POWER_GOOD signal is de-asserted
- b10 – FANS: A fan or airflow fault or warning has occurred
- b9 – OTHER: A bit in STATUS_OTHER is set. A fault type not given in bits [15:1]
|
|79h|UNKNOWN| | | |- b8 – UKNOWN: A fault was declared because the device was busy and unable to respond
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 - VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred
- b0 – NONE_OF_THE_ABOVE: A fault or warning not listed in bits[7:1] of this byte has occurred
|
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|7Ah|STATUS_VOUT|00|R|1|Bitmapped Output voltage related faults and warnings|
|b7|VOUT Over-voltage Fault| | | | |
|b6|VOUT Over-voltage warning| | | | |
|b5|VOUT Under-voltage Warning| | | | |
|b4|VOUT Under-voltage Fault| | | | |
|b3|Not supported| | | | |
|b2|Not supported| | | | |
|b1|Not supported| | | | |
|b0|Not supported| | | | |
|7Bh|STATUS_IOUT|00|R|1|Bitmapped Output Current related faults and warnings|
|b7|IOUT Over current Fault| | | | |
|b6|IOUT Over current And Low Voltage shutdown Fault| | | | |
|b5|VOUT Under-voltage Warning| | | | |
|b4|VOUT Under-voltage Fault| | | | |
|b3|VOUT_MAX Warning, an attempt has been made to set output to a value higher that the highest permissible voltage.| | | | |
|b2|TON_MAX_FAULT| | | | |
|b1|TOFF_MAX Warning| | | | |
|b0|reserved| | | | |
|7Ch|STATUS_INPUT|-|R|1|Bitmapped|
|7Dh|STATUS_TEMPERATURE|00|R|1|Bitmapped Temperature related faults and warnings|
|b7|Overtemperature Fault| | | | |
|b6|Overtemperature Warning| | | | |
|b5|Undertemperature Warning| | | | |
|b4|Undertemperature Fault| | | | |
|b3:0|Reserved| | | | |
|7Eh|STATUS_CML|00|R|1|Bitmapped Communications, Logic and Memory|
|80h|STATUS_MFR_SPECIFIC|00|R|1|Bitmapped Manufacturer Status codes|
|81h|STATUS_FANS_1_2|00|R|1|Bitmapped|
|87h|READ_EOUT|-|BR|6|Linear Returns the accumulated output power over time|
|8Bh|READ_VOUT|-|R|2|Linear Returns the actual, measured voltage in Volts.|
|8Ch|READ_IOUT|-|R|2|Linear Returns the output current in amperes.|
|8Dh|READ_TEMPERATURE_1|-|R|2|Linear PSU’s inter hot spot temperature typically that of the main output rail heat sink. Format is Linear-11|

Rev. 06.26.24_#3.2 advancedenergy.com 41
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code| |Command Name|Default Value|Access|Data Bytes|Type|Format|Description|
|---|---|---|---|---|---|---|---|---|
|90h|READ_FAN SPEED_1|-|R|2|Linear|Speed of Fan| | |
|96h|READ_POUT|-|R|2|Linear|Returns the output power, in Watts.| | |
|98h|PMBUS_REVISION|-|R|1|Linear|Reads the PMBus revision number| | |
|99h|MFR_ID|“Artesyn”|BR|7|ASCII|Abbrev or symbol of manufacturers name.| | |
|9Ah|MFR_MODEL|“LCM300L-T-4”|BR|11|ASCII|Manufacturers Model number| | |
|9Bh|MFR_REVISION|30,30 - 00|BR/W|2|ASCII|Manufacturers, revision number| | |
|9Ch|MFR_LOCATION|"Philippines "|BR/W|11|ASCII|Manufacturers facility| | |
|9Dh|MFR_DATE|“YYWW”|BR/W|4|ASCII|Manufacture Date, ASCII format structure : YYMMDD| | |
|9Eh|MFR_SERIAL|-|BR/W|13|ASCII| | | |
|A0h|MFR_VIN_MIN|90|R|2|Linear|Minimum Input Voltage (90Vac)| | |
|A1h|MFR_VIN_MAX|264|R|2|Linear|Maximum Input Voltage (264Vac)| | |
|A2h|MFR_IIN_MAX|5|R|2|Linear|Maximum Input Current (5A)| | |
|A3h|MFR_PIN_MAX|411.5|R|2|Linear|Default:411.5 W| | |
|A4h|MFR_VOUT_MIN|9.6|R|2|Linear|Minimum Output Voltage Regulation Window. (12V)| | |
|A5h|MFR_VOUT_MAX|14.398|R|2|Linear|Maximum Output Voltage Regulation Window (19.5V)| | |
|A6h|MFR_IOUT_MAX|29.188|R|2|Linear|Maximum Output Current (23A)| | |
|A7h|MFR_POUT_MAX|310|R|2|Linear|Maximum Output Power| | |
|A8h|MFR_TAMBIENT_MAX|70|R|2|Linear|Maximum Operating Ambient Temperature (Secondary Ambient) (70 degC)| | |
|A9h|MFR_TAMBIENT_MIN|-40|R|2|Linear|Minimum Operating Ambient Temperature (Secondary Ambient) (-40 degC)| | |
|AAh|MFR_EFFICIENCY_LL|100,300,85,300,85,300,85|BR|14|Linear|Default:100,300,85,300,85,300,85| | |
|ABh|MFR_EFFICIENCY_HL|230,300,89,300,89,300,89|BR|14|Linear|Default:230,300,89,300,89,300,89| | |
|B0h|USER_DATA_B0|FF-y|BR/BW| |Hex|Can not inter write value by keyboard)| | |
|E0h|USER_DATA_00|-|BR|8|ASCII| | | |
|E1h|FW_SEC_VERSION|30,31,2E,30,39,2E,30,30-01.09.00|R|8|ASCII| | | |
|F1h|ISP_UNLOCK_CODE|0,0,0,0 -|BR/W|4|ASCII|MAP Mode only| | |
|F2h|ISP_CTRL_CMD|FF|W|1|Bitmapped|MAP and ISP Mode| | |
|F3h|ISP_STATUS_BYTE|00|R|1|Bitmapped|MAP and ISP Mode| | |
|F5h|ISP_FLASH_DATA|FF-y|BR/W|16|Direct|ISP Mode only| | |

Rev. 06.26.24_#3.2 advancedenergy.com 42
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|00h|PAGE|
|01h|OPERATION|
|02h|ON_OFF_CONFIG|
|03h|CLEAR_FAULTS|
|10h|WRITE_PROTECT|
|15h|STORE_USER_ALL|
|19h|CAPABILITY|
|1Ah|QUERY|
|20h|VOUT_MODE|
|21h|VOUT_COMMAND|
|24h|VOUT_MAX|
|30h|COEFFICIENTS|
|35h|VIN_ON|
|36h|VIN_OFF|
|3Ah|FAN_CONFIG_1_2|
|3Bh|FAN_COMMAND_1|
|40h|VOUT_OV_FAULT_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|00h|R|1|Bitmapped|
|80h|R/W|1|Bitmapped Used to Turn the unit ON/OFF in conjunction with the input CONTROL pin. 80h-turn on 40h-turn off|
|1E|R|1|Bitmapped Configures the combination of CONTROL pin and serial communication commands needed to turn the Unit ON/OFF.|
|-|S|0|-|
|80|R/W|1|Bitmapped Used to Control Writing to the PMBus Device|
|-|S|0|-|
|90|R|1|Bitmapped Provides a way for the hosts system to determine some key capabilities of a PMBus device.|
|-|BW-BR-PC|1/1|Bitmapped|
|17|R|1|Linear Specifies the mode and parameters of Output Voltage related Data Formats|
|14.949|R|2|Linear Set output voltage at 15V. Valid Range:12-18V|
|19.5|R|2|Linear Sets the max adjustable output voltage limit.|
|-|BW-BR-PC|2/5|Raw Hex m = 1, b = 0, R = 0|
|EA94|R|2|Linear Sets the value of input, in volts, at which the unit should start. AC GOOD 82.5 Vac|
|EA54|R|2|Linear Sets the value of input, in volts, at which the unit should stop power conversion. AC BAD 74.5 Vac|
|90H|R|1|Bitmapped Read only to reflect setting of Fans|
|0|R/W|2|Linear Adjusts the operation of the Fans. The device may override the command, if it requires higher value, to maintain proper device temperature. Duty cycle Control - Commands Speeds from 0 to 100%|
|20.18|R|2|Linear 135% of VOUT_COMMAND value Writeable in factory configuration mode for testing only max value is 20.25V|

Rev. 06.26.24_#3.2 advancedenergy.com 43
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|41h|VOUT_OV_FAULT_RESPONSE|
|42h|VOUT_OV_WARN_LIMIT|
|43h|VOUT_UV_WARN_LIMIT|
|44h|VOUT_UV_FAULT_LIMIT|
|45h|VOUT_UV_FAULT_RESPONSE|
|46h|IOUT_OC_FAULT_LIMIT|
|47h|IOUT_OC_FAULT_RESPONSE|
|4Ah|IOUT_OC_WARN_LIMIT|
|4Fh|OT_FAULT_LIMIT|
|50h|OT_FAULT_RESPONSE|
|51h|OT_WARN_LIMIT|
|55h|VIN_OV_FAULT_LIMIT|
|56h|VIN_OV_FAULT_RESPONSE|
|59h|VIN_UV_FAULT_LIMIT|
|5Ah|VIN_UV_FAULT_RESPONSE|
|5Eh|POWER_GOOD_ON|
|5Fh|POWER_GOOD_OFF|
|60h|TON_DELAY|
|61h|TON_RISE|
|64h|TOFF_DELAY|
|6Ah|POUT_OP_WARN_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|80|R|1|Bitmapped Unit Latches OFF. Resets on PSON or CONTROL pin recycle or AC recycle.|
|15.238|R|2|Linear 102% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|14.648|R|2|Linear 98% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|12.709|R|2|Linear 85% of VOUT_COMMAND value @15V,12.75V. Writeable in factory configuration mode for testing only.|
|80|R|1|Bitmapped Turn PSU OFF|
|23|R|2|Linear|
|FA|R|1|Bitmapped OCP ride through. If OCP persists.|
|20.688|R|2|Linear 90% of IOUT_OC_FAULT_LIMIT value|
|115|R|2|Linear Secondary ambient temperature Fault threshold, in degree C.|
|C0|R|1|Bitmapped Turn PSU OFF and will retry indefinitely. Supported enable/disable of protection and recoverability.|
|110|R|2|Linear Secondary ambient temperature warning threshold|
|290|R|2|Sets input over-voltage threshold. (270Vac) Valid Range: 264 to 300 Vac|
|F8|R|1|Bitmapped Default: 80 Vac Valid Rang: 70 to 90 Vac|
|F8|R|1|Bitmapped|
|14.648|R|2|Linear Support read only 98% of VOUT_COMMAND value|
|14.35|R|2|Linear Support read only 98% of VOUT_COMMAND value|
|0|R|2|Sets the time (sec), from start condition (Power ON) until the output starts to rise.|
|33|R|2|Sets the time (ms), for the output rises from 0 to regulation. (33ms)|
|2.801|R|2|Sets the time (ms), from a stop condition (Power OFF) until the output starts to drop (converter OFF).(2.8ms)|
|354.5|R|2|Vout_Cmd*Iout_OCP_level*1.03|

Rev. 06.26.24_#3.2 advancedenergy.com 44
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|78h|STATUS_BYTE|00|R|1|Returns the summary of critical faults: - b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE OF THE ABOVE: A Fault Warning not listed in bits[7:1] has occurred.
|
|79h| | | | |- b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE_OF_THE_ABOVE: A fault or warning not listed in bits[7:1] of this byte has occurred.
|
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|STATUS_VOUT|00|R|1|Bitmapped|Output voltage related faults and warnings|
|b7|VOUT Over-voltage Fault| | | | |
|b6|VOUT Over-voltage warning| | | | |
|b5|VOUT Under-voltage Warning| | | | |
|b4|VOUT Under-voltage Fault| | | | |
|b3 - b0|Not supported| | | | |
|STATUS_IOUT|00|R|1|Bitmapped|Output Current related faults and warnings|
|b7|IOUT Over current Fault| | | | |
|b6|IOUT Over current And Low Voltage shutdown Fault| | | | |
|b5|VOUT Under-voltage Warning| | | | |
|b4|VOUT Under-voltage Fault| | | | |
|b3|VOUT_MAX Warning, an attempt has been made to set output to a value higher that the highest permissible voltage.| | | | |
|b2|TON_MAX_FAULT| | | | |
|b1|TOFF_MAX Warning| | | | |
|b0|reserved| | | | |
|STATUS_INPUT|-|R|1|Bitmapped| |
|STATUS_TEMPERATURE|00|R|1|Bitmapped|Temperature related faults and warnings|
|b7|Overtemperature Fault| | | | |
|b6|Overtemperature Warning| | | | |
|b5|Undertemperature Warning| | | | |
|b4|Undertemperature Fault| | | | |
|b3 - b0|Reserved| | | | |
|STATUS_CML|00|R|1|Bitmapped|Communications, Logic and Memory|
|STATUS_MFR_SPECIFIC|00|R|1|Bitmapped|Manufacturer Status codes|
|STATUS_FANS_1_2|00|R|1|Bitmapped| |
|READ_EOUT|-|BR|6|Linear|Returns the accumulated output power over time|
|READ_VOUT|-|R|2|Linear|Returns the actual, measured voltage in Volts.|
|READ_IOUT|-|R|2|Linear|Returns the output current in amperes.|
|READ_TEMPERATURE_1|-|R|2|Linear|PSU’s inter hot spot temperature typically that of the main output rail heat sink. Format is Linear-11|

Rev. 06.26.24_#3.2

advancedenergy.com

46
---
# LCM300

|Command Code| |Command Name|Default Value|Access|Data Bytes|Type|Format|Description|
|---|---|---|---|---|---|---|---|---|
|90h|READ_FAN SPEED_1|-|R|2|Linear|Speed of Fan| | |
|96h|READ_POUT|-|R|2|Linear|Returns the output power, in Watts.| | |
|98h|PMBUS_REVISION|-|R|1|Linear|Reads the PMBus revision number| | |
|99h|MFR_ID|“Artesyn”|R/W|7|ASCII|Abbrev or symbol of manufacturers name.| | |
|9Ah|MFR_MODEL|“LCM300N-T-4”|BR|11|ASCII|Manufacturers Model number| | |
|9Bh|MFR_REVISION|30,30-00|R/W|2|ASCII|Manufacturers, revision number| | |
|9Ch|MFR_LOCATION|"Philippines"|R/W|11|ASCII|Manufacturers facility| | |
|9Dh|MFR_SERIAL|“YYWW”|R/W|4|ASCII|Manufacture Date structure : YYMMDD| | |
|9Eh|MFR_SERIAL|-|BR/W|13|ASCII| | | |
|A0h|MFR_VIN_MIN|90|R|2|Linear|Minimum Input Voltage (90Vac)| | |
|A1h|MFR_VIN_MAX|264|R|2|Linear|Maximum Input Voltage (264Vac)| | |
|A2h|MFR_IIN_MAX|5|R|2|Linear|Maximum Input Current (5A)| | |
|A3h|MFR_PIN_MAX|411.5|R|2|Linear|Default:411.5 W| | |
|A4h|MFR_VOUT_MIN|12|R|2|Linear|Minimum Output Voltage Regulation Window. (12V)| | |
|A5h|MFR_VOUT_MAX|19.5|R|2|Linear|Maximum Output Voltage Regulation Window (19.5V)| | |
|A6h|MFR_IOUT_MAX|23|R|2|Linear|Maximum Output Current (23A)| | |
|A7h|MFR_POUT_MAX|310|R|2|Linear|Maximum Output Power| | |
|A8h|MFR_TAMBIENT_MAX|70|R|2|Linear|Maximum Operating Ambient Temperature (Secondary Ambient) (70 degC)| | |
|A9h|MFR_TAMBIENT_MIN|-40|R|2|Linear|Minimum Operating Ambient Temperature (Secondary Ambient) (-40 degC)| | |
|AAh|MFR_EFFICIENCY_LL|100,300,85,300,85,300,85|BR|14|Linear|Default:100,300,85,300,85,300,85| | |
|ABh|MFR_EFFICIENCY_HL|230,300,89,300,89,300,89|BR|14|Linear|Default:230,300,89,300,89,300,89| | |
|B0h|USER_DATA_B0|FF-y|BR|Varies|Hex|Can not inter write value by keyboard)| | |
|E0h|USER_DATA_00|-|BR|8|ASCII| | | |
|E1|FW_SEC_REVISION|-|BR|8|ASCII| | | |
|F1h|ISP_UNLOCK_CODE|-|BR/W|4|ASCII|00h,00h,00h,00h| | |
|F2h|ISP_CTRL_CMD|-|W|1|Bitmapped|MAP and ISP Mode| | |
|F3h|ISP_STATUS_BYTE|-|R|1|Bitmapped|MAP and ISP Mode| | |
|F5h|ISP_FLASH_DATA|-|BR/W|16|Direct|ISP Mode only| | |

Rev. 06.26.24_#3.2 advancedenergy.com 47
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|00h|PAGE|
|01h|OPERATION|
|02h|ON_OFF_CONFIG|
|03h|CLEAR_FAULTS|
|10h|WRITE_PROTECT|
|15h|STORE_USER_ALL|
|19h|CAPABILITY|
|1Ah|QUERY|
|20h|VOUT_MODE|
|21h|VOUT_COMMAND|
|24h|VOUT_MAX|
|30h|COEFFICIENTS|
|35h|VIN_ON|
|36h|VIN_OFF|
|3Ah|FAN_CONFIG_1_2|
|3Bh|FAN_COMMAND_1|
|40h|VOUT_OV_FAULT_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|00|R|1|Bitmapped|
|80|R/W|1|Bitmapped Used to turn the unit ON/OFF inconjunction with the input CONTROL pin. It is also used to set output to upper or lower margin voltages.|
|1E|R|Bitmapped|Configures the combination of CONTROL pin and serial communication commands needed to turn the Unit ON/OFF.|
|-|S|0|-|
|80|R/W|1|Bitmapped Used to Control Writing to the PMBus Device 80h - Disables write except 10h 40h – Disables write except 10h, 01h, 00h 20h – Disables write except 10h,01h,00h,02h and 21h commands 00 – Enables write to all writeable commands.|
|-|S|0|-|
|90|R|1|Bitmapped Provides a way for the hosts system to determine some key capabilities of a PMBus device.|
|-|BW-BR-PC|1/1|Bitmapped|
|17|R|1|Linear Specifies the mode and parameters of Output Voltage related Data Formats|
|2FE6|R|2|Linear Set output voltage at 24V. Valid range:19.09-33.60V|
|3999|R|2|Linear Sets the max adjustable output voltage limit 28.9V|
|-|BW-BR-PC|2/5|Raw Hex m = 1, b = 0, R = 0|
|EA94|R|2|Linear Sets the value of input, in volts, at which the unit should start. AC GOOD 82.5 Vac|
|EA54|R|2|Linear Sets the value of input, in volts, at which the unit should stop power conversion. AC BAD 74.5 Vac|
|90|R|1|Bitmapped Read only to reflect setting of Fans|
|0|R/W|2|Linear Adjusts the operation of the Fans. The device may override the command, if it requires higher value, to maintain proper device temperature. Duty cycle Control – Commands Speeds from 0 to 100%|
|Varies|R|2|Linear 135% of VOUT_COMMAND value Writeable in factory configuration mode for testing only|

Rev. 06.26.24_#3.2 advancedenergy.com 48
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|41h|VOUT_OV_FAULT_RESPONSE|
|42h|VOUT_OV_WARN_LIMIT|
|43h|VOUT_UV_WARN_LIMIT|
|44h|VOUT_UV_FAULT_LIMIT|
|45h|VOUT_UV_FAULT_RESPONSE|
|46h|IOUT_OC_FAULT_LIMIT|
|47h|IOUT_OC_FAULT_RESPONSE|
|4Ah|IOUT_OC_WARN_LIMIT|
|4Fh|OT_FAULT_LIMIT|
|50h|OT_FAULT_RESPONSE|
|51h|OT_WARN_LIMIT|
|55h|VIN_OV_FAULT_LIMIT|
|56h|VIN_OV_FAULT_RESPONSE|
|59h|VIN_UV_FAULT_LIMIT|
|5Ah|VIN_UV_FAULT_RESPONSE|
|5Eh|POWER_GOOD_ON|
|5Fh|POWER_GOOD_OFF|
|60h|TON_DELAY|
|61h|TON_RISE|
|64h|TOFF_DELAY|
|6Ah|POUT_OP_WARN_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|80|R|1|Bitmapped Unit Latches OFF. Resets on PSON or CONTROL pin recycle or AC recycle.|
|30DC|R|2|Linear 102% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|2EF5|R|2|Linear 98% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|28BD|R|2|Linear 85% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only.|
|80|R|1|Bitmapped Turn PSU OFF|
|D3C1|R|2|Linear 16.68A at VOUT_COMMAND <= 24V Linear decrease, 16.68A at VOUT_COMMAND 24V to 13.97A at 28.9V|
|BA|R|1|Bitmapped OCP ride through. If OCP persists. Default: BAh|
|C0|R|2|Linear Support read only 90% of IOUT_OC_FAULT_LIMIT value @24v,15.012A|
|EAA8|R|2|Linear Secondary ambient temperature Fault threshold, in degree C. (97degC)|
|C0|R|1|Bitmapped Turn PSU OFF and will retry indefinitely. Supported enable/disable of protection and recoverability.|
|E330|R|2|Linear Secondary ambient temperature warning threshold.|
|FA1C|R|2|Sets input over-voltage threshold. (266Vac) Valid Range: 264 to 300 Vac|
|80|R|1|Bitmapped|
|EA80|R|2|Linear Default: 80 Vac Valid Range: 70 to 90 Vac|
|C0|R|1|Bitmapped|
|2EF0|R|2|Linear 98% of VOUT_COMMAND value@24V-23.52V|
|2EF0|R|2|Linear 96% of VOUT_COMMAND value@24V-23.04V|
|0|R|2|Sets the time (sec), from start condition (Power ON) until the output starts to rise. (0-32767uS)|
|E210|R|2|Sets the time (ms), for the output rises from 0 to regulation. (33ms)|
|C2CD|R|2|Sets the time (ms), from a stop condition (Power OFF) until the output starts to drop (converter OFF).(2.8ms)|
|FB37|R|2|Linear|

Rev. 06.26.24_#3.2 advancedenergy.com 49
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|78h|STATUS_BYTE|00|R|1|Returns the summary of critical faults: - b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE OF THE ABOVE: A Fault Warning not listed in bits[7:1] has occurred.
|
|78h|STATUS_WORD|0000|R|2|Summary of units Fault and warning status: - b15 – VOUT: An output voltage fault or warning has occurred
- b14 – IOUT/POUT: An Output current or power fault or warning has occurred.
- b13 – INPUT: An input voltage, current or power fault or warning has occurred.
- b12 – MFR: A manufacturer specific fault or warning has occurred.
- b11 – POWER_GOOD#: The POWER_GOOD signal is de-asserted
- b10 - FANS: A fan or airflow fault or warning has occurred.
- b9 – OTHER: A bit in STATUS_OTHER is set.
- b8 – UKNOWN: A fault type not given in bits [15:1] of the STATUS_WORD has been detected.
|
|79h| | | | |- b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE_OF_THE_ABOVE: A fault or warning not listed in bits[7:1] of this byte has occurred.
|
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Type|Format|Description|
|---|---|---|---|---|---|---|---|
|STATUS_VOUT|00|R|1|Bitmapped|Output voltage related faults and warnings| | |
|b7|VOUT Over-voltage Fault| | | | | | |
|b6|VOUT Over-voltage warning| | | | | | |
|b5|VOUT Under-voltage Warning| | | | | | |
|b4|VOUT Under-voltage Fault| | | | | | |
|b3 - b0|Not supported| | | | | | |
|STATUS_IOUT|00|R|1|Bitmapped|Output Current related faults and warnings| | |
|b7|IOUT Over current Fault| | | | | | |
|b6|IOUT Over current And Low Voltage shutdown Fault| | | | | | |
|b5|VOUT Under-voltage Warning| | | | | | |
|b4|VOUT Under-voltage Fault| | | | | | |
|b3|VOUT_MAX Warning, an attempt has been made to set output to a value higher that the highest permissible voltage.| | | | | | |
|b2|TON_MAX_FAULT| | | | | | |
|b1|TOFF_MAX Warning| | | | | | |
|b0|reserved| | | | | | |
|STATUS_INPUT|-|R|1|Bitmapped| | | |
|STATUS_TEMPERATURE|00|R|1|Bitmapped|Temperature related faults and warnings| | |
|b7|Overtemperature Fault| | | | | | |
|b6|Overtemperature Warning| | | | | | |
|b5|Undertemperature Warning| | | | | | |
|b4|Undertemperature Fault| | | | | | |
|b3 - b0|Reserved| | | | | | |
|STATUS_CML|00|R|1|Bitmapped|Communications, Logic and Memory| | |
|STATUS_MFR_SPECIFIC|00|R|1|Bitmapped|Manufacturer Status codes| | |
|STATUS_FANS_1_2|-|R|1|Bitmapped| | | |
|READ_EOUT|-|BR|6|Linear|Returns the accumulated output power over time| | |
|READ_VOUT|-|R|2|Linear|Returns the actual, measured voltage in Volts.| | |
|READ_IOUT|-|R|2|Linear|Returns the output current in amperes.| | |

Rev. 06.26.24_#3.2

advancedenergy.com

51
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Type|Description|
|---|---|---|---|---|---|---|
|8Dh|READ_TEMPERATURE_2|-|R|2|Linear| |
|90h|READ_FAN SPEED| | | |Linear|Speed of Fan|
|96h|READ_POUT|-|R|2|Linear|Returns the output power, in Watts.|
|98h|PMBUS_REVISION|22|R|1|Linear|Reads the PMBus revision number|
|99h|MFR_ID|-|BR|7|ASCII|Abbrev or symbol of manufacturers name.|
|9Ah|MFR_MODEL|“LCM300Q-T-4”|RR|11|ASCII|Manufacturers Model number|
|9Bh|MFR_REVISION|"0A”|RR/W|2|ASCII|Manufacturers, revision number|
|9Ch|MFR_LOCATION|"Philippines "|RR/W|11|ASCII|Manufacturers facility|
|9Dh|MFR_DATE|-|BR/W|4|ASCII| |
|9Eh|MFR_SERIAL|-|BR/W|13|ASCII| |
|A0h|MFR_VIN_MIN|EB20|R|2|Linear|Minimum Input Voltage (100Vac)|
|A1h|MFR_VIN_MAX|F3C0|R|2|Linear|Maximum Input Voltage (240Vac)|
|A2h|MFR_IIN_MAX|CA80|R|2|Linear|Maximum Input Current (5A)|
|A3h|MFR_PIN_MAX|-|R|2|Linear|Default: 411.75W|
|A4h|MFR_VOUT_MIN|2F0A|R|2|Linear|Minimum Output Voltage Regulation Window. (19.2V)|
|A5h|MFR_VOUT_MAX|30F6|R|2|Linear|Maximum Output Voltage Regulation Window (28.8V)|
|A6h|MFR_IOUT_MAX|DB20|R|2|Linear|Maximum Output Current (14.5A)|
|A7h|MFR_POUT_MAX|FABC|R|2|Linear|Maximum Output Power|
|A8h|MFR_TAMBIENT_MAX|EA30|R|2|Linear|Maximum Operating Ambient Temperature (Secondary Ambient) (70degC)|
|A9h|MFR_TAMBIENT_MIN|E580|R|2|Linear|Minimum Operating Ambient Temperature (Secondary Ambient) (-40 degC)|
|AAh|MFR_EFFICIENCY_LL|100,350,85,350,85,350,85,350,85|BR|14|Linear|Default:100,350,85,350,85,350,85|
|ABh|MFR_EFFICIENCY_HL|230,350,87,350,87,350,87,350,87|BR|14|Linear|Default:230,350,87,350,87,350,87|
|B0h|USER_DATA_00|-|BR/BR|Varies|Hex| |
|E0h|USER_DATA_00|-|BR|8|ASCII| |
|E1h|FW_SEC_REVISION|-|BR|8|ASCII| |
|F1h|ISP_UNLOCK_CODE|-|BR/W|4|ASCII|00h,00h,00h,00h|
|F2h|ISP_CTRL_CMD| |W|1|Bitmapped|MAP and ISP Mode|
|F3h|ISP_STATUS_BYTE|-|R|1|Bitmapped|MAP and ISP Mode|
|F5h|ISP_FLASH_DATA|-|BR/W|16|Direct|ISP Mode only|

Rev. 06.26.24_#3.2 advancedenergy.com 52
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|00h|PAGE|
|01h|OPERATION|
|02h|ON_OFF_CONFIG|
|03h|CLEAR_FAULTS|
|10h|WRITE_PROTECT|
|15h|STORE_USER_ALL|
|19h|CAPABILITY|
|1Ah|QUERY|
|20h|VOUT_MODE|
|21h|VOUT_COMMAND|
|24h|VOUT_MAX|
|30h|COEFFICIENTS|
|35h|VIN_ON|
|36h|VIN_OFF|
|3Ah|FAN_CONFIG_1_2|
|3Bh|FAN_COMMAND_1|
|40h|VOUT_OV_FAULT_LIMIT|
|41h|VOUT_OV_FAULT_RESPONSE|
|42h|VOUT_OV_WARN_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|00|R|1|Bitmapped|
|80|R/W|1|Bitmapped|
|1E|Bitmapped|1|Bitmapped|
|-|S|0|-|
|80|R/W|1|Bitmapped Used to Control Writing to the PMBus Device 80h - Disables write except 10h 40h – Disables write except 10h, 01h, 00h 20h – Disables write except 10h, 01h, 00h, 02h and 21h commands 00 – Enables write to all writeable commands.|
|-|S|0|-|
|90|R|1|Bitmapped Provides a way for the hosts system to determine some key capabilities of a PMBus device|
|Varies|BW-BR-PC|1/1|Bitmapped|
|17|R|1|Linear Specifies the mode and parameters of Output Voltage related Data Formats|
|3F9E|R|2|Linear Set output voltage at 36V. Valid range: 28.79-50.41V|
|5666|R|2|Linear Sets the max adjustable output voltage limit. 43.2V|
|-|BW-BR-PC|2/5|Raw Hex m = 1, b = 0, R = 0|
|EA94|R|2|Linear Sets the value of input, in volts, at which the unit should start. AC GOOD 82.5 Vac|
|EA54|R|2|Linear Sets the value of input, in volts, at which the unit should stop power conversion. AC BAD74.5 Vac|
|90|R|1|Bitmapped Read only to reflect setting of Fans|
|0|R/W|2|Linear Adjusts the operation of the Fans. The device may override the command, if it requires higher value, to maintain proper device temperature. Duty cycle control – Commands Speeds from 0 to 100%|
|Varies|R|2|Linear 135% of VOUT_COMMAND value Writeable in factory configuration mode for testing only|
|80|R|1|Bitmapped Unit Latches OFF. Resets on PSON or CONTROL pin recycle or AC recycle|
|Varies|R|2|Linear 102% of VOUT_COMMAND value Writeable in factory configuration mode for testing only@36V,36.72V|

Rev. 06.26.24_#3.2 advancedenergy.com 53
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Type|Format|Description|
|---|---|---|---|---|---|---|---|
|43h|VOUT_UV_WARN_LIMIT|98% of VOUT_COMMAND value|R|2|Varies|Linear|Writeable in factory configuration mode for testing only@36V,36.60V|
|44h|VOUT_UV_FAULT_LIMIT|85% of VOUT_COMMAND value|R|2|Varies|Linear|Writeable in factory configuration mode for testing only@36V,36.60V|
|45h|VOUT_UV_FAULT_RESPONSE|80h|R|1|Varies|Bitmapped|Turn PSU OFF|
|46h|IOUT_OC_FAULT_LIMIT|Varies|R|2|Varies|Linear| |
|47h|IOUT_OC_FAULT_RESPONSE|BA|R|1|Varies|Bitmapped|OCP ride through. If OCP persists.|
|4Ah|IOUT_OC_WARN_LIMIT|90% of IOUT_OC_FAULT_LIMIT value @36V,10.035A|R|2|Varies|Linear| |
|4Fh|OT_FAULT_LIMIT|Default:85degC|R|2|EAA8|Linear|Valid Range:80-85degC|
|50h|OT_FAULT_RESPONSE|C0|R|1|EA80|Bitmapped| |
|51h|OT_WARN_LIMIT|Secondary ambient temperature warning threshold.|R|2|EA80|Linear| |
|55h|VIN_OV_FAULT_LIMIT|Sets input over-voltage threshold. (270Vac) Valid Range: 264 to 300Vac|R|2|FA1C|Linear| |
|56h|VIN_OV_FAULT_RESPONSE|80|R|1| |Bitmapped| |
|59h|VIN_UV_FAULT_LIMIT|Default: 80 Vac Valid rang: 70 to 90 Vac|R|2|EA80|Linear| |
|5Ah|VIN_UV_FAULT_RESPONSE|C0|R|1| |Bitmapped| |
|5Eh|POWER_GOOD_ON|98% of VOUT_COMMAND value @36v-35.28V|R|2|Varies|Linear| |
|5Fh|POWER_GOOD_OFF|98% of VOUT_COMMAND value @36v-34.56V|R|2|Varies|Linear| |
|60h|TON_DELAY|Sets the time (sec), from start condition (Power ON) until the output starts to rise. (0-32767uS)|R|2|0|Linear| |
|61h|TON_RISE|Sets the time (ms), for the output rises from 0 to regulation. (33ms)|R|2|E210|Linear| |
|64h|TOFF_DELAY|Sets the time (ms), from a stop condition (Power OFF) until the output starts to drop (converter OFF)(2.8ms) Valid Range:0-32.7ms|R|2|C2CD|Linear| |
|6Ah|POUT_OP_WARN_LIMIT|Vout_Cmd*Iout _OCP_level*1.03|R|2|Varies|Linear| |

Rev. 06.26.24_#3.2 advancedenergy.com 54
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|78h|STATUS_BYTE|00|R|1|Returns the summary of critical faults: - b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE OF THE ABOVE: A Fault Warning not listed in bits[7:1] has occurred.
|
|79h| | | | |- b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE_OF_THE_ABOVE: A fault or warning not listed in bits[7:1] of this byte has occurred.
|
---
# LCM300

|Command Code|Command Name|Default Value|Access|Data Bytes|Type|Format|Description| | | |
|---|---|---|---|---|---|---|---|---|---|---|
| |STATUS_VOUT|00|R|1|Bitmapped|Output voltage related faults and warnings| | | | |
|STATUS_VOUT b7|VOUT Over-voltage Fault| | | | | | | | | |
|STATUS_VOUT b6| | | | | |VOUT Over-voltage warning| | | | |
|STATUS_VOUT b5| | | | | |VOUT Under-voltage Warning| | | | |
|STATUS_VOUT 7Ah| | | | | |VOUT Under-voltage Fault| | | | |
|STATUS_VOUT b3-b0| | | | |Not supported| | | | | |
| |STATUS_IOUT|00|R|1|Bitmapped|Output Current related faults and warnings| | | | |
|STATUS_IOUT b7| | | | | |IOUT Over current Fault| | | | |
|STATUS_IOUT b6|IOUT Over current And Low Voltage shutdown Fault| | | | | | | | | |
|STATUS_IOUT b5| | | | | |VOUT Under-voltage Warning| | | | |
|STATUS_IOUT b4| | | | | |VOUT Under-voltage Fault| | | | |
|STATUS_IOUT b3|VOUT_MAX Warning, an attempt has been made to set output to a value higher that the highest permissible voltage.| | | | | | | | | |
|STATUS_IOUT b2| | | | |TON_MAX_FAULT| | | | | |
|STATUS_IOUT b1| | | | |TOFF_MAX Warning| | | | | |
|STATUS_IOUT b0| | | | |reserved| | | | | |
| |STATUS_INPUT|-|R|1|Bitmapped| | | | | |
| |STATUS_TEMPERATURE|00|R|1|Bitmapped|Temperature related faults and warnings| | | | |
|STATUS_TEMPERATURE b7| | | | | |Overtemperature Fault| | | | |
|STATUS_TEMPERATURE b6| | | | | |Overtemperature Warning| | | | |
|STATUS_TEMPERATURE b5| | | | | |Undertemperature Warning| | | | |
|STATUS_TEMPERATURE b4| | | | | |Undertemperature Fault| | | | |
|STATUS_TEMPERATURE b3-b0| | | | |reserved| | | | | |
| |STATUS_CML|00|R|1|Bitmapped| | | | | |
| |STATUS_MFR_SPECIFIC|00|R|1|Bitmapped| | | | | |
| |STATUS_FANS_1_2|00|R|1|Bitmapped| | | | | |
| |READ_EOUT|-|BR|6|Linear|5% accuracy @ > 5% load| | | | |
| |READ_VOUT|-|R|2|Linear|5% accuracy| | | | |
| |READ_IOUT|-|R|2|Linear|5% accuracy @ > 40% load| | | | |
| |READ_TEMPERATURE_2|-|R|2|Linear|5 degC accuracy| | | | |
| |READ_FAN SPEED|-|R|2|Linear|500 RPM accuracy| | | | |

Rev. 06.26.24_#3.2 advancedenergy.com 56
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Type|Format|Description| | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
|96h|READ_POUT| |-|R|2|Linear|5% accuracy @ > 5% load| | | | |
|98h|PMBUS_REVISION|22h|R| |1|Linear|Reads the PMBus revision number| | | | |
|99h|MFR_ID|“Artesyn”| |BR|7|ASCII|Abbrev or symbol of manufacturers name.| | | | |
|9Ah|MFR_MODEL|“LCM300U-T-4”| |BR|11|ASCII|Manufacturers Model number| | | | |
|9Bh|MFR_REVISION|“0A”| |BR/W|2|ASCII|Manufacturers, revision number| | | | |
|9Ch|MFR_LOCATION|“Philippines”| |BR/W|11|ASCII|Manufacturers facility| | | | |
|9Dh|MFR_DATE|“YYWW”| |BR/W|4|ASCII|Manufacture Date, ASCII format structure: YYMMDD| | | | |
|9Eh|MFR_SERIAL| |-|BR/W|13|ASCII| | | | | |
|A0h|MFR_VIN_MIN|EAD0|R| |2|Linear|Minimum Input Voltage (90Vac)| | | | |
|A1h|MFR_VIN_MAX|FA10|R| |2|Linear|Maximum Input Voltage (240Vac)| | | | |
|A2h|MFR_IIN_MAX|CA80|R|2| |Linear|Maximum Input Current (5A)| | | | |
|A3h|MFR_PIN_MAX| |-|R|2|Linear|Default: 411.75 W| | | | |
|A4h|MFR_VOUT_MIN|2666|R|2| |Linear|Minimum Output Voltage Regulation Window. (28.8V)| | | | |
|A5h|MFR_VOUT_MAX|3999|R| |2|Linear|Maximum Output Voltage Regulation Window (43.2V)| | | | |
|A6h|MFR_IOUT_MAX|D3A0|R| |2|Linear|Maximum Output Current (9.7A)| | | | |
|A7h|MFR_POUT_MAX|FABC|R| |2|Linear|Maximum Output Power| | | | |
|A8h|MFR_TAMBIENT_MAX|EA30|R| |2|Linear|Maximum Operating Ambient Temperature (Secondary Ambient) (70degC)| | | | |
|A9h|MFR_TAMBIENT_MIN|E580|R| |2|Linear|Minimum Operating Ambient Temperature (Secondary Ambient) (-40 degC)| | | | |
|ACh|MFR_EFFICIENCY_LL| | | | | |100,350,85,350,85,350,85|BR|14|Linear|Default: 100,350,85,350,85,350,85|
|ABh|MFR_EFFICIENCY_HL| | | | | |230,350,87,350,87,350,87|BR|14|Linear|Default: 230,350,87,350,87,350,87|
|B0h|USER_DATA_00| |-|BR/BW| |ASCII| | | | | |
|E0h|USER_DATA_00| |-|BR|8|ASCII| | | | | |
|E1h|FW_SEC_REVISION| |-|BR|8|ASCII| | | | | |
|F1h|ISP_UNLOCK_CODE| |-|BR/W|4|ASCII|00h, 00h, 00h, 00h| | | | |
|F2h|ISP_CTRL_CMD| |-|W|1|Bitmapped|MAP and ISP Mode| | | | |
|F3h|ISP_STATUS_BYTE| |-|R|1|Bitmapped|MAP and ISP Mode| | | | |
|F5h|ISP_FLASH_DATA| |-|BR/W|16|Direct|ISP Mode only| | | | |

Rev. 06.26.24_#3.2 advancedenergy.com 57
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|00h|PAGE|
|01h|OPERATION|
|02h|ON_OFF_CONFIG|
|03h|CLEAR_FAULTS|
|10h|WRITE_PROTECT|
|15h|STORE_USER_ALL|
|19h|CAPABILITY|
|1Ah|QUERY|
|20h|VOUT_MODE|
|21h|VOUT_COMMAND|
|24h|VOUT_MAX|
|30h|COEFFICIENTS|
|35h|VIN_ON|
|36h|VIN_OFF|
|3Ah|FAN_CONFIG_1_2|
|3Bh|FAN_COMMAND_1|
|40h|VOUT_OV_FAULT_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|00|R|1|Bitmapped|
|80|R/W|1|Bitmapped Used to Turn the unit ON/OFF in conjunction with the input CONTROL pin. It is also used to set output to upper or lower Margin Voltages|
|1E|R|Bitmapped|Configures the combination of CONTROL pin and serial communication commands needed to turn the Unit ON/OFF|
|-|S|0|-|
|80|R/W|1|Bitmapped Used to Control Writing to the PMBus Device|
|-|S|0|-|
|90|R|1|Bitmapped Provides a way for the hosts system to determine some key capabilities of a PMBus device|
|-|BW-BR-PC|Bitmapped| |
|18|R|1|Linear Specifies the mode and parameters of Output Voltage related Data Formats|
|2FEB|R|2|Linear Set output voltage at 48V. Valid Range: 38.39-67.21V|
|3C0|R|2|Linear Sets the max adjustable output voltage limit. 60V|
|-|BW-BR-PC|2/5|Raw Hex m = 1, b = 0, R = 0|
|EA94|R|2|Linear Sets the value of input, in volts, at which the unit should start. AC GOOD 82.5 Vac|
|EA54|R|2|Linear Sets the value of input, in volts, at which the unit should stop power conversion. AC BAD 74.5 Vac|
|90|R|1|Bitmapped Read only to reflect setting of Fans|
|0|R/W|2|Linear Adjusts the operation of the Fans. The device may override the command, if it requires higher value, to maintain proper device temperature. Duty cycle Control – Commands Speeds from 0 to 100%|
|Varies|R|2|Linear 135% of VOUT_COMMAND value Writeable in factory configuration mode for testing only max value is 63V|

Rev. 06.26.24_#3.2 advancedenergy.com 58
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|
|---|---|
|41h|VOUT_OV_FAULT_RESPONSE|
|42h|VOUT_OV_WARN_LIMIT|
|43h|VOUT_UV_WARN_LIMIT|
|44h|VOUT_UV_FAULT_LIMIT|
|45h|VOUT_UV_FAULT_RESPONSE|
|46h|IOUT_OC_FAULT_LIMIT|
|47h|IOUT_OC_FAULT_RESPONSE|
|4Ah|IOUT_OC_WARN_LIMIT|
|4Fh|OT_FAULT_LIMIT|
|50h|OT_FAULT_RESPONSE|
|51h|OT_WARN_LIMIT|
|55h|VIN_OV_FAULT_LIMIT|
|56h|VIN_OV_FAULT_RESPONSE|
|59h|VIN_UV_FAULT_LIMIT|
|5Ah|VIN_UV_FAULT_RESPONSE|
|5Eh|POWER_GOOD_ON|
|5Fh|POWER_GOOD_OFF|
|60h|TON_DELAY|
|61h|TON_RISE|
|64h|TOFF_DELAY|
|6Ah|POUT_OP_WARN_LIMIT|

|Default Value|Access Type|Data Bytes|Description|
|---|---|---|---|
|80|R|1|Unit Latches OFF. Resets on PSON or CONTROL pin recycle or AC recycle.|
|Varies|R|2|102% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only. @12V, 48.96V|
|Varies|R|2|98% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only. @48V, 47.04V|
|Varies|R|2|85% of VOUT_COMMAND value. Writeable in factory configuration mode for testing only. @48V, 40.80V|
|80|R|1|Bitmapped Turn PSU OFF|
|CB98|R|2|Linear|
|FA|R|1|Bitmapped OCP ride through. If OCP persists.|
|CB3C|R|2|Linear 90% of IOUT_OC_FAULT_LIMIT value @48V, 6.47A|
|E3C0|R|2|Linear Secondary ambient temperature Fault threshold, in degree C.|
|C0|R|1|Bitmapped Turn PSU OFF and will retry indefinitely. Supported enable/disable of protection and recoverability.|
|E370|R|2|Linear Secondary ambient temperature warning threshold|
|FA1C|R|2|Sets input over-voltage threshold. (270Vac) Valid Range: 264 to 300Vac|
|80|R|1|Bitmapped|
|EA80|R|2|Linear Default: 80 Vac Valid Range: 70 to 90 Vac|
|C0|R|1|Bitmapped|
|Varies|R|2|98% of VOUT_COMMAND value|
|Varies|R|2|98% of VOUT_COMMAND value|
|0|R|2|Sets the time (sec), from start condition (Power ON) until the output starts to rise. (0-32767uS)|
|E210|R|2|Sets the time (ms), for the output rises from 0 to regulation. (33ms)|
|C2CD|R|2|Sets the time (ms), from a stop condition (Power OFF) until the output starts to drop (converter OFF). (2.8ms) Valid Range: 0-32.7ms|
|FAC6|R|2|Vout_Cmd*Iout_OCP_level*1.03|

Rev. 06.26.24_#3.2 advancedenergy.com 59
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Description|
|---|---|---|---|---|---|
|78h|STATUS_BYTE|00|R|1|Returns the summary of critical faults: - b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE OF THE ABOVE: A Fault Warning not listed in bits[7:1] has occurred.
|
|79h|STATUS_WORD|0000|R|2|Summary of units Fault and warning status: - b15 – VOUT: An output voltage fault or warning has occurred
- b14 – IOUT/POUT: An Output current or power fault or warning has occurred.
- b13 – INPUT: An input voltage, current or power fault or warning as occurred.
- b12 – MFR: A manufacturer specific fault or warning has occurred.
- b11 – POWER_GOOD#: The POWER_GOOD signal is de-asserted
- b10 - FANS: A fan or airflow fault or warning has occurred.
- b9 – OTHER: A bit in STATUS_OTHER is set.
- b8 – UKNOWN: A fault type not given in bits [15:1] of the STATUS_WORD has been detected.
- b7 – BUSY: A fault was declared because the device was busy and unable to respond.
- b6 – OFF: Unit is OFF
- b5 – VOUT_OV: Output over-voltage fault has occurred
- b4 – IOUT_OC: Output over-current fault has occurred
- b3 – VIN_UV: An input under-voltage fault has occurred
- b2 – TEMPERATURE: A temperature fault or warning has occurred
- b1 – CML: A communication, memory or logic fault has occurred.
- b0 – NONE_OF_THE_ABOVE: A fault or warning not listed in bits[7:1] of this byte has occurred.
|
---
# LCM300

# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code|Command Name|Default Value|Access|Data Bytes|Data Type|Description|
|---|---|---|---|---|---|---|
|7Ah|STATUS_VOUT|00|R|1|Bitmapped|Output voltage related faults and warnings: - VOUT Over-voltage Fault
- VOUT Over-voltage warning
- VOUT Under-voltage Warning
- VOUT Under-voltage Fault
- Not supported
- Not supported
- Not supported
- Not supported
|
|7Bh|STATUS_IOUT|00|R|1|Bitmapped|Output Current related faults and warnings: - IOUT Over current Fault
- IOUT Over current And Low Voltage shutdown Fault
- VOUT Under-voltage Warning
- VOUT Under-voltage Fault
- VOUT_MAX Warning, an attempt has been made to set output to a value higher that the highest permissible voltage.
- TON_MAX_FAULT
- TOFF_MAX Warning
- reserved
|
|7Ch|STATUS_INPUT|-|R|1|Bitmapped| |
|7Dh|STATUS_TEMPERATURE|00|R|1|Bitmapped|Temperature related faults and warnings: - Overtemperature Fault
- Overtemperature Warning
- Undertemperature Warning
- Undertemperature Fault
- Reserved
|
|7Eh|STATUS_CML|00|R|1|Bitmapped|Communications, Logic and Memory|
|80h|STATUS_MFR_SPECIFIC|00|R|1|Bitmapped|Manufacturer Status codes|
|81h|STATUS_FANS_1_2|00|R|1|Bitmapped| |
|87h|READ_EOUT|-|BR|6|Linear|Returns the accumulated output power over time|
|8Bh|READ_VOUT|-|R|2|Linear|Returns the actual, measured voltage in Volts.|
|8Ch|READ_IOUT|-|R|2|Linear|Returns the output current in amperes.|
|8Dh|READ_TEMPERATURE_2|-|R|2|Linear|PSU’s inter hot spot temperature typically that of the main output rail heat sink. Format is Linear-11|

Rev. 06.26.24_#3.2 advancedenergy.com 61
---
# PMBUSTM SPECIFICATIONS

# ELECTRICAL SPECIFICATIONS

|Command Code| |Command Name|Default Value|Access|Data Bytes|Type|Format|Description|
|---|---|---|---|---|---|---|---|---|
|90h|READ_FAN SPEED|-|R|2|Linear|Speed of Fan| | |
|96h|READ_POUT|-|R|2|Linear|Returns the output power, in Watts.| | |
|98h|PMBUS_REVISION|22h|R|1|Linear|Reads the PMBus revision number| | |
|99h|MFR_ID|“Artesyn”|BR|7|ASCII|Abbrev or symbol of manufacturers name.| | |
|9Ah|MFR_MODEL|“LCM300W-T-4”|BR|11|ASCII|Manufacturers Model number| | |
|9Bh|MFR_REVISION|“0A”|BR/W|2|ASCII|Manufacturers, revision number| | |
|9Ch|MFR_LOCATION|“Philippines”|BR/W|11|ASCII|Manufacturers facility| | |
|9Dh|MFR_Date|“YYWWDD”|BR/W|4|ASCII|Manufacture Date structure : YYMMDD| | |
|9Eh|MFR_SERIAL|-|BR/W|13|ASCII|Manufacture series number| | |
|A0h|MFR_VIN_MIN|EB20|R|2|Linear|Minimum Input Voltage (100Vac)| | |
|A1h|MFR_VIN_MAX|F3C0|R|2|Linear|Maximum Input Voltage (240Vac)| | |
|A2h|MFR_IIN_MAX|CA80|R|2|Linear|Maximum Input Current (5A)| | |
|A3h|MFR_PIN_MAX|-|R|2|Linear|Default:411.75 W| | |
|A4h|MFR_VOUT_MIN|280|R|2|Linear|Minimum Output Voltage Regulation Window. (43V)| | |
|A5h|MFR_VOUT_MAX|3C0|R|2|Linear|Maximum Output Voltage Regulation Window (60V)| | |
|A6h|MFR_IOUT_MAX|CB20|R|2|Linear|Maximum Output Current (6.25A)| | |
|A7h|MFR_POUT_MAX|FA58|R|2|Linear|Maximum Output Power (300W for High Line and 1000 For Low Line)| | |
|A8h|MFR_TAMBIENT_MAX|EA30|R|2|Linear|Maximum Operating Ambient Temperature (Secondary Ambient) (70 degC)| | |
|A9h|MFR_TAMBIENT_MIN|E580|R|2|Linear|Minimum Operating Ambient Temperature (Secondary Ambient) (-40 degC)| | |
|ACh|MFR_EFFICIENCY_LL|100,300,85,300,85,300,85|BR|14|Linear|Default:100,300,85,300,85,300,85| | |
|ABh|MFR_EFFICIENCY_HL|230,300,89,300,89,300,89|BR|14|Hex|Default:230,300,89,300,89,300,89| | |
|B0h|USER_DATA_00|-|BR/BW|Varies|ASCII| | | |
|E0h|FW_PRI_VERSION|-|BR|8|ASCII| | | |
|E1h|FW_SEC_VERSION|-|BR|8|ASCII| | | |
|F1h|ISP_UNLOCK_CODE|-|BR/W|4|ASCII|MAP Mode only| | |
|F2h|ISP_CTRL_CMD|-|W|1|Bitmapped|MAP and ISP Mode| | |
|F3h|ISP_STATUS_BYTE|-|R|1|Bitmapped|MAP and ISP Mode| | |
|F5h|ISP_FLASH_DATA|-|BR/W|16|Direct|ISP Mode only| | |

Rev. 06.26.24_#3.2

advancedenergy.com

62
---
# ELECTRICAL SPECIFICATIONS

# APPLICATION NOTES

Current Sharing

The LCM300 series main output V1 is equipped with current sharing capability. This will allow up to 10 power supplies to be connected in parallel for higher power application. Current share accuracy is typically 10% of full load. Ishare voltage at full load is to be 5.0-6.6 Volts and 2.5-4.0 Volts at 50% of maximum current. The I2C Line should be connected separately when the number of units in parallel is more than 8. The minimum load at parallel operation is 1% of the total Output current that the units can deliver.

The table below shows the derated Maximum Power capacity when units are in parallel configuration. This is to consider the 10% load sharing tolerance.

|Number of Units in Parallel (N)|Maximum Output power|
|---|---|
|Stand-alone|300W|
|2|570W|
|3|840W|
|...|...|
|10|2730W|

Supports redundant operation up to 10 units in parallel.

Rev. 06.26.24_#3.2 advancedenergy.com 63
---
# ELECTRICAL SPECIFICATIONS

# APPLICATION NOTES

Output Ripple and Noise Measurement

The setup outlined in the diagram below has been used for output voltage ripple and noise measurements on the LCM300 series. When measuring output ripple and noise, a scope jack in parallel with a 0.1mF ceramic chip capacitor, and a 10mF Tantalum capacitor should be used. Oscilloscope should be set to 20 MHz bandwidth for this measurement.

|OSCILLOSCOPE|8 mm|50 mm|POWER|
|---|---|---|---|
|CH inputGND|0.1 pF|10 pF|RETURN|

Rev. 06.26.24_#3.2 advancedenergy.com 64
---
# ELECTRICAL SPECIFICATIONS

|Issue|Date|Description|Originators|
|---|---|---|---|
|1.0|08.10.2015|First Issue|G. Xue|
|1.1|01.12.2016|Updated the I2C detail|G. Xue|
|1.2|05.03.2016|Update the page 2 module number/Update the remote sense description|K. Wang|
|1.3|04.13.2017|Add LCM300L and LCM300N|K.Ma|
|1.4|05.22.2017|Update the OCP and SCP description/Update the output voltage adjust range of LCM300N and LCM300W|K.Ma|
|1.5|03.01.2018|Update the 9Dh to MFR_Date. Add 9Eh.|K. Wang|
|1.6|03.09.2018|Update 3B to R/W|K. Wang|
|1.7|05.09.2019|Update mating connector Update the PFC Frequency|K. Wang|
|1.8|01.14.2019|Update the VIN_OV_FAULT_LIMIT default value|K. Wang|
|1.9|03.19.2019|Update mating connector|K. Wang|
|2.0|03.25.2020|Update isolation voltage (Production)|J. Ma|
|2.1|04.14.2020|Update mating connector|K. Ma|
|2.2|05.08.2020|Update the leakage current for different test method|K. Ma|
|2.3|07.01.2020|1. Update safety cert from 60950 to 62368 2. Update 21h command|K. Ma|
|2.4|07.01.2021|Update the output voltage adjust range of LCM300N and LCM300W Update PMBusTM command list|K. Ma|
|2.5|08.18.2021|Update PMBus address pins internal pull up voltage Update safety approvals Update EMC part|K. Ma|
|2.6|01.20.2022|Add UKCA mark and PMBus logo Update minimum SCL frequency Add SK4 and SK5 mating connector|K. Ma|
|2.7|02.14.2022|Update timing diagram Update the connector pinout view|J. Zhang, K. Ma|
|2.8|08.30.2022|Update isolation voltage typo|K. Ma|
|2.9|04.18.2023|Add note for the maximum output power on LCM300 Q and U variant|K. Ma|
|3.0|07.18.2023|Add trim pot location in mechanical drawing|K. Ma|
|3.1|09.05.2023|Add “Supports redundant operation up to 10 units”|K. Ma|
|3.2|06.26.2024|Update operating altitude spec to 10,000 feet|K. Ma|
---
# LCM300

ABOUT ADVANCED ENERGY

Advanced Energy (AE) has devoted more than three decades to perfecting power for its global customers. AE designs and manufactures highly engineered, precision power conversion, measurement and control solutions for mission-critical applications and processes.

Our products enable customer innovation in complex applications for a wide range of industries including semiconductor equipment, industrial, manufacturing, telecommunications, data center computing, and medical. With deep applications know-how and responsive service and support across the globe, we build collaborative partnerships to meet rapid technological developments, propel growth for our customers, and innovate the future of power.

For international contact information, visit advancedenergy.com.

Contacts:

powersales@aei.com (Sales Support)productsupport.ep@aei.com (Technical Support)+1 888 412 7832

Specifications are subject to change without notice. Not responsible for errors or omissions. ©2020 Advanced Energy Industries, Inc. All rights reserved. Advanced Energy®, and AE® are U.S. trademarks of Advanced Energy Industries, Inc.

LCM300 - Rev.06.26.24_#3.2