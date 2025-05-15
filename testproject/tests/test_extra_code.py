import unittest
import sys
import os
from unittest.mock import patch, Mock
import io

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extra_code import poser_questions, calculer_correction, afficher_resultat

class TestExtraCode(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['Paris', '7', '4'])
    def test_poser_questions(self, mock_input):
        """Test if questions are properly asked and answers stored"""
        reponses = poser_questions('test_user')
        expected = {'Q0': 'Paris', 'Q1': '7', 'Q2': '4'}
        self.assertEqual(reponses, expected)
    
    def test_calculer_correction(self):
        """Test the scoring system"""
        # Test with all correct answers
        reponses = {'Q1': 'Paris', 'Q2': '7', 'Q5': '4'}
        score = calculer_correction('test_user', reponses)
        self.assertEqual(score, 3)
        
        # Test with some incorrect answers
        reponses = {'Q1': 'Lyon', 'Q2': '7', 'Q5': '5'}
        score = calculer_correction('test_user', reponses)
        self.assertEqual(score, 1)
        
        # Test with all incorrect answers
        reponses = {'Q1': 'Lyon', 'Q2': '8', 'Q5': '5'}
        score = calculer_correction('test_user', reponses)
        self.assertEqual(score, 0)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_afficher_resultat(self, mock_stdout):
        """Test if results are displayed properly"""
        afficher_resultat('test_user', 5)
        self.assertIn('test_user: 5', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
