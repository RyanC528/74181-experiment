import unittest

from src.lowlevel.python import chip

# used https://kobi32768.github.io/emulator-74181/ to double check

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

output: list[int] = [
    0,  # F
    0,  # F
    0,  # F
    0,  # F
    0,  # A=B
    0,  # Cout
    0,  # PX
    0,  # GY
]


class test_chip(unittest.TestCase):
    def test_sum(self):
        out: list[int] = chip.chip(
            0,  # A0
            0,  # A1
            1,  # A2
            0,  # A3
            1,  # B0
            0,  # B1
            0,  # B2
            0,  # B3
            1,  # S0
            0,  # S1
            0,  # S2
            0,  # S3
            1,  # CN
            0,  # M
        )
        self.assertEqual(
            out,
            [
                1,  # F0
                0,  # F1
                1,  # F2
                0,  # F3
                0,  # A=B
                1,  # Cout
                0,  # PX
                0,  # GY
            ],
            "sum fail",
        )

    def test_a1(self):
        out: list[int] = chip.chip(
            0,  # A0
            1,  # A1
            0,  # A2
            1,  # A3
            1,  # B0
            0,  # B1
            1,  # B2
            0,  # B3
            0,  # S0
            0,  # S1
            0,  # S2
            0,  # S3
            0,  # CN
            0,  # M
        )
        self.assertEqual(
            out,
            [
                1,  # F
                1,  # F
                0,  # F
                1,  # F
                0,  # A=B
                0,  # Cout
                0,  # PX
                0,  # GY
            ],
            "+1 fail",
        )

    def test_minus(self):
        out: list[int] = chip.chip(
            0,  # A0
            1,  # A1
            0,  # A2
            1,  # A3
            0,  # B0
            0,  # B1
            0,  # B2
            0,  # B3
            1,  # S0
            1,  # S1
            1,  # S2
            1,  # S3
            1,  # CN
            0,  # M
        )
        self.assertEqual(
            out,
            [
                1,  # F
                0,  # F
                0,  # F
                1,  # F
                0,  # A=B
                1,  # Cout
                1,  # PX
                1,  # GY
            ],
            "minus pass",
        )


if __name__ == "__main__":
    unittest.main()
