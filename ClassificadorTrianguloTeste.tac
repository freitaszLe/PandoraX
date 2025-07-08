_t0 = summon <Digite o lado A: >
a = _t0
_t1 = summon <Digite o lado B: >
b = _t1
_t2 = summon <Digite o lado C: >
c = _t2
_t3 = a <= 0
_t4 = b <= 0
_t5 = _t3 or _t4
_t6 = c <= 0
_t7 = _t5 or _t6
if_false _t7 goto L0
print <Erro: medidas devem ser maiores que zero.>
goto L1
L0:
_t8 = a + b
_t9 = _t8 > c
_t10 = a + c
_t11 = _t10 > b
_t12 = _t9 and _t11
_t13 = b + c
_t14 = _t13 > a
_t15 = _t12 and _t14
if_false _t15 goto L2
_t16 = a == b
_t17 = b == c
_t18 = _t16 and _t17
if_false _t18 goto L4
print <Triângulo equilátero válido>
goto L5
L4:
_t19 = a == b
_t20 = a == c
_t21 = _t19 or _t20
_t22 = b == c
_t23 = _t21 or _t22
if_false _t23 goto L6
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
