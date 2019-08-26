-- Adapted from https://www.thingiverse.com/thing:281539

code = [[

float solid(vec3 p) 
{
  float v = sqrt(p.x*p.x+p.y*p.y+p.z*p.z);
  if ((abs(cos(2.0*p.x)+cos(2.0*p.y)+cos(2.0*p.z)) < 0.45) && (6.0 < v) && (v < 9.0)) {
    return -1.0;
  } else {
    return 1.0;
  }
}
]]

n = 20
s = implicit_solid(v(-n/2,-n/2,-n/2), v(n/2,n/2,n/2), 0.05, code)
emit(scale(2)*s)
