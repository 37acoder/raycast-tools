#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title ts2time
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }

import sys

ts = sys.argv[1]

# turn timestamp to time
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(float(ts)))))
