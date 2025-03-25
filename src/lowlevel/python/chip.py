def or_2_and_inputs(a_1: bin, a_2: bin, a_3: bin, b_1: bin, b_2: bin, b_3: bin) -> bin:
    return (a_1 & a_2 & a_3) ^ (b_1 & b_2 & b_3)


def or_3_and_inputs(a_1: bin, a_2: bin, b_1: bin, b_2: bin, c_1: bin, c_2: bin) -> bin:
    return (a_1 & a_2) ^ (b_1 & b_2) ^ (c_1 & c_2)


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

    nor_1: bin = ~or_2_and_inputs(B3, S2, A3, A3, S2, ~B3)
    nor_2: bin = ~or_3_and_inputs(~B3, S1, S0, B3, A3, A3)

    nor_3: bin = ~or_2_and_inputs(B2, S3, A2, A2, S2, ~B2)
    nor_4: bin = ~or_3_and_inputs(~B2, S1, S0, B2, A2, A2)

    nor_5: bin = ~or_2_and_inputs(B1, S3, A1, A1, S2, ~B1)
    nor_6: bin = ~or_3_and_inputs(~B1, S1, S0, B1, A1, A1)

    nor_7: bin = ~or_2_and_inputs(B0, S3, A0, A0, S2, ~B0)
    nor_8: bin = ~or_3_and_inputs(~B0, S1, S0, B0, A0, A0)

    F0 = ~(~M & Cn) ^ (nor_8 ^ nor_7)
