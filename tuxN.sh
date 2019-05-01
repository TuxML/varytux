#!/bin/bash

for i in {1..30}
do
python3 tuxml-vary.py > TuxVariant$i.svg
svgexport TuxVariant$i.svg TuxVariant$i.png
done
convert -delay 100 -loop 0 TuxVariant*.png SuperTux.gif