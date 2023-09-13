![CI](https://github.com/TheNewThinkTank/tomark/actions/workflows/wf.yml/badge.svg)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/tomark?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/tomark/archive/refs/heads/main.zip)
# tomark

A Python module that converts a list of dictionaries to a markdown formatted table.

Note: Each dict in the list must have the same number of elements.

Installing

`!python3 -m pip install --upgrade tomark`

Usage:

```
from tomark import Tomark

data = [
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

markdown = Tomark.table(data)
print(markdown)
```

Example table output:

| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | v1.0 | None | Updates UI to be more awesome |

Example raw ouput:

```
| PR  | Status | Date | Title |
|----|----|----|----|
| 292 | open | None | Adds new wiz bang feature |
| 286 | v1.0 | None | Updates UI to be more awesome |

```
