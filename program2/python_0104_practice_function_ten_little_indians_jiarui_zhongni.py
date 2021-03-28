def lyric_main(s1, s2, s3):
    print(f"{s1} little, {s2} little, {s3} little Indians")


def lyric_end(s4, s5):
    print(f"{s4} little Indian boy{s5}")


print("")

lyric_main("One", "two", "three")
lyric_main("Four", "five", "six")
lyric_main("Seven", "eight", "nine")
lyric_end("Ten", "s")

print("")

lyric_main("Ten", "nine", "eight")
lyric_main("Seven", "six", "five")
lyric_main("Four", "three", "two")
lyric_end("One", "")