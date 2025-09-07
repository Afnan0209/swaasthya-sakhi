import csv

def load_symptoms_from_csv(filepath):
    """
    Reads a 2-column CSV (disease, symptoms_keywords) and converts it into
    a dictionary where the key is the disease name and the value is a list of keywords.
    """
    symptom_map = {}
    try:
        # The 'with open()' statement correctly uses the 'filepath' parameter
      # CHANGE THIS LINE IN csv_loader.py
        with open(filepath, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                disease_name = row['disease'].strip()
                keywords = [keyword.strip() for keyword in row['symptoms_keywords'].lower().split(',')]
                symptom_map[disease_name] = keywords
        return symptom_map
    except FileNotFoundError:
        print(f"ERROR: The data file '{filepath}' was not found. Symptom matching will not work.")
        return {}
    except KeyError as e:
        print(f"ERROR: The CSV file is missing a required column header: {e}. Please use 'disease' and 'symptoms_keywords'.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return {}
