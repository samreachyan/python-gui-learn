import csv
import os
import json
from .constants import FieldTypes as FT


class CSVModel:
    """CSV file storage"""

    def __init__(self, filename):
        self.filename = filename

    fields = {
        "Date": {'req': True, 'type': FT.iso_date_string},
        "Time": {'req': True, 'type': FT.string_list,
                 'values': ['8:00', '12:00', '16:00', '20:00']},
        "Technician": {'req': True, 'type': FT.string},
        "Lab": {'req': True, 'type': FT.string_list,
                'values': ['A', 'B', 'C', 'D', 'E']},
        "Plot": {'req': True, 'type': FT.string_list,
                 'values': [str(x) for x in range(1, 21)]},
        "Seed sample": {'req': True, 'type': FT.string},
        "Humidity": {'req': True, 'type': FT.decimal,
                     'min': 0.5, 'max': 52.0, 'inc': .01},
        "Light": {'req': True, 'type': FT.decimal,
                  'min': 0, 'max': 100.0, 'inc': .01},
        "Temperature": {'req': True, 'type': FT.decimal,
                        'min': 4, 'max': 40, 'inc': .01},
        "Equipment Fault": {'req': False, 'type': FT.boolean},
        "Plants": {'req': True, 'type': FT.integer,
                   'min': 0, 'max': 20},
        "Blossoms": {'req': True, 'type': FT.integer,
                     'min': 0, 'max': 1000},
        "Fruit": {'req': True, 'type': FT.integer,
                  'min': 0, 'max': 1000},
        "Min Height": {'req': True, 'type': FT.decimal,
                       'min': 0, 'max': 1000, 'inc': .01},
        "Max Height": {'req': True, 'type': FT.decimal,
                       'min': 0, 'max': 1000, 'inc': .01},
        "Median Height": {'req': True, 'type': FT.decimal,
                          'min': 0, 'max': 1000, 'inc': .01},
        "Notes": {'req': False, 'type': FT.long_string}
    }

    def save_record(self, data, rownum=None):
        """Save a dict of data to the CSV file"""

        if rownum is not None:

            records = self.get_all_records()
            records[rownum] = data

            with open(self.filename, 'w', encoding='utf-8') as fh:
                csvwriter = csv.DictWriter(fh,
                                           fieldnames=self.fields.keys())
                csvwriter.writeheader()
                csvwriter.writerows(records)

        else:

            newfile = not os.path.exists(self.filename)

            with open(self.filename, 'a', encoding='utf-8') as fh:
                csvwriter = csv.DictWriter(fh,
                                           fieldnames=self.fields.keys())
                if newfile:
                    csvwriter.writeheader()
                csvwriter.writerow(data)

    def get_all_records(self):
        if not os.path.exists(self.filename):
            return[]

        with open(self.filename, 'r', encoding='utf-8') as fh:
            csvreader = csv.DictReader(list(fh.readlines()))
            missing_fields = (set(self.fields.keys()) -
                              set(csvreader.fieldnames))
            if len(missing_fields) > 0:
                raise Exception(
                    "File is missing fields: {}"
                    .format(','.join(missing_fields))
                )
            else:
                records = list(csvreader)
                trues = ('true', 'yes', '1')

                bool_fields = [
                    key for key, meta
                    in self.fields.items()
                    if meta['type'] == FT.boolean]

                for record in records:
                    for key in bool_fields:
                        record[key] = record[key].lower() in trues

                return records

    def get_record(self, rownum):
        return self.get_all_records()[rownum]


class SettingsModel:
    """A model for saving data"""

    variables = {
        'autofill date': {'type': 'bool', 'value': True},
        'autofill sheet data': {'type': 'bool', 'value': True},
        'font size': {'type': 'int', 'value': 9},
        'theme': {'type': 'str', 'value': 'default'}
    }

    def __init__(self, filename='abq_settings.json', path='~'):
        # determine the file path
        self.filepath = os.path.join(
            os.path.expanduser(path), filename)

        self.load()

    def load(self):
        # if file does not exist, return
        if not os.path.exists(self.filepath):
            return

        # open the file and read in raw values
        with open(self.filepath, 'r') as fh:
            raw_values = json.loads(fh.read())

        # don't just trust raw values
        # but only get known keys

        for key in self.variables:
            if key in raw_values and 'value' in raw_values[key]:
                raw_value = raw_values[key]['value']
                self.variables[key]['value'] = raw_value

    def save(self, settings=None):
        json_string = json.dumps(self.variables)
        with open(self.filepath, 'w') as fh:
            fh.write(json_string)

    def set(self, key, value):
        if(key in self.variables and
           type(value).__name__ == self.variables[key]['type']):
            self.variables[key]['value'] = value
        else:
            raise ValueError("Bad key or wrong variable type")
