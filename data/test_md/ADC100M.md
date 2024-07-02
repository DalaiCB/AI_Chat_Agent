# ARTESYN ADC100M SERIES

100 Amp & 120 Amp PSA Main DC/DC Converter

Advanced Energy’s Artesyn ADC100M-04 is a direct conversion PSA main unit. With the ever increasing power demands of server processors and associated memory devices, new power conversion design approaches need to be considered both at system and server level. The solution to achieve the high power required is to move to a 48 volt system with the power conversion design approaches of either distributed power conversion, or direct power conversion employed in the server.

ADC100 series follow The Power Stamp Alliance’s standard product footprint and functions that provide a standard modular board-mounted solution for power conversion for 48Vin / 54Vin to low voltage, high current applications.

# SPECIAL FEATURES

|Up to 120 Amp peak current|Pre-bias startup capability|
|---|---|
|PSA compliant|High reliability|
|Up to 91% efficient|RoHS 3.0 (2011/65/EU) compliant|
|Low ripple and noise|UL94 V-0 materials|
|Data center 48 Vdc input range|Two year warranty (consult factory for extended terms)|
|Open frame optimized for air cooling| |
|Surface mount termination| |
|Fixed switching frequency| |
|High capacitive load capability| |

# SAFETY

TUV/CE 62368-1
UL/cUL 62368-1

©2020 Advanced Energy Industries, Inc.
---
# ADC100M SERIES

|Electrical Specifications|
|---|
|Input voltage|40 to 60 Vdc|
|Input undervoltage shutdown/startup|39 Vdc startup|
| |37 Vdc shutdown|
|Efficiency|91%|
|I/O insulation|Functional insulation|
|I/O isolation|500 Vdc|
|Output voltage|1.0 V nominal (-04J variant)|
| |1.8 V nominal (-04Y variant)|
|Output voltage adjustment|0.8 V to 1.1 V (-04J variant)|
| |1.6 V to 2.0 V (-04Y variant)|
|Output current maximum|1.0 V at 120 Amps (-04J variant)|
| |1.8 V at 100 Amps (-04Y variant)|
|Noise and ripple|±22 mV (04Y variant)|
| |TBD (04J variant)|
|Overtemperature protection (Open frame)|125 °C hot spot|
| |Latch protection, configurable|
|Overvoltage protection method/OVP operation|400 mV above Vout (-04Y variant)|
| |TBD (-04J variant)|
| |Latch protection, configurable|
|Overcurrent protection method/OCP operation|Latch protection, configurable|
|Control|Enable: Positive enable|
| |Control: AVSBus commands supported|
| |SVID control supported|
|Remote sense|Provided|
|Columbus™ communication|All control provided for up to 5 satellite stamps supported|
|Switching frequency|TBD|

# Ordering Information

|Model Number|Input Voltage|Output Voltage|Output Current|Structure|
|---|---|---|---|---|
|ADC100M-04J|40 - 60 Vdc|1.0 Vdc|120 A|Open frame, surface mount|
|ADC100M-04Y|40 - 60 Vdc|1.8 Vdc|100 A|Open frame, surface mount|

ADC = Artesyn Direct Conversion, J = 1.0 V output version, 100 = 100/120 A peak current, Y = 1.8 V output version, 04 = 40-60 Vin

advancedenergy.com
---
# ADC100M SERIES

# ENVIRONMENTAL SPECIFICATIONS

|Storage temperature|-40 to +125 °C|
|---|---|
|Ambient operating temperature|-40 to +55 °C|
|MTBF|>3800 k hours at 25 °C, nominal input / rated output, TDC load, Telcordia, SR332 Method 1 Case 3|

# TERMINATION DESCRIPTIONS

| |1AI|1B1|2A1|2B1|2C1|2D1|
|---|---|---|---|---|---|---|
|1A2| | | | | |202|
|8|1A3| | | | |203|
| |1A4| | | | |204|
| |1AS|1B5|2AS|285|2C5|2D5|

BOTTOM VIEW

30.00

Pin 1-18 Functions

|Pad #|Pin Name|Pin Function|Pad #|Pin Name|Pin Function|
|---|---|---|---|---|---|
|1A1|+IN|Positive Input voltage supply connection|2B1|No connection|Pad present, no connection made|
|1A2|PWM_Y|PWM input Y connection|2B5|VCC|Secondary side Auxiliary voltage supply|
|1A3|VDD|Primary Auxiliary voltage supply|2C1|No connection|Pad present, no connection made|
|1A4|PWM_X|PWM input X connection|2C5|No connection|Pad present, no connection made|
|1A5|+IN|Positive input voltage supply connection|2D1|GND|Secondary side ground connection|
|1B1|-IN|Primary side ground connection|2D2|VOUT|Positive output voltage connection|
|1B5|-IN|Primary side ground connection|2D3|No connection|Pad present, no connection made|
|2A1|No connection|Pad present, no connection made|2D4|VOUT|Positive output voltage connection|
|2A5|No connection|Pad present, no connection made|2D5|GND|Secondary side ground connection|

advancedenergy.com

3
---
# ADC100M SERIES

|A|B|C|D|E|F|G|H|J|K|L|M|N|P|R|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|N/A|N/A|N/A|PFAULT|PUC|PUCDTI|PWM1Y|PWM2Y|PWM3Y|PWM4Y|PWM5Y|N/A|N/A|N/A|N/A|
|N/A|N/A|N/A|VSR|PUCCS|PUCCK|PWM1X|PWM2X|PWM3X|PWM4X|PWM5X|N/A|N/A|N/A|N/A|
|-IN|-IN|N/A|TMP5|CSP5|CSN5|GND|GND|GND|GND|PWM6X|PWM6Y|START5|GND|GND|
|-IN|-IN|N/A|TMP3|CSP3|CSN3|GND|GND|GND|GND|FAULT#|START6|START3|GND|GND|
|-IN|-IN|N/A|TMP2|CSP2|CSN2|GND|GND|GND|GND|VR_RDY|VREG|START2|GND|GND|
|-IN|-IN|N/A|TMP4|CSP4|CSN4|GND|GND|GND|GND|EN|VCTRL|START4|GND|GND|
|N/A|N/A|N/A|TMP6|CSP6|CSN6|SALERT|SDA|SVDAT/AVSAMDAT|VR_HOT#|VCCIO_|N/A|N/A|N/A|N/A|
|N/A|N/A|N/A|TMN|+S|-S|SADDR|SCL|SVCLK/AVSCLK|SV_ALRT/AVSSDAT|PAD_|N/A|N/A|N/A|N/A|

1. The areas for 0 V connection through the center line of the module.

2. The relative groupadg of similar signals (by color in the grid-matrix above).

3. The groupadg of -In and GND pads.

4. The grid above does NOT include the power connections.

# Signal Pin Assignments

|Pad #|Pad Name|Pad Function|Pad #|Pad Name|Pad Function|
|---|---|---|---|---|---|
|A1|N/A|No Pad present|A4|N/C (-In)|Pad present, N/C, Thermal via|
|B1|N/A|No Pad present|B4|N/C (-In)|Pad present, N/C, Thermal via|
|C1|N/A|No Pad present|C4|N/A|No Pad present|
|D1|PFAULT_IN#|Primary side fault indicator|D4|TMP3|Temperature sense Satellite 3|
|E1|PUCDTO|Primary side microcontroller data output|E4|CSP3|Current sense +ve Satellite 3|
|F1|PUCDTI|Primary side microcontroller data input|F4|CSN3|Current sense -ve Satellite 3|
|G1|PWM1Y|PWM signal for Satellite 1|G4|GND|Secondary side ground|
|H1|PWM2Y|PWM signal for Satellite 2|H4|GND|Secondary side ground|
|J1|PWM3Y|PWM signal for Satellite 3|J4|GND|Secondary side ground|
|K1|PWM4Y|PWM signal for Satellite 4|K4|GND|Secondary side ground|
|L1|PWM5Y|PWM signal for Satellite 5|L4|FAULT#|Programmable fault indicator|
|M1|N/A|No Pad present|M4|START6|Start for Satellite 6|
|N1|N/A|No Pad present|N4|START3|Start for Satellite 3|
|P1|N/A|No Pad present|P4|GND|Secondary side ground|
|R1|N/A|No Pad present|R4|GND|Secondary side ground|
|A2|N/A|No Pad present|A5|N/C (-In)|Pad present, N/C, Thermal via|
|B2|N/A|No Pad present|B5|N/C (-In)|Pad present, N/C, Thermal via|
|C2|N/A|No Pad present|C5|N/A|No Pad present|
|D2|VSRMON|Feed-forward sensor input|D5|TMP2|Temperature sense Satellite 2|
|E2|PUCCS|Primary side microcontroller chip-select|E5|CSP2|Current sense +ve Satellite 2|
|F2|PUCCK|Primary side u-controller clk|F5|CSN2|Current sense -ve Satellite 2|
|G2|PWM1X|PWM signal for Satellite 1|G5|GND|Secondary side ground|
|H2|PWM2X|PWM signal for Satellite 2|H5|GND|Secondary side ground|
|J2|PWM3X|PWM signal for Satellite 3|J5|GND|Secondary side ground|
|K2|PWM4X|PWM signal for Satellite 4|K5|GND|Secondary side ground|
|L2|PWM5X|PWM signal for Satellite 5|L5|VR_RDY|Voltage regulator ready signal|
|M2|N/A|No Pad present|M5|VREG|Optional regulator input|
|N2|N/A|No Pad present|N5|START2|Start for Satellite 3|
---
# ADC100M SERIES

# SIGNAL LOCATION IDENTIFICATION (CONTINUED)

|Pin #|Pin Name|Termination|Pin Function|Pin #|Pin Name|Pin Function|
|---|---|---|---|---|---|---|
|P2|N/A|No Pad present| |P5|GND|Secondary side ground|
|R2|N/A|No Pad present| |R5|GND|Secondary side ground|
|A3|N/C (-In)|Pad present, N/C, Thermal via| |A6|N/C (-Vin)|Pad present, N/C, Thermal via|
|B3|N/C (-In)|Pad present, N/C, Thermal via| |B6|N/C (-Vin)|Pad present, N/C, Thermal via|
|C3|N/A|No Pad present| |C6|N/A|No Pad present|
|D3|TMP5|Temperature sense Satellite 5| |D6|TMP4|Temperature sense Satellite 4|
|E3|CSP5|Current sense +ve Satellite 5| |E6|CSP4|Current sense +ve Satellite 4|
|F3|CSN5|Current sense -ve Satellite 5| |F6|CSN4|Current sense -ve Satellite 4|
|G3|GND|Secondary side ground| |G6|GND|Secondary side ground|
|H3|GND|Secondary side ground| |H6|GND|Secondary side ground|
|J3|GND|Secondary side ground| |J6|GND|Secondary side ground|
|K3|GND|Secondary side ground| |K6|GND|Secondary side ground|
|L3|PWM6X|PWM signal for Satellite 6| |L6|EN|Enable Pad|
|M3|PWM6Y|PWM signal for Satellite 6| |M6|VCTRL|Controller supply voltage|
|N3|START5|Start for Satellite 5| |N6|START4|Start for Satellite 4|
|P3|GND|Secondary side ground| |P6|GND|Secondary side ground|
|R3|GND|Secondary side ground| |R6|GND|Secondary side ground|
|A7|N/A|No Pad present| |A8|N/A|No Pad present|
|B7|N/A|No Pad present| |B8|N/A|No Pad present|
|C7|N/A|No Pad present| |C8|N/A|No Pad present|
|D7|TMP6|Temperature sense Satellite 6| |D8|TMN|Temp sense -ve common for TMN of all Satellites.|
|E7|CSP6|Current sense +ve Satellite 6| |E8|+S|Remote sense +ve|
|F7|CSN6|Current sense -ve Satellite 6| |F8|-S|Remote sense -ve|
|G7|SALERT|PMBus Alert| |G8|SADDR|PMBus address setting|
|H7|SDA|PMBus data| |H8|SCL|PMBus clock|
|J7|SVDAT / AVSMDAT|SVID data / AVS MData| |J8|SVCLK / AVSCLK|SVID clock / AVS clock|
|K7|VR_HOT#|SVI VR hot| |K8|SVALRT / AVSSDAT|SVID alert / AVS SData|
|L7|VCCIO_OK|VCC fault shutdown – immediate unit shutdown| |L8|PAD_ALERT#|SVI Pad Alert #|
|M7|N/A|No Pad present| |M8|N/A|No Pad present|
|N7|N/A|No Pad present| |N8|N/A|No Pad present|
|P7|N/A|No Pad present| |P8|N/A|No Pad present|
|R7|N/A|No Pad present| |R8|N/A|No Pad present|

1. VSRMON; should have a local pull down resistor (perhaps in parallel with a capacitor) to GND, also connected to Vin via a resistor in non-isolated applications.

2. All CSP* and CSN*; As an option it should be possible to mount a capacitor between the CSxP and the CSxN pads. If not used CSxP should be shorted to CSxN and then to Vout.

3. PM_ADDR; Should have a local pull-down resistor to GND

4. VDAT and SVCLK; Should have a local pull-up resistor to 5V

advancedenergy.com 5
---
|A|B|Detail|Detail|Rn size|
|---|---|---|---|
|Z4|leldi|E|
|advancedenergy.com|advancedenergy.com|advancedenergy.com|advancedenergy.com|advancedenergy.com|
---
# ADC100M SERIES

PSA STANDARD PRODUCT ENVELOP DEFINITION

| |Resistor_down (on the Host board)|Resistor_up (inside the Main unit)|
|---|---|---|
|PMBus Address|Resistor Series|Pin Function|Resistor Series|Pin Name|
|B8|E12|OPEN|E12|10,000|
|B4|E12|220,000|E12|10,000|
|B2|E12|120,000|E12|10,000|
|B0|E12|82,000|E12|10,000|
|E8|E24|62,000|E12|10,000|
|E4|E96|48,700|E12|10,000|
|E2|E12|39,000|E12|10,000|
|E0|E12|33,000|E12|10,000|
|D8|E48|27,400|E12|10,000|
|D4|E48|23,700|E12|10,000|
|D2|E96|20,500|E12|10,000|
|D0|E48|17,800|E12|10,000|
|C8|E96|15,800|E12|10,000|
|C4|E96|13,700|E12|10,000|
|C2|E48|12,100|E12|10,000|
|C0|E96|10,700|E12|10,000|

advancedenergy.com 7