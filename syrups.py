'''
PCM 125/ 5ml 
Lecocet 30ml 2.5/ml 
Azithro 200/5
Ambroxol 15/5
Dom 30ml 1/ml 
Vit D sachets 60000IU/gm 
Glycerine 100ml 
ifa 20/100 per ml 100ml 
Zn 20/5ml 60ml 
Metro 100/5ml 60ml 
DMR 13.5/5ml 60ml 
Salbutamol 2/5 100 
Gamma benzene 1% 100ml
'''

import re


def extract_weight(input_value):
  match = re.search(r'(\d+(\.\d+)?)kg', input_value)
  if match:
    return float(match.group(1))
  return "Provide Weight (ex. 10kg)"


def extract_age(input_value):
  match_year = re.search(r'(\d+(\.\d+)?)yr', input_value)
  match_month = re.search(r'(\d+(\.\d+)?)mo', input_value)
  if match_year:
    return float(match_year.group(1)) * 12
  if match_month:
    return float(match_month.group(1))
  return "Provide Age (ex. 2yr or 24mo)"


def pcm_dose(input_value, conc="125/5"):
  weight = extract_weight(input_value)
  if type(weight) != float:
    return weight

  per_dose = (15 * weight) / float(eval(conc))
  per_dose = round(per_dose, 1)
  return f"Syp. PCM {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"


def levocet_dose(input_value, conc="2.5/1"):
  age = extract_age(input_value)
  if type(age) != float:
    return age
  age_in_years = age / 12

  if age_in_years < 0.5:
    return "Not recommended for under 6 months"
  elif 0.5 <= age_in_years < 5:
    dose = 1.25
  elif 5 <= age_in_years < 11:
    dose = 2.5
  else:
    dose = 5
  print(dose / float(eval(conc)))
  per_dose = dose / float(eval(conc))
  return f"Syp. Levocet {conc}\n{round(per_dose,1)}ml OD in evening"


def ambroxol_dose(input_value, conc="15/5"):
  age = extract_age(input_value)
  if type(age) != float:
    return age
  age_in_years = age / 12

  if age_in_years < 2:
    return "Not recommended for under 2 years"
  elif 2 <= age_in_years < 6:
    min_dose = 7.5
    max_dose = 15
  elif 6 <= age_in_years < 12:
    min_dose = 15
    max_dose = 30
  else:
    min_dose = 60
    max_dose = 120

  min_per_dose = min_dose / float(eval(conc))
  max_per_dose = max_dose / float(eval(conc))
  return f"Syp. Ambroxol {conc}\n{round(min_per_dose,2)}ml to {round(max_per_dose,2)}ml TID"


def dom_dose(input_value, conc="1/1"):
  weight = extract_weight(input_value)
  if type(weight) != float:
    return weight

  if weight < 35:
    dose = 0.25 * weight
  else:
    dose = 10
  per_dose = dose / float(eval(conc))
  per_dose = round(per_dose, 1)
  return f"Syp. Dom {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"


def azithro_dose(weight_str, severity='mild', conc="200/5"):
  weight = extract_weight(weight_str)
  if type(weight) != float:
    return weight

  if severity == 'mild':
    dose_day1 = 10 * weight if weight <= 20 else 200  # 10-12 mg/kg on day1, max 200mg
    dose_rest = 5 * weight if weight <= 40 else 200  # 5-6 mg/kg on day1, max 200mg
  elif severity == 'severe':
    dose_day1 = 10 * weight if weight <= 50 else 500  # 10 mg/kg on day1, max 500mg
    dose_rest = dose_day1  # same dose for rest of the days
  else:
    return "Invalid severity. Enter either 'mild' or 'severe'."

  vol_day1 = (dose_day1 / float(eval(conc)))  # converting dose to volume
  vol_rest = (dose_rest / float(eval(conc)))  # converting dose to volume

  vol_day1 = round(vol_day1, 1)
  vol_rest = round(vol_rest, 1)

  return f"Syp. Azithro {conc}\nDay 1: {vol_day1}ml\nDay 2 onwards: {vol_rest}ml OD"


def ifa_dose(input_value, conc="20/1"):
  weight = extract_weight(input_value)
  if type(weight) != float:
    return weight

  # Convert dose to volume based on concentration
  total_daily_volume = 6 * weight / float(eval(conc))

  # Divide total daily volume into three doses
  per_dose = total_daily_volume / 3

  # Round to 1 decimal place
  per_dose = round(per_dose, 1)
  return f"Syp. IFA {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"


def salbutamol_dose(input_value, conc="2/5"):
  age = extract_age(input_value)
  if type(age) != float:
    return age
  age_in_years = age / 12
  # Calculate daily dose based on age
  if age_in_years < 2:
    return "Not recommended for children under 2 years"
  elif 2 <= age_in_years < 6:
    daily_dose = 1.5 * 3
  else:
    daily_dose = 2 * 3

  # Convert dose to volume based on concentration
  daily_volume = daily_dose / float(eval(conc))

  # Divide daily volume into three doses
  per_dose = daily_volume / 3

  # Round to 1 decimal place
  per_dose = round(per_dose, 1)

  return f"Syp. Salbutamol {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"  # Return a formatted string of three doses


def dmr_dose(input_value, conc="13.5/5"):
  age = extract_age(input_value)
  if type(age) != float:
    return age
  age_in_years = age / 12

  # Calculate daily dose based on age
  if age_in_years < 2:
    return "Not recommended for children under 2 years"
  elif 2 <= age_in_years < 6:
    daily_dose = 30
  elif 6 <= age_in_years < 12:
    daily_dose = 60
  else:
    daily_dose = 120

  # Convert dose to volume based on concentration
  daily_volume = daily_dose / float(eval(conc))

  # Divide daily volume into three doses
  per_dose = daily_volume / 3

  # Round to 1 decimal place
  per_dose = round(per_dose, 1)

  return f"Syp. DMR {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"  # Return a formatted string of three doses


def metro_dose(input_value, conc="100/5"):
  weight = extract_weight(input_value)
  if type(weight) != float:
    return weight

  # Dose per kg is between 15 to 50 mg, but the total daily dose should not exceed 2250 mg
  total_daily_dose = min(50 * weight, 2250)
  total_daily_volume = total_daily_dose / float(eval(conc))
  per_dose = total_daily_volume / 3
  per_dose = round(per_dose, 1)

  return f"Syp. Metro {conc}\n{per_dose}ml - {per_dose}ml - {per_dose}ml"  # Return a formatted string of three doses


def zinc_dose(input_value, conc="20/5"):
  age = extract_age(input_value)
  if type(age) != float:
    return age
  age_in_months = age

  # Calculate dose based on age
  if age_in_months < 6:
    # If age is less than 6 months, use 10mg
    dose = 10
  else:
    # If age is 6 months or more, use 20mg
    dose = 20

  # Convert dose to volume based on concentration
  per_dose = dose / float(eval(conc))

  # Round to 1 decimal place
  per_dose = round(per_dose, 1)
  return f"Syp. Zinc {conc}\n{per_dose}ml OD"


def mox_dose(input_weight, severity='mild', conc="125/5"):
  weight = extract_weight(input_weight)
  if type(weight) != float:
    return weight

  if severity == 'mild':
    mg_per_kg_per_day_range = (25, 50)
  else:  # Severe infection
    mg_per_kg_per_day_range = (80, 100)

  max_single_dose = 500  # Maximum single dose for most indications
  doses_per_day = 3

  total_dose_per_day_range = [
      dose * weight for dose in mg_per_kg_per_day_range
  ]
  single_dose_range = [
      min(dose / doses_per_day, max_single_dose)
      for dose in total_dose_per_day_range
  ]

  concentration = [float(x) for x in conc.split('/')]
  mg_per_ml = concentration[0] / concentration[1]
  volume_per_dose_range = [
      round(dose / mg_per_ml, 2) for dose in single_dose_range
  ]

  return (
      f"Syp. Amoxy {conc}\n"
      f"{volume_per_dose_range[0]}{(' to ' + str(volume_per_dose_range[1])) if volume_per_dose_range[0] != volume_per_dose_range[1] else ''} ml TID"
  )


def moxclav_dose(input_weight, conc="200+28.5/5"):
  weight = extract_weight(input_weight)
  if type(weight) != float:
    return weight

  # Extract the concentrations of Amoxicillin and Clavulanate from the string
  amoxicillin_conc, clavulanate_conc = map(float,
                                           conc.split('/')[0].split('+'))
  ratio = round(amoxicillin_conc / clavulanate_conc)

  # Dosing guidelines based on the ratio
  dosing_guidelines = {
      4: (20, 40, 3, 1500),
      7: (25, 45, 2, 1750),
      14: (90, 90, 2, 4000),
      16: (4000, 4000, 2, 4000)
  }

  if ratio not in dosing_guidelines:
    return "Amoxicillin:Clavulanate ratio not found in dosing guidelines."

  mg_per_kg_per_day_min, mg_per_kg_per_day_max, doses_per_day, max_dose_per_day = dosing_guidelines[
      ratio]

  # Calculate the total daily dose range based on weight and severity, not exceeding the max dose per day
  total_daily_dose_min = min(mg_per_kg_per_day_min * weight, max_dose_per_day)
  total_daily_dose_max = min(mg_per_kg_per_day_max * weight, max_dose_per_day)

  # Calculate the single dose range
  single_dose_min = total_daily_dose_min / doses_per_day
  single_dose_max = total_daily_dose_max / doses_per_day

  # Calculate the volume of syrup per dose for the range
  mg_per_ml = amoxicillin_conc / (float(conc.split('/')[-1]))
  volume_per_dose_min = round(single_dose_min / mg_per_ml, 2)
  volume_per_dose_max = round(single_dose_max / mg_per_ml, 2)

  dosing_frequency = "TID" if doses_per_day == 3 else "BID"

  return (
      f"Syp. Amoxyclav {conc}\n"
      f"{volume_per_dose_min}{(' to ' + str(volume_per_dose_max)) if volume_per_dose_min != volume_per_dose_max else ''} ml {dosing_frequency}"
  )


command_dict = {
    '$pcm': pcm_dose,
    '$levocet': levocet_dose,
    '$dom': dom_dose,
    '$ifa': ifa_dose,
    '$zn': zinc_dose,
    '$dmr': dmr_dose,
    '$metro': metro_dose,
    '$salbu': salbutamol_dose,
    '$azithro': azithro_dose,
    '$ambroxol': ambroxol_dose,
    '$moxclav': moxclav_dose,
    '$mox': mox_dose,
}
