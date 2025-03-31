import sys
from typing import TextIO

import chip


# input key A0, A1, A2, A3,  B0, B1, B2, B3,
def read_file(file_in: TextIO, file_out: TextIO) -> None:
    pass


def run_chip(command: list[int]) -> list[int]:

    output: list[int]
    return output


# output key F0, F1, F2, F3,  AB, Cout, Px, Gy
def write_file(output: list[int], file_out: TextIO) -> None:
    file_out.write(
        f"{output[0]}{output[1]}{output[2]}{output[3]} {output[4]}{output[5]}{output[6]}{output[7]}\n"
    )


def main() -> None:
    if len(sys.argv) > 1:
        file_path: str = sys.argv[1]
        file_in: TextIO = open(file_path + "files/input.txt", "r")
        file_out: TextIO = open(file_path + "files/output.txt", "w")
        read_file(file_in, file_out)

        file_in.close()
        file_out.close()

    else:
        print("ERROR NO TEXT FILE GIVEN")
        sys.exit(1)
