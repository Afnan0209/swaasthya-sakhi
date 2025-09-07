from csv_loader import load_symptoms_from_csv

# --- KNOWLEDGE SOURCE 1: THE ADVICE BANK (Managed in Code) ---
# THIS IS THE FIX: The keys here now exactly match the names in your CSV file.
# For example, "Dengue Fever" has been changed to "Dengue".
ADVICE_BANK = {
    "Drug Reaction": "**Possible Condition:** Drug Reaction.\n**Recommendation:** Stop taking the suspected medication and consult your doctor immediately. Do not stop prescribed medication without medical advice.",
    "Malaria": "**Possible Condition:** Malaria. This is serious.\n**Recommendation:** You must see a doctor **immediately** for testing and treatment. Malaria requires specific anti-malarial medication.",
    "Allergy": "**Possible Condition:** Allergy.\n**Recommendation:** Identify and avoid the allergen if possible. Over-the-counter antihistamines can help with mild symptoms. For severe reactions, seek medical attention.",
    "Hypothyroidism": "**Possible Condition:** Hypothyroidism.\n**Recommendation:** This is a condition that requires a doctor's diagnosis and treatment, usually with hormone medication. Please consult a doctor.",
    "Psoriasis": "**Possible Condition:** Psoriasis.\n**Recommendation:** A dermatologist can provide the best treatment plan, which may include creams or other medications. Moisturizing regularly can help manage symptoms.",
    "GERD": "**Possible Condition:** GERD (Acid Reflux).\n**Recommendation:** Avoid trigger foods like spicy or fatty meals. Try not to lie down immediately after eating. Over-the-counter antacids can provide relief.",
    "Chronic cholestasis": "**Possible Condition:** Chronic Cholestasis.\n**Recommendation:** This indicates a liver issue and requires a medical diagnosis. Please consult a doctor immediately for tests.",
    "Hepatitis A": "**Possible Condition:** Hepatitis A.\n**Recommendation:** Rest and hydration are key. It usually resolves on its own, but a doctor's diagnosis is important to rule out other liver issues.",
    "Osteoarthristis": "**Possible Condition:** Osteoarthritis.\n**Recommendation:** Low-impact exercise like walking or swimming can help. Maintain a healthy weight. A doctor can recommend pain relief options.",
    "Paroymsal Positional Vertigo": "**Possible Condition:** BPPV (Vertigo).\n**Recommendation:** A doctor can perform specific head movements (like the Epley maneuver) to help resolve it. Avoid sudden head movements.",
    "Hypoglycemia": "**Possible Condition:** Hypoglycemia (Low Blood Sugar).\n**Recommendation:** Consume a sugary snack or drink immediately. If you have diabetes, follow your doctor's advice. If it happens often, see a doctor.",
    "Acne": "**Possible Condition:** Acne.\n**Recommendation:** Keep your face clean and avoid harsh scrubbing. Over-the-counter creams with benzoyl peroxide can help. For persistent acne, see a dermatologist.",
    "Diabetes": "**Possible Condition:** Diabetes.\n**Recommendation:** This requires a doctor's diagnosis and a comprehensive management plan including diet, exercise, and possibly medication.",
    "Impetigo": "**Possible Condition:** Impetigo.\n**Recommendation:** This is a contagious bacterial infection that requires a doctor's visit. You will likely need an antibiotic cream or ointment.",
    "Hypertension": "**Possible Condition:** Hypertension (High Blood Pressure).\n**Recommendation:** This is a long-term condition to be managed with a doctor's help, often involving lifestyle changes and medication.",
    "Peptic ulcer diseae": "**Possible Condition:** Peptic Ulcer Disease.\n**Recommendation:** Please see a doctor for diagnosis and treatment, which may include antacids and antibiotics.",
    "Dimorphic hemorrhoids(piles)": "**Possible Condition:** Hemorrhoids (Piles).\n**Recommendation:** Increase fiber and water intake. Over-the-counter creams can help. If there is bleeding or severe pain, consult a doctor.",
    "Common Cold": "**Possible Condition:** Common Cold.\n**Recommendation:** Rest, stay hydrated with warm water, and gargle with salt water for a sore throat.",
    "Chicken pox": "**Possible Condition:** Chicken Pox.\n**Recommendation:** Rest and drink fluids. Calamine lotion and oatmeal baths can help with itching. Avoid scratching the blisters.",
    "Cervical spondylosis": "**Possible Condition:** Cervical Spondylosis.\n**Recommendation:** A doctor can recommend physical therapy and pain relief. Gentle neck exercises may help.",
    "Hyperthyroidism": "**Possible Condition:** Hyperthyroidism.\n**Recommendation:** This requires a doctor's diagnosis and treatment, which can include medication or other procedures.",
    "Urinary Tract Infection": "**Possible Condition:** Urinary Tract Infection (UTI).\n**Recommendation:** Drink plenty of water. It's important to see a doctor as you will likely need antibiotics.",
    "Varicose veins": "**Possible Condition:** Varicose Veins.\n**Recommendation:** Elevating your legs and regular exercise can help. For discomfort, a doctor might suggest compression stockings.",
    "AIDS": "**Possible Condition:** AIDS (from HIV).\n**Recommendation:** This is a serious condition requiring medical care from a specialist. Modern treatments are very effective at managing the virus.",
    "Paralysis (brain hemorrhage)": "**Possible Condition:** Paralysis (Brain Hemorrhage). This is a medical emergency.\n**Recommendation:** Call for emergency medical help **immediately**.",
    "Typhoid": "**Possible Condition:** Typhoid Fever.\n**Recommendation:** Medical attention is required. Please visit a doctor or clinic for antibiotics.",
    "Hepatitis B": "**Possible Condition:** Hepatitis B.\n**Recommendation:** This requires diagnosis and management by a doctor to prevent long-term liver damage.",
    "Fungal infection": "**Possible Condition:** Fungal Infection.\n**Recommendation:** Over-the-counter antifungal creams are often effective. If the infection is widespread or doesn't improve, see a doctor.",
    "Hepatitis C": "**Possible Condition:** Hepatitis C.\n**Recommendation:** This is a serious condition that requires a doctor's diagnosis and treatment with antiviral medications.",
    "Migraine": "**Possible Condition:** Migraine.\n**Recommendation:** Rest in a quiet, dark room. A cold compress can help. See a doctor for frequent or severe headaches.",
    "Bronchial Asthma": "**Possible Condition:** Bronchial Asthma.\n**Recommendation:** This is a chronic condition that must be managed with a doctor's guidance, usually involving inhalers.",
    "Alcoholic hepatitis": "**Possible Condition:** Alcoholic Hepatitis.\n**Recommendation:** Stopping all alcohol consumption is critical. Please see a doctor immediately for liver assessment and support.",
    "Jaundice": "**Possible Condition:** Jaundice.\n**Recommendation:** Jaundice indicates an underlying issue and requires a medical diagnosis. Please consult a doctor immediately.",
    "Hepatitis E": "**Possible Condition:** Hepatitis E.\n**Recommendation:** This usually resolves on its own with rest and fluids, but a doctor's diagnosis is important.",
    "Dengue": "**Possible Condition:** Dengue. This is serious.\n**Recommendation:** Consult a doctor **immediately**. Do not take aspirin or ibuprofen. Focus on fluid intake (water, coconut water).",
    "Hepatitis D": "**Possible Condition:** Hepatitis D.\n**Recommendation:** This requires management by a liver specialist.",
    "Heart attack": "**Possible Condition:** Heart Attack. This is a medical emergency.\n**Recommendation:** Call for emergency medical help **immediately**.",
    "Pneumonia": "**Possible Condition:** Pneumonia.\n**Recommendation:** Pneumonia requires a doctor's diagnosis and treatment, usually with antibiotics.",
    "Arthritis": "**Possible Condition:** Arthritis.\n**Recommendation:** A doctor can help manage symptoms with medication and physical therapy recommendations.",
    "Gastroenteritis": "**Possible Condition:** Gastroenteritis.\n**Recommendation:** Stay hydrated with water or ORS. Eat bland foods. If symptoms are severe, see a doctor.",
    "Tuberculosis": "**Possible Condition:** Tuberculosis (TB). This is serious.\n**Recommendation:** TB requires a long course of specific antibiotics prescribed by a doctor. It is crucial to complete the treatment."
}

# --- KNOWLEDGE SOURCE 2: THE SYMPTOM MAP (Loaded from your CSV) ---
symptoms_from_csv = load_symptoms_from_csv('diseases.csv')

# --- MERGE THE KNOWLEDGE ---
def build_knowledge_base():
    knowledge_base = {}
    for disease_name, keywords in symptoms_from_csv.items():
        disease_key = disease_name.lower().strip().replace(' ', '_').replace('(', '').replace(')','')
        if disease_name in ADVICE_BANK:
            knowledge_base[disease_key] = {
                'name': disease_name,
                'keywords': keywords,
                'advice': ADVICE_BANK[disease_name]
            }
    return knowledge_base

DISEASES = {
    'en': build_knowledge_base()
}

# --- DIAGNOSTIC CHECK ---
if not DISEASES['en']:
    print("\n" + "="*50)
    print("!!! KNOWLEDGE BASE FAILED TO LOAD !!!")
    print("Check that the disease names in 'diseases.csv' match the keys in ADVICE_BANK.")
    print("="*50 + "\n")
else:
    disease_count = len(DISEASES['en'])
    print("\n" + "*"*50)
    print(f"SUCCESS: Knowledge base loaded with {disease_count} diseases from diseases.csv.")
    print("*"*50 + "\n")