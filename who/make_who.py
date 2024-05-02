#!/usr/bin/env python

import json

# Return the year of the start date with .5 added for spring dates
def by_date(data_name, user):
  date = user.get(data_name, '')
  if date == '' or date == '???':
    return 0
  if date[0:6].lower() == "spring":
    return int(date[-4:]) + .5
  elif date[0:6].lower() == "winter":
    return int(date[-4:]) + .25
  else:
    return int(date[-4:])

# first open the input file for reading
with open('./who.json', 'r') as who_file:
  # first load the data
  json_data = json.load(who_file)
  who_data = json_data['who']

  # then sort it by priority of end date, then start date, then username
  sorted_data = sorted(who_data, key=lambda user: user['username'])
  sorted_data = sorted(sorted_data, key=lambda user: by_date('start', user))
  sorted_data = sorted(sorted_data, key=lambda user: by_date('end', user))

# now open the output file for writing
with open('./who.markdown', 'w') as markdown_file:
  table_header  = '| Username | Name | Start | End | Coord? | Jobs | Link | Misc. |\n'
  table_header += '| ---------|------|-------|-----|--------|------|------|------ |\n'

  table_header = table_header.strip()

  markdown_file.write(table_header)

  for user in sorted_data:

    # first set the emoji for the coord status
    # emojis are supported assuming this is put on GitHub via GFM
    coord_emoji = None
    if user.get('coord', False):
      coord_emoji = ':white_check_mark:'
    else:
      coord_emoji = ':x:'

    name      = user['name']      # should throw error if DNE
    username  = user['username']  # should throw error if DNE
    start     = user.get('start', '???')
    end       = user.get('end',   '???')
    jobs      = user.get('jobs', '')
    link      = user.get('link', '')
    misc      = user.get('misc', '')

    row_entry = '\n| `%s` | %s | %s | %s | %s | %s | %s | %s |'
    cols = (username, name, start, end, coord_emoji, jobs, link, misc)
    cols = tuple(c.replace('|', '\|') for c in cols)
    row_entry %= cols

    markdown_file.write(row_entry)

  markdown_file.write('\n\n')
