# Convert input mesh to output mesh format using pymeshlab
# Install pymeshlab:
# pip3 install pymeshlab

# Usage:
# python3 meshlab_convert.py <input_mesh> <output_mesh>

# Batch convert PLY files in a directory to OBJ files:
# find ./ -name '*.ply' -exec python3 meshlab_convert.py {} {}.obj \;

import sys
from os.path import exists, dirname
import pymeshlab

if len(sys.argv) != 3:
	print("Incorrect number of arguments")
	sys.exit(1)

sourceMesh = sys.argv[1]
destMesh = sys.argv[2]

if not exists(sourceMesh):
	print(f"Source mesh file '{sourceMesh}' does not exist")
	sys.exit(1)

print(f"Converting {sourceMesh} to {destMesh} ...")

ms = pymeshlab.MeshSet()
ms.load_new_mesh(sourceMesh)
ms.save_current_mesh(destMesh)
