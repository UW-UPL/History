#!/usr/bin/env python

import json

# first open the input file for reading
with open('./who.json', 'r') as who_file:
  # first load the data
  json_data = json.load(who_file)
  who_data = json_data['who']

  # then sort it by (1) start date (2) username

  # TODO: might need to map start date to something more suited for sorting
  by_start_date  = lambda user: user.get('start', '') # start date not required
  by_username    = lambda user: user['username']

  sorted_data = sorted(who_data, key=by_start_date)
  sorted_data = sorted(sorted_data, key=by_username)

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
    row_entry %= (username, name, start, end, coord_emoji, jobs, link, misc)

    markdown_file.write(row_entry)

  markdown_file.write('\n\n')
