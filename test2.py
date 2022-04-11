import shapefile
import matplotlib.pyplot as plt
import os

from ACAD import *

def nearest(cand,all):
  return min(all, key=lambda i: i.vertices[0].pt_to_pt(cand.vertices[-1]))

fig,ax = plt.subplots()

fname = os.path.join("project_data","TMPL_ED41.35628","all_lines.shp")
with shapefile.Reader(fname) as shp:
  shapes = shp.shapes()
  points = [[Point(i[0],i[1]) for i in shape.points] for shape in shapes]
  polylines = [Polyline(i) for i in points]
  
latest = polylines[2]
latest.plot(ax,"r")
vertices_sorted = []

while polylines:
  vertices_sorted += latest.vertices
  latest = nearest(latest,polylines)
  polylines.remove(latest)

vertices_sorted[0].plot(ax,"ro")
vertices_sorted[-1].plot(ax,"go")


final = Polyline(vertices_sorted)
final.plot(ax)

ax.set_aspect('equal', adjustable='box')
plt.show()

fname = os.path.join("project_data","TMPL_ED41.35628","sorted_lines")
with shapefile.Writer(fname) as shp:
  shp.field("name","C")
  shp.line([final.KML_coords()])
  shp.record("TMPL Centerline")

print("DONE")
