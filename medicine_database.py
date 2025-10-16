"""
COMPREHENSIVE MEDICINE DATABASE
Separate file for medicine recommendations
Place this file in the same directory as your main code
"""

DISEASE_MEDICINE_DATABASE = {
    'fungal infection': {
        'medicines': [
            {'name': 'Fluconazole', 'type': 'Antifungal', 'dosage': '150mg once weekly'},
            {'name': 'Itraconazole', 'type': 'Antifungal', 'dosage': '200mg daily'},
            {'name': 'Terbinafine', 'type': 'Antifungal', 'dosage': '250mg daily'},
            {'name': 'Clotrimazole (topical)', 'type': 'Antifungal cream', 'dosage': 'Apply twice daily'}
        ],
        'alternatives': ['Flucan', 'Candid', 'Terbinex']
    },
    'malaria': {
        'medicines': [
            {'name': 'Chloroquine', 'type': 'Antimalarial', 'dosage': '600mg initially'},
            {'name': 'Artemether-Lumefantrine', 'type': 'Antimalarial', 'dosage': '4 tablets twice daily'},
            {'name': 'Quinine', 'type': 'Antimalarial', 'dosage': '600mg every 8 hours'}
        ],
        'alternatives': ['Lariago', 'Malarone', 'Falcigo']
    },
    'typhoid': {
        'medicines': [
            {'name': 'Azithromycin', 'type': 'Antibiotic', 'dosage': '500mg daily for 7 days'},
            {'name': 'Ceftriaxone', 'type': 'Antibiotic (Injectable)', 'dosage': '2g IV daily'},
            {'name': 'Ciprofloxacin', 'type': 'Antibiotic', 'dosage': '500mg twice daily'}
        ],
        'alternatives': ['Azee', 'Ciplox', 'Taxim']
    },
    'dengue': {
        'medicines': [
            {'name': 'Paracetamol', 'type': 'Antipyretic', 'dosage': '500-1000mg every 6 hours'},
            {'name': 'ORS', 'type': 'Electrolyte', 'dosage': 'As needed'},
            {'name': 'IV Fluids', 'type': 'Supportive', 'dosage': 'If severe dehydration'}
        ],
        'note': '⚠️ AVOID aspirin and ibuprofen!',
        'alternatives': ['Crocin', 'Dolo 650', 'Calpol']
    },
    'chicken pox': {
        'medicines': [
            {'name': 'Acyclovir', 'type': 'Antiviral', 'dosage': '800mg 5 times daily'},
            {'name': 'Calamine Lotion', 'type': 'Topical', 'dosage': 'Apply as needed'},
            {'name': 'Cetirizine', 'type': 'Antihistamine', 'dosage': '10mg once daily'}
        ],
        'alternatives': ['Zovirax', 'Lacalamine', 'Okacet']
    },
    'common cold': {
        'medicines': [
            {'name': 'Paracetamol', 'type': 'Antipyretic', 'dosage': '500mg every 6 hours'},
            {'name': 'Cetirizine', 'type': 'Antihistamine', 'dosage': '10mg once daily'},
            {'name': 'Vitamin C', 'type': 'Supplement', 'dosage': '500mg daily'}
        ],
        'alternatives': ['Crocin Cold', 'Sinarest', 'Cheston']
    },
    'pneumonia': {
        'medicines': [
            {'name': 'Azithromycin', 'type': 'Antibiotic', 'dosage': '500mg daily for 3-5 days'},
            {'name': 'Amoxicillin', 'type': 'Antibiotic', 'dosage': '500mg three times daily'},
            {'name': 'Levofloxacin', 'type': 'Antibiotic', 'dosage': '500mg once daily'}
        ],
        'alternatives': ['Azee', 'Moxclav', 'Levocin']
    },
    'tuberculosis': {
        'medicines': [
            {'name': 'Isoniazid', 'type': 'Anti-TB', 'dosage': '300mg daily'},
            {'name': 'Rifampicin', 'type': 'Anti-TB', 'dosage': '600mg daily'},
            {'name': 'Ethambutol', 'type': 'Anti-TB', 'dosage': '800-1200mg daily'}
        ],
        'note': '⚠️ Complete 6-9 month course!',
        'alternatives': ['AKT-4', 'Rifagut', 'R-Cinex']
    },
    'urinary tract infection': {
        'medicines': [
            {'name': 'Nitrofurantoin', 'type': 'Antibiotic', 'dosage': '100mg twice daily'},
            {'name': 'Ciprofloxacin', 'type': 'Antibiotic', 'dosage': '500mg twice daily'},
            {'name': 'Trimethoprim', 'type': 'Antibiotic', 'dosage': '160/800mg twice daily'}
        ],
        'alternatives': ['Macrobid', 'Ciplox', 'Bactrim']
    },
    'hepatitis b': {
        'medicines': [
            {'name': 'Tenofovir', 'type': 'Antiviral', 'dosage': '300mg daily'},
            {'name': 'Entecavir', 'type': 'Antiviral', 'dosage': '0.5-1mg daily'}
        ],
        'note': '⚠️ Lifelong monitoring required',
        'alternatives': ['Tenvir', 'Baraclude', 'Hepbest']
    },
    'hepatitis c': {
        'medicines': [
            {'name': 'Sofosbuvir-Velpatasvir', 'type': 'Antiviral', 'dosage': '1 tablet daily for 12 weeks'},
            {'name': 'Ledipasvir-Sofosbuvir', 'type': 'Antiviral', 'dosage': '1 tablet daily'}
        ],
        'note': '✅ Now CURABLE!',
        'alternatives': ['Velpanat', 'Harvoni', 'Hepcinat']
    },
    'gastroenteritis': {
        'medicines': [
            {'name': 'ORS', 'type': 'Electrolyte', 'dosage': 'As needed'},
            {'name': 'Ondansetron', 'type': 'Antiemetic', 'dosage': '4-8mg every 8 hours'},
            {'name': 'Probiotics', 'type': 'Gut flora', 'dosage': 'Daily'}
        ],
        'alternatives': ['Electral', 'Emeset', 'Econorm']
    },
    'peptic ulcer disease': {
        'medicines': [
            {'name': 'Omeprazole', 'type': 'PPI', 'dosage': '20-40mg daily'},
            {'name': 'Pantoprazole', 'type': 'PPI', 'dosage': '40mg daily'},
            {'name': 'Amoxicillin', 'type': 'Antibiotic', 'dosage': '1000mg twice daily'}
        ],
        'alternatives': ['Omez', 'Pan-40', 'Carafate']
    },
    'gerd': {
        'medicines': [
            {'name': 'Omeprazole', 'type': 'PPI', 'dosage': '20mg before breakfast'},
            {'name': 'Pantoprazole', 'type': 'PPI', 'dosage': '40mg once daily'},
            {'name': 'Ranitidine', 'type': 'H2 blocker', 'dosage': '150mg twice daily'}
        ],
        'alternatives': ['Omez', 'Razo', 'Nexium']
    },
    'jaundice': {
        'medicines': [
            {'name': 'Ursodeoxycholic acid', 'type': 'Bile acid', 'dosage': '300mg twice daily'},
            {'name': 'Vitamin K', 'type': 'Supplement', 'dosage': 'If INR elevated'}
        ],
        'note': '⚠️ Find the underlying cause!',
        'alternatives': ['Ursocol', 'Udiliv']
    },
    'chronic cholestasis': {
        'medicines': [
            {'name': 'Ursodeoxycholic acid', 'type': 'Bile acid', 'dosage': '13-15mg/kg daily'},
            {'name': 'Cholestyramine', 'type': 'Bile sequestrant', 'dosage': '4g 1-2 times daily'}
        ],
        'alternatives': ['Udiliv', 'Ursocol']
    },
    'hypertension': {
        'medicines': [
            {'name': 'Amlodipine', 'type': 'CCB', 'dosage': '5-10mg once daily'},
            {'name': 'Losartan', 'type': 'ARB', 'dosage': '50-100mg once daily'},
            {'name': 'Atenolol', 'type': 'Beta-blocker', 'dosage': '25-100mg once daily'}
        ],
        'alternatives': ['Amlong', 'Losar', 'Tenoret']
    },
    'heart attack': {
        'medicines': [
            {'name': 'Aspirin', 'type': 'Antiplatelet', 'dosage': '300mg immediately'},
            {'name': 'Clopidogrel', 'type': 'Antiplatelet', 'dosage': '75mg daily'},
            {'name': 'Atorvastatin', 'type': 'Statin', 'dosage': '40-80mg daily'}
        ],
        'note': '🚨 EMERGENCY - Call ambulance!',
        'alternatives': ['Disprin', 'Ecosprin', 'Lipitor']
    },
    'bronchial asthma': {
        'medicines': [
            {'name': 'Salbutamol Inhaler', 'type': 'Bronchodilator', 'dosage': '2 puffs as needed'},
            {'name': 'Fluticasone Inhaler', 'type': 'Corticosteroid', 'dosage': '2 puffs twice daily'},
            {'name': 'Montelukast', 'type': 'Leukotriene inhibitor', 'dosage': '10mg at night'}
        ],
        'alternatives': ['Asthalin', 'Seroflo', 'Montair']
    },
    'diabetes': {
        'medicines': [
            {'name': 'Metformin', 'type': 'Biguanide', 'dosage': '500-1000mg twice daily'},
            {'name': 'Glimepiride', 'type': 'Sulfonylurea', 'dosage': '1-4mg once daily'},
            {'name': 'Sitagliptin', 'type': 'DPP-4 inhibitor', 'dosage': '100mg once daily'}
        ],
        'alternatives': ['Glycomet', 'Amaryl', 'Januvia']
    },
    'hypothyroidism': {
        'medicines': [
            {'name': 'Levothyroxine', 'type': 'Thyroid hormone', 'dosage': '25-200mcg once daily'}
        ],
        'note': '⚠️ Take empty stomach, 30-60min before breakfast',
        'alternatives': ['Thyronorm', 'Eltroxin', 'Thyrox']
    },
    'hyperthyroidism': {
        'medicines': [
            {'name': 'Methimazole', 'type': 'Antithyroid', 'dosage': '10-40mg daily'},
            {'name': 'Propylthiouracil', 'type': 'Antithyroid', 'dosage': '100mg three times daily'}
        ],
        'alternatives': ['Neomercazole', 'Propycil']
    },
    'hypoglycemia': {
        'medicines': [
            {'name': 'Glucose tablets', 'type': 'Sugar', 'dosage': '15g immediately'},
            {'name': 'Glucagon injection', 'type': 'Emergency', 'dosage': '1mg IM/SC'}
        ],
        'note': '⚠️ Rule of 15: 15g sugar, wait 15min'
    },
    'arthritis': {
        'medicines': [
            {'name': 'Ibuprofen', 'type': 'NSAID', 'dosage': '400-600mg three times daily'},
            {'name': 'Diclofenac', 'type': 'NSAID', 'dosage': '50mg 2-3 times daily'},
            {'name': 'Methotrexate', 'type': 'DMARD', 'dosage': '7.5-25mg weekly'}
        ],
        'alternatives': ['Brufen', 'Voveran', 'Folitrax']
    },
    'osteoarthritis': {
        'medicines': [
            {'name': 'Paracetamol', 'type': 'Analgesic', 'dosage': '1000mg three times daily'},
            {'name': 'Naproxen', 'type': 'NSAID', 'dosage': '500mg twice daily'},
            {'name': 'Glucosamine', 'type': 'Supplement', 'dosage': '1500mg daily'}
        ],
        'alternatives': ['Crocin', 'Naprosyn', 'Cartigen']
    },
    'cervical spondylosis': {
        'medicines': [
            {'name': 'Ibuprofen', 'type': 'NSAID', 'dosage': '400mg three times daily'},
            {'name': 'Gabapentin', 'type': 'Neuropathic pain', 'dosage': '300-900mg three times daily'},
            {'name': 'Methylcobalamin', 'type': 'Vitamin B12', 'dosage': '1500mcg daily'}
        ],
        'alternatives': ['Brufen', 'Gabapin', 'Neurobion']
    },
    'migraine': {
        'medicines': [
            {'name': 'Sumatriptan', 'type': 'Triptan', 'dosage': '50-100mg at onset'},
            {'name': 'Ibuprofen', 'type': 'NSAID', 'dosage': '400-600mg'},
            {'name': 'Propranolol', 'type': 'Preventive', 'dosage': '40-80mg twice daily'}
        ],
        'alternatives': ['Suminat', 'Brufen', 'Inderal']
    },
    '(vertigo) paroymsal positional vertigo': {
        'medicines': [
            {'name': 'Betahistine', 'type': 'Antivertigo', 'dosage': '16mg three times daily'},
            {'name': 'Meclizine', 'type': 'Antivertigo', 'dosage': '25-50mg three times daily'},
            {'name': 'Epley maneuver', 'type': 'Physical therapy', 'dosage': 'Best treatment!'}
        ],
        'alternatives': ['Vertin', 'Stugeron', 'Dramamine']
    },
    'acne': {
        'medicines': [
            {'name': 'Benzoyl Peroxide gel', 'type': 'Topical', 'dosage': 'Apply once daily'},
            {'name': 'Clindamycin gel', 'type': 'Antibiotic', 'dosage': 'Apply twice daily'},
            {'name': 'Adapalene gel', 'type': 'Retinoid', 'dosage': 'Apply at night'}
        ],
        'alternatives': ['Persol', 'Deriva', 'Clindac']
    },
    'psoriasis': {
        'medicines': [
            {'name': 'Clobetasol cream', 'type': 'Topical steroid', 'dosage': 'Apply twice daily'},
            {'name': 'Calcipotriol', 'type': 'Vitamin D analog', 'dosage': 'Apply twice daily'},
            {'name': 'Methotrexate', 'type': 'Immunosuppressant', 'dosage': '7.5-25mg weekly'}
        ],
        'alternatives': ['Daivonex', 'Folitrax']
    },
    'impetigo': {
        'medicines': [
            {'name': 'Mupirocin ointment', 'type': 'Topical antibiotic', 'dosage': 'Apply 3 times daily'},
            {'name': 'Retapamulin ointment', 'type': 'Topical antibiotic', 'dosage': 'Apply twice daily'}
        ],
        'alternatives': ['Bactroban', 'Altabax']
    },
    'allergy': {
        'medicines': [
            {'name': 'Cetirizine', 'type': 'Antihistamine', 'dosage': '10mg once daily'},
            {'name': 'Loratadine', 'type': 'Antihistamine', 'dosage': '10mg once daily'},
            {'name': 'Fexofenadine', 'type': 'Antihistamine', 'dosage': '120-180mg once daily'}
        ],
        'alternatives': ['Okacet', 'Lorfast', 'Allegra']
    },
    'drug reaction': {
        'medicines': [
            {'name': 'Cetirizine', 'type': 'Antihistamine', 'dosage': '10mg twice daily'},
            {'name': 'Prednisolone', 'type': 'Corticosteroid', 'dosage': '40-60mg daily'},
            {'name': 'Stop causative drug', 'type': 'Essential', 'dosage': 'Immediately!'}
        ],
        'note': '⚠️ STOP the drug causing reaction!',
        'alternatives': ['Okacet', 'Wysolone', 'EpiPen']
    },
    'aids': {
        'medicines': [
            {'name': 'Tenofovir-Emtricitabine', 'type': 'NRTI', 'dosage': '1 tablet daily'},
            {'name': 'Efavirenz', 'type': 'NNRTI', 'dosage': '600mg at bedtime'},
            {'name': 'Dolutegravir', 'type': 'Integrase inhibitor', 'dosage': '50mg once daily'}
        ],
        'note': '⚠️ Lifelong ART - NEVER skip!',
        'alternatives': ['Ricovir-EM', 'Viraday', 'Tenvir']
    },
    'dimorphic hemorrhoids(piles)': {
        'medicines': [
            {'name': 'Diosmin-Hesperidin', 'type': 'Venotonic', 'dosage': '500mg twice daily'},
            {'name': 'Lidocaine cream', 'type': 'Local anesthetic', 'dosage': 'Apply as needed'},
            {'name': 'Psyllium husk', 'type': 'Fiber', 'dosage': '1 teaspoon twice daily'}
        ],
        'alternatives': ['Daflon', 'Anobliss', 'Pilex']
    },
    'varicose veins': {
        'medicines': [
            {'name': 'Diosmin-Hesperidin', 'type': 'Venotonic', 'dosage': '500mg twice daily'},
            {'name': 'Compression stockings', 'type': 'Supportive', 'dosage': 'Wear during day'}
        ],
        'note': '💡 Leg elevation important!',
        'alternatives': ['Daflon', 'Varikosette']
    },
    'alcoholic hepatitis': {
        'medicines': [
            {'name': 'Stop alcohol', 'type': 'Essential', 'dosage': 'Permanent abstinence'},
            {'name': 'Prednisolone', 'type': 'Corticosteroid', 'dosage': '40mg daily for 28 days'},
            {'name': 'Thiamine', 'type': 'Vitamin B1', 'dosage': '100mg daily'}
        ],
        'note': '⚠️ Alcohol continuation is FATAL!',
        'alternatives': ['Wysolone', 'Trental', 'Neurobion']
    },
    'paralysis (brain hemorrhage)': {
        'medicines': [
            {'name': 'Aspirin', 'type': 'Antiplatelet', 'dosage': '300mg if ischemic'},
            {'name': 'BP control', 'type': 'Antihypertensive', 'dosage': 'As per BP'},
            {'name': 'Physical therapy', 'type': 'Rehabilitation', 'dosage': 'Daily'}
        ],
        'note': '🚨 EMERGENCY - Hospital now!',
    },
    'hepatitis a': {
        'medicines': [
            {'name': 'Rest and hydration', 'type': 'Supportive', 'dosage': 'Self-limiting'},
            {'name': 'Multivitamin', 'type': 'Supplement', 'dosage': 'Daily'}
        ],
        'note': '✅ Usually self-limiting',
        'alternatives': ['Electral']
    },
    'hepatitis d': {
        'medicines': [
            {'name': 'Interferon alfa', 'type': 'Immunomodulator', 'dosage': 'Injectable'},
            {'name': 'Treat Hepatitis B', 'type': 'Essential', 'dosage': 'HDV needs HBV'}
        ],
        'note': '⚠️ Requires specialist care',
    },
    'hepatitis e': {
        'medicines': [
            {'name': 'Rest and hydration', 'type': 'Supportive', 'dosage': 'Self-limiting'},
            {'name': 'Ribavirin', 'type': 'Antiviral', 'dosage': 'Severe cases only'}
        ],
        'note': '⚠️ Dangerous for pregnant women!',
        'alternatives': ['ORS', 'Electral']
    },
}
