# each block is listed from the chart
# starting from top left, moving down then right
# end goal each block have only one ouypuy

# A,B,C... are and gates, O or gates and X xor gates


def left_block1(A1: bin, A2: bin, A3: bin, B1: bin, B2: bin, B3: bin) -> bin:
    return ~((A1 & A2 & A3) | (B1 & B2 & B3))


def left_block2(A1: bin, A2: bin, B1: bin, B2: bin, C1: bin) -> bin:
    return ~((A1 & A2) | (B1 & B2) | (C1))


def right_block1() -> bin:
    pass


def right_block2() -> bin:
    pass


def right_block3() -> bin:
    pass


def right_block4() -> bin:
    pass


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
    P: bin,
) -> bin[4]:
    # set
    Vcc: bin = 1
    Gnd: bin = 0

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
