# each block is listed from the chart
# starting from top left, moving down then right
# end goal each block have only one ouypuy

# A,B,C... are and gates, O or gates and X xor gates

def bit_not(a: int) -> int:
    return 1 - a


def left_block1(A1: int, A2: int, A3: int, B1: int, B2: int, B3: int) -> int:
    return bit_not((A1 & A2 & A3) | (B1 & B2 & B3))


def left_block2(A1: int, A2: int, B1: int, B2: int, C1: int) -> int:
    return bit_not((A1 & A2) | (B1 & B2) | (C1))


def right_block1(
    A1: int,
    B1: int,
    B2: int,
    C1: int,
    C2: int,
    C3: int,
    D1: int,
    D2: int,
    D3: int,
    D4: int,
) -> int:
    return bit_not((A1) | (B1 & B2) | (C1 & C2 & C3) | (D1 & D2 & D3 & D4))


def right_block2(
    A1: int,
    A2: int,
    A3: int,
    A4: int,
    A5: int,
    B1: int,
    B2: int,
    B3: int,
    B4: int,
    C1: int,
    C2: int,
    C3: int,
    D1: int,
    D2: int,
) -> int:
    return bit_not(
        (A1 & A2 & A3 & A4 & A5) | (B1 & B2 & B3 & B4) | (C1 & C2 & C3) | (D1 & D2)
    )


def right_block3(
    A1: int,
    A2: int,
    A3: int,
    A4: int,
    B1: int,
    B2: int,
    B3: int,
    C1: int,
    C2: int,
) -> int:
    return bit_not((A1 & A2 & A3 & A4) | (B1 & B2 & B3) | (C1 & C2))


def right_block4(A1: int, A2: int, A3: int, B1: int, B2: int) -> int:
    return bit_not((A1 & A2 & A3) | (B1 & B2))


def chip(
    # input 1
    A0: int,
    A1: int,
    A2: int,
    A3: int,
    # input 2
    B0: int,
    B1: int,
    B2: int,
    B3: int,
    # select
    S0: int,
    S1: int,
    S2: int,
    S3: int,
    # other
    Cn: int,
    M: int,
) -> list[int]:
    # set
    M = bit_not(M)

    # output
    F0: int = 0
    F1: int = 0
    F2: int = 0
    F3: int = 0

    nor1: int = left_block1(B3, S3, A3, A3, S2, bit_not(B3))
    nor3: int = left_block1(B2, S3, A2, A2, S2, bit_not(B2))
    nor5: int = left_block1(B1, S3, A1, A1, S2, bit_not(B1))
    nor7: int = left_block1(B0, S3, A0, A0, S2, bit_not(B0))

    nor2: int = left_block2(bit_not(B3), S1, S0, B3, A3)
    nor4: int = left_block2(bit_not(B2), S1, S0, B2, A2)
    nor6: int = left_block2(bit_not(B1), S1, S0, B1, A1)
    nor8: int = left_block2(bit_not(B0), S1, S0, B0, A0)

    F0 = (nor8 ^ nor7) ^ bit_not(M & Cn)
    F1 = (nor6 ^ nor5) ^ right_block4(Cn, nor7, M, nor8, M)
    F2 = (nor4 ^ nor3) ^ right_block3(Cn, nor7, nor5, M, nor5, nor8, M, nor6, M)
    F3 = (nor2 ^ nor1) ^ right_block2(
        Cn, nor7, nor5, nor3, M, nor5, nor3, nor8, M, nor3, nor6, M, nor4, M
    )

    AB = F0 & F1 & F2 & F3
    Cout = right_block1(nor2, nor1, nor4, nor1, nor3, nor6, nor1, nor3, nor5, nor8) ^ (
        nor1 & nor3 & nor5 & nor7 & Cn
    )
    PX = nor1 & nor3 & nor5 & nor7
    GY = right_block1(nor2, nor1, nor4, nor1, nor3, nor6, nor1, nor3, nor5, nor8)

    output: list[int] = [F0, F1, F2, F3, AB, Cout, bit_not(PX), GY]

    return output
