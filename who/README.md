# `who`

This directory contains data on past UPLers.

It is entirely crowd-sourced (via PRs), so if you want to submit your (__own__) data,
__please do!__

You should be able to edit this directly on GitHub, as well.

Please send any questions to the coords email (`upl-coords...`).

## JSON Format

__Please only enter your data in the `who.json` file.__

Your object should be a member of the `who` array in that file.

The data should follow the following format:

```json
{
  "name": "your actual name",
  "username": "your upl username",
  "start": "semester and year you became a UPL member (e.g. Spring 2016)",
  "end": "semester and year you left the UPL (i.e. graduated)",
  "coord": "`true`|`false` --> were you a coord?",
  "link": "link to your personal website or whatever!",
  "jobs": "a string of places you've worked (for bragging :D)",
  "misc": "a _short_ chunk of text to add whatever you want"
}
```

If you want to be a good citizen, run the new JSON through a linter/validator
such as [this one](https://jsonformatter.curiousconcept.com/).

## Run the Markdown generator

Editing tables in Markdown is not fun. That's why we're using JSON.

In order to convert from JSON to Markdown, we have a script called `make_who.py`

To run this command, enter the following into your terminal:

```bash
$ python make_who.py
```

This will update the `who.markdown` file for you.

If you want to be a good citizen _again_, run the Markdown output through a
generator/viewer such as [this one](https://jbt.github.io/markdown-editor/#).
