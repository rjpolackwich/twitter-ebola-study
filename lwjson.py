import json

def load_json(filename):
	with open(filename, 'r') as input_data:
		comm_data_in = json.load(input_data)
		print 'Read JSON from %s' % filename
		return comm_data_in

def write_json(filename, updated_data):
	with open(filename, 'w') as output_data:
		json_out = json.dump(updated_data, output_data, sort_keys=True, indent=4)
		print 'Wrote JSON to %s' % filename