================================================================================
                                    READ ME
================================================================================
Directory name: 
    - MESH_MAT_EXPORTER/src/tools/.

================================================================================
Directory description:
================================================================================
src/			Collection of all the source codes of current project
			+ sub projects:
			OAuthTestGenerator and OAuthTimeReportDashboard.
	========================================================================
	main/		Main project source codes
		WYCoordsys/		WYCoordsys 	class folder.
		WYMain/			WYMain 	 	class folder.
		WYMaterial/		WYMaterial 	class folder.
		WYMesh/			WYMesh 		class folder.
		WYModel/		WYModel 	class folder.
		WYModelManager/		WYModelManger 	class folder.
		WYUtil/			WYUtil 		class folder.
	========================================================================
	test/		Main project test cases folder which contains all the 
			project test case related folders and files, the test 
			cases are generated through the OAuthTestGenerator
			sub project inside "tools" folder.
	========================================================================
	tools/		Tools to support main project development which contains 
			2 sub project tools.

		================================================================
		OAuthTestGenerator/	
			Python test case generator tool sub project directory 
			which is to generate the Python unit test cases using 
			the data retrieved from Google Spreadsheet which can be
			accessed by OAuth and Google Developer Console API.

		================================================================
		OAuthTimeReportDashboard/ 
			HTML time report dashboard generator tool sub project
			directory which is to generate the HTML page which shows
			the data of the time report provided in the Google 
			Spreadsheet and generates a dashboard like chart to 
			visualize the data in trivial way drawn with a 
			external Javascript library called amChart.js.
		================================================================
		PydocIterator/
			Tool for generating the Pydoc HTML pages for all the 
			".py" extension files iterated inside provided folder
			path. Each Pydoc HTML pages is generated in the same 
			folder where ".py" extension file exists.
		================================================================
		FuncDefRetriever/
			Tool for retreiving function definition lines for all
			the ".py" extension files iterated inside provided folder
			path. 
			This is for developers to view the function prototypes 
			more easily.
	========================================================================




