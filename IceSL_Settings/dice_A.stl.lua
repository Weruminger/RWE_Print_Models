emit(Void)
m0 = load('C:/Users/werum/GIT_REPO/RWE_Print_Models/Models/STL/_TEST_/dice_A.stl')
m0 = rotate(0,0,0) * scale(1) * m0
emit(m0, 0)
m1 = load('C:/Users/werum/GIT_REPO/RWE_Print_Models/Models/STL/_TEST_/dice_B.stl')
m1 = rotate(0,0,0) * scale(1) * m1
emit(m1, 1)
