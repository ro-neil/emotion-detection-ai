"""
Unit Test Module for emotion_detector
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector
`1`
class TestEmotionDetector(unittest.TestCase):
    """
    Emotion Detector TestCase class
    """
    def test_emotion_detector(self):
        """
        A function that runs test cases using the emotion_detector
        """
        joy_statement = "I am glad this happened"
        anger_statement = "I am really mad about this"
        disgust_statement = "I feel disgusted just hearing about this"
        sadness_statement = "I am so sad about this"
        fear_statement = "I am really afraid that this will happen"

        analyze_joy = emotion_detector(joy_statement)
        self.assertEqual(analyze_joy['dominant_emotion'], "joy")

        analyze_anger = emotion_detector(anger_statement)
        self.assertEqual(analyze_anger['dominant_emotion'], "anger")

        analyze_disgust = emotion_detector(disgust_statement)
        self.assertEqual(analyze_disgust['dominant_emotion'], "disgust")

        analyze_sadness = emotion_detector(sadness_statement)
        self.assertEqual(analyze_sadness['dominant_emotion'], "sadness")

        analyze_fear = emotion_detector(fear_statement)
        self.assertEqual(analyze_fear['dominant_emotion'], "fear")

unittest.main()
