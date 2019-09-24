-- IceSL Lua script
-- (c) by Rolf Werum, weruminger@gmail.com
-- Model: Platform to lay a mobile phone
--        EQ planar on an GEM Telescope mount
--        fixed with a VIXEN Clamp

objPrism = {v(2.5,0),v(41,0),v(43.5,13.3),v(0,13.3)}
objDir = v(0,0,103.3)
prism = linear_extrude(objDir,objPrism)


objSteg = {v(4,0),v(9,0),v(13,6),v(0,6)}
objDirSteg = v(0,0,60)
steg = rotate(0,90,0) * linear_extrude(objDirSteg, objSteg)

stripesA = union( 
{translate(0,0,0) * steg,
translate(0,0,15) * steg,
translate(0,0,30) * steg,
translate(0,0,45) * steg,
translate(0,0,60) * steg,
translate(0,0,75) * steg,
translate(0,0,90) * steg } )

plate = translate(21.75,-3.3,0) * cube(60,6,100)
conterPlate = translate(21.75,-9.3,0) * cube(60,6,6)
mountStopper = rotate(90,0,0) * translate(21.75,95,-19) * cylinder(4,6)

boltCutC = union(rotate(90,0,0) * translate(6.75,6.5,-19) * cylinder(1.7,30),
 rotate(90,0,0) * translate(6.75,6.5,-19) * cylinder(3.2,10) )

boltCut = union({
translate(0,0,0) * boltCutC,
translate(14,0,0) * boltCutC,
translate(28,0,0) * boltCutC
})
stripe = translate(21.75,-3.3,10) * cube(60,6,10)

objModelF = union ( { translate(-8,-6,13)*stripesA,prism, mountStopper } )
objModel=rotate(90,0,0) * difference(objModelF, boltCut)

emit(objModel)