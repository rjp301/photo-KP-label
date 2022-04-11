import shapefile
import simplekml
import matplotlib.pyplot as plt
import random
import os

from pprint import pprint
from ACAD import *

from pyproj import CRS,Proj
crs = CRS.from_epsg(26910)
proj = Proj(crs)

def import_CL(shp_path) -> Polyline:
  fname = os.path.join(shp_path,"points")
  with shapefile.Reader(fname) as shp:
    KP_index = [i[0] for i in shp.fields].index("KP") - 1
    KPs = []
    for shp_rcd in shp.iterShapeRecords():
      coords_x = shp_rcd.shape.points[0][0]
      coords_y = shp_rcd.shape.points[0][1]
      label = float(shp_rcd.record[KP_index])
      KPs.append(Point(coords_x,coords_y,label=label))
    KPs.sort(key = lambda i: i.label)

  fname = os.path.join(shp_path,"line")
  with shapefile.Reader(fname) as shp:
    pprint(shp.shapes()[0].points)
    vertices = [Point(i[0],i[1]) for i in shp.shapes()[0].points]
    print(f"{len(vertices)} vertices in CL")

  return Polyline(vertices,KPs)

path = os.path.join("project_data","TMPL_ED41.35628")
CL = import_CL(path)

fig,ax = plt.subplots()
CL.plot(ax)

kml = simplekml.Kml()

for i in range(15):
  pt = random.choice(CL.vertices)
  new_pt = pt.copy(random.randint(1,50),random.randint(1,50))
  chainage = CL.find_KP(pt)
  print(chainage)

  kml.newpoint(
    name = format_KP(chainage),
    coords = new_pt.to_geo(proj).KML_coords(),
  )

kml.save("test.kml")
print("DONE")

CL.vertices[0].plot(ax,"ro")
ax.set_aspect('equal', adjustable='box')
plt.show()

# print(CL)
