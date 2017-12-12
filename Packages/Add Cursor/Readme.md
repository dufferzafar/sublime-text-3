
## Readme

Improved multiple cursor support.

Allows you to add cursors at arbitrary positions.

Taken from: https://gist.github.com/skuroda/5201642

Sample Keymap:

```json
{ "keys": ["f12"], "command": "cursor", "args": {"action": "add"}},
{ "keys": ["f11"], "command": "cursor", "args": {"action": "show"}},
{ "keys": ["f10"], "command": "cursor", "args": {"action": "clear"}},
{ "keys": ["f9"], "command": "cursor", "args": {"action": "remove"}}
```