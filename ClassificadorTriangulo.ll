; ModuleID = "meu_programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 3, i32* %"a"
  %"b" = alloca i32
  store i32 4, i32* %"b"
  %"c" = alloca i32
  store i32 5, i32* %"c"
  %".5" = load i32, i32* %"a"
  %".6" = load i32, i32* %"b"
  %".7" = add i32 %".5", %".6"
  %"_t0" = alloca i32
  store i32 %".7", i32* %"_t0"
  %".9" = load i32, i32* %"_t0"
  %".10" = load i32, i32* %"c"
  %".11" = icmp sgt i32 %".9", %".10"
  %"_t1" = alloca i32
  %".12" = zext i1 %".11" to i32
  store i32 %".12", i32* %"_t1"
  %".14" = load i32, i32* %"a"
  %".15" = load i32, i32* %"c"
  %".16" = add i32 %".14", %".15"
  %"_t2" = alloca i32
  store i32 %".16", i32* %"_t2"
  %".18" = load i32, i32* %"_t2"
  %".19" = load i32, i32* %"b"
  %".20" = icmp sgt i32 %".18", %".19"
  %"_t3" = alloca i32
  %".21" = zext i1 %".20" to i32
  store i32 %".21", i32* %"_t3"
  %".23" = load i32, i32* %"_t1"
  %".24" = load i32, i32* %"_t3"
  %".25" = trunc i32 %".23" to i1
  %".26" = trunc i32 %".24" to i1
  %".27" = and i1 %".25", %".26"
  %"_t4" = alloca i32
  %".28" = zext i1 %".27" to i32
  store i32 %".28", i32* %"_t4"
  %".30" = load i32, i32* %"b"
  %".31" = load i32, i32* %"c"
  %".32" = add i32 %".30", %".31"
  %"_t5" = alloca i32
  store i32 %".32", i32* %"_t5"
  %".34" = load i32, i32* %"_t5"
  %".35" = load i32, i32* %"a"
  %".36" = icmp sgt i32 %".34", %".35"
  %"_t6" = alloca i32
  %".37" = zext i1 %".36" to i32
  store i32 %".37", i32* %"_t6"
  %".39" = load i32, i32* %"_t4"
  %".40" = load i32, i32* %"_t6"
  %".41" = trunc i32 %".39" to i1
  %".42" = trunc i32 %".40" to i1
  %".43" = and i1 %".41", %".42"
  %"_t7" = alloca i32
  %".44" = zext i1 %".43" to i32
  store i32 %".44", i32* %"_t7"
  %".46" = load i32, i32* %"_t7"
  %".47" = trunc i32 %".46" to i1
  br i1 %".47", label %"if_true", label %"L0"
L2:
  %".74" = load i32, i32* %"a"
  %".75" = load i32, i32* %"b"
  %".76" = icmp eq i32 %".74", %".75"
  %"_t11" = alloca i32
  %".77" = zext i1 %".76" to i32
  store i32 %".77", i32* %"_t11"
  %".79" = load i32, i32* %"a"
  %".80" = load i32, i32* %"c"
  %".81" = icmp eq i32 %".79", %".80"
  %"_t12" = alloca i32
  %".82" = zext i1 %".81" to i32
  store i32 %".82", i32* %"_t12"
  %".84" = load i32, i32* %"_t11"
  %".85" = load i32, i32* %"_t12"
  %".86" = trunc i32 %".84" to i1
  %".87" = trunc i32 %".85" to i1
  %".88" = or i1 %".86", %".87"
  %"_t13" = alloca i32
  %".89" = zext i1 %".88" to i32
  store i32 %".89", i32* %"_t13"
  %".91" = load i32, i32* %"b"
  %".92" = load i32, i32* %"c"
  %".93" = icmp eq i32 %".91", %".92"
  %"_t14" = alloca i32
  %".94" = zext i1 %".93" to i32
  store i32 %".94", i32* %"_t14"
  %".96" = load i32, i32* %"_t13"
  %".97" = load i32, i32* %"_t14"
  %".98" = trunc i32 %".96" to i1
  %".99" = trunc i32 %".97" to i1
  %".100" = or i1 %".98", %".99"
  %"_t15" = alloca i32
  %".101" = zext i1 %".100" to i32
  store i32 %".101", i32* %"_t15"
  %".103" = load i32, i32* %"_t15"
  %".104" = trunc i32 %".103" to i1
  br i1 %".104", label %"if_true.2", label %"L4"
L4:
  %".111" = alloca [27 x i8]
  store [27 x i8] c"Tri\c3\a2ngulo escaleno v\c3\a1lido\0a\00", [27 x i8]* %".111"
  %".113" = bitcast [27 x i8]* %".111" to i8*
  %".114" = call i32 (i8*, ...) @"printf"(i8* %".113")
  br label %"L5"
L5:
  br label %"L3"
L3:
  br label %"L1"
L0:
  %".118" = alloca [38 x i8]
  store [38 x i8] c"Medidas inv\c3\a1lidas para um tri\c3\a2ngulo.\0a\00", [38 x i8]* %".118"
  %".120" = bitcast [38 x i8]* %".118" to i8*
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".120")
  br label %"L1"
L1:
  ret i32 0
if_true:
  %".49" = load i32, i32* %"a"
  %".50" = load i32, i32* %"b"
  %".51" = icmp eq i32 %".49", %".50"
  %"_t8" = alloca i32
  %".52" = zext i1 %".51" to i32
  store i32 %".52", i32* %"_t8"
  %".54" = load i32, i32* %"b"
  %".55" = load i32, i32* %"c"
  %".56" = icmp eq i32 %".54", %".55"
  %"_t9" = alloca i32
  %".57" = zext i1 %".56" to i32
  store i32 %".57", i32* %"_t9"
  %".59" = load i32, i32* %"_t8"
  %".60" = load i32, i32* %"_t9"
  %".61" = trunc i32 %".59" to i1
  %".62" = trunc i32 %".60" to i1
  %".63" = and i1 %".61", %".62"
  %"_t10" = alloca i32
  %".64" = zext i1 %".63" to i32
  store i32 %".64", i32* %"_t10"
  %".66" = load i32, i32* %"_t10"
  %".67" = trunc i32 %".66" to i1
  br i1 %".67", label %"if_true.1", label %"L2"
if_true.1:
  %".69" = alloca [29 x i8]
  store [29 x i8] c"Tri\c3\a2ngulo equil\c3\a1tero v\c3\a1lido\0a\00", [29 x i8]* %".69"
  %".71" = bitcast [29 x i8]* %".69" to i8*
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".71")
  br label %"L3"
if_true.2:
  %".106" = alloca [28 x i8]
  store [28 x i8] c"Tri\c3\a2ngulo is\c3\b3sceles v\c3\a1lido\0a\00", [28 x i8]* %".106"
  %".108" = bitcast [28 x i8]* %".106" to i8*
  %".109" = call i32 (i8*, ...) @"printf"(i8* %".108")
  br label %"L5"
}
