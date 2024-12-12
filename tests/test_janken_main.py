import unittest
from unittest.mock import patch
from source.janken_main import rounds, final_round

class TestMain(unittest.TestCase):
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='チョキ')
    @patch('source.janken_judge', return_value='compurter_win')
    def test_rounds_comp_win(self, mock_cpon, mock_ppon, mock_juege):
        player_win, computer_win, round = rounds(0, 0, 1)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 1)
        self.assertEqual(round, 2)
        
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='パー')
    @patch('source.janken_judge', return_value='compurter_win')
    def test_rounds_pla_win(self, mock_cpon, mock_ppon, mock_juege):
        player_win, computer_win, round = rounds(1, 0, 2)
        self.assertEqual(player_win, 2)
        self.assertEqual(computer_win, 0)
        self.assertEqual(round, 3)
        
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='グー')
    @patch('source.janken_judge', return_value='draw')
    def test_rounds_draw_win(self, mock_cpon, mock_ppon, mock_juege):
        player_win, computer_win, round = rounds(0, 2, 3)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 2)
        self.assertEqual(round, 3)
    
    def test_final_round(self):
        patterns = [
            (3, 0, 'あなたの総合勝利です！'),
            (2, 1, 'あなたの総合勝利です！'),
            (1, 2, 'コンピュータの総合勝利です！'),
            (0, 3, 'コンピュータの総合勝利です！'),
        ]
        for player_win, computer_win, result in patterns:
            with self.subTest():
                self.assertEqual(final_round(player_win, computer_win), result)