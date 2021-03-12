###Solution to problem 62 in ben stephenson's "the python workbook"

prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for p in prices:
  print(f'${p} - ${.6 * p:.2f} = ${p - .6 * p:.2f}')
