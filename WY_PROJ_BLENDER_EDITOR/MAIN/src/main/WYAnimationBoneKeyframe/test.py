import os
import sys
import math
import unittest


precompile_filename = "../WYMesh/WYMesh.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

precompile_filename = "../WYModel/WYModel.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

precompile_filename = "WYArmatureBone.py"
exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))

class WYArmatureBoneTestCase(unittest.TestCase):
    def test_WYArmatureBoneTestCase(self):
        myArmature = bpy.data.armatures.new("TestArmature0001")
        myArmatureObject = bpy.data.objects.new("TestArmature0001", myArmature)
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0001"
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)  
        myArmatureBone = myArmatureObject.data.edit_bones.new("TestArmatureBone0001")
        myArmatureBone.head = [0,0,0]
        myArmatureBone.tail = [0,0,0]
        cube.vertex_groups.new("TestArmatureBone0001")
        cube.vertex_groups["TestArmatureBone0001"].add([0], 0, "REPLACE")
        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_data()
        wymodel = WYModel(wymesh, None)
        wyarmaturebone = WYArmatureBone(myArmatureBone, wymodel)
        wyarmaturebone.init_armature_bone_data()
        print(wyarmaturebone.armature_bone_head)
        self.assertTrue(wyarmaturebone.armature_bone_head == [0,0,0] and wyarmaturebone.armature_bone_tail == [0,0,0] and wyarmaturebone.armature_bone_name == "TestArmatureBone0001")
        self.assertTrue(wyarmaturebone.armature_vertex_group_array[0][0] == 0 and wyarmaturebone.armature_vertex_group_array[0][1][0] == cube.data.vertices[0].co.x and wyarmaturebone.armature_vertex_group_array[0][1][1] == cube.data.vertices[0].co.y and wyarmaturebone.armature_vertex_group_array[0][1][2] == cube.data.vertices[0].co.z and wyarmaturebone.armature_vertex_group_array[0][2] == 0)
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)  
        bpy.data.objects["TestArmature0001"].select = True
        bpy.ops.object.delete() 

        '''
        myArmature = bpy.data.armatures.new("TestArmature0001")
        myArmatureObject = bpy.data.objects.new("TestArmature0001", myArmature)
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), rotation=(0,0,0))
        cube = bpy.context.object
        cube.name = "TestCube0001"
        bpy.context.scene.objects.link(myArmatureObject)
        bpy.context.scene.objects.active = myArmatureObject
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)  

        myArmatureObject.data.edit_bones.new("TestArmatureBone0001")

        cube.vertex_groups.new("TestArmatureBone0001")
        cube.vertex_groups["TestArmatureBone0001"].add([0], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([1], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([2], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([3], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([4], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([5], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([6], 0, "REPLACE")
        cube.vertex_groups["TestArmatureBone0001"].add([7], 0, "REPLACE")

        wymesh = WYMesh(cube, WYCoordsys(False,False,False,False,True,False,False,False,True,False,False,False))
        wymesh.init_mesh_data()
        wymodel = WYModel(wymesh, None)

        wyarmaturebone = WYArmatureBone(myArmatureObject.data.edit_bones["TestArmatureBone0001"], wymodel)
        wyarmaturebone.init_armature_bone_name()
        wyarmaturebone.init_armature_bone_vertex_group_data()

        print(wyarmaturebone.get_armature_bone_vg_str())

        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)  
        bpy.data.objects['TestArmature0001'].select = True
        bpy.ops.object.delete() 
        '''
if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(WYArmatureBoneTestCase))
