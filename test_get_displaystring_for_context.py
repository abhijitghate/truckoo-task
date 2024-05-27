


import unittest
from unittest.mock import patch
from get_displaystring import get_displaystring_for_context



def mock_get_target_object(displaystring_holder):
    return {
        "contexts": {
            "assessment": {
                "bs-BA": "Na strani suvoza\u010da",
                "de-DE": "Auf der Beifahrerseite",
                "en-GB": "at the passenger side"
            },
            "offer": {
                "de-DE": "Beifahrerseite"
            },
            "tag": {
                "de-DE": "Rechts",
                "it-IT": "destra"
            }
        },
        "qualityAssured": {
            "bs-BA": True
        },
        "technicalDescription": "1te Achse | Bewerten Sie das Reifenprofil",
        "uid": "question.tire1_r_profile.description"
    }


class TestGetDisplaystringForContext(unittest.TestCase):

    @patch('get_displaystring.get_target_object', side_effect=mock_get_target_object)
    def test_exact_match(self, mock_get_target_object):
        result = get_displaystring_for_context("question.tire1_r_profile.description", "en-GB", "assessment")
        self.assertEqual(result, 'at the passenger side')
        mock_get_target_object.assert_called_once_with("question.tire1_r_profile.description")

    @patch('get_displaystring.get_target_object', side_effect=mock_get_target_object)
    def test_fallback_hirarchy(self, mock_get_target_object):
        result = get_displaystring_for_context("question.tire1_r_profile.description", "en-GB", "tag")
        self.assertEqual(result, 'at the passenger side')
        mock_get_target_object.assert_called_once_with("question.tire1_r_profile.description")

    @patch('get_displaystring.get_target_object', side_effect=mock_get_target_object)
    def test_default_locale(self, mock_get_target_object):
        result = get_displaystring_for_context("question.tire1_r_profile.description", "bg-BG", "tag")
        self.assertEqual(result, 'at the passenger side')
        mock_get_target_object.assert_called_once_with("question.tire1_r_profile.description")



if __name__ == "__main__":
    unittest.main()