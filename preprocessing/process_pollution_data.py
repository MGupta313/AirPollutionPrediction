import csv
import pdb
import json

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

    print(i, ' entries have \'NA\' dates and are ignored.')
    return processed_data

def process_stats(extracted_data, results_filepath):
    '''
    Generates dictionary with averaged stats. Saves dictionary as JSON file.

    Args:
        extracted_data(Map)
    '''

    city_level_dict = {}
    for state in extracted_data:
        for city in extracted_data[state]:
            stats = calculate_stats(extract_data[state][city])

            if state not in city_level_dict:
                city_level_dict[state] = {}
            city_level_dict[state][city] = stats

    pdb.set_trace()
    print(city_level_dict)

    with open(city_level_dict, 'w') as fp:
        json.dump(city_level_dict, fp)

    #state_level_dict = {}
    #for key in extracted_data:
        #state_level_dict[key]

    # with open(results_filepath, 'w') as fp:
    #     json.dump(state_level_dict, fp)


    return None

def calculate_stats(all_entries):
    len = len(all_entries)
    for entry in all_entries:
        print("in progress")


if __name__=='__main__':
    extracted_data = extract_data('../data/pollution-data.csv')
    stats = process_stats(extracted_data, '../data/pollution-stats.json')
