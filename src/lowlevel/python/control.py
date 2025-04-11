import sys
from typing import TextIO

import chip


# input key A0, A1, A2, A3,  B0, B1, B2, B3,
def read_file(file_in: TextIO, file_out: TextIO) -> None:
    command: list[int] = [
        0,  # A0
        0,  # A1
        0,  # A2
        0,  # A3
        0,  # B0
        0,  # B1
        0,  # B2
        0,  # B3
        0,  # S0
        0,  # S1
        0,  # S2
        0,  # S3
        0,  # CN
        0,  # M
    ]
    for line in file_in:
        command[0] = int(line[0])
        command[1] = int(line[1])
        command[2] = int(line[2])
        command[3] = int(line[3])

        command[4] = int(line[5])
        command[5] = int(line[6])
        command[6] = int(line[7])
        command[7] = int(line[8])

        command[8] = int(line[10])
        command[9] = int(line[11])
        command[10] = int(line[12])
        command[11] = int(line[13])

        command[12] = int(line[15])
        command[13] = int(line[16])

        run_chip(command)


def run_chip(command: list[int]) -> list[int]:

    output: list[int] = chip.chip(
        #changed edditor and now wont take command as an input
        command[0],
        command[1],
        command[2],
        command[3],
        command[4],
        command[5],
        command[6],
        command[7],
        command[8],
        command[9],
        command[10],
        command[11],
        command[12],
        command[13]
    )
    return output


# output key F0, F1, F2, F3,  AB, Cout, Px, Gy
def write_file(output: list[int], file_out: TextIO) -> None:
    file_out.write(
        f"{output[0]}{output[1]}{output[2]}{output[3]} {output[4]}{output[5]}{output[6]}{output[7]}\n"
    )


def main() -> int:
    if len(sys.argv) > 1:
        file_path: str = sys.argv[1]
        file_in: TextIO = open(file_path + "files/input.txt", "r")
        file_out: TextIO = open(file_path + "files/output.txt", "w")
        read_file(file_in, file_out)

        file_in.close()
        file_out.close()

        return 0

    else:
        print("ERROR NO TEXT FILE GIVEN")
        sys.exit(1)

        return 1
