import os
import json

entries = os.listdir('../data/plots')


state_images_dict = {}
for entry in entries:
	entryname = entry.split("_")[0]
	state_images_dict[entryname] = entry

print(state_images_dict)
	

with open('../data/'+'aqi-images-state.json', 'w') as fp:
        json.dump(state_images_dict, fp)