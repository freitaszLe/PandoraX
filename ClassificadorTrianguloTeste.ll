; ModuleID = "meu_programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([19 x i8], [19 x i8]* @"prompt_str_4", i32 0, i32 0))
  %"input_buffer" = alloca i32
  %".3" = call i32 (i8*, ...) @"scanf"(i8* getelementptr ([3 x i8], [3 x i8]* @"scanf_fmt_3", i32 0, i32 0), i32* %"input_buffer")
  %".4" = load i32, i32* %"input_buffer"
  %"_t0" = alloca i32
  store i32 %".4", i32* %"_t0"
  %"a" = alloca i32
  %".6" = load i32, i32* %"_t0"
  store i32 %".6", i32* %"a"
  %".8" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([19 x i8], [19 x i8]* @"prompt_str_5", i32 0, i32 0))
  %"input_buffer.1" = alloca i32
  %".9" = call i32 (i8*, ...) @"scanf"(i8* getelementptr ([3 x i8], [3 x i8]* @"scanf_fmt_3", i32 0, i32 0), i32* %"input_buffer.1")
  %".10" = load i32, i32* %"input_buffer.1"
  %"_t1" = alloca i32
  store i32 %".10", i32* %"_t1"
  %"b" = alloca i32
  %".12" = load i32, i32* %"_t1"
  store i32 %".12", i32* %"b"
  %".14" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([19 x i8], [19 x i8]* @"prompt_str_6", i32 0, i32 0))
  %"input_buffer.2" = alloca i32
  %".15" = call i32 (i8*, ...) @"scanf"(i8* getelementptr ([3 x i8], [3 x i8]* @"scanf_fmt_3", i32 0, i32 0), i32* %"input_buffer.2")
  %".16" = load i32, i32* %"input_buffer.2"
  %"_t2" = alloca i32
  store i32 %".16", i32* %"_t2"
  %"c" = alloca i32
  %".18" = load i32, i32* %"_t2"
  store i32 %".18", i32* %"c"
  %"0" = alloca i32
  %".20" = load i32, i32* %"a"
  %".21" = load i32, i32* %"0"
  %".22" = icmp sle i32 %".20", %".21"
  %"_t3" = alloca i32
  %".23" = zext i1 %".22" to i32
  store i32 %".23", i32* %"_t3"
  %".25" = load i32, i32* %"b"
  %".26" = load i32, i32* %"0"
  %".27" = icmp sle i32 %".25", %".26"
  %"_t4" = alloca i32
  %".28" = zext i1 %".27" to i32
  store i32 %".28", i32* %"_t4"
  %".30" = load i32, i32* %"_t3"
  %".31" = load i32, i32* %"_t4"
  %".32" = trunc i32 %".30" to i1
  %".33" = trunc i32 %".31" to i1
  %".34" = or i1 %".32", %".33"
  %"_t5" = alloca i32
  %".35" = zext i1 %".34" to i32
  store i32 %".35", i32* %"_t5"
  %".37" = load i32, i32* %"c"
  %".38" = load i32, i32* %"0"
  %".39" = icmp sle i32 %".37", %".38"
  %"_t6" = alloca i32
  %".40" = zext i1 %".39" to i32
  store i32 %".40", i32* %"_t6"
  %".42" = load i32, i32* %"_t5"
  %".43" = load i32, i32* %"_t6"
  %".44" = trunc i32 %".42" to i1
  %".45" = trunc i32 %".43" to i1
  %".46" = or i1 %".44", %".45"
  %"_t7" = alloca i32
  %".47" = zext i1 %".46" to i32
  store i32 %".47", i32* %"_t7"
  %".49" = load i32, i32* %"_t7"
  %".50" = trunc i32 %".49" to i1
  br i1 %".50", label %"if_true", label %"L0"
L0:
  %".54" = load i32, i32* %"a"
  %".55" = load i32, i32* %"b"
  %".56" = add i32 %".54", %".55"
  %"_t8" = alloca i32
  store i32 %".56", i32* %"_t8"
  %".58" = load i32, i32* %"_t8"
  %".59" = load i32, i32* %"c"
  %".60" = icmp sgt i32 %".58", %".59"
  %"_t9" = alloca i32
  %".61" = zext i1 %".60" to i32
  store i32 %".61", i32* %"_t9"
  %".63" = load i32, i32* %"a"
  %".64" = load i32, i32* %"c"
  %".65" = add i32 %".63", %".64"
  %"_t10" = alloca i32
  store i32 %".65", i32* %"_t10"
  %".67" = load i32, i32* %"_t10"
  %".68" = load i32, i32* %"b"
  %".69" = icmp sgt i32 %".67", %".68"
  %"_t11" = alloca i32
  %".70" = zext i1 %".69" to i32
  store i32 %".70", i32* %"_t11"
  %".72" = load i32, i32* %"_t9"
  %".73" = load i32, i32* %"_t11"
  %".74" = trunc i32 %".72" to i1
  %".75" = trunc i32 %".73" to i1
  %".76" = and i1 %".74", %".75"
  %"_t12" = alloca i32
  %".77" = zext i1 %".76" to i32
  store i32 %".77", i32* %"_t12"
  %".79" = load i32, i32* %"b"
  %".80" = load i32, i32* %"c"
  %".81" = add i32 %".79", %".80"
  %"_t13" = alloca i32
  store i32 %".81", i32* %"_t13"
  %".83" = load i32, i32* %"_t13"
  %".84" = load i32, i32* %"a"
  %".85" = icmp sgt i32 %".83", %".84"
  %"_t14" = alloca i32
  %".86" = zext i1 %".85" to i32
  store i32 %".86", i32* %"_t14"
  %".88" = load i32, i32* %"_t12"
  %".89" = load i32, i32* %"_t14"
  %".90" = trunc i32 %".88" to i1
  %".91" = trunc i32 %".89" to i1
  %".92" = and i1 %".90", %".91"
  %"_t15" = alloca i32
  %".93" = zext i1 %".92" to i32
  store i32 %".93", i32* %"_t15"
  %".95" = load i32, i32* %"_t15"
  %".96" = trunc i32 %".95" to i1
  br i1 %".96", label %"if_true.1", label %"L2"
L4:
  %".120" = load i32, i32* %"a"
  %".121" = load i32, i32* %"b"
  %".122" = icmp eq i32 %".120", %".121"
  %"_t19" = alloca i32
  %".123" = zext i1 %".122" to i32
  store i32 %".123", i32* %"_t19"
  %".125" = load i32, i32* %"a"
  %".126" = load i32, i32* %"c"
  %".127" = icmp eq i32 %".125", %".126"
  %"_t20" = alloca i32
  %".128" = zext i1 %".127" to i32
  store i32 %".128", i32* %"_t20"
  %".130" = load i32, i32* %"_t19"
  %".131" = load i32, i32* %"_t20"
  %".132" = trunc i32 %".130" to i1
  %".133" = trunc i32 %".131" to i1
  %".134" = or i1 %".132", %".133"
  %"_t21" = alloca i32
  %".135" = zext i1 %".134" to i32
  store i32 %".135", i32* %"_t21"
  %".137" = load i32, i32* %"b"
  %".138" = load i32, i32* %"c"
  %".139" = icmp eq i32 %".137", %".138"
  %"_t22" = alloca i32
  %".140" = zext i1 %".139" to i32
  store i32 %".140", i32* %"_t22"
  %".142" = load i32, i32* %"_t21"
  %".143" = load i32, i32* %"_t22"
  %".144" = trunc i32 %".142" to i1
  %".145" = trunc i32 %".143" to i1
  %".146" = or i1 %".144", %".145"
  %"_t23" = alloca i32
  %".147" = zext i1 %".146" to i32
  store i32 %".147", i32* %"_t23"
  %".149" = load i32, i32* %"_t23"
  %".150" = trunc i32 %".149" to i1
  br i1 %".150", label %"if_true.3", label %"L6"
L6:
  %".154" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([29 x i8], [29 x i8]* @"print_str_10", i32 0, i32 0))
  br label %"L7"
L7:
  br label %"L5"
L5:
  br label %"L3"
L2:
  %".158" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([20 x i8], [20 x i8]* @"print_str_11", i32 0, i32 0))
  br label %"L3"
L3:
  br label %"L1"
L1:
  ret i32 0
if_true:
  %".52" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([43 x i8], [43 x i8]* @"print_str_7", i32 0, i32 0))
  br label %"L1"
if_true.1:
  %".98" = load i32, i32* %"a"
  %".99" = load i32, i32* %"b"
  %".100" = icmp eq i32 %".98", %".99"
  %"_t16" = alloca i32
  %".101" = zext i1 %".100" to i32
  store i32 %".101", i32* %"_t16"
  %".103" = load i32, i32* %"b"
  %".104" = load i32, i32* %"c"
  %".105" = icmp eq i32 %".103", %".104"
  %"_t17" = alloca i32
  %".106" = zext i1 %".105" to i32
  store i32 %".106", i32* %"_t17"
  %".108" = load i32, i32* %"_t16"
  %".109" = load i32, i32* %"_t17"
  %".110" = trunc i32 %".108" to i1
  %".111" = trunc i32 %".109" to i1
  %".112" = and i1 %".110", %".111"
  %"_t18" = alloca i32
  %".113" = zext i1 %".112" to i32
  store i32 %".113", i32* %"_t18"
  %".115" = load i32, i32* %"_t18"
  %".116" = trunc i32 %".115" to i1
  br i1 %".116", label %"if_true.2", label %"L4"
if_true.2:
  %".118" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([32 x i8], [32 x i8]* @"print_str_8", i32 0, i32 0))
  br label %"L5"
if_true.3:
  %".152" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([31 x i8], [31 x i8]* @"print_str_9", i32 0, i32 0))
  br label %"L7"
}

@"scanf_fmt_3" = internal constant [3 x i8] c"%d\00"
@"prompt_str_4" = internal constant [19 x i8] c"Digite o lado A:  \00"
@"prompt_str_5" = internal constant [19 x i8] c"Digite o lado B:  \00"
@"prompt_str_6" = internal constant [19 x i8] c"Digite o lado C:  \00"
@"print_str_7" = internal constant [43 x i8] c"Erro: medidas devem ser maiores que zero.\0a\00"
@"print_str_8" = internal constant [32 x i8] c"Tri\c3\a2ngulo equil\c3\a1tero v\c3\a1lido\0a\00"
@"print_str_9" = internal constant [31 x i8] c"Tri\c3\a2ngulo is\c3\b3sceles v\c3\a1lido\0a\00"
@"print_str_10" = internal constant [29 x i8] c"Tri\c3\a2ngulo escaleno v\c3\a1lido\0a\00"
@"print_str_11" = internal constant [20 x i8] c"Medidas inv\c3\a1lidas\0a\00"