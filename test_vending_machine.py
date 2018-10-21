import unittest


class VendingMachine:
    def push_コーラボタン(self) -> str:
        return "コーラ "


class TestVendingMachine(unittest.TestCase):
    def test_お題1_コーラボタンを押すとコーラが出る(self):
        vending_machine = VendingMachine()
        actual = vending_machine.push_コーラボタン()

        self.assertEqual("コーラ", actual)


if __name__ == "__main__":
    unittest.main()
