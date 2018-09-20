# tomark

A Python module that converts a list of dictionaries to a markdown formatted table.

Note: Each dict in the list must have the same number of elements.

Example table output:

| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | v1.0 | None | Updates UI to be more awesome |

Example list of dictionaries:

```
[
  {
    'pr': 291, 
    'status': 'closed', 
    'date': 'None', 
    'title': 'Adds new wiz bang feature'
  },
  {
    'pr': 290, 
    'status': 'v1.0', 
    'date': 'None', 
    'title': 'Updates UI to be more awesome'
  }
]
```

Example raw ouput:

```
| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | v1.0 | None | Updates UI to be more awesome |

```
