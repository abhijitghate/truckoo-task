import unittest

from resolve_displaystring import resolve_displaystring
dummy_data  = {
    "displaystringUID": "question.tire1_r_profile.description",
		"subdocument_01": {
	    "displaystringUID": "question.tire1_r_profile.description",
		},
		"subdocument_02": {
	    "displaystringUID": "question.tire1_r_profile.description",
			"subdocuments": [
					{
					"displaystringUID": "question.tire1_r_profile.description",
					},
					["some", "weird", "other", {"displayStringUID": "question.tire1_r_profile.description"}, "subdocument"],
					{
					"displaystringUID": "question.tire1_r_profile.description",
					},
				]
		},
}

dummy_result = {
    "displaystring": "at the passenger side",
    "subdocument_01": {
        "displaystring": "at the passenger side"
    },
    "subdocument_02": {
        "displaystring": "at the passenger side",
        "subdocuments": [
            {
                "displaystring": "at the passenger side"
            },
            [
                "some",
                "weird",
                "other",
                {
                    "displaystring": "at the passenger side"
                },
                "subdocument"
            ],
            {
                "displaystring": "at the passenger side"
            }
        ]
    }
}

class TestResolveDisplayString(unittest.TestCase):

    def test_resolve_display_string(self):
        result = resolve_displaystring(dummy_data, "en-GB", "assessment")
        self.assertEqual(result, dummy_result)


if __name__ == "__main__":
    unittest.main()