#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title base64
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "dropdown", "placeholder": "mode","data": [ {"title": "Encode", "value": "encode"},{"title": "Decode", "value": "decode"}], "required": true}
# @raycast.argument2 { "type": "text", "placeholder": "input"}


import sys
import base64

if sys.argv[1] == "encode":
    print(base64.b64encode(sys.argv[2].encode("utf-8")).decode("utf-8"))
else:
    print(base64.b64decode(sys.argv[2]).decode("utf-8"))
