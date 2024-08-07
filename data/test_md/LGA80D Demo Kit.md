# POWER Technical Reference NoteRev.09.18.19_#1.0LGA80D Evaluation Board

Page 1

# LGA80D Evaluation Test Board Digital DC-DC Converter

DIGitALDCDC PMBus

- Contents Overview
- Test Setup
- Supported Models Descriptions
- Schematic
- BOM
- PCB Layout

LGA80D-EVAL-KIT gives you the ability to connect the demonstration board to a USB socket on a PC, with the PMBus interface, dongle and cable provided in the kit to control and monitor the LGA80D units as they would be used in an application.

This document is a reference guide for the evaluation test board of the compatible series power supply. It is for evaluation purposes only. The evaluation board provides output terminals, test points to power signals, control signals and communication interface via I2C bus. Refer to the technical reference note of the power supply for more information about the specifications and the signal definitions.

ARTESYN EMBEDDED TECHNOLOGIES
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 2

Overview

The key components and connection locations are shown in the picture of the evaluation board below. Note that the LGA80D shown at the ‘top’ of this picture is the one that is configured as the single output unit, and the ‘bottom’ converter is configured as a dual output module.

|Vin2 & Vout3|Vouta Regulation & Ripple Measurement Point|Vout3 Setting|Vout3|
|---|---|---|---|
|Efficiency Test Point| | | |
|Vin2| | | |
|GND| | |GND|
|Vout2 & Vout3 Regulation Test Point|8888|8833|Vout2|
|Vin1 GND| | |Vout|
|Vin1, Vouti Vout2 Efficiency Test Point| | | |
|I2C Enable Connector Jumper| |Vout2| |
|Voutt Regulation & Ripple Measurement Point| |Setting|Setting|

Figure 1. Evaluation Test Board for LGA80D

Artesyn Embedded Technologies
---
# Pin Assignment

|Item|Pin Number|Designation|Functions|
|---|---|---|---|
|BUSB101|VIN1|Input terminal| |
|BUSB102|VIN1_rtn|Input return terminal| |
|BUSB1101|VIN2|Input terminal| |
|BUSB1102|VIN2_rtn|Input return terminal| |
|BUSB103|VO2|Output terminal| |
|BUSB104|VO2_rtn|Output return terminal| |
|BUSB105|VO1|Output terminal| |
|BUSB106|VO1_rtn|Output return terminal| |
|Test Point|BUSB1103|VO3|Output terminal|
| |BUSB1104|VO3_rtn|Output return terminal|
| |BUSB1105|VO3|Output terminal|
| |BUSB1106|VO3_rtn|Output return terminal|

# Efficiency and Regulation Test Points

|Test Points|Connections|
|---|---|
|J205|VIN1, VO1 & VO2|
|J1205|VIN2 & VO3|
|J1206|VO2 & VO3|
|J303|VO2|
|J403|VO1|
|J1403|VO3|

# Output Enable and Settings

|Jumper/Switch|Designation|Functions|
|---|---|---|
|J203|Enable Jumper|Output Enable|
|S201|Enable Switch|Output Enable|
|SW601|VO1|VO1 setting|
|SW631|VO2|VO2 setting|
|SW1601|VO3|VO3 setting|

# Connector

|Connector|Designation|Functions|
|---|---|---|
|J204|I2C Connector|I2C Communication|
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D Evaluation Board

|LGA80D Output Enable Connection (S201, J203)|Page 4|
|---|---|
|J201 DISABLE +SV OUTPUT ENABLE J203 J203 EN1 12863w C211 Ez87 J203 J203 EN2 5201 C212 E888| 28v84 J203 J203 EN3 S201 C213 Ez8e| J202 SGND J203 |J201 DISABLE +SV OUTPUT ENABLE J203 J203 EN1 12863w C211 Ez87 J203 J203 EN2 5201 C212 E888| 28v84 J203 J203 EN3 S201 C213 Ez8e| J202 SGND J203 |

Notes: S201 and J201 work with each other. S201 is used to enable / disable the output of LGA80D (2 modules, 3 outputs), if EN1 of J201 is connected, the Vout1 will be enabled /disabled, if EN1, EN2 & EN3 are connected, Vout1, Vout2 & Vout3 will be all enabled /disabled.

LGA80D I2C Connection (J204)

VBUS
R2e8 VbusJ204        1204                 Sda
J284          J204                  SCL
Pin1                                                                 NC J204           J204
SGND   NC J284           J204 NC
NC J204    910   J204 NC

|Pin Number|Designation|Pin Number|Designation|
|---|---|---|---|
|1|VBUS|6|NC|
|2|SDA|7|NC|
|3|SGND|8|NC|
|4|SCL|9|NC|
|5|NC|10|NC|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D Evaluation Board

|LGA80D Voltage Setting (SW601, SW631, SW1601)| | |Page 5| | | | |
|---|---|---|---|---|---|---|---|
| | |Vol SETTING| | | | | |
| | |5 . OV|3 .3v|2.5V|1.8V|1.OV|0.6v|
| | |Sw6a1|Sh601|SW601|Sw601|S4601|Sn601|
|Vout2 Setting|Vout1 Setting| | | | | | |
| | |5.04|3.3V|2.59|1.84|1.04|0.6M|
| | |Sw631|5h631|Sw631|5h631|S4631|50631|
|Vout3 Setting| | | | | | | |
| | |5.0M|3.3v|2.5V|1.8V|1.0V|0.6v|
| | |Sw1601|S01601|SW1601|Sh1601|541601|501601|

|LGA80D Efficiency Test Point (J205, J1205)| | | | |
|---|---|---|---|---|
| |Vout-1|EFFICIENCY MEASUREMENT| | |
| |Vin-1|Vout-2| | |
| | |J205|J205|WINI_SENSE|
| | |J205|J205|VOUT1_SENSE|
| | |J205|J205|~VOUT2_SENSE|
| |Vin-1-rtn|J205|J205| |
| |Vout-2-rtn| | | |
| |Vout-1-rtn|VIN_GND|VOuT2_GND| |
| | |VOUT1 GND| | |

Vin1, Vout1 & Vout2 Efficiency Test Point

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Vin2 & Vout3

Page 6

|Efficiency Test Point| | |EFFICIENCY MEASUREMENT| |
|---|---|---|---|---|
|Vin-2|Vout-3|J1205|J1205|VIN2_SENSE|
|Vin-2-mtn|Vout-3-rtn|J1205|J1205|Vout3SENSE|
| | |J1205|J1205|Vout3_GND_SENSE|
| | | |VIN GND3| |

5. LGA80D Regulation Test Point (J1206)

| |8|8|3|U|PHASES CONNECTOR| |Ivs3+VS3 -| |
|---|---|---|---|---|---|---|---|---|
|8888| | | | | | |EN3| |
| | | | |J1206|J1206|J1206|SHARE| |
| | | | | |J1206|J1206|J1206|SYNC|
| | | | | |J1206|J1206|J1206|EN2|
|Vout2 & Vout3| | | |VS2+| | | | |
| | | | | | | |VS2 -| |

Regulation Test Point

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 7

# Test Setup

# Hardware Test Setup

The LGA80D can be connected with the E-load via the Vout and Return terminals, and communicates with LGA80D GUI through the I2C connector J204.

| |Vin2| |Vo3 Setting|Vo3|Vo3_rtn|E-load|
|---|---|---|---|---|---|---|
|DC Source| | |3|Vo3|Vo3| |
| |GND| | |Voz|Voz rn|E-load|
|Vint|8| |Vo1| | | |
|Enable Switch|GND| |J204|Voz Setting|Vo1 Setting|LGABODGUI|
|Enable Jumper| | | | | | |
|Adapter| | | | | | |

Figure 2. Hardware Interface Setup

Assumption: The user has made the power connections to and from the evaluation card. These will not be described further.

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0 LGA80D Evaluation Board

Software Test Setup Page 8

The LGA80D has an evaluation software, LGA80D GUI, designed to make the unit accessible to the user. It is intended to control and monitor the LGA80D units as they would be used in an application.

| |USB Cable|USB I2C Cable| | |
|---|---|---|---|---|
|Computer| |USB I2C Adapter (73-769-00x)|Evaluation Test Board|LGA80D|

Figure 3. Software Interface Setup

The LGA80D GUI must be installed on a PC before using of all of the functions of this program. Please refer to the Figure 4.

Artesyn POL GUl Test vO 30 loporer QWcE Cov Addiess 0,4+ ige0a 1207 4 0x54 Deapalica UVLO OvP Temnare ulOTP B OVP Ovo OPA OCP JJE04 OCP Addne = Encx Type Ena D2tt Onl 0"1 Conliq LralR zad Nautat 4u Digital Chonoa DciDC

Figure 4. Universal PMBusTM GUI

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

# Hardware Test Setup

Page 9

The setup example is shown in figure 5. It contains the input cord, LGA80D, evaluation test board, USB to I2C adapter
and computer. The adapter is required to connect the unit to the computer. The Artesyn USB-to-I2C interface adapter P/N
is 73-769-001 or 73-769-002.

Figure 5. Setup Example

Artesyn Embedded Technologies
---
# Technical Reference Note

|Supported Models|Part Number|
|---|---|
| |LGA80D-00DADJJ|

Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 10

# Description

Dual O/P Non-isolated 80 A Digital DC/DC Converter

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 11

# Schematic

|0192+-0227|51e7|C|#ete|Rjet|
|---|---|---|---|---|
|Bn8- ~Oled|17| | | |
|PG LED|6214| |[T0l-019820-0227 ]| |
|0115| | | | |
|REXD DIGITAL datA|StD| | |DUSD 1e6|
|GL|Ezes| | | |
|SLERT|LGA8OO-KODULE| | | |
|COYNECT T0|[oxoereFui|Nomz|TcuI_SENSE|Bze8sexs||
|5k5 OF| | | | |

|TABLE-A 1206|TLAS1OI|
|---|---|
|NBLE- 1204|St Urin|

|R216|ACROFG [Lgabeo-882401J]|
|---|---|
|ASCRCFG|SETTING|
|QuiPUL ERABLE| |

920

|EFFICIENCY MEASUREKERT|QB6|
|---|---|
|2205| |
|J205 KOMi_SENSE|Ee5|
|(1265| |

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 12

SchematicG4800-NOOULE"[sea-427781-0182] @s @ #" IVCLT I Hucu 5dan Sr TLAS1IO MASES COWNECIOA Virl (LGaceo-@ODADJ) Vou} RIZIG iepizet Va} SETTING 16ax FJO IGCrE IC CFE Icche VDi W Q0 I 08 O# 08 0 0 0E Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 13

|Schematic|CIRCUIT-A|CIRCUIT-B|CIRCUIT-C|R3B1|
|---|---|---|---|---|
|Refdes start from 31X|Refdes start from 41X| | | |
|VSZ+|VS2 - VS22 - V52Z+|AND BODE PLOT|VSIWS1 - VS1IVSIltOvP AND BODE PLOTA|VS33+ Refdes start from S1X|
|OVP| |VS3t VS3 - VS33 -|VS2 - Z5w VZ|R302|
|J314|J414| | | |
|R311|J314|R41- J414|J514 J514 J514|R305 R405 R401|
|Bode PLOT REF TEST POInT|J419| | | |
|bodE PLoT CIRCUIT| | | | |
|J316|R412 1416|R9KS 1519|R208 Vbus J284 J204 SDA| |
|R312|J316|J416 1516|3 R51Z 1516| |
|J318| | | | |
|J311| | | | |
|BODE PLOT GND|SGND| | | |
|Vol SETTING|5.01 3.3V 2.5V 1.81 1.0v 0.6v|Vo3 SETTING|54681 S46O1 S0601 S4601 Sk501 SW601| |
|J206 SDA|5.01 3.30 2.5V 1.8V 1.0v 0.61|5.0v 3.30 2.5V 1.8V 1.0W 0.61| | |
|J206 SCL| | | | |
|J206 SGRD| | | | |
|Vo2SETTING|5.0v 3.3v 2.5v 1.8V 1.0v 0.6v|1631| | |
|Vo2SETTING|5.0v 3.3v 2.5v 1.8V 1.0v 0.6v|1631| | |

Artesyn Embedded Technologies
---
# Technical Reference Note

# LGA80D Test Board BOM

|Item|Qty|Manufacture P/N|Description|
|---|---|---|---|
|1|1|LGA80D-EVAL-KIT|Test Board (PCB), 8 layers|

Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 14

Manufacture: Advanced Circuits

Reference: 8 Layers_PCB

Part: LGA80D

|Item|Qty|Manufacture P/N|Description|Part|Other|Other|Other|
|---|---|---|---|---|---|---|---|
|2|3|F800102|CONN, HDR, FEM, STRAIGHT, 2, 2.54 mm, 3A, GOLD, 2.54 MM MINI JUMPER|LANDWIN|OTHR1|OTHR2|F800102|
|3|4|ETS-3(V0)-1|MECH. OTHR PUR, OTHR, MOUNTING, PLASTIC CONICAL ANCHORS, N66, V0|KANG YANG|OTHR-SPCR1|OTHR-SPCR2|ETS-3(V0)-1|
|4|12|EME-SW-0616|FSTNR, MTL MET, SEMS, SST, OTHER, PAN HEAD, CROSS RECESS (PHILLIPS), M6 X 1, 12mm, PLAIN & SPRING|VICTOR METAL PRODUCTS (HK) COMPANY LIMITED|SCRW1|SCRW2|EME-SW-0616|
|5|4|ZLH 10X20_EFC|CAP, ELECT, LIMPD, 1500μF, 16VDC, 20%, -20%, 10 X 20|RUBYCON|C147|C154|35ZLH560MEFC|
|6|3|NDS-06V|SWI, MECH, SLD, SLIDE, SPST, 25mA, 999W, 999V, 24VDC|DIPTRONICS MANUFACTURING|SW601|SW631|NDS-06V|
|7|1|T801x-SEC|SWI, MECH, TOG, TOGGLE, SPDT, 5A, 0W, 125V, 0VDC|SALECOM|S201| |T801x-SEC|
|8|1|2052P1000T-01|CONN, HDR, M, RIGHT-ANGLE, 10, 2mm, 3A, SOLDER TAIL, TIN, N/A|LANDWIN|J204| |2052P1000T-01|
|9|1|7313P06011-6|CONN, HDR, M, STRAIGHT, 6, 2.54mm, 3A, SOLDER TAIL, GOLD, PIN HEADER|LANDWIN|J203| |7313P06011-6|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 15

|Item|Qty|Manufacture P/N|Description|Manufacture Reference Part|
|---|---|---|---|---|
|10|1|GPHA201-0502A001B1BA|CONN,HDR,M,STRAIGHT,10,2,2.54mm,SOLDER TAIL,GOLD,DUAL ROW PIN HEADER|GREENCONN ELECTRONIC TECHNOLOGY (SUZHOU) CO., LTD. J205 J1205 J1206 GPHA201-0502A001B1BA|
|11|4|5013|CONN,OTHR,MALE,STRAIGHT,1.0mm,TIN,ORANGE TEST POINT|KEYSTONE ELECTRONICS CORP. J201 J202 J701 J702 5013|
|12|12|500-007761-TABD|MECH,FAB MET,BUSBAR,CU,STMP,BUSBAR TEST-JIG OUTPUT|ARTESYN BUSB101 BUSB102 BUSB103 BUSB104 BUSB105 BUSB106 BUSB1101 BUSB1102 BUSB1103 BUSB1104 BUSB1105 BUSB1106 500-007761-TABD|
|13|1|AP239TR|IC,ANALOG,DRVR,SOIC8 IC,VREG,|STMICROELECTRONICS U702 AP239TR|
|14|1|LF33ABDT-TR|LDO-FXD,LF33AB,3.3V,1%,1A,125°C,TO252 (DPAK) XSTR,FET,NLVMOS|STMICROELECTRONICS ASIA U201 LF33ABDT-TR|
|15|3|BSC009NE2LS|,25V,0.9mΩ,100A,BSC009NE2,PG-TDSON-8|INFINEON Q703 Q704 BSC009NE2LS|
|16|18|2N7002KW|0.31A,2N7002W,SOT323 (SC-70) XSTR,FET,NLVMOS,60V,1.6Ω,|SEMICONDUCTOR Q601 Q602 Q603 Q604 Q605 Q606 Q607 Q608 Q609 Q610 Q611 Q612 Q631 Q632 Q634 Q635 Q636 Q1631 2N7002KW|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 16

|Item|Qty|Manufacture P/N|Description|Manufacture Reference Part|
|---|---|---|---|---|
|16|11|2N7002KW|NLVMOS,60V,1.6Ω, 0.31A,2N7002W, SOT323 (SC-70)|ON Q1632 Q1633 Q1634 Q1635 Q1636 Q1637 2N7002KW Q1638 Q1639 Q1640 Q1641 Q1642|
|17|18|0603B821K500CT|CAP,CER,X7R,10nF, 50VDC,10%, -10%,0603|WALSIN C601 C602 C603 C604 C605 C606 C631 C632 C633 C634 0603B821K500CT C635 C636 C1631 C1632 C1633 C1634 C1635 C1636|
|18|18|CL32X107MQVNN|CAP,CER,X6S,100 μF,6.3VDC,20%, -20%,1210|SAMSUNG CL32X107MQVNN C132 C133 NE C134 C135 C137 C138 C1123 C1125 C1127 C1128 C1129 C1130|
|19|3|CL21B105KAFNFN|CAP,CER,X7R,10μF, 10VDC,10%, -10%,0805|SAMSUNG C301 E CL21B105KAFNFN C401 E C1401|
|20|4|CC1206KKX7R8BB|475 CAP,CER,X7R,2.2 μF,25VDC,10%, -10%,1206|YAGEO C205 CC1206KKX7R8BB 475 C210 C216|
|21|3|CC0603KRX7R8BB|563 CAP,CER,X5R,1μF, 10VDC,±15%,10%, -10%,0603|YAGEO C302 CC0603KRX7R8B C402 B563 C1402|
|22|1|CC0402KRX7R9BB|332 CAP,CER,X7R, 100nF,25VDC,10%, -10%,0402|YAGEO C701 CC0402KRX7R9B B332|
|23|1|TMK316AB7106KL-T|CAP,CER,X7R, 10μF,25VDC,10%, -10%,1206|TAIYO YUDEN C215 TMK316AB7106KL-T|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 17

|Item|Qty|Manufacture P/N|Description|Manufacture Reference Part|
|---|---|---|---|---|
|24|2|C1210C476M4PAC|CAP,CER,X5R, 47μF,16VDC,20%,-20%,1210|KEMET C206 C214 TU|
|25|8|APXS160ARA121MH70G|CAP,ELECT,POLY, 120μF,16VDC,20%,-20%,8 X 6.7|NIPPON CHEMI-CON C101 C102 C103 C104 C1101 C1102 C1103 C1104 APXS160ARA121|
|26|17|C1206C222K1RAC|CAP,CER,X7R,10μF,10VDC,10%,-10%,1206|KEMET C702 C1139 TU C1140 C1141 C1142 C1143 C1144 C1145 C1146 C145 C146|
|27|12|CL21B105KAFNFNE|CAP,CER,X7R,10μF,16VDC,10%,-10%,0805|SAMSUNG ELECTRO-MECHANICS C1148 C1149 E C1150 C1151 C1152 C1153 C107 C108 C109 C110 C111 C112 CL21B105KAFNFN|
|28|18|6TPF220M5L|CAP,OTHR,SPCLPOLY,220μF,6.3VDC,20%,-20%,TANTALUM|PANASONIC C115 C116 C117 C118 C1107 C1110 C1111 C1114 C1115 C1118|
|29|4|0402WGF1803TCE|RES,DIS,TKF,10KΩ,0.063W,1%,100ppm [TC],0402|ROYAL R202 R203 R205 R206 0402WGF1803TCE|
|30|3|0402WGF1803TCE|RES,DIS,TKF,100KΩ,0.063W,1%,100ppm [TC],0402|ROYAL R207 R209 R210 0402WGF1803TCE|
|31|6|0603WAF2700T5E|RES,DIS,TKF,0Ω,0.1W,5%,100ppm [TC],0603|ROYALOHM R204 R303 R304 R403 0603WA R404 R1201|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 18

|Item|Qty|Manufacture P/N|Description|Manufacture Reference|Part|
|---|---|---|---|---|---|
|31|4|0603WAF2700T5E|0.1W,5%, 100ppm [TC],0603|ROYALOHM|R1202 R1203 R1403 R1404 0603WAF2700T5E|
|32|18|0603SAF6491T5E|0.1W,1%,200ppm [TC],0603|ROYALOHM|R601 R604 R607 R610 R613 R616 R631 R634 R637 R640 0603SAF6491T5E R643 R646 R1631 R1634 R1637 R1640 R1643 R1646|
|33|23|0603WAF2700T5E|0.1W,1%,100ppm [TC],0603|ROYALOHM|R213 R602 R603 R605 R608 R611 R614 R617 R632 R633 R635 R638 0603WAF2700T5E R641 R644 R647 R1213 R1632 R1633 R1635 R1638 R1641 R1644 R1647|
|34|6|0603SAF6491T5E|0.1W,1%,100ppm [TC],0603|ROYALOHM|R649 R650 R651 R652 0603SAF6491T5E R653 R654|
|35|3|0603WAF2700T5E|0.1W,1%,100ppm [TC],0603|ROYALOHM|R612 R642 R1642 0603WAF2700T5E|
|36| |RC0603FR-071R1L|0.1W,1%,100ppm [TC],0603|YAGEO|R1645 071R1L|
|37|3|0603WAF2700T5E|0.1W,1%,100 ppm [TC],0603|ROYALOHM|R618 R648 R1648 0603WA|
|38|3|RM06FTN1002|0.1W,1%,100 ppm [TC],0603|TA-I|R606 R636 R1636 RM06FTN1002|
|39|2|RC0603FR-071R1L|0.1W,1%,100 ppm [TC],0603|YAGEO|R216 R1214 071R1L|
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 19

|Item|Qty|Manufacture P/N|Description|Manufacture Reference Part|
|---|---|---|---|---|
|40|1|WR06W1R00FTL|RES,DIS,TKF,56.2KΩ,0.1W,1%,100ppm [TC],0603|WALSIN R1211 WR06W1R00FTL|
|41|4|0603SAF6491T5E|RES,DIS,TKF,61.9KΩ,0.1W,1%,100ppm [TC],0603|ROYALOHM R639 R1639 0603SAF6491T5E|
|42|6|RC0603FR-071R1L|RES,DIS,TKF,68.1KΩ,0.1W,1%,100ppm [TC],0603|YAGEO R1651 R1652 071R1L R1653 R1654|
|43|6|RM10FTN1000|RES,DIS,TKF,0Ω,0.1 25W,1%,100ppm [TC],0805|TA-I R301 R302 R401 R402 RM10FTN1000 R1401 R1402|
|44|2|RK73H1ERTTP10|RES,DIS,TKFS,10KΩ,0.063W,1%,200ppm [TC],0402|KOA R701 R702 00F|
|45|3|RLP25FECR100|RES,DIS,PWR MTL STRP,30mΩ,3W,1%,75ppm [TC]|TA-I R707 R708 R709 RLP25FECR100|
|46|2|CSD95490Q5MC|IC,ANLG,DRVR,125°C,CSD95490Q5MC,DFN22|TEXAS INSTRUMENTS U1 U2 CSD95490Q5MC|
|47|1|ZL8802ALAFT|IC,DGTL,CNTLR,125°C,ZL8802,QFN44|INTERSIL U3 ZL8802ALAFT|
|48|2|CL05B152KB5NFN|CAP,CER,X7R,5.6nF,50VDC,10%,-10%,0402|SAMSUNG ELECTRO-MECHANICS C7 C27 CL05B152KB5NF|
|49|1|CL05B152KB5NFN|CAP,CER,X7R,470pF,50VDC,10%,-10%,0402|SAMSUNG ELECTRO-MECHANICS C37 CL05B152KB5NF|
|50|3|CC0603KRX7R8BB|CAP,CER,X7R,1μF,16VDC,10%,-10%,0603|YAGEO C39 CC 0603 X7R|
|51|14|CL21B105KAFNFN|CAP,CER,X7R,10μF,16VDC,20%,-20%,0805|SAMSUNG ELECTRO-MECHANICS C4 C5 C6 C21 C22 C23 C24 C25 C26 C32 C34 CL21B105KAFNFNE|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 20

|Item|Qty|Manufacture P/N|Description|Manufacture Reference|Part|
|---|---|---|---|---|---|
|52|2|CL05B152KB5NFN|CAP,CER,X7R,1μF,6.3VDC,10%,-10%,0402|SAMSUNG ELECTRO-MECHANICS|CL05B152KB5NF|
|53|2|0805B102K102CT|CAP,CER,X7R,10μF,6.3VDC,10%,-10%,0805|WALSIN|0805B102K102CT|
|54|2|GRM0335C1E680J A01D|CAP,CER,C0G/NP0,68pF,25VDC,5%,-5%,0201|MURATA|GRM0335C1E680 JA01D|
|55|2|EMK063C7104KPQ F|CAP,CER,X7S,100nF,16VDC,10%,-10%,0201|TAIYO YUDEN|EMK063C7104KP QF|
|56|1|RM04FTN5R10|RES,DIS,TKF,1KΩ,0.063W,1%,100ppm[TC],0402|TA-I|RM04FTN5R10|
|57|3|0402WGF1803TCE|RES,DIS,TKF,10KΩ,0.063W,1%,100ppm[TC],0402|ROYAL|0402WGF1803TC E|
|58|2|RC0402FR-0749K9L|RES,DIS,TKF,100KΩ,0.063W,1%,100ppm[TC],0402|YAGEO|RC0402FR-0749K9L|
|59|1|RM04FTN5R10|RES,DIS,TKF,3.48KΩ,0.063W,1%,100ppm[TC],0402|TA-I|RM04FTN5R10|
|60|1|0402WGF1803TCE|RES,DIS,TKF,38.3KΩ,0.063W,1%,100ppm[TC],0402|ROYAL|0402WGF1803TC E|
|61|4|RC0402FR-0749K9L|RES,DIS,TKF,47Ω,0.063W,1%,100ppm[TC],0402|YAGEO|RC0402|
|62|2|RT0402BRD073K9 L|RES,DIS,TNF,1.05KΩ,0.063W,0.1%,25ppm[TC],0402|YAGEO USA (HK) LTD|RT0402|
|63|2|RT0402BRD073K9 L|RES,DIS,TNF,221Ω,0.063W,0.1%,25ppm[TC],0402|YAGEO USA (HK) LTD|RT0402|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 21

|Item|Qty|Manufacture P/N|Description|Manufacture Reference Part|
|---|---|---|---|---|
|64|2|RMCS0402FT100K-AS|RES,DIS,TKFS,1.4KΩ, STACKPOLE 0.063W,1%,200ppm [TC],0402|RMCS0402FT100 K-AS|
|65|2|SG73S1ETTP4R70F|RES,DIS,TKF,4.7Ω, KOA 0.125W,1%,200ppm [TC],0402|SG73S1ETTP4R7 0F|
|66|2|RK73H1HTTC3320F|RES,DIS,TKF,10KΩ, KOA SPEER 0.05W,1%,200ppm [TC],0201|RK73H1HTTC332 0F|

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 22

PCB Layout

|Top copper| |E|
|---|---|---|
|Artesyn Embedded Technologies| | |
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 23

# PCB Layout

Layer 2 copper

Artesyn Embedded Technologies
---
# Technical Reference Note

Rev.09.18.19_#1.0

LGA80D Evaluation Board

Page 24

# PCB Layout

Layer 3 copperArtesyn Embedded Technologies
---
# Technical Reference Note

Rev.09.18.19_#1.0

LGA80D Evaluation Board

Page 25

PCB Layout

Layer 4 copper

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 26

|PCB Layout|Layer 5 copper|
|---|---|
|aa8d| |
|l| |
|00niin| |
|el| |
|Wuaaivs| |

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 27

PCB Layout

Layer 6 copper

Artesyn Embedded Technologies
---
# Technical Reference Note


Rev.09.18.19_#1.0

LGA80D

Evaluation Board

Page 28

PCB Layout

|Layer 7 copper|'8888|
|---|---|
|Artesyn Embedded Technologies| |
---
# Technical Reference Note

Rev.09.18.19_#1.0

LGA80D Evaluation Board

Page 29

# PCB Layout

Bottom copper

Artesyn Embedded Technologies
---
# Technical Reference Note

|Record of Revision and Changes| | |
|---|---|---|
|Issue|Date|Description|
|1.0|11.06.2019|First Issue|

WORLDWIDE OFFICES

|2900 S.Diablo Way|Americas|Europe (UK)|Asia (HK)|
|---|---|---|---|
| |Tempe, AZ 85282|Merry Hill, Dudley|Wing Yip StreetTong; Kowloon|
| |USA|West Midlands, DYS ILX|Kwun Hong Kong|
| |888 412 7832|United Kingdom|4852 2176 3333|

While every precaution has been taken to ensure accuracy and completeness of this literature, Artesyn Embedded Technologies assumes no responsibility and disclaims liability for damages resulting from the use of this information. Artesyn and the Artesyn Embedded Technologies logo are trademarks and service marks of Artesyn Technologies, Inc. All other names, logos referred to are trade names, trademarks, registered trademarks of their respective owners. 2014 All rights reserved.

Rev.09.18.19_#1.0

LGA80D Evaluation Board

Page 30

Originators

J. Ma

ARTESYN EMBEDDED TECHNOLOGIES

WWW.artesyn.com

For more information: WWW.artesyn.com/power

For support: techsupport embeddedpower@artesyn.com

For more information: www.artesyn.com/power

For support: productsupport.ep@artesyn.com

LPS360-M DS Rev. 02.22.14