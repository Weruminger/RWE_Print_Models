; M503 ; Before Change 
; ### G21    ; Units in mm (mm)
; ### M149 C ; Units in Celsius
; ### 
; ### lament settings:
; ### M200 D1.75
; ### M200 T1 D1.75
; ### eps per unit:
; ### 92 X100.00 Y100.00 Z1600.00
; ### 92 T0 E414.99
; ### 92 T1 E414.99
; ### ximum feedrates (units/s):
; ### M203 X400.00 Y400.00 Z5.00
; ### M203 T0 E45.00
; ### M203 T1 E45.00
; ### ;Maximum Acceleration (units/s2):
; ### M201 X1500.00 Y1500.00 Z50.00
; ### M201 T0 E8000.00
; ### M201 T1 E8000.00
; ### ;Acceleration (units/s2): P<print_accel> R<retract_accel> T<travel_accel>
; ### M204 P3000.00 R750.00 T3000.00
; ### ;Advanced: B<min_segment_time_us> S<min_feedrate> T<min_travel_feedrate> J<junc_dev>
; ### M205 B20000.00 S0.00 T0.00 J0.01
; ### ;Home offset:
; ### M206 X-32.00 Y0.00 Z0.00
; ### ;Hotend offsets:
; ### M218 T1 X-0.60 Y-0.45 Z-0.100
; ### ;Auto Bed Leveling:
; ### M420 S0 Z0.00
; ### ;Material heatup parameters:
; ### M145 S0 H180 B70 F0
; ### M145 S1 H240 B110 F0
; ### ;PID settings:
; ### M301 P31.45 I3.19 D77.61
; ### M301 P31.45 I3.19 D77.61
; ### M304 P453.27 I38.16 D1346.04
; ### ;Retract: S<length> F<units/m> Z<lift>
; ### M207 S5.00 W35.00 F2700.00 Z0.60
; ### ;Recover: S<length> F<units/m>
; ### M208 S0.00 W0.00 F1800.00
; ### ;Auto-Retract: S=0 to disable, 1 to interpret E-only moves as retract/recover
; ### M209 S0
; ### ;Z-Probe Offset (mm):
; ### M851 X0.00 Y10.00 Z-1.85
; ### ;Stepper driver current:
; ### M906 X800 Y800 Z900
; ### M906 T0 E800
; ### M906 T1 E800
; ### ;
; ### ;Driver stepping mode:
; ### M569 S1 T1 E
; ### ;Tool-changing:
; ### ; Z3.00

