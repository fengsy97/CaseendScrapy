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
# print(type(GPUS))
f1 = open('NVIDIA.json')
NvidiaGPUS = json.loads(f1.read())
count = 0
items = ["GPU Name","Architecture","Foundry","Release Date","Generation","Production Active","Base Clock","Boost Clock","Memory Clock","Memory Size","Memory Type","Memory Bus","Bandwidth","TDP","Weight","DirectX","Slot Width","Length","Width","Height"]
# for gpu in GPUS:
#     print(gpu)
#     for spec in GPUS[gpu]:
#         print(spec,GPUS[gpu][spec])
#     # break
#     count += 1
#     if(count > 10):
#         break

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('GPU.xlsx')
worksheet = workbook.add_worksheet()


# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

for item in items:
    worksheet.write(row, col, item)
    col += 1
row = 1
col = 0

for gpu in GPUS:
    worksheet.write(row, col, gpu)
    col += 1
    for item in items[1:]:
        if(item in GPUS[gpu]):
            worksheet.write(row, col, GPUS[gpu][item])
        else:
            worksheet.write(row, col, "N/A")
        col += 1
    row += 1
    col = 0
for gpu in NvidiaGPUS:
    worksheet.write(row, col, gpu)
    col += 1
    for item in items[1:]:
        if(item in NvidiaGPUS[gpu]):
            worksheet.write(row, col, NvidiaGPUS[gpu][item])
        else:
            worksheet.write(row, col, "N/A")
        col += 1
    row += 1
    col = 0

# # Iterate over the data and write it out row by row.
# for item, cost in (expenses):
#     worksheet.write(row, col,     item)
#     worksheet.write(row, col + 1, cost)
#     row += 1

# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()