-- Common Prusa I3 with Diamond 3 filaments
-- Bedell Pierre 18/07/2019

processing = false

current_z = 0.0

current_frate = 0
changed_frate = false

current_extruder = 0

extruder_e = {} -- table of extrusion values for each extruder
extruder_e_reset = {} -- table of extrusion values for each extruder for e reset (to comply with G92 E0)
extruder_e_adjusted = {} -- table of adjusted extrusion values for each extruder for the filament_diameter_management feature
extruder_e_swap = {} -- table of extrusion values for each extruder before to keep track of e at an extruder swap

for i = 0, extruder_count -1 do
  extruder_e[i] = 0.0
  extruder_e_reset[i] = 0.0
  extruder_e_adjusted[i] = 0.0
  extruder_e_swap[i] = 0.0
end

skip_prime_retract = false
skip_ratios_change = false
last_extruder_selected = 0 -- counter to track the selected / prepared extruders

current_fan_speed = -1

current_mix_ratio = {} -- array to store the current mixing ratios, with the first number for the A ratio, etc.
for i = 1, nb_input do
  current_mix_ratio[i] = 1 / nb_input
end

craftware_debug = true

--##################################################

function comment(text)
  output('; ' .. text)
end

function header()
  local auto_level_string = 'G29 ; auto bed levelling\nG0 F6200 X0 Y0 ; back to the origin to begin the purge '
  
  local h = file('header.gcode')
  h = h:gsub( '<TOOLTEMP>', extruder_temp_degree_c[extruders[0]] )
  h = h:gsub( '<HBPTEMP>', bed_temp_degree_c )

  if auto_bed_leveling == true then
    h = h:gsub( '<BEDLVL>', auto_level_string )
  else
    h = h:gsub( '<BEDLVL>', "G0 F6200 X0 Y0" )
  end

  local purge_ratios = ""
  for i = 1, nb_input do
    purge_ratios = purge_ratios .. " " .. extruder_letters[i] .. f(1 / nb_input)
  end

  h = h:gsub( '<PURGE_RATIOS>', purge_ratios)

  output(h)
  current_frate = travel_speed_mm_per_sec * 60
  changed_frate = true
end

function footer()
  output(file('footer.gcode'))
end

function layer_start(zheight)
  output(';<layer ' .. layer_id .. '>')
  output('G0 Z' .. f(zheight))
end

function layer_stop()
  extruder_e_reset[current_extruder] = extruder_e[current_extruder]
  output('G92 E0')
  comment('</layer>')
end

function retract(extruder,e)
  extruder_e[current_extruder] = e
  if skip_prime_retract then 
    --comment('retract skipped')
    skip_prime_retract = false
    return e
  else
    comment('retract')
    local len    = filament_priming_mm[extruder] * nb_input
    local speed  = (priming_mm_per_sec[extruder] * nb_input) * 60;
    local e_value = e - len - extruder_e_reset[current_extruder]
    if filament_diameter_management == true then
      extruder_e_adjusted[current_extruder] = extruder_e_adjusted[current_extruder] - len
      e_value = extruder_e_adjusted[current_extruder] - extruder_e_reset[current_extruder]
    end

    local retract_ratios = ""
    for i = 1, nb_input do
      retract_ratios = retract_ratios .. " " .. extruder_letters[i] .. f(1 / nb_input)
    end
    output('G1 F' .. speed .. ' E' .. ff(e_value) .. retract_ratios)

    extruder_e[current_extruder] = e - len
    current_frate = speed
    changed_frate = true
    return e - len
  end
end

function prime(extruder,e)
  extruder_e[current_extruder] = e
  if skip_prime_retract then 
    --comment('retract skipped')
    skip_prime_retract = false
    return e
  else
    comment('prime')
    local len   = filament_priming_mm[extruder] * nb_input
    local speed = (priming_mm_per_sec[extruder] * nb_input) * 60;
    local e_value = e + len - extruder_e_reset[current_extruder]
    if filament_diameter_management == true then
      extruder_e_adjusted[current_extruder] = extruder_e_adjusted[current_extruder] + len
      e_value = extruder_e_adjusted[current_extruder] - extruder_e_reset[current_extruder] 
    end

    local prime_ratios = ""
    for i = 1, nb_input do
      prime_ratios = prime_ratios .. " " .. extruder_letters[i] .. f(1 / nb_input)
    end
    output('G1 F' .. speed .. ' E' .. ff(e_value) .. prime_ratios)

    extruder_e[current_extruder] = e + len
    current_frate = speed
    changed_frate = true
    return e + len
  end
end

function select_extruder(extruder)
  last_extruder_selected = last_extruder_selected + 1
  -- skip unnecessary prime/retract and ratios setup
  skip_prime_retract = true
  skip_ratios_change = true

  if last_extruder_selected == number_of_extruders then -- number_of_extruders is an IceSL internal Lua global variable which is used to know how many extruders will be used for a print job
    skip_prime_retract = false
    skip_ratios_change = false
    current_extruder = extruder
  end
end

function swap_extruder(from,to,x,y,z)
  output('; Extruder change from vE' .. from .. ' to vE' .. to)

  extruder_e_swap[from] = extruder_e_swap[from] + extruder_e[from] - extruder_e_reset[from]
  current_extruder = to
  skip_prime_retract = true
end

function move_xyz(x,y,z)
  if processing == true then
    processing = false
    comment('travel')
  end
    if z == current_z then
    if changed_frate == true then 
      output('G0 F' .. current_frate .. ' X' .. f(x) .. ' Y' .. f(y))
      changed_frate = false
    else
      output('G0 X' .. f(x) .. ' Y' .. f(y))
    end
  else
    if changed_frate == true then
      output('G0 F' .. current_frate .. ' X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. ff(z))
      changed_frate = false
    else
      output('G0 X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. ff(z))
    end
    current_z = z
  end
end

function move_xyze(x,y,z,e)
  local delta_e = e - extruder_e[current_extruder]
  extruder_e[current_extruder] = e

  local e_value = extruder_e[current_extruder] - extruder_e_reset[current_extruder]

  if path_is_raft then
    for i = 1, nb_input do
      current_mix_ratio[i] = 1 / nb_input
    end
  end
  
  if processing == false then 
    processing = true
    if craftware_debug == true then
      if      path_is_perimeter then output(';segType:Perimeter')
      elseif  path_is_shell     then output(';segType:HShell')
      elseif  path_is_infill    then output(';segType:Infill')
      elseif  path_is_raft      then output(';segType:Raft')
      elseif  path_is_brim      then output(';segType:Skirt')
      elseif  path_is_shield    then output(';segType:Pillar')
      elseif  path_is_support   then output(';segType:Support')
      elseif  path_is_tower     then output(';segType:Pillar')
      end
    else
      if      path_is_perimeter then comment('perimeter')
      elseif  path_is_shell     then comment('shell')
      elseif  path_is_infill    then comment('infill')
      elseif  path_is_raft      then comment('raft')
      elseif  path_is_brim      then comment('brim')
      elseif  path_is_shield    then comment('shield')
      elseif  path_is_support   then comment('support')
      elseif  path_is_tower     then comment('tower')
      end
    end
  end

  local r_ = {} -- local array to compute new mixing ratios
  for i = 1, nb_input do
    r_[i] = current_mix_ratio[i]
  end

  -- adjust based on filament diameters  
  if filament_diameter_management == true then
    local sum = 0
    for i = 1, nb_input do
      r_[i] = r_[i] * (filament_diameter_mm_0^2) / (_G['filament_diameter_' .. extruder_letters[i]]^2)
      sum = sum + r_[i]
    end

    for i = 1, nb_input do
      r_[i] = r_[i] / sum
    end

    local delta_e_adjusted = delta_e * sum
    extruder_e_adjusted[current_extruder] = extruder_e_adjusted[current_extruder] + delta_e_adjusted

    e_value = extruder_e_adjusted[current_extruder] - extruder_e_reset[current_extruder]
  end

  local ratios_string = ""
  for i = 1, nb_input do
    ratios_string = ratios_string .. " " .. extruder_letters[i] .. f(r_[i])
  end
  -------------------------------------

  if z == current_z then
    if changed_frate == true then 
      output('G1 F' .. current_frate .. ' X' .. f(x) .. ' Y' .. f(y) .. ' E' .. ff(e_value) .. ratios_string)
      changed_frate = false
    else
      output('G1 X' .. f(x) .. ' Y' .. f(y) .. ' E' .. ff(e_value) .. ratios_string)
    end
  else
    if changed_frate == true then
      output('G1 F' .. current_frate .. ' X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. ff(z) .. ' E' .. ff(e_value) .. ratios_string)
      changed_frate = false
    else
      output('G1 X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. ff(z) .. ' E' .. ff(e_value) .. ratios_string)
    end
    current_z = z
  end

end

function move_e(e)
  comment('dampener reset')
  local delta_e = e - extruder_e[current_extruder]
  extruder_e[current_extruder] = e

  local e_value = extruder_e[current_extruder] - extruder_e_reset[current_extruder]

  if filament_diameter_management == true then
    extruder_e_adjusted[current_extruder] = extruder_e_adjusted[current_extruder] + delta_e
    e_value = extruder_e_adjusted[current_extruder] - extruder_e_reset[current_extruder]
  end

  local ratios_string = ""
  for i = 1, nb_input do
    ratios_string = ratios_string .. " " .. extruder_letters[i] .. f(r_[i])
  end

  if changed_frate == true then 
    output('G1 F' .. current_frate .. ' E' .. ff(e_value) .. ratios_string)
    changed_frate = false
  else
    output('G1 E' .. ff(e_value) .. ratios_string)
  end
end

function set_feedrate(feedrate)
  if feedrate ~= current_frate then
    current_frate =  math.floor(feedrate)
    changed_frate = true
  end
end

function extruder_start()
end

function extruder_stop()
end

function progress(percent)
end

function set_extruder_temperature(extruder,temperature)
  output('M104 S' .. temperature)
end

function set_and_wait_extruder_temperature(extruder,temperature)
  output('M109 S' .. temperature)
end

function set_mixing_ratios(ratios)
  if skip_ratios_change then 
    skip_ratios_change = false
  else
    local sum = 0
    for i = 0, table.getn(ratios) do
      sum = sum + ratios[i]
    end

    if sum == 0 then
      for i = 0, table.getn(ratios) do
        ratios[i] = 1 / nb_input
      end
    end

    local ratios_string = ""
    local changed = false
    for i = 1, nb_input do
      if ratios[i-1] ~= current_mix_ratio[i] then
        current_mix_ratio[i] = f(ratios[i-1])
        ratios_string = ratios_string .. " " .. extruder_letters[i] .. current_mix_ratio[i]
        changed = true
      end
    end

    if changed == true then
      comment('Mixing Ratios set to' .. ratios_string)
      --output('G92 E0')
      --extruder_e_reset[current_extruder] = extruder_e[current_extruder]
    end
  end
end

function set_fan_speed(speed)
  if speed ~= current_fan_speed then
    output('M106 S'.. math.floor(255 * speed/100))
    current_fan_speed = speed
  end
end
