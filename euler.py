fibinachi_thing_main = 1
fibinachi_thing_1_before = 1
fibinachi_thing_2_before = 0
total = 0
while fibinachi_thing_main < 4000000:
    # print(fibinachi_thing_main)
    total += fibinachi_thing_main
    fibinachi_thing_main = fibinachi_thing_1_before + fibinachi_thing_2_before
    fibinachi_thing_2_before = fibinachi_thing_1_before
    fibinachi_thing_1_before = fibinachi_thing_main
print(total)
