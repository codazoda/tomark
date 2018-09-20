# tomark

A Python module that converts a list of dictionaries to a markdown formatted table.

Note: Each dict in the list must have the same number of elements.

Example table output:

| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | open | None | Updates UI to be more awesome |

Example list of dictionaries:

```
[
  {
    'pr': 291, 
    'status': 'closed', 
    'date': datetime.datetime(2018, 9, 14, 14, 40, 55), 
    'title': 'Adds new wiz bang feature'
  },
  {
    'pr': 290, 
    'status': 'v1.0', 
    'date': datetime.datetime(2018, 9, 14, 14, 40, 55), 
    'title': 'Updates UI to be more awesome'
  }
]
```

Example raw ouput:

```
| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | open | None | Updates UI to be more awesome |

```

```
grip README.md --export readme.html
wkhtmltoimage --width 1920 --height 1080 https://www.google.com test.png
```
