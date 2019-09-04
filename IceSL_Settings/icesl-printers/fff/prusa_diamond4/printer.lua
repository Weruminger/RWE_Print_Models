-- Diamond with Diamond 5 filaments

version = 2

function comment(text)
  output('; ' .. text)
end

extruder_e = 0
extruder_e_reset = 0
extruder_e_adjusted = 0

current_A = 0.25
current_B = 0.25
current_C = 0.25
current_D = 0.25

function header()
  if auto_bed_leveling == true then
    h = file('bed_level_header.gcode')
  else
    h = file('header.gcode')
  end
  h = h:gsub( '<TOOLTEMP>', extruder_temp_degree_c[extruders[0]] )
  h = h:gsub( '<HBPTEMP>', bed_temp_degree_c )
  output(h)
end

function footer()
  output(file('footer.gcode'))
end

function layer_start(zheight)
  comment('<layer>')
  output('G92 E0')
  extruder_e_reset = extruder_e
  output('G1 Z' .. f(zheight))
end

function layer_stop()
  comment('</layer>')
end

function retract(extruder,e)
  len   = filament_priming_mm[extruder] * nb_nozzle_in
  speed = (priming_mm_per_sec * nb_nozzle_in) * 60;
  letter = ' E'

  extruder_e_adjusted = extruder_e_adjusted - len
  output('G1 F' .. speed .. letter .. ff(extruder_e_adjusted-extruder_e_reset) .. ' A0.25 B0.25 C0.25 D0.25')
  
  extruder_e = e - len
  return e - len
end

function prime(extruder,e)
  len   = filament_priming_mm[extruder] * nb_nozzle_in
  speed = (priming_mm_per_sec * nb_nozzle_in) * 60;
  letter = ' E'

  extruder_e_adjusted = extruder_e_adjusted + len
  output('G1 F' .. speed .. letter .. ff(extruder_e_adjusted-extruder_e_reset) .. ' A0.25 B0.25 C0.25 D0.25')
  
  extruder_e = e + len
  return e + len
end

current_extruder = 0
current_frate = 0

function select_extruder(extruder)
end

function swap_extruder(from,to,x,y,z)
end

function move_xyz(x,y,z)
  output('G1 X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. f(z+z_offset))
end

function move_xyze(x,y,z,e)
  letter = ' E'
  if path_is_raft then
    current_A = 0.25
    current_B = 0.25
    current_C = 0.25
    current_D = 0.25
  end
   -- adjust based on filament diameters
  delta_e    = e - extruder_e
  extruder_e = e
  r_a = current_A * (filament_diameter_mm_0 * filament_diameter_mm_0)
        / (filament_diameter_A * filament_diameter_A)
  r_b = current_B * (filament_diameter_mm_0 * filament_diameter_mm_0)
        / (filament_diameter_B * filament_diameter_B)
  r_c = current_C * (filament_diameter_mm_0 * filament_diameter_mm_0)
        / (filament_diameter_C * filament_diameter_C)
  r_d = current_D * (filament_diameter_mm_0 * filament_diameter_mm_0)
        / (filament_diameter_D * filament_diameter_D)
  sum = (r_a + r_b + r_c + r_d)
  r_a = r_a / sum
  r_b = r_b / sum
  r_c = r_c / sum
  r_d = r_d / sum
  delta_e_adjusted = delta_e * sum
  extruder_e_adjusted = extruder_e_adjusted + delta_e_adjusted
  -------------------------------------
  output('G1 X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. f(z+z_offset) .. ' F' .. current_frate .. ' ' .. letter .. ff(extruder_e_adjusted-extruder_e_reset) .. ' A' .. f(r_a) .. ' B' .. f(r_b) .. ' C' .. f(r_c) .. ' D' .. f(r_d))
end

function move_e(e)
  delta_e             = e - extruder_e
  extruder_e          = e
  extruder_e_adjusted = extruder_e_adjusted + delta_e
  letter = ' E'
  output('G1 ' .. letter .. ff(e-extruder_e_reset))
end

function set_feedrate(feedrate)
  feedrate = math.floor(feedrate)
  output('G1 F' .. feedrate)
  current_frate = feedrate
end

function extruder_start()
end

function extruder_stop()
end

function progress(percent)
end

function set_extruder_temperature(extruder,temperature)
  output('M104 S' .. temperature .. ' T' .. extruder)
end

function set_mixing_ratios(ratios)
  sum = ratios[0] + ratios[1] + ratios[2] + ratios[3]
  if sum == 0 then
    ratios[0] = 0.25
    ratios[1] = 0.25
    ratios[2] = 0.25
    ratios[3] = 0.25
  end
  current_A = ratios[0]
  current_B = ratios[1]
  current_C = ratios[2]
  current_D = ratios[3]
end

current_fan_speed = -1
function set_fan_speed(speed)
  if speed ~= current_fan_speed then
    output('M106 S'.. math.floor(255 * speed/100))
    current_fan_speed = speed
  end
end
