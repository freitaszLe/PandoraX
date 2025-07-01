a = None
b = None
c = None
_t0 = a <= 0
_t1 = b <= 0
_t2 = _t0 or _t1
_t3 = c <= 0
_t4 = _t2 or _t3
if_false _t4 goto L0
print <Erro: medidas devem ser maiores que zero.>
goto L1
L0:
_t5 = a + b
_t6 = _t5 > c
_t7 = a + c
_t8 = _t7 > b
_t9 = _t6 and _t8
_t10 = b + c
_t11 = _t10 > a
_t12 = _t9 and _t11
if_false _t12 goto L2
_t13 = a == b
_t14 = b == c
_t15 = _t13 and _t14
if_false _t15 goto L4
print <Triângulo equilátero válido>
goto L5
L4:
_t16 = a == b
_t17 = a == c
_t18 = _t16 or _t17
_t19 = b == c
_t20 = _t18 or _t19
if_false _t20 goto L6
print <Triângulo isósceles válido>
goto L7
L6:
print <Triângulo escaleno válido>
L7:
L5:
goto L3
L2:
print <Medidas inválidas>
L3:
L1:
