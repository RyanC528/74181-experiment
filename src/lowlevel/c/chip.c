#include <stdio.h>
#include <stdlib.h>

#include "chip.h"

bool* byte_to_bin(char byte){
    bool* output = (bool*)malloc(8 * sizeof(bool));

    return output;
}

char bin_to_byte(
    bool A,bool B,bool C,bool D,bool E,bool F,bool G,bool H
){
    char output;

    return;
}

bool left_block1(bool A1, bool A2, bool A3, bool B1, bool B2, bool B3){

    return ~((A1 & A2 & A3) | (B1 & B2 & B3));
}

bool left_block2(bool A1, bool A2, bool B1, bool B2, bool C1){

    return ~((A1 & A2) | (B1 & B2) | (C1));
}

bool right_block1(
    bool A1,
    bool B1,
    bool B2,
    bool C1,
    bool C2,
    bool C3,
    bool D1,
    bool D2,
    bool D3,
    bool D4
){

    return ~((A1) | (B1 & B2) | (C1 & C2 & C3) | (D1 & D2 & D3 & D4));
}

bool right_block2(
    bool A1,
    bool A2,
    bool A3,
    bool A4,
    bool A5,
    bool B1,
    bool B2,
    bool B3,
    bool B4,
    bool C1,
    bool C2,
    bool C3,
    bool D1,
    bool D2
){

    return ~((A1 & A2 & A3 & A4 & A5) | (B1 & B2 & B3 & B4) | (C1 & C2 & C3) | (D1 & D2));
}

bool right_block3(
    bool A1,
    bool A2,
    bool A3,
    bool A4,
    bool B1,
    bool B2,
    bool B3,
    bool C1,
    bool C2
){

    return ~((A1 & A2 & A3 & A4) | (B1 & B2 & B3) | (C1 & C2));
}

bool right_block4(
    bool A1,
    bool A2,
    bool A3,
    bool B1,
    bool B2
){

    return ~((A1 & A2 & A3) | (B1 & B2));
}

char chip( char input, char command){
    //decs

    bool A0, A1, A2, A3, B0, B1, B2, B3; //input hold

    bool S0, S1, S2, S3, Cn, M; //command hold

    bool F0, F1, F2, F3, AB, Cout, PX, GY; //output bits

    bool nor1, nor2, nor3, nor4, nor5, nor6, nor7, nor8;//outputs from left hand of schematic

    //decs

    return;
}