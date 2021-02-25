# Find min and max number in string
# (example of numbers: 12, 12.22, -434.4)

import re

s = "kfmk23mk32m4kmdvk3m4523-343lkm234km234lkm3$#$234.323.33"

nums = re.findall(r"[+-]?\d+(?:\.\d+)?", s)
print('Min: ', min(nums))
print('Max: ', max(nums))
