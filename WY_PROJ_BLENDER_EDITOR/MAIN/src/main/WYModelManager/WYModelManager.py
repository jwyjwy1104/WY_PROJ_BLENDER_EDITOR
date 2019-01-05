################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYModelManager.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYModelManager test plan  : https://docs.google.com/document/d/1WMQES609yV3yxMbQBqHI5BEUIHDYofaa6VoLwnf2Gd4/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import os 
import bpy
import bmesh
import sys
import struct
import math
from bpy import context

filename = os.getcwd() + "\\..\\..\\main\\WYModel\\WYModel.py"
exec(compile(open(filename).read(), filename, 'exec')) # Import WYModel.py

filename = os.getcwd() + "\\..\\..\\main\\WYArmature\\WYArmature.py"
exec(compile(open(filename).read(), filename, 'exec')) # Import WYArmature.py

filename = os.getcwd() + "\\..\\..\\main\\WYArmatureBone\\WYArmatureBone.py" 
exec(compile(open(filename).read(), filename, 'exec')) # Import WYArmatureBone.py

filename = os.getcwd() + "\\..\\..\\main\\WYAnimation\\WYAnimation.py"
exec(compile(open(filename).read(), filename, 'exec')) # Import WYAnimation.py

class WYModelManager:
    '''
    This class holds all the operator and functions to export and import the 
    model objects.

    .. seealso:: ../WYModel/WYModel.py
    .. seealso:: ../WYMesh/WYMesh.py
    .. seealso:: ../WYMaterial/WYMaterial.py

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable wyutil: WYUtil object to use the utility functions.

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self):
        Test: https://docs.google.com/spreadsheets/d/1xN4-exy7Uh98Tc6ovree4VDkLdwT7t8VqC-f14idYro/edit#gid=0 
    # def export_model(self, model, wycoordsys, file_path):
        Test: https://docs.google.com/spreadsheets/d/1uH6t-7qX2jDz4dPL5Bs6x3jnd1dyOL_LSMOfFhYHynw/edit#gid=0
    # def export_wymodel(self, wymodel, wymodel_file_path):
        Test: https://docs.google.com/spreadsheets/d/1D3mJt1VoWVkHqNy0aRJJwHDBsoaE3dKzN4loyw6qgyM/edit#gid=0
    # def export_wymesh(self, wymesh, wymesh_file_path):
        Test: https://docs.google.com/spreadsheets/d/1Mc_wcLqxg-H-0ynavwr8u2yPotRocm2lqYgZEqOq4d0/edit#gid=0
    # def export_wymaterial(self, wymaterial, wymaterial_file_path):
        Test: https://docs.google.com/spreadsheets/d/1o6E18H33vaPJ427nB7p5Ys37NbknKKlLBBhAScA3N-8/edit#gid=0
    # def import_model(self, file_path):
        Test: https://docs.google.com/spreadsheets/d/1CUmV8PgNtZH5n2fcC0QUqcGLYF1uUuh6BWriNV4Yxmk/edit#gid=0
    # def import_mesh(self, mesh_file_path):
        Test: https://docs.google.com/spreadsheets/d/1rDVAsp_CE6uRglEGrImrnhmUgCG3EWH7mgduQJSTwgo/edit#gid=0 
    # def import_wymesh(self, wymesh_file_path):
        Test: https://docs.google.com/spreadsheets/d/1KsQmU5zFlfgDWacTtxUDNpqaBb0WPFkQ9VR35RPT344/edit#gid=0 
    # def import_wycoordsys(self, wycoordsys_file_path):
        Test: https://docs.google.com/spreadsheets/d/1M42DG9S4zQ4-R4Ux5QH5clSMGpBZQQGQbkx0W-jDj5E/edit#gid=0 
    # def import_material(self, material_file_path):
        Test: https://docs.google.com/spreadsheets/d/1BpzoQgV1P4VjUXjmI-xkInaossHdzQRjiCbhnrsb8Go/edit#gid=0 
    # def import_wymaterial(self, wymaterial_file_path):
        Test: https://docs.google.com/spreadsheets/d/1yzNPEYhUXkbTVx_xDnKQCgavE3qsjpNRTAHZYmQqwqo/edit#gid=0 

    # def export_armature_model(self, armature, model, wycoordsys, file_path):
        Test: https://docs.google.com/spreadsheets/d/149_si9VpupsrSnovcJWXwUKmz5W-DnQzcHozawrIBmM/edit#gid=0
    # def export_wyarmature(self, wyarmature, wyarmature_file_path):
        Test: https://docs.google.com/spreadsheets/d/11fbNudcP6Jor4lVYvqqII4CINhreFV9ZsycHRx2_voo/edit#gid=0
    # def import_armature_model(self, file_path):
        Test: https://docs.google.com/spreadsheets/d/1-7GY89tbi46-TH5Y8CjldHzSQfaQQvjRsnb_sN3OdHU/edit#gid=0
    # def import_armature(self, armature_file_path):
        Test: https://docs.google.com/spreadsheets/d/1SftdDc9ied2QCtu10oeE9C8P2TGiSmucvM32hhlE-P0/edit#gid=0
    # def import_wyarmature(self, wyarmature_file_path):
        Test: https://docs.google.com/spreadsheets/d/1Lddy0D1mUnQBpv-yHjQwY5zQ_rw_AKeTocFCukzrk-c/edit#gid=0
    # def import_wyarmaturebone(self, wyarmature, wyarmature_file_obj):
        Test: https://docs.google.com/spreadsheets/d/1STjdZobtxHn3NvHafDbojuaYcB6x0PP5f0NZL4zGW1U/edit#gid=0

    # def export_animation_model(self, animation, armature, model, wycoordsys, start_index, end_index, file_path):
        Test: https://docs.google.com/spreadsheets/d/1G4DKzKU1Ecfjsm7FBKN0clHXQNJp7k0J5xMGPkxW6ow/edit#gid=0
    # def export_wyanimation(self, wyanimation, wyanimation_file_path):
        Test: https://docs.google.com/spreadsheets/d/1awVA75jihNoe2m_5cK5F2qWChFP2PdYZnTmCuaJiAEg/edit#gid=0
    # def import_animation_model(self, file_path):
        Test: https://docs.google.com/spreadsheets/d/1a__vFyk9Ae669GaZ9XSHY_tncb1UkrazyXVFm6GRupE/edit#gid=0
    # def import_animation(self, animation_file_path):
        Test: https://docs.google.com/spreadsheets/d/1MPCt5qTCpE2oPRsmjUmFbprHaMg8dJ4E9t6Kz5bW_tg/edit#gid=0
    # def import_wyanimation(self, wyanimation_file_path):           
        Test: https://docs.google.com/spreadsheets/d/1VicT9n6C2LH5zK_ldFFnaQLfZuInJkhQsYHePuvFWvQ/edit#gid=0
    # def import_wyanimationbone(self, wyanimation, wyanimation_file_obj):       
        Test: https://docs.google.com/spreadsheets/d/1bRMkq27WFPgfg_sDjIRfK2do9lDzzcHF1qUuYGQbdMY/edit#gid=0

    '''
    def __init__(self):
        self.wyutil = WYUtil()
        
    def export_model(self, model, wycoordsys, file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYModel object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through export_wymodel sub function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the Blender bpy.data.object object convert into
        WYModel object by accessing Blender Mesh and Blender Material inside 
        the retrieved bpy.data object and pass it down to export_wymodel sub
        function to export the bpy.data onto local file with WYModel format.

        The file extension is appended manually through sub function, so 
        only file name is enough to export the file.

        Calling sub functions: WYModel::export_wymodel()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  model: Blender bpy.data.object to export with.
        :type   model: bpy.data.object
        :param  wycoordsys: WYCoordsys object to export the model with 
                            customized coordinate system.
        :type   wycoordsys: WYCoordsys
        :param file_path: Absolute file path to export the Blender 
                          bpy.data.object onto.
        :type  file_path: string

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return  wymodel: WYModel object created with bpy.data.object 
                          to export with.
        :rtype   wymodel: WYModel

        '''
        wymesh = None
        wymaterial = None
        wymodel = None

        model.data = self.wyutil.triangulate_mesh(model.data)

        if model == None:
            raise Exception("ERROR::WYModelManager::export_model::bpy.data.object is None!!!")

        if wycoordsys == None:
            wycoordsys = WYCoordsys(False,False,False,False,True,False,
                                    False,False,True,False,False,False)

        # CAUTION:
        #   For material part, I have been using texture mapping a lot with
        #   smart UV projects so I won't be using any material objects when 
        #   editing models so I will be:
        #       Exporting with texture data. (No material)
        #       Importing with texture data allocated in material object.
        #  This is easier for me to use my exporter because using material 
        #  objects for UV mapping is not as easy as I did with smart UV project 
        #  UV mapping. 
        #
        #  But this could cause some errors since the input and output is not 
        #  exactly correct so I need to make sure the input follows by the 
        #  exact expected output tested through test cases.
        #
        #  So for handling multiple texture data or material I can just adjust
        #  code here.
        if len(model.data.uv_textures) > 0:
            # len(model.data.materials) > 0 or 
            wymaterial = WYMaterial(model, bpy.data.materials.new(model.name))
            wymaterial.init_material_data()

        wymesh = WYMesh(model, wycoordsys)
        wymesh.init_mesh_data()
        wymodel = WYModel(wymesh, wymaterial)

        # Export WYModel object through sub function.
        self.export_wymodel(wymodel, file_path)

        # Return exported WYModel object.
        return wymodel

    def export_wymodel(self, wymodel, wymodel_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYModel object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through this function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the final mesh export string and final material 
        export string from WYModel object passed into the function and write 
        them onto the file on given file path also passed into the function.

        WYModel object contains one WYMesh object and one WYMaterial object
        if WYMaterial object is not None, then assign the material export
        file path to the WYMesh object in order to let the mesh exported file
        know where the relative material file is by setting the "mtllib" element
        value inside WYMesh object with the final export material file path.

        The file extension is appended manually through this function, so 
        only file name is enough to export the file.

        Calling sub functions: WYModel::get_material_export_str()
        Calling sub functions: WYModel::get_mesh_export_str()
        Calling sub functions: WYMesh::init_mesh_material_relfile_path()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  wymodel: Main WYModel object to export the mesh and material 
                         data with.
        :type   wymodel: WYModel
        :param file_path: Absolute file path to export the WYModel object onto.
        :type  file_path: string

        '''
        if wymodel == None:
            raise Exception("ERROR::WYModelManager::export_wymodel::WYModel object is None!!!")

        # If export file path starts with "." as first character, which means 
        # current working directory so prepend current working directory path.
        if wymodel_file_path[0] == ".":
            wymodel_file_path = os.getcwd() + "\\" + wymodel_file_path

        # Appending extensions to convert the file path to seperate the files 
        # with same name. 
        #   Extension .wyo - For WYMesh.
        #   Extension .wym - For WYMaterial.
        wymesh_file_path = wymodel_file_path + ".wyo"
        wymaterial_file_path = wymodel_file_path + ".wym"

        # Export WYMaterial object to file and initialize its exported file path
        # to corresponding WYMesh obejct if exist.
        if wymodel.main_wymaterial != None:
            # Export WYMaterial object.
            self.export_wymaterial(wymodel.main_wymaterial, 
                                   wymaterial_file_path)
            # Initialize WYMaterial object exported file path to corresponding 
            # WYMesh object.
            wymodel.main_wymesh.init_mesh_material_relfile_path(
                wymaterial_file_path)

        # Export WYMesh to file.
        if wymodel.main_wymesh != None:
            # Export WYMesh object.
            self.export_wymesh(wymodel.main_wymesh, wymesh_file_path)

    def export_wymesh(self, wymesh, wymesh_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYMesh object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through this function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the final mesh export string and write it to
        given export file path.

        Called by function WYModelManager::export_model()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  wymesh: WYMesh object to export the mesh data with.
        :type   wymesh: WYMesh
        :param wymesh_file_path: Absolute file path to export the WYMesh object 
                                 onto.
        :type  wymesh_file_path: string

        '''
        # Check exist.
        if wymesh == None:
            raise Exception("ERROR::WYModelManager::export_wymesh::WYMesh object is None!!!")
       
        # Export WYMesh object.
        with open(wymesh_file_path, 'w+') as wymesh_export_file:
            print("------------------------------------------------------------------------------")
            print("Writing mesh to :  " + wymesh_file_path)
            print("------------------------------------------------------------------------------")
            wymesh_export_file.write(str(wymesh))

    def export_wymaterial(self, wymaterial, wymaterial_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYMesh object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through this function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the final mesh export string and write it to
        given export file path.

        Called by function WYModelManager::export_model()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  wymaterial: WYMaterial object to export the mesh data with.
        :type   wymaterial: WYMaterial
        :param wymaterial_file_path: Absolute file path to export the 
                          WYMaterial object onto.
        :type  wymaterial_file_path: string

        '''
        # Check exist.
        if wymaterial == None:
            raise Exception("ERROR::WYModelManager::export_wymodel::WYModel object is None!!!")

        # Export WYMaterial object.
        if wymaterial != None:
            with open(wymaterial_file_path, 'w+') as wymaterial_export_file:
                print("------------------------------------------------------------------------------")
                print("Writing material to :  " + wymaterial_file_path)
                print("------------------------------------------------------------------------------")
                wymaterial_export_file.write(str(wymaterial))

    def import_model(self, file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which imports the model from local files
       
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the mesh local file and creates bpy.data.object 
        object and finds the corresponding material files to create 
        bpy.data.material object and load the model onto the Blender
        application screen.

        Calling sub function: WYModelManager::import_mesh()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param file_path: Absolute file path to import the model object from.
        :type  file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: WYModel object which all the data values are imported from 
                 given file path.
        :rtype : WYModel
        '''
        wymodel = None
        wymesh = None
        wymaterial = None

        if file_path.find(".wyo") != -1:
           mesh_file_path = file_path
        else:
           mesh_file_path = file_path + ".wyo"
        
        if os.path.isfile(mesh_file_path) == False:
            #raise Exception("ERROR::WYModelManager::import_model::Mesh file not exists!!!")
            return

        # Import Blender mesh object from file.
        wymesh = self.import_mesh(mesh_file_path)
        #wymesh.init_mesh_data()

        # Import Blender material object from file.
        if wymesh.mesh_material_relfile_path != "":
            wymaterial = self.import_material( \
                wymesh.mesh_material_relfile_path)
            # Append Blender material to the Blender mesh object.
            wymesh.main_mesh_obj.data.materials.append(
                wymaterial.main_material_obj)

        # Return WYModel object initialized with imported WYMesh and WYMaterial
        # objects.
        return WYModel(wymesh, wymaterial)

    def import_mesh(self, mesh_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the bpy.data.mesh
        object using the data loaded in the WYMesh object loaded by 
        calling sub function WYModelManager::import_wymesh().

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the mesh file from given file path
        and load the data values onto newly created WYMesh object and 
        load the WYMesh intialized value onto new bpy.data.mesh object
        and return the WYMesh object holding the newly initialized 
        bpy.data.mesh object.

        Calling sub function: WYModelManager::import_wymesh()

        :Post-condition: Blender mesh object is created using the WYMesh object 
                         imported from file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param mesh_file_path: Absolute file path to import the WYMesh object
                               from.
        :type  mesh_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wymesh: WYMesh object imported from file.
        :rtype  wymesh: WYMesh
        '''
        wymesh = None

        if os.path.isfile(mesh_file_path) == False:
            raise Exception("ERROR::WYModelManager::import_mesh::Mesh file not exists!!!")
            return
        # Load local file onto WYMesh object.
        wymesh = self.import_wymesh(mesh_file_path)

        # ----------------------------------------------------------------------
        # Create mesh on Blender scene using the WYMesh data loaded from file
        # locate it onto the Blender scene cursor
        # ----------------------------------------------------------------------
        # Set cursor location to (0,0,0).
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        # Get 3D cursor location.
        curloc = bpy.context.scene.cursor_location

        # Need to convert the vertex index array from [1,2,3,1,2,3 ...]
        # into [[1,2,3], [1,2,3], ...] in order to create the Blender mesh 
        # object with WYUtil::create_custom_mesh() function.
        temp = []
        myiter = iter(range(0, len(wymesh.mesh_vertex_index_array)))
        for i in myiter:
            temp.append([wymesh.mesh_vertex_index_array[i], wymesh.mesh_vertex_index_array[i+1], wymesh.mesh_vertex_index_array[i+2]])
            i += 2
            next(myiter, None)
            next(myiter, None)
        #wymesh.mesh_vertex_index_array = temp

        # Create Blender object on Blender scene by calling 
        # WYUtil::create_custom_mesh function with data initialized inside 
        # WYMesh object initialized from local file.
        imported_object = self.wyutil.create_custom_mesh( \
                               wymesh.mesh_obj_name, \
                               curloc[0], curloc[1], curloc[2], \
                               wymesh.mesh_vertex_array, \
                               temp)

        wymesh.main_mesh_obj = imported_object
        wymesh.main_mesh = imported_object.data

        # If "mtllib" element is not empty string then create the UV layer
        # and load the material file.
        if wymesh.mesh_material_relfile_path != "" and \
           wymesh.mesh_texture_coord_array != []:

            # Texture coordinates - UV mapping 
            uvtex = imported_object.data.uv_textures.new()
            for uvLayer in imported_object.data.uv_layers:
                for i in range(len(uvLayer.data)):
                    uvLayer.data[i].uv = wymesh.mesh_texture_coord_array[\
                        wymesh.mesh_texture_coord_index_array[i]]

        # Changing vertex and normal coordinate imported data values from 
        # (x,y,z) to Vector((x,y,z)).
        temp = []
        for i in range(0, len(wymesh.mesh_vertex_array)):
            temp.append(Vector((wymesh.mesh_vertex_array[i])))
        wymesh.mesh_vertex_array = temp

        temp = []
        for i in range(0, len(wymesh.mesh_normal_array)):
            temp.append(Vector((wymesh.mesh_normal_array[i])))
        wymesh.mesh_normal_array = temp


        # Return the WYMesh object which holds the initialized bpy.data.object
        # imported from file.
        return wymesh

    def import_wymesh(self, wymesh_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYMesh object 
        by loading data from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the mesh file from given file path
        and load the data values onto newly created WYMesh object and
        return it.

        Calling sub function: WYModelManager::import_wycoordsys()

        :Post-condition: WYMesh object is created imported from file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wymesh_file_path: Absolute file path to import the WYMesh object
                                 from.
        :type  wymesh_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wymesh: Initialized WYMesh object from the imported file.
        :rtype  wymesh: WYMesh
        '''
        # Resulting WYMesh to return.
        wymesh = WYMesh()

        # CU, CF - Coordinate exported options.
        XU,M_XU,YU,M_YU,ZU,M_ZU = (False,)* 6
        XF,M_XF,YF,M_YF,ZF,M_ZF = (False,)* 6

        # o - Name of the mesh object to export with.
        obj_name = ""
        # mtllib - Relative custom material file path of the exported mesh.
        obj_mtl_file_path = ""

        # v - Main data structure collection of vertices of current mesh object 
        # to be exported.
        obj_vertex_array = []
        # Number of vertex element values loaded from the custom mesh file.
        obj_vertex_array_count = 0
        # f v/t/n - v - Main data structure collection of the vertex indices of 
        # current mesh object to be exported. 
        obj_vertex_index_array = []
        # Number of vertex index element values loaded from the custom mesh 
        # file.
        obj_vertex_index_array_counter = 0

        # vn - Main data structure collection of vertex normal vector of current
        #  mesh object to be exported.
        obj_normal_array = []
        # Number of vertex normal vector element values loaded from the custom 
        # mesh file.
        obj_normal_array_count = 0
        # f v/t/n - n - Main data structure collection of the vertex normal 
        # vector indices of current mesh object to be exported. 
        obj_normal_index_array = []
        # Number of vertex normal vector index element values loaded from the 
        # custom mesh file.
        obj_normal_index_array_counter = 0

        # vt - Main data structure collection of vertex texture coordinate of 
        # current mesh object's texture map to be exported.
        obj_texture_coord_array = []
        # Number of vertex texture coordinate element values loaded from the custom mesh file.
        obj_texture_coord_array_count = 0
        # f v/t/n - t - Main data structure collection of the vertex texture 
        # coordinate indices of current mesh object to be exported. 
        obj_texture_coord_index_array = []
        # Number of vertex texture coordinate index element values loaded from 
        # the custom mesh file.
        obj_texture_coord_index_array_counter = 0

        # Load export coordinate system onto WYCoordsys object first and then
        # start loading the mesh data so the vertex value is converted back
        # to original values.
        wycoordsys = self.import_wycoordsys(wymesh_file_path)

        # Read data from file and load them onto local variables initialized 
        # above.
        with open(wymesh_file_path) as wymesh_file:
            print("------------------------------------------------------------------------------")
            print("Loading WYMesh from :  " + wymesh_file_path)
            print("------------------------------------------------------------------------------")
            for line in wymesh_file:
                if line == "\n":
                    break

                # Tokenize line from file to convert to actual mesh data.
                firstToken, restToken = line.split(' ', 1)

                # o - Name of the mesh object
                if firstToken == 'o':
                    obj_name = restToken.split('\n')[0]
                    #print("o : " + str(obj_name))

                # mtllib - Custom material relative file path which 
                #          contains the material informations
                if firstToken == 'mtllib':
                    obj_mtl_file_path = restToken.split('\n')[0]
                    #print("mtllib : " + str(obj_mtl_file_path))
            
                # v - Vertices  
                if firstToken == 'v':
                    vertexElem = map(float, restToken.split())
                    vertexElem = list(vertexElem)
                    vertexCoordsX = vertexElem[0]
                    vertexCoordsY = vertexElem[1]
                    vertexCoordsZ = vertexElem[2]
                    # Convert the coordinate system.
                    resultVertex = wycoordsys.import_coordconversion(
                        vertexCoordsX,
                        vertexCoordsY,
                        vertexCoordsZ)
                    #print("v : " + str(resultVertex))
                    obj_vertex_array.append(resultVertex)
                    obj_vertex_array_count += 1

                # vt - Texture coordinates (UV layout) 
                if firstToken == 'vt':
                    texcoordsStrEleme = restToken.split()
                    convertedTexcoordStr = [eval(texcoordsStrEleme[0]), 
                                            eval(texcoordsStrEleme[1])]
                    #print(convertedTexcoordStr)
                    texcoordsElem = map(float, convertedTexcoordStr)
                    #print(str(set(texcoordsElem)))
                    obj_texture_coord_array.append(tuple(texcoordsElem))
                    obj_texture_coord_array_count += 1
            
                # vn - Normals  
                if firstToken == 'vn':
                    normalElem = map(float, restToken.split())
                    obj_normal_array.append(tuple(normalElem))
                    obj_normal_array_count += 1
            
                # Indices from faces (eg. f v/t/n)
                if firstToken == 'f':
                    # From above : f v1/t1/n1 v2/t2/n2 v3/t3/n3 
                    #              --> [ f ] [ v1/t1/n1 v2/t2/n2 v3/t3/n3 ]
                    # From below : [ v1/t1/n1 v2/t2/n2 v3/t3/n3 ] 
                    #              --> [ v1,t1,n1 ] [ v2,t2,n2 ] [ v3,t3,n3 ]
                    faceElem = [item.split('/') for item in \
                        restToken.split(' ')]
                
                    # If no texture exists then the face element will only 
                    # have 2 value so i need to process them differently.
                    #print(str(len(faceElem[0])))
                    if len(faceElem[0]) == 3: # Normal format "f v/t/n"
                        # Need to read inversely (eg. 1/2/3 --> 3/2/1)
                        # Need to convert from string to float using eval()
                        # Vertex index array should have format like this : 
                        # [[3, 2, 0], [5, 6, 4], ... , [1, 2, 3]] NOT 
                        #       [3, 2, 0, 5, 6, 4, ... 1, 2, 3]
                        # This is done in parent function "import_mesh"
                        obj_vertex_index_array.append(
                             eval(faceElem[0][0]) - 1)
                        obj_vertex_index_array.append(
                             eval(faceElem[1][0]) - 1) 
                        obj_vertex_index_array.append(
                             eval(faceElem[2][0]) - 1)
                        #obj_vertex_index_array.append([
                        #     eval(faceElem[0][0]) - 1,
                        #     eval(faceElem[1][0]) - 1, 
                        #     eval(faceElem[2][0]) - 1])
                    
                        # Texture coordinate index array can be computed as 
                        # [1,2,3,4 ... ] for easier implementation
                        obj_texture_coord_index_array.append(
                            eval(faceElem[0][1]) - 1)
                        obj_texture_coord_index_array.append(
                            eval(faceElem[1][1]) - 1)
                        obj_texture_coord_index_array.append(
                            eval(faceElem[2][1]) - 1)
                    
                        obj_normal_index_array.append(
                             eval(faceElem[0][2]) - 1)
                        obj_normal_index_array.append(
                             eval(faceElem[1][2]) - 1) 
                        obj_normal_index_array.append(
                             eval(faceElem[2][2]) - 1)
                    
                        # Increment array index
                        obj_vertex_index_array_counter += 3
                        obj_normal_index_array_counter += 3
                        obj_texture_coord_index_array_counter += 3
                    elif len(faceElem[0]) == 2: 
                        # Assuming if only 2 element value means no texture 
                        # coordinate one so assuming is exported with 
                        # format "f v/n".

                        # Need to read inversely (eg. 1/2/3 --> 3/2/1)
                        # Need to convert from string to float using eval()
                        # Vertex index array should have format like this : 
                        # [[3, 2, 0], [5, 6, 4], ... , [1, 2, 3]] NOT 
                        #       [3, 2, 0, 5, 6, 4, ... 1, 2, 3]
                        # This is done in parent function "import_mesh"
                        obj_vertex_index_array.append(
                             eval(faceElem[0][0]) - 1)
                        obj_vertex_index_array.append(
                             eval(faceElem[1][0]) - 1) 
                        obj_vertex_index_array.append(
                             eval(faceElem[2][0]) - 1)
                    
                        # Vertex normal vector index array.
                        obj_normal_index_array.append(
                             eval(faceElem[0][1]) - 1)
                        obj_normal_index_array.append(
                             eval(faceElem[1][1]) - 1)
                        obj_normal_index_array.append(
                             eval(faceElem[2][1]) - 1)
                    
                        # Increment array index
                        obj_vertex_index_array_counter += 3
                        obj_normal_index_array_counter += 3
        
        # Initialize WYMesh object to return.
        wymesh.wycoordsys = wycoordsys
        wymesh.main_mesh_obj = None
        wymesh.main_mesh = None
        wymesh.mesh_obj_name = obj_name
        wymesh.mesh_material_relfile_path = obj_mtl_file_path
        wymesh.mesh_vertex_array = obj_vertex_array
        wymesh.mesh_vertex_index_array = obj_vertex_index_array
        wymesh.mesh_normal_array = obj_normal_array
        wymesh.mesh_normal_index_array = obj_normal_index_array
        wymesh.mesh_texture_coord_array = obj_texture_coord_array
        wymesh.mesh_texture_coord_index_array = obj_texture_coord_index_array

        # Return initialized WYMesh object.
        return wymesh

    def import_wycoordsys(self, wycoordsys_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYCoordsys object 
        by loading data from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the mesh file from given file path
        and load the data values onto newly created WYCoordsys object and
        return it.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wycoordsys_file_path: Absolute file path to import the WYCoordsys 
                                     object from.
        :type  wycoordsys_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Initialized WYCoordsys object from the imported file.
        :rtype: WYCoordsys
        '''
        # CU, CF - Coordinate exported options.
        XU,M_XU,YU,M_YU,ZU,M_ZU = (False,)* 6
        XF,M_XF,YF,M_YF,ZF,M_ZF = (False,)* 6

        coordoption_up_str = ""
        coordoption_forward_str = ""
        # Read data from file and load them onto local variables initialized 
        # above.
        with open(wycoordsys_file_path) as wycoordsys_file:
            #print("------------------------------------------------------------------------------")
            #print("Loading WYCoordsys from :  " + wycoordsys_file_path)
            #print("------------------------------------------------------------------------------")
            for line in wycoordsys_file:
                # Tokenize line from file to convert to actual mesh data.
                firstToken, restToken = line.split(' ', 1)
                # CU - Coordinate system option [Up]
                if firstToken == 'CU':
                    coordoption_up_str = restToken.split('\n')[0]
                    #print("coordoption_up_str : " + str(coordoption_up_str))
                    if coordoption_up_str == "Z":
                        #print("Z up")
                        ZU = True
                    elif coordoption_up_str == "-Z":
                        #print("-Z up")
                        M_ZU = True
                    elif coordoption_up_str == "Y":
                        #print("Y up")
                        YU = True
                    elif coordoption_up_str == "-Y":
                        #print("-Y up")
                        M_YU = True
                    elif coordoption_up_str == "X":
                        #print("X up")
                        XU = True
                    elif coordoption_up_str == "-X":
                        #print("-X up")
                        M_XU = True
                # CF - Coordinate system option [Forward]
                if firstToken == 'CF':
                    coordoption_forward_str = restToken.split('\n')[0]
                    #print("coordoption_forward_str : "  str(coordoption_forward_str))
            
                    if coordoption_forward_str == "Z":
                        #print("Z forward")
                        ZF = True
                    elif coordoption_forward_str == "-Z":
                        #print("-Z forward")
                        M_ZF = True
                    elif coordoption_forward_str == "Y":
                        #print("Y forward")
                        YF = True
                    elif coordoption_forward_str == "-Y":
                        #print("-Y forward")
                        M_YF = True
                    elif coordoption_forward_str == "X":
                        #print("X forward")
                        XF = True
                    elif coordoption_forward_str == "-X":
                        #print("-X forward")
                        M_XF = True

                # Don't need to reach the end of file when CU and CF is read.
                if coordoption_up_str != "" and coordoption_forward_str != "":
                    break
        # Create WYCoordsys object with data value loaded from mesh file.
        wycoordsys = WYCoordsys(XU,M_XU,YU,M_YU,ZU,M_ZU,XF,M_XF,YF,M_YF,ZF,M_ZF)
        # Return the initialized WYCoordsys object.
        return wycoordsys

    def import_material(self, material_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the bpy.data.material
        object using the data loaded in the WYMaterial object loaded by 
        calling sub function WYModelManager::import_wymaterial().

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the material file from given file path
        and load the data values onto newly created WYMaterial object and 
        load the WYMaterial intialized value onto new bpy.data.materal object
        and return the initialized bpy.data.materal object.

        Calling sub function: WYModelManager::import_wymaterial()

        :Post-condition: Blender material object is created using 
                         WYMaterial object imported from file.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param material_file_path: Absolute file path to import the WYMaterial 
                                   object from.
        :type  material_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wymaterial: WYMaterial object imported as bpy.data.materal 
                            object.
        :rtype  wymaterial: WYMaterial
        '''
        if os.path.isfile(material_file_path) == False:
            raise Exception("ERROR::WYModelManager::import_material::Material file not exists!!!")
            return
        # Get directory path of the material file.
        dir_path = os.getcwd()
        #os.path.dirname(os.path.realpath(material_file_path))

        # Load material file into WYMaterial object.
        wymaterial = self.import_wymaterial(material_file_path)

        # ----------------------------------------------------------------------
        # Material object init (lights)
        # ----------------------------------------------------------------------
        # Create material object.
        material = bpy.data.materials.new(wymaterial.mtl_material_name)
        wymaterial.main_material_obj = material

        # Initialize the material object with the data loaded from custom 
        # materal file.
        material.mirror_color = wymaterial.mtl_mirror_color
        material.ambient = wymaterial.mtl_ambient
        material.diffuse_color = wymaterial.mtl_diffuse_color
        material.diffuse_intensity = wymaterial.mtl_diffuse_intensity
        material.specular_color = wymaterial.mtl_specular_color
        material.specular_intensity = wymaterial.mtl_specular_intensity
        material.specular_hardness = wymaterial.mtl_specular_hardness
        material.emit = wymaterial.mtl_emit
        material.raytrace_transparency.ior = \
            wymaterial.mtl_raytrace_transparency_ior
        material.alpha = wymaterial.mtl_alpha

        if wymaterial.mtl_texture_map_image_path != "NULL":
            # Load image from the absolute texture file path combined.
            image = bpy.data.images.load(
                dir_path + "\\" + wymaterial.mtl_texture_map_image_path)
            #image = bpy.data.images.load(wymaterial.mtl_texture_map_image_path)

            # Create Texture object with the loaded texture image.
            texture = bpy.data.textures.new("Texture", type = 'IMAGE')
            texture.image = image
            texture.use_alpha = True
            # ------------------------------------------------------------------
            # Assign texture objects to materials
            # ------------------------------------------------------------------
            mtex = material.texture_slots.add()
            # You'll need to have a list of Texture object already, creating 
            # Textures is explained below
            mtex.texture = texture
            # Set texture mapping mode to UV mapping
            mtex.texture_coords = 'UV'

        # Return WYMaterial object which holds the initialized 
        # bpy.data.material object.
        return wymaterial

    def import_wymaterial(self, wymaterial_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYMaterial object 
        by loading data from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the material file from given file path
        and load the data values onto newly created WYMaterial object and
        return it.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wymaterial_file_path: Absolute file path to import the WYMaterial 
                                object from.
        :type  wymaterial_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wymaterial: Initialized WYMaterial object from the imported file.
        :rtype  wymaterial: WYMaterial
        '''
        # Resulting WYMaterial to return.
        wymaterial = WYMaterial()

        with open(wymaterial_file_path) as wymaterial_file:
            print("------------------------------------------------------------------------------")
            print("Loading WYMaterial from :  " + wymaterial_file_path)
            print("------------------------------------------------------------------------------")
            for line in wymaterial_file:
                firstToken, restToken = line.split(' ', 1)
                # mtl_material_name
                if firstToken == 'mtl_material_name':
                    wymaterial.mtl_material_name = restToken.split('\n')[0]
                    print("mtl_material_name : " + 
                          str(wymaterial.mtl_material_name))  
                # mtl_ambient_color
                elif firstToken == 'mtl_mirror_color':
                    wymaterial.mtl_mirror_color = map(float, restToken.split())
                    wymaterial.mtl_mirror_color = \
                        list(wymaterial.mtl_mirror_color)
                    print("mtl_mirror_color : " + 
                          str(wymaterial.mtl_mirror_color))
                # mtl_ambient
                elif firstToken == 'mtl_ambient':
                    wymaterial.mtl_ambient = eval(restToken)
                    print("mtl_ambient : " + 
                          str(wymaterial.mtl_ambient)) 
                # mtl_diffuse_color
                elif firstToken == 'mtl_diffuse_color':
                    wymaterial.mtl_diffuse_color = map(float, restToken.split())
                    wymaterial.mtl_diffuse_color = \
                        list(wymaterial.mtl_diffuse_color)
                    print("mtl_diffuse_color : " + 
                          str(wymaterial.mtl_diffuse_color))
                # mtl_diffuse_intensity
                elif firstToken == 'mtl_diffuse_intensity':
                    wymaterial.mtl_diffuse_intensity = eval(restToken)
                    print("mtl_diffuse_intensity : " + 
                          str(wymaterial.mtl_diffuse_intensity)) 
                # mtl_specular_color
                elif firstToken == 'mtl_specular_color':
                    wymaterial.mtl_specular_color = \
                        map(float, restToken.split())
                    wymaterial.mtl_specular_color = \
                        list(wymaterial.mtl_specular_color)
                    print("mtl_specular_color : " + 
                          str(wymaterial.mtl_specular_color))
                # mtl_specular_intensity
                elif firstToken == 'mtl_specular_intensity':
                    wymaterial.mtl_specular_intensity = eval(restToken)
                    print("mtl_specular_intensity : " + 
                          str(wymaterial.mtl_specular_intensity)) 
                # mtl_specular_hardness
                elif firstToken == 'mtl_specular_hardness':
                    wymaterial.mtl_specular_hardness = eval(restToken)
                    print("mtl_specular_hardness : " + 
                          str(wymaterial.mtl_specular_hardness))  
                # mtl_emit
                elif firstToken == 'mtl_emit':
                    wymaterial.mtl_emit = eval(restToken)
                    print("mtl_emit : " + str(wymaterial.mtl_emit))
                # mtl_raytrace_transparency_ior
                elif firstToken == 'mtl_raytrace_transparency_ior':
                    wymaterial.mtl_raytrace_transparency_ior = eval(restToken) 
                    print("mtl_raytrace_transparency_ior : " + 
                          str(wymaterial.mtl_raytrace_transparency_ior))   
                # mtl_alpha
                elif firstToken == 'mtl_alpha':
                    wymaterial.mtl_alpha = eval(restToken)
                    print("mtl_alpha : " + str(wymaterial.mtl_alpha)) 
                # mtl_texture_map_image_path
                elif firstToken == 'mtl_texture_map_image_path':
                    wymaterial.mtl_texture_map_image_path = \
                        restToken.split('\n')[0]
                    print("mtl_texture_map_image_path : " + 
                          str(wymaterial.mtl_texture_map_image_path))
        # Return the initialized WYMaterial object imported from file.
        return wymaterial

    def export_armature_model(self, armature, model, wycoordsys, file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the Blender armature object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through export_wymodel sub function!!!

        :Pre-condition:
            WYModelManager::export_wyarmature() function is tested.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function converts Blender armature object and Blender armature 
        mapped on Blender model object into WYArmature object and pass it down 
        to sub function export_wyarmature function to export the Blender 
        armature object onto local files with WYArmature format.

        WYArmature object contains one WYModel object and array of 
        WYArmatureBone objects. If WYModel object is not None, then 
        assign the model export file path to the WYArmature object in 
        order to let the armature exported file know where the relative 
        model file is by setting the "mdllib" element value inside WYArmature 
        object with the final export armature file path.

        The file extension is appended manually through this function, so 
        only file name is enough to export the file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  armature: Blender armature object to export with.
        :type   armature: barmature (bpy.data.objects["Armature"])
        :param  model: Blender armature mapped on model object to export along 
                       with armature.
        :type   model: bpy.data.object
        :param file_path: Absolute file path to export the WYArmature object onto.
        :type  file_path: string

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return  wyarmature: WYArmature object created with bpy.data.object 
                             to export with.
        :rtype   wyarmature: WYArmature

        '''
        wymodel = None
        wyarmature = None

        if armature == None:
            raise Exception("ERROR::WYModelManager::export_armature_model::WYArmature object is None!!!")

        # If export file path starts with "." as first character, which means 
        # current working directory so prepend current working directory path.
        if file_path[0] == ".":
            file_path = os.getcwd() + "\\" + file_path

        # Appending extensions to convert the file path to seperate the files 
        # with same name. 
        #   Extension .wya - For WYArmature.
        #   Extension .wyo - For WYMesh.
        #   Extension .wym - For WYMaterial.
        wyarmature_file_path = file_path +".wya"

        # Export the model which armature is mapped onto by calling sub function
        # export_model() which returns the exported WYModel object.
        # And create WYArmature object to export.
        if model != None:
            # Export armature mapped on model object.
            wymodel = self.export_model(model, wycoordsys, file_path)

            # Create WYArmature object with Blender armature object and exported 
            # mapped on WYModel object.
            wyarmature = WYArmature(armature, wymodel, wycoordsys)

            # Set armature file's mdllib element manually when exporting model
            # file together.
            wyarmature.init_armature_model_relfile_path(file_path)
        else:
            wyarmature = WYArmature(armature, None, wycoordsys)

        # Initialize WYArmature data.
        wyarmature.init_armature_data()

        # Export WYArmature object.
        self.export_wyarmature(wyarmature, wyarmature_file_path)

        # Return exported WYArmature object.
        return wyarmature

    def export_wyarmature(self, wyarmature, wyarmature_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYArmature object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through this function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the final armature export string and write it to
        given export file path.

        Called by function WYModelManager::export_armature_model()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  wyarmature: WYArmature object to export the armature data with.
        :type   wyarmature: WYArmature
        :param wyarmature_file_path: Absolute file path to export the WYArmature
                                     object onto.
        :type  wyarmature_file_path: string

        '''
        if wyarmature == None:
            raise Exception("ERROR::WYModelManager::export_wyarmature::WYArmature object is None!!!")

        # Export the armature to local file.
        with open(wyarmature_file_path, 'w+') as wyarmature_export_file:
            print("------------------------------------------------------------------------------")
            print("Writing armature to :  " + wyarmature_file_path)
            print("------------------------------------------------------------------------------")
            wyarmature_export_file.write(str(wyarmature))

    def import_armature_model(self, file_path):    
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which imports the armature from 
        local files
       
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the armature from local file and 
        creates bpy.data.armature object and finds the corresponding model files
        to create bpy.data.object object and load the armature onto the Blender
        application screen along with the model.

        Calling sub function: WYModelManager::import_armature()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param file_path: Absolute file path to import the armature object from.
        :type  file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyarmature: WYArmature object which all the data values are 
                            imported from given file path.
        :rtype  wyarmature: WYArmature
        '''

        # Append file extension to import from.
        armature_file_path = ""
        if file_path.find(".wya") != -1:
           armature_file_path = file_path
        else:
           armature_file_path = file_path + ".wya"

        if os.path.isfile(armature_file_path) == False:
            raise Exception("ERROR::WYModelManager::export_wyarmature::Armature file not exists!!!")
            return

        # Load armature from file.
        wyarmature = self.import_armature(armature_file_path)

        return wyarmature

    def import_armature(self, armature_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the bpy.data.aramture
        object using the data loaded in the WYArmature object loaded by 
        calling sub function WYModelManager::import_wyarmature().

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the armature file from given file path
        and load the data values onto newly created WYArmature object and 
        load the WYArmature intialized value onto new bpy.data.armature object
        and return the WYArmature object holding the newly initialized 
        bpy.data.mesh object.

        Calling sub function: WYModelManager::import_wyarmature()

        :Post-condition: Blender armature object is created using the 
                         WYArmature object imported from file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param armature_file_path: Absolute file path to import the 
                                   WYArmature object from.
        :type  armature_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyarmature: WYArmature object imported from file.
        :rtype  wyarmature: WYArmature
        '''

        # Load local file onto WYArmature object.
        # This function also detects the "mdllib" element inside armature file
        # to find the mapped on model object to be imported together.
        wyarmature = self.import_wyarmature(armature_file_path)

        # Create armature data.	
        armature = bpy.data.armatures.new(wyarmature.armature_name)
        # Create armature object.
        armature_obj = bpy.data.objects.new(wyarmature.armature_name, armature)
        wyarmature.main_armature_obj = armature_obj

        # If "mdllib" element is imported to WYArmature object, means mapped on
        # model exist.
        if wyarmature.armature_model_relfile_path != "":
            # Importing model using the "mdllib" element value retrieved from 
            # armature file.
            wymodel = \
                self.import_model(wyarmature.armature_model_relfile_path)

            if wymodel != None:
                wymodel.main_wymesh.main_mesh_obj.parent = \
                    wyarmature.main_armature_obj
                wyarmature.main_wymodel_obj = wymodel


        # Select armature object.
        bpy.context.scene.objects.active = armature_obj
        #bpy.ops.object.mode_set(mode='OBJECT')

        # Link object to scene.
        bpy.context.scene.objects.link(armature_obj)

        # Get edit bones to create armature bones.
        armature_obj_edit_bones = armature_obj.data.edit_bones

        # Set armature object to active.
        bpy.context.scene.objects.active = armature_obj

        # Set to EDIT mode.
        bpy.ops.object.mode_set(mode='EDIT')  

        # Loop through data structure to create armature bones for each
        # WYArmatureBone initialized in WYArmature object.
        for i in range(0, wyarmature.num_armature_bones):
            # Current WYArmatureBone object.
            wyarmaturebone = wyarmature.armature_bones_arr[i]

            # Get WYArmatureBone object name.
            armature_bone_name = wyarmaturebone.armature_bone_name

            # Create new armature bone.
            armature_bone_obj = armature_obj_edit_bones.new(armature_bone_name)
            wyarmaturebone.main_armature_bone_obj = armature_bone_obj

            # Set bone head coordinate.
            armature_bone_obj.head = wyarmaturebone.armature_bone_head
            # Set bone tail coordinate.
            armature_bone_obj.tail = wyarmaturebone.armature_bone_tail

            # Set parent bone.
            wyarmaturebone_parent_name = \
                wyarmaturebone.armature_bone_parent_name
            if wyarmaturebone_parent_name != "" and \
               armature_obj_edit_bones[wyarmaturebone_parent_name] != None:
                armature_bone_obj.parent = \
                    armature_obj_edit_bones[wyarmaturebone_parent_name]

            # Assign vertex groups if armature has a mapped on mesh object 
            # initialized inside WYArmature object.
            if wyarmature.main_wymodel_obj != None and wyarmaturebone != None:
                # Get mapped on mesh object.
                armature_mesh_name = \
                    wyarmature.main_wymodel_obj.main_wymesh.mesh_obj_name
                armature_mesh = bpy.data.objects[armature_mesh_name]

                # Create vertex group for each armature bone objects.
                vertex_groups = \
                    armature_mesh.vertex_groups.new(armature_bone_name)
                
                # Get vertex group for current armature bone to add 
                # vertex group data.
                vertex_group = armature_mesh.vertex_groups[armature_bone_name]

                armature_obj_vertex_group = \
                    wyarmaturebone.armature_vertex_group_array
                for i in range(0, len(armature_obj_vertex_group)):
                    # Get vertex group data from WYArmatureBone object.
                    vertex_group_vertex_index = armature_obj_vertex_group[i][0]
                    vertex_group_vertex_coordinate = \
                        armature_obj_vertex_group[i][1]
                    vertex_group_vertex_weight = armature_obj_vertex_group[i][2]

                    # Add to imported armature bone's vertex group.
                    vertex_group.add(
                        [vertex_group_vertex_index], 
                        vertex_group_vertex_weight, 
                        "REPLACE")

        #wyarmature.init_armature_data()

        # Apply armature bone automatic weight to the imported mesh object.
        bpy.ops.object.mode_set(mode='OBJECT')  
        for ob in bpy.context.scene.objects:
            ob.select = True
        bpy.ops.object.parent_set(type="ARMATURE") 

        return wyarmature

    def import_wyarmature(self, wyarmature_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYArmature object 
        by loading data from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the armature file from given file path
        and load the data values onto newly created WYArmature object and
        return it.

        Called by function: WYModelManager::import_wyarmature()
        Calling sub function: WYModelManager::import_wyarmaturebone()

        :Post-condition: WYArmature object is created imported from file.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wyarmature_file_path: Absolute file path to import the 
                                     WYArmature object from.
        :type  wyarmature_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyarmature: Initialized WYArmature object from the imported file.
        :rtype  wyarmature: WYArmature
        '''
        # WYArmature object to return.
        wyarmature = WYArmature()

        # Load export coordinate system onto WYCoordsys object first and then
        # start loading the armature data so the vertex value is converted back
        # to original values.
        wyarmature.wycoordsys = \
            self.import_wycoordsys(wyarmature_file_path)

        with open(wyarmature_file_path) as wyarmature_file:
            print("------------------------------------------------------------------------------")
            print("Loading from :  " + wyarmature_file_path)
            print("------------------------------------------------------------------------------")
            for line in wyarmature_file:
                firstToken, restToken = line.split(' ', 1)

                # an - Armature name.
                if firstToken == 'an':
                    wyarmature.armature_name = restToken.split('\n')[0]
                    print("an : " + str(wyarmature.armature_name))

                # mdllib - Relative mapped on model exported file path.
                if firstToken == 'mdllib':
                    wyarmature.armature_model_relfile_path = \
                        restToken.split('\n')[0]
                
                    print("mdllib : " + str(wyarmature.armature_model_relfile_path))

                    #myArmatureMesh = bpy.data.objects[childMeshName]

                # bc - Number of armature bones.
                if firstToken == 'bc':
                    wyarmature.num_armature_bones = int(restToken.split('\n')[0])
                    print("bc : " + str(wyarmature.num_armature_bones))
                    break

            if wyarmature.num_armature_bones > 0:
                # Load WYArmatureBone objects into the WYArmature data structure.
                # bn,bt,bh,vg - Armature bones.
                self.import_wyarmaturebone(wyarmature, wyarmature_file)
        
        # Return WYArmature object imported from file.
        return wyarmature

    def import_wyarmaturebone(self, wyarmature, wyarmature_file_obj):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYArmatureBone 
        objects to be imported to WYArmature object imported from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the armature file from given file path
        and load the data values onto newly created WYArmatureBone object and
        append the WYArmatureBone onto the data structure inside given 
        WYArmature object.

        Called by function: WYModelManager::import_wyarmature()

        :Post-condition: WYArmatureBone objects imported from file are appended
                         to WYArmature object's member variable 
                         "armature_bones_arr" data structure with data imported
                         from same armature file.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wyarmature: WYArmature object created when importing from file 
                           to import WYArmatureBone objects with.
        :type  wyarmature: WYArmature
        :param wyarmature_file_obj: Opened armature file object.
        :type  wyarmature_file_obj: File

        '''
        # WYArmatureBone object to set values onto.
        wyarmaturebone = None
        for line in wyarmature_file_obj:
            firstToken, restToken = line.split(' ', 1)

            # bn - Armature bone name.
            if firstToken == 'bn':
                wyarmaturebone = WYArmatureBone()
                wyarmaturebone.armature_bone_name = restToken.split('\n')[0]
                print("bn : " + str(wyarmaturebone.armature_bone_name))

                # Append each initialized WYArmatureBone object to the data 
                # structure inside WYArmature object.
                wyarmature.armature_bones_arr.append(wyarmaturebone)

            # pbn - Parent bone name in current armature bone.
            if firstToken == 'pbn' and wyarmaturebone != None:
                wyarmaturebone.armature_bone_parent_name = \
                    restToken.split('\n')[0]
                print("pbn : " + str(wyarmaturebone.armature_bone_parent_name))

            # bt - Current armature bone tail coordinate XYZ value.
            if firstToken == 'bt' and wyarmaturebone != None:
                armatureBoneTail = map(float, restToken.split())
                armatureBoneTail = list(armatureBoneTail)
                vertexCoordsX = armatureBoneTail[0]
                vertexCoordsY = armatureBoneTail[1]
                vertexCoordsZ = armatureBoneTail[2]

                # Convert the coordinate system.
                resultVertex = wyarmature.wycoordsys.import_coordconversion(
                    vertexCoordsX,
                    vertexCoordsY,
                    vertexCoordsZ)

                wyarmaturebone.armature_bone_tail = resultVertex
                print("bt : " + str(wyarmaturebone.armature_bone_tail))

            # bh - Current armature bone tail coordinate XYZ value.  
            if firstToken == 'bh' and wyarmaturebone != None:
                armatureBoneHead = map(float, restToken.split())
                armatureBoneHead = list(armatureBoneHead)
                    
                vertexCoordsX = armatureBoneHead[0]
                vertexCoordsY = armatureBoneHead[1]
                vertexCoordsZ = armatureBoneHead[2]
                    
                # Convert the coordinate system.
                resultVertex = wyarmature.wycoordsys.import_coordconversion(
                    vertexCoordsX,
                    vertexCoordsY,
                    vertexCoordsZ)

                wyarmaturebone.armature_bone_head = resultVertex
                print("bh : " + str(wyarmaturebone.armature_bone_head))

            # vg {v,vi,vw} - Per bone vertex group.  
            if firstToken == "vg" and wyarmaturebone != None: 
                vertex_group_vertex_index_arr = []
                vertex_group_vertex_coordinate_arr = []
                vertex_group_vertex_weight_arr = []
                vertex_group_counter = 0
                while line[0] != '}':
                    # Read next line until first character is '}'.
                    line = wyarmature_file_obj.readline()
                    if line[0] == '}':
                        break
                    firstToken, restToken = line.split(' ', 1)

                    # vi - Vertex group vertex index.
                    if firstToken == 'vi':
                        vertexIndex = eval(restToken)
                        vertex_group_vertex_index_arr.append(vertexIndex)
                        print("vi " + str(vertexIndex))

                        vertex_group_counter += 1

                    # v - Vertex group vertex coordinate.
                    if firstToken == 'v':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsX = vertCoord[0]
                        vertexCoordsY = vertCoord[1]
                        vertexCoordsZ = vertCoord[2]
                        # Convert the coordinate system.
                        resultVertex = wyarmature.wycoordsys.\
                            import_coordconversion(
                                vertexCoordsX,
                                vertexCoordsY,
                                vertexCoordsZ)

                        vertexCoordinate = resultVertex
                        vertex_group_vertex_coordinate_arr.append(
                            [vertexCoordinate[0],
                             vertexCoordinate[1],
                             vertexCoordinate[2]])

                        print("v " + str(vertexCoordinate))

                    # vw - Vertex group vertex weight.
                    if firstToken == 'vw':
                        vertexWeight = eval(restToken)
                        vertex_group_vertex_weight_arr.append(vertexWeight)
                        print("vw " + str(vertexWeight))

                # Assign the retrieved vertex group data value to the 
                # WYArmatureBone object's member variable when '}' is detected
                # out of the loop.
                for i in range(0, vertex_group_counter):
                    wyarmaturebone.armature_vertex_group_array.append([
                         vertex_group_vertex_index_arr[i],
                         vertex_group_vertex_coordinate_arr[i],
                         vertex_group_vertex_weight_arr[i]
                         ])
 
    def export_animation_model(self, animation, armature, model, wycoordsys, start_index, end_index, file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the Blender pose object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through export_wymodel sub function!!!

        :Pre-condition:
            WYModelManager::export_wyanimation() function is tested.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function converts Blender pose object and Blender armature 
        object into WYAnimation object and pass it down to sub function 
        export_wyanimation function to export the Blender 
        pose object onto local files with WYAnimation format.

        WYAnimation object contains one mapped on WYArmature object and array of 
        WYAnimationBone objects. If WYArmature object is not None, then 
        assign the armature export file path to the WYAnimation object in 
        order to let the animation exported file know where the relative 
        armature file is by setting the "mamlib" element value inside 
        WYAnimation object with the final export animation file path.

        The file extension is appended manually through this function, so 
        only file name is enough to export the file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        animation
        :param  animation: Blender pose object to export with.
        :type   animation: bpose (bpy.data.objects["Armature"].pose)
        :param  armature: Blender armature object to export with.
        :type   armature: barmature (bpy.data.objects["Armature"])
        :param  model: Blender armature mapped on model object to export along 
                       with armature.
        :type   model: bpy.data.object
        :param start_index: Start index of the animation keyframe for export.
        :type  start_index: int
        :param end_index: End index of the animation keyframe for export.
        :type  end_index: int
        :param file_path: Absolute file path to export the WYArmature object onto.
        :type  file_path: string

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return  wyanimation: WYAnimation object created to export with.
        :rtype   wyanimation: WYAnimation

        '''
        wymodel = None
        wyarmature = None
        wyanimation = None

        if animation == None:
            raise Exception("ERROR::WYModelManager::export_animation_model::WYAnimation object is None!!!")

        if armature == None:
            raise Exception("ERROR::WYModelManager::export_animation_model::WYAnimation object is None!!!")

        # If export file path starts with "." as first character, which means 
        # current working directory so prepend current working directory path.
        if file_path[0] == ".":
            file_path = os.getcwd() + "\\" + file_path

        # Appending extensions to convert the file path to seperate the files 
        # with same name. 
        #   Extension .wyan - For WYAnimation.
        #   Extension .wya - For WYArmature.
        #   Extension .wyo - For WYMesh.
        #   Extension .wym - For WYMaterial.
        wyanimation_file_path = file_path +".wyan"

        # Export the armature which animation is mapped onto by calling sub 
        # function export_armature_model() which returns the exported 
        # WYArmature object. And create WYAnimation object to export.
        if armature != None:
            # Export armature mapped on model object.
            wyarmature = self.export_armature_model(
                armature, model, wycoordsys, file_path)

            # Create WYAnimation object with Blender pose object and exported 
            # mapped on WYArmature object.
            wyanimation = WYAnimation(animation, wyarmature, wycoordsys)

            # Set animation file's mamlib element manually when exporting 
            # armaturefile together.
            wyanimation.init_animation_armature_relfile_path(file_path)
        else:
            wyanimation = WYAnimation(animation, None, wycoordsys)

        # Initialize WYAnimation data.
        wyanimation.init_animation_data(start_index, end_index)

        # Export WYAnimation object.
        self.export_wyanimation(wyanimation, wyanimation_file_path)

        # Return exported WYAnimation object.
        return wyanimation

    def export_wyanimation(self, wyanimation, wyanimation_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which exports the WYAnimation object 
        into local files.

        Caution: Must proivde the file path without extension, because the 
                 extension is added through this function!!!
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function retrieves the final animation export string and write it 
        to given export file path.

        Called by function WYModelManager::export_animation_model()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  wyanimation: WYAnimation object to export the animation data 
                             with.
        :type   wyanimation: WYAnimation
        :param wyanimation_file_path: 
                             Absolute file path to export the WYAnimation object
                             onto.
        :type  wyanimation_file_path: string

        '''
        if wyanimation == None:
            raise Exception("ERROR::WYModelManager::export_wyanimation::WYAnimation object is None!!!")

        # Export the armature to local file.
        with open(wyanimation_file_path, 'w+') as wyanimation_export_file:
            print("------------------------------------------------------------------------------")
            print("Writing armature to :  " + wyanimation_file_path)
            print("------------------------------------------------------------------------------")
            wyanimation_export_file.write(str(wyanimation))
                    
    def import_animation_model(self, file_path):    
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which imports the animation from 
        local files
        
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the animation from local file and 
        finds the corresponding armature files to create bpy.data.armature 
        object and load the animation onto the loaded armature pose bones.

        Calling sub function: WYModelManager::import_animation()
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param file_path: Absolute file path to import the animation object from.
        :type  file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyanimation: WYAnimation object which all the data values are 
                             imported from given file path.
        :rtype  wyanimation: WYAnimation
        '''

        # Append file extension to import from.
        animation_file_path = ""
        if file_path.find(".wyan") != -1:
           animation_file_path = file_path
        else:
           animation_file_path = file_path + ".wyan"

        if os.path.isfile(animation_file_path) == False:
            raise Exception("ERROR::WYModelManager::export_wyarmature::Animation file not exists!!!")
            return

        # Load armature from file.
        wyanimation = self.import_animation(animation_file_path)

        return wyanimation

    def import_animation(self, animation_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the bpy.data.pose
        object using the data loaded in the WYAnimation object loaded by 
        calling sub function WYModelManager::import_wyanimation().

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the animation file from given file path
        and load the data values onto newly created WYAnimation object and 
        load the WYAnimation intialized value onto new bpy.data.pose object
        and return the WYAnimation object holding the newly initialized 
        bpy.data.pose object.

        Calling sub function: WYModelManager::import_wyanimation()

        :Post-condition: Blender pose object is created using the 
                         WYAnimation object imported from file.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param animation_file_path: Absolute file path to import the 
                                    WYAnimation object from.
        :type  animation_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyanimation: WYAnimation object imported from file.
        :rtype  wyanimation: WYAnimation
        '''

        # Load local file onto WYAnimation object.
        # This function also detects the "mamlib" element inside animation file
        # to find the mapped on armature object to be imported together.
        wyanimation = self.import_wyanimation(animation_file_path)

        # First load the armature to mapped the imported animation onto.
        # If "mamlib" element is imported to WYAnimation object, means mapped on
        # armature  exist.
        if wyanimation.animation_armature_relfile_path != "":
            # Importing armature using the "mamlib" element value retrieved from 
            # animation file.
            wyarmature = \
                self.import_armature_model(
                    wyanimation.animation_armature_relfile_path)
            wyarmature.init_armature_data()

            # Set WYAnimation data values.
            wyanimation.main_wyarmature_obj = wyarmature
            wyanimation.main_animation_obj = wyarmature.main_armature_obj.pose
            armature = wyarmature.main_armature_obj

            # Loop through animation bones inside WYAnimation imported from 
            # file.
            for i in range(0, wyanimation.num_animation_bones):
                wyanimationbone = wyanimation.animation_bones_arr[i]

                # Get current animation bone to assign imported data 
                # values with.
                currentAnimationBoneName = wyanimation.animation_bones_arr[i]\
                    .animation_bone_name
                currentAnimationBone = wyanimation.main_animation_obj.\
                    bones[currentAnimationBoneName]

                # Assign keyframe data values for each animation bones.
                for j in range(0, len(
                    wyanimationbone.animation_bone_keyframe_arr)):
                    # Get keyframe data object.
                    currentAnimationBoneKeyframe = \
                        wyanimationbone.animation_bone_keyframe_arr[j]

                    currentAnimationBoneKeyframeIndex = \
                        currentAnimationBoneKeyframe.\
                              animation_bone_keyframe_index

                    # Set animation bone loc,rotq,sca.
                    currentAnimationBone.location = \
                        currentAnimationBoneKeyframe.animation_bone_location
                    currentAnimationBone.rotation_quaternion = \
                        currentAnimationBoneKeyframe.\
                        animation_bone_rotation_quaternion
                    currentAnimationBone.scale = \
                        currentAnimationBoneKeyframe.animation_bone_scale

                    # Insert animation keyframe on imported index.
                    currentAnimationBone.keyframe_insert(
                        data_path='location',
                        frame=currentAnimationBoneKeyframeIndex)
                    currentAnimationBone.keyframe_insert(
                        data_path='rotation_quaternion',
                        frame=currentAnimationBoneKeyframeIndex)       
                    currentAnimationBone.keyframe_insert(
                        data_path='scale',
                        frame=currentAnimationBoneKeyframeIndex)

        # Else means there is no armature to mapped the animation onto which 
        # means error.
        else:
            raise Exception("ERROR::WYModelManager::import_animation::Armature not exists!!!")
            return


        return wyanimation

    def import_wyanimation(self, wyanimation_file_path):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYAnimation object 
        by loading data from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the animation file from given file path
        and load the data values onto newly created WYAnimation object and
        return it.

        Called by function: WYModelManager::import_wyanimation()
        Calling sub function: WYModelManager::import_wyanimationbone()

        :Post-condition: WYAnimation object is created imported from file.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wyanimation_file_path: Absolute file path to import the 
                                      WYAnimation object from.
        :type  wyanimation_file_path: string

        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return wyarmature: Initialized WYAnimation object imported from file.
        :rtype  wyarmature: WYAnimation
        '''
        # WYAnimation object to return.
        wyanimation = WYAnimation()

        # Load export coordinate system onto WYCoordsys object first and then
        # start loading the armature data so the vertex value is converted back
        # to original values.
        wyanimation.wycoordsys = \
            self.import_wycoordsys(wyanimation_file_path)

        with open(wyanimation_file_path) as wyanimation_file:
            print("------------------------------------------------------------------------------")
            print("Loading from :  " + wyanimation_file_path)
            print("------------------------------------------------------------------------------")
            for line in wyanimation_file:
                firstToken, restToken = line.split(' ', 1)

                # ann - Animation name.
                if firstToken == 'ann':
                    wyanimation.animation_name = restToken.split('\n')[0]
                    print("an : " + str(wyanimation.animation_name))

                # mamlib - Relative custom armature exported file path.
                if firstToken == 'mamlib':
                    wyanimation.animation_armature_relfile_path = \
                        restToken.split('\n')[0]
                
                    print("mamlib : " + str(wyanimation.animation_armature_relfile_path))

                    #myArmatureMesh = bpy.data.objects[childMeshName]

                # abc - Number of animation bones.
                if firstToken == 'abc':
                    wyanimation.num_animation_bones = int(restToken.split('\n')[0])
                    print("abc : " + str(wyanimation.num_animation_bones))
                    break

            if wyanimation.num_animation_bones > 0:
                # Load WYAnimationBone objects into the WYAnimation data 
                # structure.
                # loc,rotq,sca - Animation bones.
                self.import_wyanimationbone(wyanimation, wyanimation_file)
        
        # Return WYAnimation object imported from file.
        return wyanimation

    def import_wyanimationbone(self, wyanimation, wyanimation_file_obj):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYModelManager member function which initializes the WYAnimationBone 
        objects to be imported to WYAnimation object imported from local files.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function reads in the armature file from given file path
        and load the data values onto newly created WYAnimationBone object and
        append the WYAnimationBone onto the data structure inside given 
        WYAnimation object.

        Called by function: WYModelManager::import_wyanimation()

        :Post-condition: WYAnimationBone objects imported from file are appended
                         to WYAnimation object's member variable 
                         "animation_bones_arr" data structure with data imported
                         from same animation file.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param wyanimation: WYAnimation object created when importing from file 
                            to import WYAnimationBone objects with.
        :type  wyanimation: WYAnimation
        :param wyanimation_file_obj: Opened animation file object.
        :type  wyanimation_file_obj: File


        '''
        # WYAnimationBone object to set values onto.
        wyanimationbone = None

        # Import WYAnimationBone objects from file and append them into 
        # data structure inside WYAnimation object passed in as argument.
        for line in wyanimation_file_obj:
            firstToken, restToken = line.split(' ', 1)

            # abn - Animation bone name.
            if firstToken == 'abn':
                wyanimationbone = WYAnimationBone()
                wyanimationbone.animation_bone_name = restToken.split('\n')[0]
                print("abn : " + str(wyanimationbone.animation_bone_name))

                # Append each initialized WYAnimationBone object to the data 
                # structure inside Animation object.
                wyanimation.animation_bones_arr.append(wyanimationbone)

            # apbn - Parent bone name in current animation bone.
            if firstToken == 'apbn' and wyanimationbone != None:
                wyanimationbone.animation_bone_parent_name = \
                    restToken.split('\n')[0]
                print("pbn : " + str(wyanimationbone.animation_bone_parent_name))

            # kf index {bh,bt,loc,rotq,sca} - Per animation bone keyframe data.  
            if firstToken == "kf" and wyanimationbone != None: 
                keyframeIndex = float(restToken.split(' ')[0])

                wyanimationbonekeyframe = WYAnimationBoneKeyframe()
                wyanimationbonekeyframe.animation_bone_keyframe_index = \
                    keyframeIndex

                locationVector = None
                rotationQuaternion = None
                scaleVector = None
                while line[0] != '}':
                    # Read next line until first character is '}'.
                    line = wyanimation_file_obj.readline()
                    if line[0] == '}':
                        break
                    firstToken, restToken = line.split(' ', 1)

                    # abh - Animation keyframe head coordinate.
                    if firstToken == 'abh':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsX = vertCoord[0]
                        vertexCoordsY = vertCoord[1]
                        vertexCoordsZ = vertCoord[2]
                        headCoord = (
                             vertexCoordsX,
                             vertexCoordsY,
                             vertexCoordsZ)

                        print("abh " + str(headCoord))

                    # abt - Animation keyframe head coordinate.
                    if firstToken == 'abt':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsX = vertCoord[0]
                        vertexCoordsY = vertCoord[1]
                        vertexCoordsZ = vertCoord[2]
                        tailCoord = (
                             vertexCoordsX,
                             vertexCoordsY,
                             vertexCoordsZ)

                        print("abt " + str(tailCoord))

                    # loc - Animation keyframe location vector.
                    if firstToken == 'loc':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsX = vertCoord[0]
                        vertexCoordsY = vertCoord[1]
                        vertexCoordsZ = vertCoord[2]
                        # Convert the coordinate system.
                        # Blender export --> Blender import location vector 
                        # conversion formula:
                        #   XYZ --> ZY-X
                        '''
                        resultVertex = wyanimation.wycoordsys.\
                            import_coordconversion(
                                vertexCoordsX,
                                vertexCoordsY,
                                vertexCoordsZ)

                        vertexCoordinate = resultVertex
                        locationVector = Vector((vertexCoordinate[0],
                             vertexCoordinate[1],
                             vertexCoordinate[2]))
                        '''
                        locationVector = (
                             vertexCoordsX,
                             vertexCoordsY,
                             vertexCoordsZ)

                        print("loc " + str(locationVector))

                    # rotq - Animation keyframe rotation quaternion.
                    if firstToken == 'rotq':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsW = vertCoord[0]
                        vertexCoordsX = vertCoord[1]
                        vertexCoordsY = vertCoord[2]
                        vertexCoordsZ = vertCoord[3]
                        # Convert the coordinate system.
                        # Blender export --> Blender import rotation quaternion
                        # conversion formula:
                        #   WXYZ --> WZY-X
                        '''
                        resultVertex = wyanimation.wycoordsys.\
                            import_coordconversion(
                                vertexCoordsX,
                                vertexCoordsY,
                                vertexCoordsZ)

                        vertexCoordinate = resultVertex
                        rotationQuaternion = Quaternion((vertexCoordinate[0],
                             vertexCoordinate[1],
                             vertexCoordinate[2],
                             vertexCoordinate[3]))
                        '''

                        rotationQuaternion = (
                             vertexCoordsW,
                             vertexCoordsX,
                             vertexCoordsY,
                             vertexCoordsZ)
                        print("rotq " + str(rotationQuaternion))

                    # sca - Animation keyframe scale vector.
                    if firstToken == 'sca':
                        vertCoord = map(float, restToken.split())
                        vertCoord = list(vertCoord)
                        vertexCoordsX = vertCoord[0]
                        vertexCoordsY = vertCoord[1]
                        vertexCoordsZ = vertCoord[2]
                        # Convert the coordinate system.
                        # Blender export --> Blender import scale vector 
                        # conversion formula:
                        #   XYZ --> ZY-X
                        '''
                        resultVertex = wyanimation.wycoordsys.\
                            import_coordconversion(
                                vertexCoordsX,
                                vertexCoordsY,
                                vertexCoordsZ)
                        vertexCoordinate = resultVertex
                        scaleVector = Vector((vertexCoordinate[0],
                             vertexCoordinate[1],
                             vertexCoordinate[2]))
                        '''
                        scaleVector = (
                             vertexCoordsX,
                             vertexCoordsY,
                             vertexCoordsZ)

                        print("sca " + str(scaleVector))

                # Out of the loop when '}' is reached, assign the imported data 
                # value into WYAnimationBoneKeyframe object and append it to the
                # WYAnimationBone's data structure.
                wyanimationbonekeyframe.animation_bone_location = locationVector
                wyanimationbonekeyframe.animation_bone_rotation_quaternion = \
                    rotationQuaternion
                wyanimationbonekeyframe.animation_bone_scale = scaleVector

                # Set head tail coordinates.
                wyanimationbonekeyframe.animation_bone_head = headCoord
                wyanimationbonekeyframe.animation_bone_tail = tailCoord

                # Append the imported keyframe to currently loading 
                # WYAnimationBone object.
                wyanimationbone.animation_bone_keyframe_arr.append(
                    wyanimationbonekeyframe)

