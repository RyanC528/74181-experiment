import chip
import sys


def chip_loop(command: str, file_out) -> None:
    output: bin[8]

    hold: bin[12] = command_to_bin(command)

    output = chip.chip(
        hold[0],
        hold[1],
        hold[2],
        hold[3],
        hold[4],
        hold[5],
        hold[6],
        hold[7],
        hold[8],
        hold[9],
        hold[10],
        hold[11],
    )

    file_out.writeline(bin_output(output))


def command_to_bin(command: str) -> bin[12]:
    output: bin[12]

    for i, num in enumerate(command):
        output[i] = bin(num)

    return output


def bin_output(sum: bin[8]):
    output: str = ""

    for bit in sum:
        output.appemd(chr(bit))

    return output


def main():
    if len(sys.argv) > 1:
        file_path: str = sys.argv(1)
        file_in = open(file_path + "files/input.txt", "r")
        file_out = open(file_path + "files/output.txt", "w")

    else:
        print("ERROR NO TEXT FILE GIVEN")
        sys.exit(1)
