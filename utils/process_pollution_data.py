import csv
import pdb
import json

from air_quality_index import AQI


EMPTY_DATA = {
    'year': -1,
    'month': -1,
    'date': -1,
    'so2': 0,
    'no2': 0,
    'rspm': 0,
    'spm': 0,
    'pm2_5': 0
}

def _get_numerical_value(num):
    try:
        num = float(num)
    except ValueError:
        num = 0
    return num


def calculate_stats(aqi_calculator, all_entries):

    num_entries = len(all_entries)
    aqi = 0.0
    for entry in all_entries:
        so2 = _get_numerical_value(entry['so2'])
        no2 = _get_numerical_value(entry['no2'])
        spm = _get_numerical_value(entry['spm'])
        rspm = _get_numerical_value(entry['rspm'])

        aqi += aqi_calculator.calculate_aqi(so2, no2, spm, rspm)

    avg_aqi = aqi / num_entries

    # stats = {
    #     'aqi': avg_aqi,
    #     'so2': avg_so2,
    #     'no2': avg_no2,
    #     'rspm': avg_rspm,
    #     'spm': avg_spm,
    #     'pm2_5': avg_pm2_5
    # }

    return avg_aqi, aqi, num_entries


def add_missing_data(processed_data):
    processed_data["Tripura"] = {"Agartala": [EMPTY_DATA]}
    return processed_data


def extract_data(filename_csv):
    processed_data = {}
    with open(filename_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:

            if row['date'] == 'NA':
                i += 1
            else:
                # process time
                year, month, date = row['date'].split("-")

                pruned_data = {
                    'year': year,
                    'month': month,
                    'date': date,
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'rspm': row['rspm'],
                    'spm': row['spm'],
                    'pm2_5': row['pm2_5']
                }

                # map keys based on location
                state = row['state']
                city = row['location']
                region = row['type']
                # pdb.set_trace()
                if state not in processed_data:
                    processed_data[state] = {}
                    processed_data[state][city] = [pruned_data]
                else:
                    if city not in processed_data[state]:
                        processed_data[state][city] = [pruned_data]
                    else:
                        processed_data[state][city].append(pruned_data)
    processed_data = add_missing_data(processed_data)
    print(i, 'entries have \'NA\' dates and are ignored.')
    return processed_data


def process_stats(extracted_data, results_dir):
    '''
    Generates dictionary with averaged stats. Saves dictionary as JSON file.

    Args:
        extracted_data(Map)
    '''

    aqi_calculator = AQI()
    city_level_dict = {}
    state_level_dict = {}
    for state in extracted_data:
        # state-wide stats
        sum_state_aqi = 0.0
        total_num_entries = 0

        for city in extracted_data[state]:
            avg_aqi, aqi, num_entries = calculate_stats(aqi_calculator, extracted_data[state][city])
            sum_state_aqi += aqi
            total_num_entries += num_entries

            if state not in city_level_dict:
                city_level_dict[state] = {}
            city_level_dict[state][city] = aqi

        avg_state_aqi = sum_state_aqi / total_num_entries
        state_level_dict[state] = avg_state_aqi

    with open(results_dir+'pollution-stats-city.json', 'w') as fp:
        json.dump(city_level_dict, fp)

    with open(results_dir+'pollution-stats-state.json', 'w') as fp:
        json.dump(state_level_dict, fp)

    return city_level_dict, state_level_dict


if __name__=='__main__':
    extracted_data = extract_data('../data/pollution-data.csv')
    city_level_dict, state_level_dict = process_stats(extracted_data, '../data/')
