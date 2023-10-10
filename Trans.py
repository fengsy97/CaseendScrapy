# GPU Name
# Architecture
# Foundry
# Release Date
# Generation
# Production Active
# Base Clock 1500 MHz
# Boost Clock 2700 MHz
# Memory Clock 1600 MHz
# Memory Size 16 GB
# Memory Type LPDDR5
# Memory Bus 64 bit
# Bandwidth 51.20 GB/s
# TDP 30 W
# Weight 608 g
# DirectX 12 Ultimate
# Slot Width Dual-slot
# Length 241 mm
# Width 127 mm
# Height 42 mm
import json
f = open('AMD.json')
GPUS = json.loads(f.read())
print(type(GPUS))
count = 0
for gpu in GPUS:
    print(gpu)
    for spec in GPUS[gpu]:
        print(spec,GPUS[gpu][spec])
    # break
    count += 1
    if(count > 10):
        break