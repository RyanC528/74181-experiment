package main

fun left_block1(A1: Byte, A2: Byte, A3: Byte, B1: Byte, B2: Byte, B3: Byte): Byte {
    var output: Byte

    output = (A1 and A2 and A3) or (B1 and B2 and B3)

    return output
}

fun left_block2(A1: Byte, A2: Byte, B1: Byte, B2: Byte, C1: Byte, C2: Byte): Byte {
    val output: Byte = (A1 and A2) or (B1 and B2) or (C1 and C2)

    return output
}

fun right_block1(
        A1: Byte,
        B1: Byte,
        B2: Byte,
        C1: Byte,
        C2: Byte,
        C3: Byte,
        D1: Byte,
        D2: Byte,
        D3: Byte,
        D4: Byte
): Byte {
    val output: Byte = ((A1) or (B1 and B2) or (C1 and C2 and C3) or (D1 and D2 and D3 and D4))

    return output
}

fun right_block2(
        A1: Byte,
        A2: Byte,
        A3: Byte,
        A4: Byte,
        A5: Byte,
        B1: Byte,
        B2: Byte,
        B3: Byte,
        B4: Byte,
        C1: Byte,
        C2: Byte,
        C3: Byte,
        D1: Byte,
        D2: Byte
): Byte {
    val output: Byte =
            ((A1 and A2 and A3 and A4 and A5) or
                    (B1 and B2 and B3 and B4) or
                    (C1 and C2 and C3) or
                    (D1 and D2))

    return output
}

fun right_block3(
        A1: Byte,
        A2: Byte,
        A3: Byte,
        A4: Byte,
        B1: Byte,
        B2: Byte,
        B3: Byte,
        C1: Byte,
        C2: Byte
): Byte {
    val output: Byte = ((A1 and A2 and A3 and A4) or (B1 and B2 and B3) or (C1 and C2))

    return output
}

fun right_block4(A1: Byte, A2: Byte, A3: Byte, A4: Byte, B1: Byte, B2: Byte): Byte {
    val output: Byte = ((A1 and A2 and A3) or (B1 and B2))

    return output
}

fun chip(numbers: Byte, command: Byte): Byte {

    val nor1: Byte = left_block1()
    val nor3: Byte = left_block1()
    val nor5: Byte = left_block1()
    val nor7: Byte = left_block1()

    val nor2: Byte = left_block2()
    val nor4: Byte = left_block2()
    val nor6: Byte = left_block2()
    val nor8: Byte = left_block2()

    val output: Byte

    return output
}
