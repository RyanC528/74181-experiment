package main

// WHY CAN'T I JUST MAKE AN ARRAY OF BITS
// I have to make a custom not because compilenting 1 != 0
fun bit_not(input: Int): Int {
    val output = input.inv()

    return (output and 1) // hack to
}

fun left_block1(A1: Int, A2: Int, A3: Int, B1: Int, B2: Int, B3: Int): Int {
    var output: Int

    output = (A1 and A2 and A3) or (B1 and B2 and B3)

    return output
}

fun left_block2(A1: Int, A2: Int, B1: Int, B2: Int, C1: Int): Int {
    val output: Int = (A1 and A2) or (B1 and B2) or (C1)

    return output
}

fun right_block1(
        A1: Int,
        B1: Int,
        B2: Int,
        C1: Int,
        C2: Int,
        C3: Int,
        D1: Int,
        D2: Int,
        D3: Int,
        D4: Int
): Int {
    val output: Int = ((A1) or (B1 and B2) or (C1 and C2 and C3) or (D1 and D2 and D3 and D4))

    return output
}

fun right_block2(
        A1: Int,
        A2: Int,
        A3: Int,
        A4: Int,
        A5: Int,
        B1: Int,
        B2: Int,
        B3: Int,
        B4: Int,
        C1: Int,
        C2: Int,
        C3: Int,
        D1: Int,
        D2: Int
): Int {
    val output: Int =
            ((A1 and A2 and A3 and A4 and A5) or
                    (B1 and B2 and B3 and B4) or
                    (C1 and C2 and C3) or
                    (D1 and D2))

    return output
}

fun right_block3(
        A1: Int,
        A2: Int,
        A3: Int,
        A4: Int,
        B1: Int,
        B2: Int,
        B3: Int,
        C1: Int,
        C2: Int
): Int {
    val output: Int = ((A1 and A2 and A3 and A4) or (B1 and B2 and B3) or (C1 and C2))

    return output
}

fun right_block4(A1: Int, A2: Int, A3: Int, B1: Int, B2: Int): Int {
    val output: Int = ((A1 and A2 and A3) or (B1 and B2))

    return output
}

fun chip(
        // input 1
        A0: Int,
        A1: Int,
        A2: Int,
        A3: Int,
        // input 2
        B0: Int,
        B1: Int,
        B2: Int,
        B3: Int,
        // select
        S0: Int,
        S1: Int,
        S2: Int,
        S3: Int,
        // other
        Cn: Int,
        M: Int,
): IntArray {

    val nor1: Int = left_block1(B3, S3, A3, A3, S2, bit_not(B3))
    val nor3: Int = left_block1(B2, S3, A2, A2, S2, bit_not(B2))
    val nor5: Int = left_block1(B1, S3, A1, A1, S2, bit_not(B1))
    val nor7: Int = left_block1(B0, S3, A0, A0, S2, bit_not(B0))

    val nor2: Int = left_block2(bit_not(B3), S1, S0, B3, A3)
    val nor4: Int = left_block2(bit_not(B2), S1, S0, B2, A2)
    val nor6: Int = left_block2(bit_not(B1), S1, S0, B1, A1)
    val nor8: Int = left_block2(bit_not(B0), S1, S0, B0, A0)

    val F0: Int = (nor8 xor nor7) xor (M and bit_not(Cn))
    val F1: Int = (nor6 xor nor5) xor right_block4(Cn, nor7, bit_not(M), nor8, bit_not(M))
    val F2: Int = (nor4 xor nor3) xor right_block3(Cn, nor7, nor5, bit_not(M), nor5, nor8, bit_not(M),nor6, bit_not(M))
    val F3: Int = (nor2 xor nor1) xor right_block2(
        Cn, nor7, nor5, nor3, bit_not(M), nor5, nor3, nor8, bit_not(M), nor3, nor6, bit_not(M), nor4, bit_not(M)
    )

    val AB: Int = F0 and F1 and F2 and F3
    val cout: Int = right_block1(
        nor2, nor1, nor4, nor1, nor3, nor6, nor1, nor3, nor5, nor8) ^ (nor1 & nor3 & nor5 & nor7 & Cn)
    )
    val PX: Int = nor1 and nor3 and nor5 and nor7
    val GY: Int = right_block1(nor2, nor1, nor4, nor3, nor6, nor1, nor3, nor5, nor8)

    val output: IntArray = IntArray(8){ F0, F1, F2, F3, AB, cout, PX, GY}

    return output
}
