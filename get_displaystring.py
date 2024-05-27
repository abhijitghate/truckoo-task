import json


FALLBACK_HIERARCHY = ["assessment", "offer", "tag"]


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

    try:
        return  target_object["contexts"][context][locale]
    except KeyError:
        pass

    for item in FALLBACK_HIERARCHY:
        try:
            return target_object["contexts"][item][locale]
        except KeyError:
            pass
    
    
    try:
        return  target_object["contexts"][context]['en-GB']
    except KeyError:
        pass


    for item in FALLBACK_HIERARCHY:
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
