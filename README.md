# VaryTux: Generator of Tux logos 

**The project has moved to: https://github.com/diverse-project/tuxart**

`sh tuxN.sh` generates 30 variants of Tux and assembles them into a gif. 
A Python script `tuxml-vary.py` is doing the random transformation of the Tux. 
Right now it is very stupid since it only changes color. And technically speaking it just replaces some portion of SVG with a regular expression (true story!). 

The plan is to:
 * significantly improve the visual variations (with more aesthetic, diverse, and understandable transformations of Tux)  
 * significantly improve the technical realization (stop regex, we should certainly use a SVG library)
 
![tux gif](SuperTux.gif)


