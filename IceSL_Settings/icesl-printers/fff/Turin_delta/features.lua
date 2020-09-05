-- Tudin_Delta
-- for FLSUN QQ S Pro MKS Robin by Rolf Werum  2020-08-08

version = 2

-- Build Area dimensions
bed_radius = 130.0

bed_size_x_mm = bed_radius * 2
bed_size_y_mm = bed_radius * 2

bed_size_z_mm = 360

-- Printer Extruder
extruder_count = 1
nozzle_diameter_mm = 0.4
filament_diameter_mm_0 = 1.75

z_offset   = 0.0

-- Layer height limits
z_layer_height_mm_min = nozzle_diameter_mm * 0.15
z_layer_height_mm_max = nozzle_diameter_mm * 0.75

-- Retraction Settings
filament_priming_mm_0 = 2.0 -- min 0.5 - max 4
priming_mm_per_sec = 30

-- Printing temperatures limits
extruder_temp_degree_c = 200
extruder_temp_degree_c_min = 170
extruder_temp_degree_c_max = 260

bed_temp_degree_c = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 120

-- Printing speed limits
print_speed_mm_per_sec = 40
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 200

perimeter_print_speed_mm_per_sec = 35
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 200

first_layer_print_speed_mm_per_sec = 15
first_layer_print_speed_mm_per_sec_min = 5
first_layer_print_speed_mm_per_sec_max = 50

for i=0,63,1 do
  _G['filament_diameter_mm_'..i] = filament_diameter_mm_0
  _G['filament_priming_mm_'..i] = filament_priming_mm_0
  _G['extruder_temp_degree_c_' ..i] = extruder_temp_degree_c
  _G['extruder_temp_degree_c_'..i..'_min'] = extruder_temp_degree_c_min
  _G['extruder_temp_degree_c_'..i..'_max'] = extruder_temp_degree_c_max
  _G['extruder_mix_count_'..i] = 1
end
