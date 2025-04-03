import unittest
from app.services.bot_control import BotControl

class TestBotControl(unittest.TestCase):

    def setUp(self):
        self.bot_control = BotControl()

    def test_start_bot(self):
        self.bot_control.start()
        self.assertTrue(self.bot_control.is_running)

    def test_stop_bot(self):
        self.bot_control.start()
        self.bot_control.stop()
        self.assertFalse(self.bot_control.is_running)

    def test_set_symbol(self):
        self.bot_control.set_symbol('AAPL')
        self.assertEqual(self.bot_control.symbol, 'AAPL')

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.bot_control.set_symbol('INVALID_SYMBOL')

if __name__ == '__main__':
    unittest.main()