import requests
from datetime import datetime,timedelta
import re

class abbr:

  def __init__(self) -> None:
    self.abbreviations = {
        'ac': 'before meals',
        'bid': 'twice a day',
        'dil': 'dilute',
        'Disp': 'dispense',
        'dis': 'dispense',
        'gr': 'grain',
        'gtt': 'drops',
        'hs': 'at bedtime',
        'OD': 'right eye',
        'prn': 'when needed',
        'q': 'every',
        'Qam': 'every morning',
        'om': 'every morning',
        'qd': 'every day',
        'qh': 'every hour',
        'q1h': 'every hour',
        'qid': 'four times a day',
        'Qs': 'sufficient quantity',
        'Rx': 'take',
        'sos': 'if needed',
        'stat': 'at once',
        'Tbsp': 'tablespoon (always write out "15 ml")',
        'tid': 'three times a day',
        'tsp': 'teaspoon (always write out "5 ml")',
        'U': 'units (always write out "units")',
        'ABG': 'arterial blood gas',
        'AFB': 'acid-fast bacilli',
        'AFP': 'acute flaccid paralysis',
        'APH': 'antepartum haemorrhage',
        'ASOM': 'acute suppurative otitis media',
        'BP': 'blood pressure',
        'CBC': 'complete blood count',
        'CCF': 'congestive cardiac failure',
        'CNS': 'central nervous system',
        'COAD': 'chronic obstructive airway diseases',
        'CPAP': 'continuous positive airway pressure',
        'CPR': 'cardiopulmonary resuscitation',
        'CSF': 'cerebrospinal fluid',
        'CSOM': 'chronic suppurative otitis media',
        'CVP': 'central venous pressure',
        'DUB': 'dysfunctional uterine bleeding',
        'EEG': 'electroencephalogram',
        'ERCP': 'endoscopic retrograde cholangiopancreatography',
        'FNAC': 'fine needle aspiration cytology',
        'GERD': 'gastroesophageal reflux disease',
        'GIT': 'gastrointestinal tract',
        'Hct': 'haematocrit',
        'HR': 'heart rate',
        'INR': 'international normalized ratio',
        'JVP': 'jugular venous pressure',
        'KFT': 'kidney function test',
        'LFT': 'liver function test',
        'MCH': 'maternal-child health',
        'MTP': 'medical termination of pregnancy',
        'Mo': 'month',
        'mth': 'month',
        'NSAIDs': 'nonsteroidal anti-inflammatory drugs',
        'OCD': 'obsessive compulsive disorder',
        'ORS': 'oral rehydration salts',
        'ORT': 'oral rehydration therapy',
        'PEEP': 'peak end expiratory pressure',
        'PCR': 'polymerase chain reaction',
        'PCWP': 'pulmonary capillary wedge pressure',
        'PEFR': 'peak expiratory flow rate',
        'PFT': 'pulmonary function test',
        'PID': 'pelvic inflammatory disease',
        'PPH': 'postpartum haemorrhage',
        'PMS': 'premenstrual syndrome',
        'PUO': 'pyrexia of unknown origin',
        'RAP': 'recurrent abdominal pain',
        'RBBB': 'right bundal branch block',
        'RBC': 'red blood cell',
        'STD': 'sexually transmitted disease',
        'USG': 'ultrasonogram',
        'WBC': 'white blood cells',
        'Wt': 'weight',
        'μg': 'microgram',
        'mcg': 'microgram',
        'g': 'gram',
        'IU': 'international units',
        'kg': 'kilogram',
        'mg': 'milligram',
        'IM': 'intramuscular',
        'IV': 'intravenous',
        'PO': 'per oral',
        'PR': 'per rectum',
        'PV': 'per vaginum',
        'SC': 'subcutaneous'
    }
    self.lowercase_abbreviations = {}

    # Create a dictionary with lowercase keys and values as list of original keys
    for key in self.abbreviations.keys():
      lowercase_key = key.lower()
      if lowercase_key in self.lowercase_abbreviations:
        self.lowercase_abbreviations[lowercase_key].append(key)
      else:
        self.lowercase_abbreviations[lowercase_key] = [key]

  def find_abbreviation(self, abb):
    abb = abb.lower()
    if abb in self.lowercase_abbreviations:
      return "\n".join([
          f"{key} : {self.abbreviations[key]}"
          for key in self.lowercase_abbreviations[abb]
      ])
    else:
      return "Abbreviation not found."

def extract_number(string):
  number = re.findall(r'\d+\.\d+|\d+', string)
  if number:
    extracted_number = float(number[0])
    return extracted_number
  else:
    return None

def get_india_date():
    response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
    data = response.json()
    datetime_str = data['datetime']
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    return datetime_obj.date()

def get_internet_date():
  response = requests.get('http://worldtimeapi.org/api/ip')
  data = response.json()
  datetime_str = data['datetime']
  datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
  return datetime_obj.date()

def iron_sucrose_pints(wt=0,
                       hb=0,
                       anc='0',
                       target='11',
                       conc='200/100',
                       pint='100'):
  if wt == 0:
    return "Provide weight"
  if hb == 0:
    return "Provide Hb"
  wt = float(extract_number(wt))
  hb = float(extract_number(hb))
  anc = True if anc == "1" else False
  target = float(eval(target))
  conc = float(eval(conc))
  pint = float(eval(pint))
  total = ((2.4 * wt * (target - hb)) + (500 if anc else 0))
  pints = (((2.4 * wt * (target - hb)) + (500 if anc else 0)) / conc) / pint
  return f"Inj Iron Sucrose {int(conc*pint)}mg in {int(pint)}cc NS {round(pints,2)} pints Needed.\n((2.4 x {wt} x ({target}-{hb}) + ({500 if anc else 0})) = {total:.2f}mg" + ("\n\nDon't give Iron if <14wk pregnancy" if anc else "")

def rabies_dates(input_date=""):
  # Determine the starting date
  if input_date == "":
    start_date = get_india_date()
  else:
    start_date = datetime.strptime(input_date, "%d/%m/%Y").date()

  # Calculate the dates of the next doses
  dose_dates = [start_date + timedelta(days=d) for d in [0, 3, 7, 28]]

  # Format the dates as strings
  dose_dates_str = [d.strftime("%d/%m/%Y") for d in dose_dates]

  return f"0 = {dose_dates_str[0]}\n3 = {dose_dates_str[1]}\n7 = {dose_dates_str[2]}\n28 = {dose_dates_str[3]}"

