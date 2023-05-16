import sys

def make_slots(size):
    i = 0
    result = []
    while i < size:
        result.append("")
        i = i + 1
    return result


def gen_str_wrap(alphabet, max_length):
    i = 1
    while i <= max_length :
        gen_str(alphabet, make_slots(i), i)
        i = i + 1

def convert2string(slots):
    i = 0
    result = ""
    while (i < len(slots)):
        result = result + slots[i]
        i = i + 1
    return result


def gen_str(alphabet, slots, current):
    if current > 0:
        position = len(slots) - current
        i = 0
        while i < len(alphabet) :
            slots[position] = alphabet[i]
            gen_str(alphabet, slots, current - 1)
            i = i + 1
    else:
        print(convert2string(slots))
    

print("generating...")
gen_str_wrap(sys.argv[1], int(sys.argv[2]))

