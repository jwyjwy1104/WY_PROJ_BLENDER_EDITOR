import unittest
import bpy

filename = "..\WYCoordsys\WYCoordsys.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "WYMesh.py"
exec(compile(open(filename).read(), filename, 'exec'))

class WYMeshTestCases___init__(unittest.TestCase):    
    def test___init__tc_nc_loc_01(self):
        
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))

        cube = bpy.context.object

        cube.name = "TestCube0001"
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))

        cube.data.uv_textures.new(name="UVMap")

	
        wymesh.init_mesh_vertex_data()
        print(len(wymesh.main_mesh.polygons))
        print(wymesh.get_mesh_v_str())

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMeshTestCases___init__))
    