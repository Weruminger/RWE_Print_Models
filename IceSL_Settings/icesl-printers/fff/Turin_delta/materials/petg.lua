;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
;Print time: {print_time}
;Filament used: {filament_amount}m {filament_weight}g
;Filament cost: {filament_cost}
;M190 S{print_bed_temperature} ;Uncomment to add your own bed temperature line
;M109 S{print_temperature} ;Uncomment to add your own temperature line
G21        ;metric values
G90        ;absolute positioning
M82        ;set extruder to absolute mode
M107       ;start with the fan off
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to min endstops
G1 X0 Y0 Z15.0 F{travel_speed} ;move the platform down 15mm
; Prime the T0 nozzle
G92 E0
G0 X-3 Y10 Z0.2 F1000
G1 Y70 E9 F1000
G1 Y110 E12.5 F1000
G0 X-2.5
G1 Y10 E25 F1000
G10
G0 X0 Y0 Z10 F1000
G11
G92 E0                  ;zero the extruded length again
; End Prime
G1 F{travel_speed}
;Put printing message on LCD screen
M117 Printing...







M104 S0                     ;extruder heater off
M140 S0                     ;heated bed heater off (if you have it)
G91                                    ;relative positioning
G1 E-1 F300                            ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F{travel_speed} ;move Z up a bit and retract filament even more
G28 X0 Y0                              ;move X/Y to min endstops, so the head is out of the way
M84                         ;steppers off
G90                         ;absolute positioning
;{profile_string}