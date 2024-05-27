

import json
import re
from get_displaystring import get_displaystring_for_context


def resolve_displaystring(dictionary, locale, context):

    stringified = str(dictionary)
    pattern = r"(?i)'displaystringUID':\s*'([^']*)'"

    for match in re.finditer(pattern, stringified):
       captured_value = match.group(1)
       stringified = stringified.replace(match.group(0), f'"displaystring": "{get_displaystring_for_context(captured_value, locale, context)}"')

    stringified = stringified.replace("\'", "\"")
    return json.loads(stringified)



# if __name__=="__main__":
#   print(resolve_displaystring(dictionary_with_displaystringuids, 'en-GB', 'assessment'))
