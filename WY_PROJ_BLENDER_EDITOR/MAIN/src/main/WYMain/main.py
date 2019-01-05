import os
import sys
import bpy
filepath = bpy.data.filepath
directory = os.path.dirname(filepath)
print(directory)

filename = os.getcwd() + "\\..\\..\\main\\WYModel\\WYModel.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYModelManager\\WYModelManager.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYMesh\\WYMesh.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYMaterial\\WYMaterial.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYUtil\\WYUtil.py" 
exec(compile(open(filename).read(), filename, 'exec'))
filename = os.getcwd() + "\\..\\..\\main\\WYCoordsys\\WYCoordsys.py" 
exec(compile(open(filename).read(), filename, 'exec'))

if __name__ == "__main__":
    current_working_dir = os.getcwd()
    wymodelmanager = WYModelManager()
    XU = False
    M_XU = False
    YU = False
    M_YU = False
    ZU = True
    M_ZU = False

    XF = False
    M_XF = False
    YF = True
    M_YF = False
    ZF = False
    M_ZF = False
    wycoordsys = WYCoordsys(XU, M_XU, YU, M_YU, ZU, M_ZU, 
                            XF, M_XF, YF, M_YF, ZF, M_ZF)

    '''
    bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
    cube = bpy.context.object
    cube.name = "TestCube0001"
    cube.data.uv_textures.new(name="TestTexture0001")
    image = bpy.data.images.new("TestTexture0001", width=100, height=100)
    image.filepath_raw = "TestTextureImagePath0001.png"
    cube.data.uv_textures[0].data[0].image = image
    mat = bpy.data.materials.new(name="TestMaterial0001")
    
    wymesh = WYMesh(cube, wycoordsys)
    wymaterial = WYMaterial(cube, mat)
    wymodel = WYModel(wymesh, wymaterial)
    '''
    cube = bpy.context.object
    mat = cube.data.materials[0]
    wymesh = WYMesh(cube, wycoordsys)
    wymesh.init_mesh_data()

    wymaterial = WYMaterial(cube, mat)
    wymaterial.init_mat_data()

    wymodel = WYModel(wymesh, wymaterial)
    wymodelmanager.export_model(wymodel, current_working_dir + "\\..\\test")
    #wymodelmanager.import_model(current_working_dir + "\\..\\test")
