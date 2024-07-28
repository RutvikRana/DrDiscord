synonyms = {
    "TT": {"tt", "tetanus", "tetanustoxoid", "tetanus-toxoid"},
    "BCG": {"bcg", "tb", "tuberculosis"},
    "Hepatitis B": {"hepb", "hepatitis", "hepatitisb", "hep-b", "hepatitis-b"},
    "OPV": {
        "opv", "polio", "oralpolio", "oralpoliovaccine", "oral-polio",
        "oral-polio-vaccine"
    },
    "IPV": {
        "ipv", "polio", "injectablepolio", "injectablepoliovaccine",
        "injectable-polio", "injectable-polio-vaccine", "fipv",
        "fractionalinjectablepolio", "fractionalinjectablepoliovaccine",
        "fractional-injectable-polio", "fractional-injectable-polio-vaccine"
    },
    "Pentavalent": {
        "pentavalent", "penta", "pentavaccine", "5in1", "fiveinone", "hib",
        "diphtheria", "pertussis", "tt", "tetanus", "hepb", "hepatitis",
        "hepatitisb", "hep-b", "hepatitis-b", "tetanustoxoid", "tetanus-toxoid"
    },
    "DPT": {
        "dpt", "diphtheria", "pertussis", "tetanus", "whoppingcough",
        "tetanustoxoid", "tetanus-toxoid", "tt"
    },
    "MR": {"measles", "rubella", "mr"},
    "JE": {"je", "japaneseencephalitis", "encephalitis"},
    "Vitamin A": {"vita", "vitamina", "vit-a", "vitamin-a"},
    "Rotavirus": {"rota", "rotavirus"},
    "Booster": {"b", "booster", "boost"}
}

immunization_schedule = {
    "Pregnant Woman": {
        "-9mo - -2wk": {
            "TT-1": {
                "Timing": "Early in pregnancy",
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
            "TT-2": {
                "Timing": "4 weeks after TT-1",
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
            "TT-Booster": {
                "Timing":
                "If received 2 TT doses in a pregnancy within the last 3 yrs",
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
        },
    },
    "Infant": {
        "0": {
            "BCG-0": {
                "Dose": "0.1ml (0.05ml until 1mo)",
                "Route": "Intra-dermal",
                "Site": "Left Upper Arm",
                "Give-before": "give before 1yr"
            },
            "Hepatitis B-0": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Antero-lateral side of mid-thigh",
                "Give-before": "give before 24hr"
            },
            "OPV-0": {
                "Dose": "2 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 15day"
            },
        },
        "6wk": {
            "OPV-1": {
                "Dose": "2 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 5yr"
            },
            "Pentavalent-1": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Antero-lateral side of mid-thigh",
                "Give-before": "give before 1yr"
            },
            "Rotavirus-1": {
                "Dose": "5 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 1yr"
            },
            "IPV-1": {
                "Dose": "0.1 ml",
                "Route": "Intra-dermal",
                "Site": "Right Upper Arm"
            },
        },
        "10wk": {
            "OPV-2": {
                "Dose": "2 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 5yr"
            },
            "Pentavalent-2": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Antero-lateral side of mid-thigh",
                "Give-before": "give before 1yr"
            },
            "Rotavirus-2": {
                "Dose": "5 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 1yr"
            },
        },
        "14wk": {
            "OPV-3": {
                "Dose": "2 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 5yr"
            },
            "Pentavalent-3": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Antero-lateral side of mid-thigh",
                "Give-before": "give before 1yr"
            },
            "Rotavirus-3": {
                "Dose": "5 drops",
                "Route": "Oral",
                "Site": "Oral",
                "Give-before": "give before 1yr"
            },
            "IPV-2": {
                "Dose": "0.1 ml",
                "Route": "Intra-dermal",
                "Site": "Right Upper Arm"
            },
        },
        "9mo - 12mo": {
            "MR-1": {
                "Dose": "0.5 ml",
                "Route": "Sub-cutaneous",
                "Site": "Right upper Arm",
                "Give-before": "give before 5yr"
            },
            "JE-1": {
                "Dose": "0.5 ml",
                "Route": "Sub-cutaneous",
                "Site": "Left Upper Arm"
            },
            "Vitamin A-1": {
                "Dose": "1 ml (1 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        }
    },
    "Children": {
        "16mo - 18mo": {
            "DPT booster-1": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Antero-lateral side of mid-thigh"
            },
            "MR-2": {
                "Dose": "0.5 ml",
                "Route": "Sub-cutaneous",
                "Site": "Right upper Arm"
            },
            "OPV Booster-1": {
                "Dose": "2 drops",
                "Route": "Oral",
                "Site": "Oral"
            },
            "JE-2": {
                "Dose": "0.5 ml",
                "Route": "Sub-cutaneous",
                "Site": "Left Upper Arm"
            },
            "Vitamin A-2": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "24mo": {
            "Vitamin A-3": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "30mo": {
            "Vitamin A-4": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "36mo": {
            "Vitamin A-5": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "42mo": {
            "Vitamin A-6": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "48mo": {
            "Vitamin A-7": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "54mo": {
            "Vitamin A-8": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "5yr": {
            "Vitamin A-9": {
                "Dose": "2 ml (2 lakh IU)",
                "Route": "Oral",
                "Site": "Oral"
            },
        },
        "5yr - 6yr": {
            "DPT Booster-2": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
        },
        "10yr": {
            "TT Booster-1": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
        },
        "16yr": {
            "TT Booster-2": {
                "Dose": "0.5 ml",
                "Route": "Intra-muscular",
                "Site": "Upper Arm"
            },
        },
    }
}


def convert_age_to_months(age: str):
  if age == None:
    return None
  if "," in age:
    return [convert_age_to_months(i) for i in age.split(",")]
  if " - " in age:
    return [convert_age_to_months(i) for i in age.split(" - ")]
  elif '<=' in age:
    return [-9.0, convert_age_to_months(age.split('<=')[1])]
  elif '>=' in age:
    return [convert_age_to_months(age.split('>=')[1]), 240]
  elif '<' in age:
    return [-9.0, convert_age_to_months(age.split('<')[1]) - 0.1]
  elif '>' in age:
    return [convert_age_to_months(age.split('>')[1]) + 0.1, 240]
  if age == "0":
    return 0.0
  elif 'mo' in age:
    return round(float(age.replace('mo', '')), 1)
  elif 'yr' in age:
    return round(float(age.replace('yr', '')) * 12, 1)
  elif 'wk' in age:
    return round(float(age.replace('wk', '')) / 4, 1)
  elif 'day' in age:
    return round(float(age.replace('day', '')) / 30, 1)
  return None


def valid_vaccine(vaccine, target):
  target_keywords = target.split(',')
  converted_keywords = []
  for keyword in target_keywords:
    keys = []
    for vaccine_synonym, synonyms_set in synonyms.items():
      if keyword.strip().lower() in synonyms_set:
        keys.append(vaccine_synonym.lower())
    keys.append(keyword)
    converted_keywords.append(keys)

  return all([
      any([keyword in vaccine.lower() for keyword in keys])
      for keys in converted_keywords
  ])


def get_vaccine_schedule_by_age(age,
                                immunization_schedule=immunization_schedule):
  age_in_months = convert_age_to_months(age)
  if age_in_months == None:
    return None
  if type(age_in_months) == float:
    age_in_months = [age_in_months, age_in_months]

  schedule = {}
  for group in immunization_schedule:
    for vaccine_age in immunization_schedule[group]:
      vaccine_age_in_months = convert_age_to_months(vaccine_age)
      if type(vaccine_age_in_months) == float:
        vaccine_age_in_months = [vaccine_age_in_months, vaccine_age_in_months]
      if not (age_in_months[1] < vaccine_age_in_months[0]
              or age_in_months[0] > vaccine_age_in_months[1]):
        if group not in schedule:
          schedule[group] = {}
        if vaccine_age not in schedule[group]:
          schedule[group][vaccine_age] = {}
        for vaccine in immunization_schedule[group][vaccine_age]:
          schedule[group][vaccine_age][vaccine] = immunization_schedule[group][
              vaccine_age][vaccine]

  # Remove empty timings and groups
  schedule = {
      group: {age: vaccines
              for age, vaccines in ages.items() if vaccines}
      for group, ages in schedule.items() if ages
  }
  return schedule


def get_vaccine_schedule(vaccine_name,
                         immunization_schedule=immunization_schedule):
  if vaccine_name == None:
    return None
  schedule = {}
  for group in immunization_schedule:
    for vaccine_age in immunization_schedule[group]:
      for vaccine in immunization_schedule[group][vaccine_age]:
        if valid_vaccine(vaccine, vaccine_name):
          if group not in schedule:
            schedule[group] = {}
          if vaccine_age not in schedule[group]:
            schedule[group][vaccine_age] = {}
          schedule[group][vaccine_age][vaccine] = immunization_schedule[group][
              vaccine_age][vaccine]

  # Remove empty timings and groups
  schedule = {
      group: {age: vaccines
              for age, vaccines in ages.items() if vaccines}
      for group, ages in schedule.items() if ages
  }
  return schedule


def get_vaccine_schedule_by_age_and_vaccine(
    age, vaccine_name, immunization_schedule=immunization_schedule):
  vaccines_by_age = get_vaccine_schedule_by_age(age, immunization_schedule)
  vaccines_by_name = get_vaccine_schedule(vaccine_name, immunization_schedule)

  if (age == None and vaccine_name == None) or (
      age != None and vaccines_by_age == None) or (vaccine_name != None
                                                   and vaccines_by_name == {}):
    return None

  if (age != None and vaccine_name == None):
    return get_vaccine_schedule_by_age(age)

  if (age == None and vaccine_name != None):
    return get_vaccine_schedule(vaccine_name)

  schedule = {}

  for group in vaccines_by_age:
    for vaccine_age in vaccines_by_age[group]:
      for vaccine in vaccines_by_age[group][vaccine_age]:
        if vaccine in vaccines_by_name.get(group, {}).get(vaccine_age, {}):
          if group not in schedule:
            schedule[group] = {}
          if vaccine_age not in schedule[group]:
            schedule[group][vaccine_age] = {}
          schedule[group][vaccine_age][vaccine] = vaccines_by_age[group][
              vaccine_age][vaccine]

  # Remove empty timings and groups
  schedule = {
      group: {age: vaccines
              for age, vaccines in ages.items() if vaccines}
      for group, ages in schedule.items() if ages
  }
  return None if schedule == {} else schedule

def format_schedule(schedule, isD):
  # Calculate the maximum length of each column
  max_age_length = max(len(age) for group in schedule.values() for age in group.keys())
  max_vaccine_length = max(len(vaccine) for group in schedule.values() for vaccines in group.values() for vaccine in vaccines.keys())

  message = ''
  for group, ages in schedule.items():
    message += f'<< {group} >>\n'
    for age, vaccines in ages.items():
        # Use string formatting to align the columns
        age_str = f'{age:<{max_age_length}}'
        for vaccine, details in vaccines.items():
            vaccine_str = f'{vaccine:<{max_vaccine_length}}'
            if isD:
                details_str = ', '.join([j for i, j in details.items()])
                message += f'{age_str} | {vaccine_str} | {details_str}\n'
            else:
                message += f'{age_str} | {vaccine_str} \n'
    message += '\n'
  return message

def format_synonyms(synonyms):
  # Calculate the maximum length of each column
  max_vaccine_length = max(len(vaccine) for vaccine in synonyms.keys())

  message = ''
  for vaccine, synonyms_set in synonyms.items():
    # Use string formatting to align the columns
    vaccine_str = f'{vaccine:<{max_vaccine_length}}'
    synonyms_str = ', '.join(synonyms_set)
    message += f'{vaccine_str} | {synonyms_str}\n'

  return message


#print(format_synonyms(synonyms))

#print(get_vaccine_schedule_by_age("6wk"))
#print(get_vaccine_schedule("vit-a,2"))
#print(format_schedule(get_vaccine_schedule_by_age_and_vaccine("<5yr","tt")))
#print((format_schedule(immunization_schedule)[:2000]))
