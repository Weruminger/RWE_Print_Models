-- Ethrendil
-- for Marlin FW with FW Retracktion by Rolf Werum  2019-08-25

version = 2

function comment(text)
  output('; ' .. text)
end

current_z = 0
current_extruder = -1

extruder_e = {}
extruder_e_restart = {}

extruder_e[0] = 0
extruder_e[1] = 0
extruder_e_restart[0] = 0
extruder_e_restart[1] = 0

traveling = 0

extruder_stored = {}
extruder_stored[0] = false
extruder_stored[1] = false

function header()
  h = file('header.gcode')
  h = h:gsub( '<TOOLTEMP>', extruder_temp_degree_c[extruders[0]] )
  h = h:gsub( '<HBPTEMP>', bed_temp_degree_c )
  output(h)
end

function footer()
  output(file('footer.gcode'))
end

function layer_start(zheight)
  comment('<layer>')
  output('G1 Z' .. f(zheight))
end

function layer_stop()
  extruder_e_restart = extruder_e
  output('G92 E0')
  comment('</layer>')
end

function retract(extruder,e)
  output('G10')
  return e
end

function prime(extruder,e)
  output('G11')
  return e
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
  extruder_e = e
  letter = 'E'
  output('G1 X' .. f(x) .. ' Y' .. f(y) .. ' Z' .. f(z+z_offset) .. ' F' .. current_frate .. ' ' .. letter .. f(e - extruder_e_restart))
end

function move_e(e)
  extruder_e = e
  letter = 'E'
  output('G1 ' .. letter .. f(e - extruder_e_restart))
end

function set_feedrate(feedrate)
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

current_fan_speed = -1
function set_fan_speed(speed)
  if speed ~= current_fan_speed then
    output('M106 S'.. math.floor(255 * speed/100))
    current_fan_speed = speed
  end
end

