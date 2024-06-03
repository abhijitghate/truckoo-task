import json


FALLBACK_HIERARCHY = {
    "assessment": ["assessment", "offer", "tag"],
    "tag": ["tag", "assessment", "offer"],
    "offer": ["offer", "assessment", "tag"],
    "preference": ["preference", "assessment", "offer"]
}


def get_target_object(displaystring_holder):
    try:
      with open("displaystring_database_indexed.json", 'r') as f:
          data = json.load(f)
          return data[displaystring_holder]
    except FileNotFoundError:
        print(f"Error: Input file displaystring_database.json not found.")
        return None
    except KeyError:
        return None
    

def get_displaystring_for_context(displaystring_holder, locale, context):

    target_object = get_target_object(displaystring_holder)

    # straightforward lookup
    try:
        return  target_object["contexts"][context][locale]
    except KeyError:
        pass
    except Exception as e:
        return None

    # lookoing up through fallback startegy with given locale
    for item in FALLBACK_HIERARCHY[context]:
        try:
            return target_object["contexts"][item][locale]
        except KeyError:
            pass
    
    # trying en-GB (default locale)
    try:
        return  target_object["contexts"][context]['en-GB']
    except KeyError:
        pass
    

    # trying en-GB (default locale) through fallback strategy
    for item in FALLBACK_HIERARCHY[context]:
        try:
            return target_object["contexts"][item]['en-GB']
        except KeyError:
            pass
    
    return None


# if __name__ == "__main__":
#     # print(get_displaystring_for_context("", "de-DE", "assessment"))
#     # print(get_displaystring_for_context("", "en-GB", "offer"))
#     # print(get_displaystring_for_context("", "it-IT", "offer"))
#     print(get_displaystring_for_context("","it-IT", "preference")) # english | preference
