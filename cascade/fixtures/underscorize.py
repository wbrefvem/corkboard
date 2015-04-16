import json
import inflection
import shutil
import sys

file_name = sys.argv[1]

shutil.copyfile(file_name, '%s.copy' % file_name)

f = open(sys.argv[1], 'r+')
se = json.load(f)

for fixture in se:
    fields = fixture['fields']
    for key in fields.keys():
        new_key = inflection.underscore(key)
        if new_key != key:
            fields[new_key] = fields[key]
            del fields[key]

f.seek(0)
json.dump(se, f, indent=4)
