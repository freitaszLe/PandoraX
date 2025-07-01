a = 3
b = 4
c = 5
_t0 = a + b
_t1 = _t0 > c
_t2 = a + c
_t3 = _t2 > b
_t4 = _t1 and _t3
_t5 = b + c
_t6 = _t5 > a
_t7 = _t4 and _t6
if_false _t7 goto L0
_t8 = a == b
_t9 = b == c
_t10 = _t8 and _t9
if_false _t10 goto L2
print <Triângulo equilátero válido>
goto L3
L2:
_t11 = a == b
_t12 = a == c
_t13 = _t11 or _t12
_t14 = b == c
_t15 = _t13 or _t14
if_false _t15 goto L4
print <Triângulo isósceles válido>
goto L5
L4:
print <Triângulo escaleno válido>
L5:
L3:
goto L1
L0:
print <Medidas inválidas para um triângulo.>
L1:
