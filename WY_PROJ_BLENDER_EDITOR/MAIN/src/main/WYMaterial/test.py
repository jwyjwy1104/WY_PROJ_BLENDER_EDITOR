import unittest
import bpy
import mathutils

filename = "..\WYCoordsys\WYCoordsys.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "WYMaterial.py"
exec(compile(open(filename).read(), filename, 'exec'))

class WYMaterialTestCases(unittest.TestCase):    
    def test_01(self):
        
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))

        mat = bpy.data.materials.new(name="TestMaterial0001")
        
        mat.ambient = 0.0
        
        mat.mirror_color = (0,0,0)
        
        mat.diffuse_intensity = 0.0
        
        mat.diffuse_color = (0,0,0)
        
        mat.specular_intensity = 0.0
        
        mat.specular_color = (0,0,0)
        
        mat.specular_hardness = 1.0
        
        mat.raytrace_transparency.ior = 0.25
        
        mat.alpha = 0.0
        
        cube = bpy.context.object
        
        cube.name = "TestCube0001"       
        cube.data.uv_textures.new(name="TestTexture0001")

        image = bpy.data.images.new("TestTexture0001", width=100, height=100)
   
        image.filepath_raw = "TestTextureImagePath0001.png" 
        cube.data.uv_textures[0].data[0].image = image 
        
        cube.data.materials.append(mat)
        
        wymaterial = WYMaterial(cube, mat)
   
        wymaterial.init_mat_data()
        print(str(wymaterial))     


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYMaterialTestCases))
    