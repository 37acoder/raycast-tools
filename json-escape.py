#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title json-escape
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "json" }

import sys
import json

print(json.dumps(sys.argv[1]))
