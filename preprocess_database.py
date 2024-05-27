import json



def index_database_by_uid(data):
    new_data = {}
    for item in data:
        new_data[item["uid"]] = item
    return new_data


def index_database():
    try:
      with open("displaystring_database.json", 'r') as f:
          data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file displaystring_database.json not found.")
        return
    
    indexed_data = index_database_by_uid(data)

    try:
      with open("displaystring_database_indexed.json", 'w') as f:
          json.dump(indexed_data, f, indent=4)
      print(f"Successfully wrote modified data to displaystring_database_indexed.json.")
    except Exception as e:
        print(f"Error writing to output file: {e}")


if __name__ == "__main__":
    index_database()