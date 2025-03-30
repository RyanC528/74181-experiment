# each block is listed from the chart
# starting from top left, moving down then right
# end goal each block have only one ouypuy

# A,B,C... are and gates, O or gates and X xor gates


def left_block1(A1: bin, A2: bin, A3: bin, B1: bin, B2: bin, B3: bin) -> bin:
    return ~((A1 & A2 & A3) | (B1 & B2 & B3))


def left_block2(A1: bin, A2: bin, B1: bin, B2: bin, C1: bin) -> bin:
    return ~((A1 & A2) | (B1 & B2) | (C1))


def right_block1(
    A1: bin,
    B1: bin,
    B2: bin,
    C1: bin,
    C2: bin,
    C3: bin,
    D1: bin,
    D2: bin,
    D3: bin,
    D4: bin,
) -> bin:
    return ~((A1) | (B1 & B2) | (C1 & C2 & C3) | (D1 & D2 & D3 & D4))


def right_block2(
    A1: bin,
    A2: bin,
    A3: bin,
    A4: bin,
    A5: bin,
    B1: bin,
    B2: bin,
    B3: bin,
    B4: bin,
    C1: bin,
    C2: bin,
    C3: bin,
    D1: bin,
    D2: bin,
) -> bin:
    return ~(
        (A1 & A2 & A3 & A4 & A5) | (B1 & B2 & B3 & B4) | (C1 & C2 & C3) | (D1 & D2)
    )


def right_block3(
    A1: bin, A2: bin, A3: bin, A4: bin, B1: bin, B2: bin, B3: bin, C1: bin, C2: bin
) -> bin:
    return ~((A1 & A2 & A3 & A4) | (B1 & B2 & B3) | (C1 & C2))


def right_block4(A1: bin, A2: bin, A3: bin, B1: bin, B2: bin) -> bin:
    return ~((A1 & A2 & A3) | (B1 & B2))


def chip(
    # input 1
    A0: bin,
    A1: bin,
    A2: bin,
    A3: bin,
    # input 2
    B0: bin,
    B1: bin,
    B2: bin,
    B3: bin,
    # select
    S0: bin,
    S1: bin,
    S2: bin,
    S3: bin,
    # other
    Cn: bin,
    M: bin,
    Cout: bin,
    PX: bin,
) -> bin:
    # set
    M = ~M

    # output
    F0: bin = 0
    F1: bin = 0
    F2: bin = 0
    F3: bin = 0

    nor1 = left_block1(B3, S3, A3, A3, S2, ~B3)
    nor3 = left_block1(B2, S3, A2, A2, S2, ~B2)
    nor5 = left_block1(B1, S3, A1, A1, S2, ~B1)
    nor7 = left_block1(B0, S3, A0, A0, S2, ~B0)

    nor2 = left_block2(~B3, S1, S0, B3, A3)
    nor4 = left_block2(~B2, S1, S0, B2, A2)
    nor6 = left_block2(~B1, S1, S0, B1, A1)
    nor8 = left_block2(~B0, S1, S0, B0, A0)

    F0 = (nor8 ^ nor7) ^ ~(M & Cn)
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

    return F0, F1, F2, F3, AB, Cout, PX, GY
