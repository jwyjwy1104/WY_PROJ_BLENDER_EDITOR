################################################################################
# Project Name          	: WY_PROJ_BLENDER_EDITOR
# File Name             	: WYCoordsys.py
# Project Headquarter   	: https://docs.google.com/document/d/1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit#
# Test Plan Headquarter 	: https://docs.google.com/document/d/1wlFujpygsVKtqiz596ZdD1sCeUPkpIgr1lNlE_GN-_w/edit#
# WYCoordsys test plan  	: https://docs.google.com/document/d/1g8EEbVXKorZn7_jSUZ0STpsBOUX2wqhSBvRLXb2k420/edit#
# Lead Programmer       	: Samil Chai
# Junior Programmer     	: Nick Jang
# Time                  	: 
# Description           	: 
################################################################################

import sys
class WYCoordsys:
    '''
    This class represents the coordinate system option values chosen for 
    exporting the data through my custom exporter.

    WYCoordsys contains the value to define the coordinate system which current 
    exported or imported values are going to be converted with.

    User must choose 1 of each 6 options in these 2 option values:
        1. Up vector axis       : X, -X, Y, -Y, Z, -Z
        2. Forward vector axis  : X, -X, Y, -Y, Z, -Z
    Or else the option will be chosen automatically with default Blender 
    coordinate system value which is [Z up Y forward].

    So the user choose one of these 2 options before exporting the model:
        :Example: If user chose X up Y forward before exporting, then the 
                 coordinate values for each model will be converted from 
                 Blender coordinate system [Z up Y forward] to
                 [X up Y forward].

    This conversion mechanism is organized in the separate document called:
        WY_PROJ_3D_ENGINE_BLENDER_EXPORT_COORDINATE_SYSTEM_MECHANISM.xlsx

    .. seealso:: 
        WY_PROJ_3D_ENGINE_BLENDER_EXPORT_COORDINATE_SYSTEM_MECHANISM.xlsx
    .. seealso:: 
        WY_PROJ_3D_ENGINE_IMPORT_FROM_BLENDER_COORDINATE_SYSTEM_MECHANISM.xlsx

    ----------------------------------------------------------------------------
    Member variables:
    ----------------------------------------------------------------------------
    :Memeber variable XU    : Up vector towards positive X axis boolean value.
    :Memeber variable M_XU  : Up vector towards negative X axis boolean value.
    :Memeber variable YU    : Up vector towards positive Y axis boolean value.
    :Memeber variable M_YU  : Up vector towards negative Y axis boolean value.
    :Memeber variable ZU    : Up vector towards positive Z axis boolean value.
    :Memeber variable M_ZU  : Up vector towards negative Z axis boolean value.
    :Memeber variable XF    : Forward vector towards positive X axis boolean value.
    :Memeber variable M_XF  : Forward vector towards negative X axis boolean value.
    :Memeber variable YF    : Forward vector towards positive Y axis boolean value.
    :Memeber variable M_YF  : Forward vector towards negative Y axis boolean value.
    :Memeber variable ZF    : Forward vector towards positive Z axis boolean value.
    :Memeber variable M_ZF  : Forward vector towards negative Z axis boolean value.
    :Member variable coordoption_up_str: Up vector final export string value.
    :Member variable coordoption_forward_str: Forward vector final export string value.

    ----------------------------------------------------------------------------
    Member functions:
    ----------------------------------------------------------------------------
    # def __init__(self, 
        Test: https://docs.google.com/spreadsheets/d/1FAibaRk-by5_1UbVad9Nhmu_QPOuBZDEeZidoQqIxFA/edit#gid=0
	# def __eq__(self, other):
        Test: https://docs.google.com/spreadsheets/d/1aSzu5Ml-zuXqhTufurVJM7SBrwmabj_ZYSPQ6NUr_QA/edit#gid=0
	# def __str__(self):
        Test: https://docs.google.com/spreadsheets/d/1qaKGTW1wKdC7k4qASe1gIVy-WVNbQVIGq50hbtE3SJk/edit#gid=0
	# def import_coordconversion(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1AoXBweyJkTicTz_7svmPN9wLKOJa3URKYVqZtOkceVU/edit#gid=0
	# def export_coordconversion(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1FfrKnad-OWsK8obkfRhNPImxOo-08Z-rrlgoxP84eO0/edit#gid=0
	# def export_xu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/11MttC-nDvd0uNrvicLUIOdtbN-LJGkG4KrXNxadC3MY/edit#gid=0
	# def export_xu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/13KjPn-WSAX8jOsSLhl95wpsAq6CVpAs58k0ykO6UoCk/edit#gid=0
	# def export_xu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1vxZ36lBdIXG_Nd6zC3sd4rwi_VZIBaMqhYhAyScsvWc/edit#gid=0
	# def export_xu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1fWq_Ts3ok4VFy82jkeZ71PABuTEGyeqvbTThUO_B3k0/edit#gid=0
	# def export_m_xu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1a2thhP0be7_IGbF0OHVm-wghfOLExD3QugdP3DWqvjU/edit#gid=0
	# def export_m_xu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1DfTZC-uvAZqRwdxkpAFBYX6zaB3nimLI74pIjQVUkpI/edit#gid=0
	# def export_m_xu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1lqJGL_pwIDoj8JmWVgJugUYLsLEVQ27kydXEaUOs9cc/edit#gid=0
	# def export_m_xu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1adAa-IiqMiZJW0wW47y3WEOP0STcuj-O5LdpPySpwXQ/edit#gid=0
	# def export_yu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1KNcnahyONSlbFzCW19WZyQXfAXi_Umjdulmg8UTcmfA/edit#gid=0
	# def export_yu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1r60inQTgKtjrWZUkKsShmySSuCl6wvC1eihd3yNuBVQ/edit#gid=0
	# def export_yu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1Z9jpdBbTlGqDGAqFGhYsqWsupVhqPn7po_lQ9gtuLyE/edit#gid=0 
	# def export_yu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1V-IJxGflg8t_G0548ldkNGDr8bWPDuxsv1xkomacWbc/edit#gid=0
	# def export_m_yu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/168meUMrJALGlroCh-L-rmmU-ekUGdV2B0js9DG0lADA/edit#gid=0
	# def export_m_yu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/103dRd6LSzOsc1wojbmMxq3-6MqeBzqxfwM0cYZddPdY/edit#gid=0
	# def export_m_yu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1XTiaeFicg4M37H_bR4rTDPZJQxrOopE-Jr539-8_nLI/edit#gid=0
	# def export_m_yu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/10Q74n_W-6Ertw_xw8rFq2wnT0xFeBC05LGMeNLw5yBE/edit#gid=0
	# def export_zu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1FC9Js1pPjugjGxLQNHbHbc_0F87ixuS9ZyvDyzDQP8E/edit#gid=0
	# def export_zu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1OlYmymnrNovVCzFIQ_Yr2932iINktaeFRLRBTi9kR5g/edit#gid=0
	# def export_zu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1YL9VeYOeZ9J4S9EaLTZCRPeihhhDvziD0nLwNM1w7js/edit#gid=0
	# def export_zu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1NSHAh6p4z_Et3whg8mx7rJmC8aoxQL7OZlLBxe37mMI/edit#gid=0
	# def export_m_zu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1ehgUYy3iUB-q7e-N5YIm1x5qynCKMKp1jMSzBOaZeuc/edit#gid=0
	# def export_m_zu_m_xf(self,x , y, z):
        Test: https://docs.google.com/spreadsheets/d/1JxZ23BxRbVewZHP2O0P8SfAc5ULV-DyuSq04Jcdfcyc/edit#gid=0
	# def export_m_zu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1QfXFJeLLPR3ZMJHBnIzUq076bcUd_EnfE7ZhnzYmbCs/edit#gid=0
	# def export_m_zu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1dKha2rLBGHXogtq_5aqQGnwvFJoVn4Lk0Fg60wpEgm8/edit#gid=0
	# def import_xu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/15q6p9WxESIhi3Y3LMnHXGgDjzeUUeyxptJ63hzSj2LA/edit#gid=0
	# def import_xu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1lWaXrMOvvFVUnbLxoI_Slnt1UV4QoIUJZsInsJ5NL_E/edit#gid=0
	# def import_xu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1dUZeM6hMiD4A_kl6arTTuLmAeNgTMZFbKenPei6xmfY/edit#gid=0
	# def import_xu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1AmsIQiYZxaxk_XgWdY4-_3t1CSOUn2QlO3KnThoVl_Q/edit#gid=0
	# def import_m_xu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1N4XBDC8Qe8a9za61Djf0q24-u5brtp7dQb0iv5eNCR0/edit#gid=0
	# def import_m_xu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1mgCkgXSLjR9b-c4PFvLX_s2nmE05-uMlSciLfPTVdTk/edit#gid=0
	# def import_m_xu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1AnIChXac5-ShiU2E49cgX8xz7ZimxBjqLH_sojBwsNE/edit#gid=0
	# def import_m_xu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/18yIn12VbRUrhxzCsrGG0uJYQuEXBcrEXPObe6Q6Y8vE/edit#gid=0
	# def import_yu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1kRn-A4Ev54c2wuqK7h4B05GgeV_eTBWML_J5hEsnGXI/edit#gid=0
	# def import_yu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1agfL9JPhEObBTkE79i-3YJKdoVu269pBMOF7R7SG2Wk/edit#gid=0
	# def import_yu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1sIkOekTvKGd7MYPQO7WPurp-tpcNi3W4N4j_B2QxbzY/edit#gid=0
	# def import_yu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1Dpyf70ZwrqvStDlfeQFnXpirZx9hgFm87ZVcNNVjeWI/edit#gid=0
	# def import_m_yu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1QuGVQGDfspcMzt0x-g3Zy3DyDMrfAPbPgcbXOWIKmoI/edit#gid=0
	# def import_m_yu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1gn08gu4SA_E1Wzs4tAj2dWA_NTgfN_riKXscWNhhosA/edit#gid=0
	# def import_m_yu_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1FHLTrROr3MbLFT6_OGLMTKQD3WTghjUHcg7rBHi2sC4/edit#gid=0
	# def import_m_yu_m_zf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1xw_ny58_aSWpcLB6Rh0424Uh5hpTPiOU49aeZaBrFOc/edit#gid=0
	# def import_zu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/17F3XfK7n2MF_swOyL85c6QougJRexaiiY2ikulHMW8Y/edit#gid=0
	# def import_zu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1y13JbzX5pO2eN7m8DlC7KJl506Hr3KjF0n1TociGsgA/edit#gid=0
	# def import_zu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/15RoQXygBariZP_ZdcRrJ1ojn2MQ5B58vOcKBC9EsDj8/edit#gid=0
	# def import_zu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1YBbN5mb3z-sK1TaYFyBBvNOu7m8OfyaDc2WPmeiKdJI/edit#gid=0
	# def import_m_zu_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/17jWj4mwHrA50JnBvV6wmRE3tDuRIHiypqkwtiOqxnyw/edit#gid=0
	# def import_m_zu_m_xf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/13oxpypyNUCYu4NMIpb1_XSgFF4ik2zWbfZiPBAVPcqQ/edit#gid=0
	# def import_m_zu_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1_2o8J5IPTP7zpEou_xXAOHs3mkDimNSzqi48DHhUv70/edit#gid=0
	# def import_m_zu_m_yf(self, x, y, z):
        Test: https://docs.google.com/spreadsheets/d/1pNdP4up14eMtwy2kH-VtLhPUMHl7SviDwIVNG7PEn38/edit#gid=0

    '''
    def __init__(self, 
             XU=False, M_XU=False, YU=False, M_YU=False, ZU=False, M_ZU=False,
             XF=False, M_XF=False, YF=False, M_YF=False, ZF=False, M_ZF=False):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYCoordsys general constructor.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Initialize the member variables using the values passed into the allocation call.
        
        This constructor intialize these member variables:
            :Memeber variable XU    : Up vector towards positive X axis boolean value.
            :Memeber variable M_XU  : Up vector towards negative X axis boolean value.
            :Memeber variable YU    : Up vector towards positive Y axis boolean value.
            :Memeber variable M_YU  : Up vector towards negative Y axis boolean value.
            :Memeber variable ZU    : Up vector towards positive Z axis boolean value.
            :Memeber variable M_ZU  : Up vector towards negative Z axis boolean value.
            :Memeber variable XF    : Forward vector towards positive X axis boolean value.
            :Memeber variable M_XF  : Forward vector towards negative X axis boolean value.
            :Memeber variable YF    : Forward vector towards positive Y axis boolean value.
            :Memeber variable M_YF  : Forward vector towards negative Y axis boolean value.
            :Memeber variable ZF    : Forward vector towards positive Z axis boolean value.
            :Memeber variable M_ZF  : Forward vector towards negative Z axis boolean value.
            :Member variable coordoption_up_str: Up vector final export string value.
            :Member variable coordoption_forward_str: Forward vector final export string value.

        And also intializes these member variables when above variables are 
        initialized properly:
            :Memeber variable coordoption_up_str        : Up vector axis value in string format, if initialize with XU set to true then this value will be "X", where if M_XU is set to true then this value will be "-X"
            :Memeber variable coordoption_forward_str   : Forward vector axis value in string format, if initialize with XF set to true then this value will be "X", where if M_XF is set to true then this value will be "-X"
        If not then below member variables are set to Blender coordinate axis 
        default values [Z up Y forward]:
            :Memeber variable coordoption_up_str        : Default value string "Z" 
            :Memeber variable coordoption_forward_str   : Default value string "Y"

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param XU: Coordsnate system export option UP vector axis points to X axis.
        :type  XU: boolean.
        :param M_XU: Coordsnate system export option UP vector axis points to -X axis.
        :type  M_XU: boolean.
        :param YU: Coordsnate system export option UP vector axis points to Y axis.
        :type  YU: boolean.
        :param M_YU: Coordsnate system export option UP vector axis points to -Y axis.
        :type  M_YU: boolean.
        :param ZU: Coordsnate system export option UP vector axis points to Z axis.
        :type  ZU: boolean.
        :param M_ZU: Coordsnate system export option UP vector axis points to -Z axis.
        :type  M_ZU: boolean.
        :param XF: Coordsnate system export option FORWARD vector axis points to X axis.
        :type  XF: boolean.
        :param M_XF: Coordsnate system export option FORWARD vector axis points to -X axis.
        :type  M_XF: boolean.
        :param YF: Coordsnate system export option FORWARD vector axis points to Y axis.
        :type  YF: boolean.
        :param M_YF: Coordsnate system export option FORWARD vector axis points to -Y axis.
        :type  M_YF: boolean.
        :param ZF: Coordsnate system export option FORWARD vector axis points to Z axis.
        :type  ZF: boolean.
        :param M_ZF: Coordsnate system export option FORWARD vector axis points to -Z axis.
        :type  M_ZF: boolean.
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
            :return: Return initialized WYCoordsys object with member variables 
                     intialized properly
            :rtype : WYCoordsys
        '''
        #-----------------------------------------------------------------------
        # Coordinate system options [UP] vector boolean values.
        #----------------------------------------------------------------------- 
        self.XU = XU
        self.M_XU = M_XU
        self.YU = YU
        self.M_YU = M_YU
        self.ZU = ZU
        self.M_ZU = M_ZU
        
        coordoption_up_array = [self.XU, self.M_XU, self.YU, 
                                self.M_YU, self.ZU, self.M_ZU]
        coordoption_up_true_counter = 0
        for i in range(0, len(coordoption_up_array)):
            if coordoption_up_array[i] == True:
                coordoption_up_true_counter += 1
                
        #-----------------------------------------------------------------------
        # Coordinate system options [FORWARD] vector boolean values.
        #-----------------------------------------------------------------------
        self.XF = XF
        self.M_XF = M_XF
        self.YF = YF
        self.M_YF = M_YF
        self.ZF = ZF
        self.M_ZF = M_ZF
        
        coordoption_forward_array = [self.XF, self.M_XF, self.YF, 
                                     self.M_YF, self.ZF, self.M_ZF]
        coordoption_forward_true_counter = 0
        for elem in coordoption_forward_array:
            if elem:
                coordoption_forward_true_counter += 1
             
        #-----------------------------------------------------------------------
        # Coordinate system options settings:
        #       Cannot have format eg. [X up X forward], [X up -X forward] ... 
        #       Cannot have more than 1 flag on on no flag on.
        # If not match above conditions, will be exported with default 
        # Blender right handed coordinate system [Z up, Y forward]
        #-----------------------------------------------------------------------
        if (coordoption_up_true_counter > 1 or \
            coordoption_up_true_counter <= 0) or \
           (coordoption_forward_true_counter > 1 or \
           coordoption_forward_true_counter <= 0) \
        or ((XU or M_XU) and (XF or M_XF)) \
        or ((YU or M_YU) and (YF or M_YF)) \
        or ((ZU or M_ZU) and (ZF or M_ZF)) :
            '''
            print("==========================================================================================================")
            print("ERROR::WYCoordsys::__init__::Coordinate system option cannot be processed --> Exported as : Default Z up Y forward")
            print("==========================================================================================================")
            '''
            self.XU = False
            self.M_XU = False
            self.YU = False
            self.M_YU = False
            self.ZU = True
            self.M_ZU = False

            self.XF = False
            self.M_XF = False
            self.YF = True
            self.M_YF = False
            self.ZF = False
            self.M_ZF = False
            
        #-----------------------------------------------------------------------
        # Evaluate the coordinate UP vector string value to be exported.
        #-----------------------------------------------------------------------
        self.coordoption_up_str = "X" if (self.XU == True) \
        else "-X" if (self.M_XU == True) \
        else "Y" if (self.YU == True) \
        else "-Y" if (self.M_YU == True) \
        else "Z" if (self.ZU == True) \
        else "-Z" if (self.M_ZU == True) \
        else "Z" 
            
        #-----------------------------------------------------------------------
        # Evaluate the coordinate UP vector string value to be exported.
        #-----------------------------------------------------------------------
        self.coordoption_forward_str = "X" if (self.XF == True) \
        else "-X" if (self.M_XF == True) \
        else "Y" if (self.YF == True) \
        else "-Y" if (self.M_YF == True) \
        else "Z" if (self.ZF == True) \
        else "-Z" if (self.M_ZF == True) \
        else "Y"

    #---------------------------------------------------------------------------
    # Overriden equal function.
    #---------------------------------------------------------------------------
    def __eq__(self, other):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYCoordsys overrided equal function.
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Compares the member variables with the memeber variables intialized 
        in "other" object return True if these 2 object has all the member 
        variables same values else return False.

        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param  other: Second WYCoordsys object to compare with.
        :type   other: WYCoordsys
        ------------------------------------------------------------------------
        Return:
        ------------------------------------------------------------------------
        :return: Return the result of comparison between 2 objects.
        :rtype: boolean

        '''
        if other == None:
            return False
        return (self.XU == other.XU and \
                self.M_XU == other.M_XU and \
                self.YU == other.YU  and \
                self.M_YU == other.M_YU and \
                self.ZU == other.ZU  and \
                self.M_ZU == other.M_ZU and \
                self.XF == other.XF and \
                self.M_XF == other.M_XF and \
                self.YF == other.YF and \
                self.M_YF == other.M_YF and \
                self.ZF == other.ZF and \
                self.M_ZF == other.M_ZF and \
                self.coordoption_up_str == other.coordoption_up_str and \
                self.coordoption_forward_str == other.coordoption_forward_str)    
    
    def __str__(self):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        WYCoordsys toString function.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Manipulate the string to represent the current WYCoordsys object in the 
        file using the values initialized when allocated.

        :Memeber variable coordoption_up_str        : Up vector axis value in string format, if initialize with XU set to true then this value will be "X", where if M_XU is set to true then this value will be "-X"
        :Memeber variable coordoption_forward_str   : Forward vector axis value in string format, if initialize with XF set to true then this value will be "X", where if M_XF is set to true then this value will be "-X"

        This function acts like toString function in Java so when I print the 
        WYCoordsys object directly, so when WYMesh is exported current 
        WYCoordsys inside WYMesh wil be printed directly through file stream
        and the information about this WYCoordsys object will be printed to file
        with following format:
        :Example: 
             CU X
             CF Y
        '''
        # ----------------------------------------------------------------------
        # CU - Coordinate system option [Up]
        # CF - Coordinate system option [Forward]
        # ----------------------------------------------------------------------
        return "CU " + self.coordoption_up_str + '\n' + \
               "CF " + self.coordoption_forward_str + '\n'
    
    #===========================================================================
    #===========================================================================
    #===========================================================================
    # Main coordinate system import function
    #===========================================================================
    #===========================================================================
    #===========================================================================
    def import_coordconversion(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Main coordinate system conversion function to convert the coordinate
        values back into import format.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function converts the XYZ coordinate value using the corodinate
        system import option indicated in current WYCoordsys object when 
        initialized through general constructor.

        :pre-condition: Current WYCoordsys object must have member variables
               "coordoption_up_str" and "coordoption_forward_str" initialized
               using proper boolean flags passed into the default constructor.
               These member variables are automatically initialized using the 
               boolean values passed into the default constructor.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Calculate the final import format vertex tuple by accessing the 
        # data inside current WYCoordsys object and calling each cases'
        # corresponding sub functions to convert the coordinate values
        # by each cases.
        resultVertex = \
            self.import_xu_yf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "Y" \
        else self.import_xu_m_yf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "-Y" \
        else self.import_xu_zf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "Z" \
        else self.import_xu_m_zf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "-Z" \
        else self.import_m_xu_yf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "Y" \
        else self.import_m_xu_m_yf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "-Y" \
        else self.import_m_xu_zf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "Z" \
        else self.import_m_xu_m_zf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "-Z" \
        else self.import_yu_xf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "X" \
        else self.import_yu_m_xf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "-X" \
        else self.import_yu_zf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "Z" \
        else self.import_yu_m_zf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "-Z" \
        else self.import_m_yu_xf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "X" \
        else self.import_m_yu_m_xf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "-X" \
        else self.import_m_yu_zf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "Z" \
        else self.import_m_yu_m_zf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "-Z" \
        else self.import_zu_xf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "X" \
        else self.import_zu_m_xf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "-X" \
        else self.import_zu_yf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "Y" \
        else self.import_zu_m_yf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "-Y" \
        else self.import_m_zu_xf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "X" \
        else self.import_m_zu_m_xf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "-X" \
        else self.import_m_zu_yf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "Y" \
        else self.import_m_zu_m_yf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "-Y" \
        else self.import_zu_yf(x, y, z)
        
        # Return converted coordinate vertex value.
        return resultVertex

    #===========================================================================
    #===========================================================================
    #===========================================================================
    # Main coordinate system export function
    #===========================================================================
    #===========================================================================
    #===========================================================================
    def export_coordconversion(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Main coordinate system conversion function to convert the coordinate
        values into export format.

        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        This function converts the XYZ coordinate value using the corodinate
        system export option indicated in current WYCoordsys object when 
        initialized through general constructor.

        :pre-condition: Current WYCoordsys object must have member variables
               "coordoption_up_str" and "coordoption_forward_str" initialized
               using proper boolean flags passed into the default constructor.
               These member variables are automatically initialized using the 
               boolean values passed into the default constructor.
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Calculate the final export format vertex tuple by accessing the 
        # data inside current WYCoordsys object and calling each cases'
        # corresponding sub functions to convert the coordinate values
        # by each cases.
        resultVertex = \
            self.export_xu_yf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "Y" \
        else self.export_xu_m_yf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "-Y" \
        else self.export_xu_zf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "Z" \
        else self.export_xu_m_zf(x, y, z) \
            if self.coordoption_up_str == "X" and \
               self.coordoption_forward_str == "-Z" \
        else self.export_m_xu_yf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "Y" \
        else self.export_m_xu_m_yf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "-Y" \
        else self.export_m_xu_zf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "Z" \
        else self.export_m_xu_m_zf(x, y, z) \
            if self.coordoption_up_str == "-X" and \
               self.coordoption_forward_str == "-Z" \
        else self.export_yu_xf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "X" \
        else self.export_yu_m_xf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "-X" \
        else self.export_yu_zf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "Z" \
        else self.export_yu_m_zf(x, y, z) \
            if self.coordoption_up_str == "Y" and \
               self.coordoption_forward_str == "-Z" \
        else self.export_m_yu_xf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "X" \
        else self.export_m_yu_m_xf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "-X" \
        else self.export_m_yu_zf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "Z" \
        else self.export_m_yu_m_zf(x, y, z) \
            if self.coordoption_up_str == "-Y" and \
               self.coordoption_forward_str == "-Z" \
        else self.export_zu_xf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "X" \
        else self.export_zu_m_xf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "-X" \
        else self.export_zu_yf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "Y" \
        else self.export_zu_m_yf(x, y, z) \
            if self.coordoption_up_str == "Z" and \
               self.coordoption_forward_str == "-Y" \
        else self.export_m_zu_xf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "X" \
        else self.export_m_zu_m_xf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "-X" \
        else self.export_m_zu_yf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "Y" \
        else self.export_m_zu_m_yf(x, y, z) \
            if self.coordoption_up_str == "-Z" and \
               self.coordoption_forward_str == "-Y" \
        else self.export_zu_yf(x, y, z)
        
        # Return converted coordinate vertex value.
        return resultVertex
        
    #===========================================================================
    #===========================================================================
    #===========================================================================
    # Coordinate system export sub functions
    #===========================================================================
    #===========================================================================
    #===========================================================================

    #===========================================================================
    # X UP Y FORWARD
    #===========================================================================
    def export_xu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [X up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up Y forward] format:
        
        # Export option        :[ X up Y forward  ]
        # Conversion formula   :[ Z <-> X, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
        if (x <= int(-sys.maxsize) or
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        #print("Export conversion:[ X up Y forward ][ Z <-> X, Z * -1 ]")
        temp = x
        x = z
        z = temp 
        z = z* -1
        return (x,y,z)
    #===========================================================================
    # X UP -Y FORWARD
    #===========================================================================
    def export_xu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [X up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up -Y forward] format:
        
        # Export option     :[ X up -Y forward ]
        # Convert formula   :[ Z <-> X, Y * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        #print("Export conversion:[ X up -Y forward ][ Z <-> X, Y * -1 ]")
        temp = x
        x = z
        z = temp
        y = y * -1
        return (x,y,z)
    
    #===========================================================================
    # X UP Z FORWARD
    #===========================================================================
    def export_xu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [X up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up Z forward] format:
        
        # Export option     :[ X up Z forward   ]
        # Convert formula   :[ Z <-> X, Y <-> Z ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ X up Z forward ][ Z <-> X, Y <-> Z ]")
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        return (x,y,z)
    
    #===========================================================================
    # X UP -Z FORWARD
    #===========================================================================
    def export_xu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [X up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up -Z forward] format:
        
        # Export option     :[ X up -Z forward ]
        # Convert formula   :[ Z <-> X, Y <-> Z, Z * -1, Y * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ X up -Z forward ][ Z <-> X, Y <-> Z, Z * -1, Y * -1 ]")
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        z = z * -1
        y = y * -1
        return (x,y,z)

    #===========================================================================
    # -X UP Y FORWARD
    #===========================================================================
    def export_m_xu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-X up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up -Z forward] format:
        
        # Export option     :[ -X up Y forward ]
        # Convert formula   :[ Z <-> X, X * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -X up Y forward ][ Z <-> X, X * -1 ]")
        
        temp = x
        x = z
        z = temp
        
        x = x * -1
        return (x,y,z)
    #===========================================================================
    # -X UP -Y FORWARD
    #===========================================================================
    def export_m_xu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-X up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up -Y forward] format:
        
        # Export option     :[ -X up -Y forward                ]
        # Convert formula   :[ Z <-> X, X * -1, Y * -1, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -X up -Y forward ][ Z <-> X, X * -1, Y * -1, Z * -1 ]")
        temp = x
        x = z
        z = temp        
        x = x * -1
        y = y * -1
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # -X UP Z FORWARD
    #===========================================================================
    def export_m_xu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-X up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up Z forward] format:
        
        # Export option     :[ -X up Z forward                  ]
        # Convert formula   :[ Z <-> X, Y <-> Z, X * -1, Y * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -X up Z forward ][ Z <-> X, Y <-> Z, X * -1, Y * -1 ]")
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        x = x * -1
        y = y * -1
        return (x,y,z)
    
    #===========================================================================
    # -X UP -Z FORWARD
    #===========================================================================
    def export_m_xu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-X up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up -Z forward] format:
        
        # Export option     :[ -X up -Z forward                 ]
        # Convert formula   :[ Z <-> X, Y <-> Z, X * -1, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -X up -Z forward ][ Z <-> X, Y <-> Z, X * -1, Z * -1 ]")
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        x = x * -1
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # Y UP X FORWARD
    #===========================================================================
    def export_yu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Y up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up X forward] format:
        
        # Export option     :[ Y up X forward   ]
        # Convert formula   :[ Z <-> Y, Z <-> X ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Y up X forward ][ Z <-> Y, Z <-> X ]")
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        return (x,y,z)
    
    
    #===========================================================================
    # Y UP -X FORWARD
    #===========================================================================
    def export_yu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Y up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up -X forward] format:
        
        # Export option     :[ Y up -X forward                  ]
        # Convert formula   :[ Z <-> Y, Z <-> X, X * -1, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Y up -X forward ][ Z <-> Y, Z <-> X, X * -1, Z * -1 ]")
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        x = x * -1
        z = z * -1    
        return (x,y,z)
    
    
    #===========================================================================
    # Y UP Z FORWARD
    #===========================================================================
    def export_yu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Y up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up Z forward] format:
        
        # Export option     :[ Y up Z forward  ]
        # Convert formula   :[ Z <-> Y, X * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Y up Z forward ][ Z <-> Y, X * -1 ]")
        temp = y
        y = z
        z = temp
        
        x = x * -1
        return (x,y,z)
    
    
    #===========================================================================
    # Y UP Z FORWARD
    #===========================================================================
    def export_yu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Y up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up -Z forward] format:
        
        # Export option     :[ Y up -Z forward ]
        # Convert formula   :[ Z <-> Y, Z * -1 ]    
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Y up -Z forward ][ Z <-> Y, Z * -1 ]")
        temp = y
        y = z
        z = temp

        z = z * -1
        return (x,y,z)

    #===========================================================================
    # -Y UP X FORWARD
    #===========================================================================
    def export_m_yu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Y up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up X forward] format:
        
        # Export option     :[ -Y up X forward                   ]
        # Convert formula   :[ Z <-> Y, Z <-> X, Y * -1,  Z * -1 ]   
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Y up X forward ][ Z <-> Y, Z <-> X, Y * -1,  Z * -1 ]")
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        y = y * -1
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # -Y UP -X FORWARD
    #===========================================================================
    def export_m_yu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Y up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up -X forward] format:
        
        # Export option     :[ -Y up -X forward                  ]
        # Convert formula   :[ Z <-> Y, Z <-> X, Y * -1,  X * -1 ]  
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Y up -X forward ][ Z <-> Y, Z <-> X, Y * -1,  X * -1 ]")
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        y = y * -1
        x = x * -1
        return (x,y,z)
    
    #===========================================================================
    # -Y UP Z FORWARD
    #===========================================================================
    def export_m_yu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Y up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up Z forward] format:
        
        # Export option     :[ -Y up Z forward ]
        # Convert formula   :[ Z <-> Y, Y * -1 ] 
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Y up Z forward ][ Z <-> Y, Y * -1 ]")
        temp = y
        y = z
        z = temp
        y = y * -1 
        return (x,y,z)
    
    #===========================================================================
    # -Y UP -Z FORWARD
    #===========================================================================
    def export_m_yu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Y up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up -Z forward] format:
        
        # Export option     :[ -Y up -Z forward                ]
        # Convert formula   :[ Z <-> Y, X * -1, Y * -1, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Y up -Z forward ][ Z <-> Y, X * -1, Y * -1, Z * -1 ]")
        temp = y
        y = z
        z = temp
        
        x = x * -1
        y = y * -1
        z = z * -1    
        return (x,y,z)
    
    #===========================================================================
    # Z UP X FORWARD
    #===========================================================================
    def export_zu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Z up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up X forward] format:
        
        # Export option     :[ Z up X forward  ]
        # Convert formula   :[ Y <-> X, Y * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Z up X forward ][ Y <-> X, Y * -1 ]")
        temp = y
        y = x
        x = temp    
        y = y * -1
        return (x,y,z)
    
    #===========================================================================
    # Z UP -X FORWARD
    #===========================================================================
    def export_zu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Z up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up -X forward] format:
        
        # Export option     :[ Z up -X forward ]
        # Convert formula   :[ Y <-> X, X * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Z up -X forward ][ Y <-> X, X * -1 ]")
        temp = y
        y = x
        x = temp
        x = x * -1
        return (x,y,z)
    
    #===========================================================================
    # Z UP Y FORWARD
    #===========================================================================
    def export_zu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Z up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up Y forward] format:
        
        # Export option     :[ Z up Y forward ]
        # Convert formula   :[ DEFAULT VALUE  ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Z up Y forward ][ DEFAULT VALUE ]")
        return (x,y,z)
    
    #===========================================================================
    # Z UP -Y FORWARD
    #===========================================================================
    def export_zu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [Z up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up -Y forward] format:
        
        # Export option     :[ Z up -Y forward ]
        # Convert formula   :[ Y * -1 ,  X * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ Z up -Y forward ][ Y * -1 ,  X * -1 ]")
        x = x * -1
        y = y * -1
        return (x,y,z)
        
    #===========================================================================
    # -Z UP X FORWARD
    #===========================================================================
    def export_m_zu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Z up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up X forward] format:
        
        # Export option     :[ -Z up X forward ]
        # Convert formula   :[ Y <-> X, Z * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Z up X forward ][ Y <-> X, Z * -1 ]")
        temp = y
        y = x
        x = temp
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # -Z UP -X FORWARD
    #===========================================================================
    def export_m_zu_m_xf(self,x , y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Z up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up X forward] format:
        
        # Export option     :[ -Z up -X forward                ]
        # Convert formula   :[ Y <-> X, Z * -1, X * -1, Y * -1 ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Z up -X forward ][ Y <-> X, Z * -1, X * -1, Y * -1 ]")
        temp = y
        y = x
        x = temp
        x = x * -1
        y = y * -1
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # -Z UP Y FORWARD
    #===========================================================================
    def export_m_zu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Z up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up Y forward] format:
        
        # Export option     :[ -Z up Y forward ]
        # Convert formula   :[ Z * -1, X * -1  ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Z up Y forward ][ Z * -1, X * -1 ]")
        x = x * -1
        z = z * -1
        return (x,y,z)
    
    #===========================================================================
    # -Z UP -Y FORWARD
    #===========================================================================
    def export_m_zu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Exporting to coordinate system format: [-Z up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up -Y forward] format:
        
        # Export option     :[ -Z up -Y forward ]
        # Convert formula   :[ Z * -1, Y * -1   ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into export 
                 format using current WYCoordsys data values intialized when
                 allocated.
        :rtype : (X,Y,Z)
        '''
        # Must use int(sys.maxsize) because following is the only way to test
        # the boundary using following code:
        # eg. Decimal(sys.maxsize) - Decimal(0.1) < int(sys.maxsize) 
        # eg. Decimal(sys.maxsize) + Decimal(0.1) > int(sys.maxsize) 
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
            
        #print("Export conversion:[ -Z up -Y forward ][ Z * -1, Y * -1 ]")
        y = y * -1
        z = z * -1
        return (x,y,z)
  
    #===========================================================================
    #===========================================================================
    #===========================================================================
    # Coordinate system import sub functions
    #===========================================================================
    #===========================================================================
    #===========================================================================

    #===========================================================================
    # X UP Y FORWARD
    #===========================================================================
    def import_xu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [X up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up Y forward] format:
        
        # Export option     :[ X up Y forward   ]
        # Convert formula   :[ Z * -1, X <-> Z  ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh files.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None

        z = z * -1
        temp = x
        x = z
        z = temp
        return (x,y,z)

    #===========================================================================
    # X UP -Y FORWARD
    #===========================================================================
    def import_xu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [X up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up -Y forward] format:
        
        # Export option     :[ X up -Y forward  ]
        # Convert formula   :[ Y * -1, X <-> Z  ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None

        y = y * -1
        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # X UP Z FORWARD
    #===========================================================================
    def import_xu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [X up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up Z forward] format:
        
        # Export option     :[ X up Z forward   ]
        # Convert formula   :[ Y <-> Z, X <-> Z ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None

        temp = y
        y = z
        z = temp

        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # X UP -Z FORWARD
    #===========================================================================
    def import_xu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [X up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [X up -Z forward] format:
        
        # Export option     :[ X up -Z forward                   ]
        # Convert formula   :[ Z * -1, Y * -1, Y <-> Z, X <-> Z  ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        z = z * -1
        y = y * -1

        temp = y
        y = z
        z = temp

        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -X UP Y FORWARD
    #===========================================================================
    def import_m_xu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-X up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up Y forward] format:
        
        # Export option     :[ -X up Y forward   ]
        # Convert formula   :[ X * -1, X <-> Z   ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -X UP -Y FORWARD
    #===========================================================================
    def import_m_xu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-X up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up -Y forward] format:
        
        # Export option     :[ -X up -Y forward                     ]
        # Convert formula   :[ X * -1, Y * -1, Z * -1, X <-> Z      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        y = y * -1
        z = z * -1
        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -X UP Z FORWARD
    #===========================================================================
    def import_m_xu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-X up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up Z forward] format:
        
        # Export option     :[ -X up Z forward                     ]
        # Convert formula   :[ X * -1, Y * -1, Y <-> Z, X <-> Z    ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        y = y * -1
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -X UP -Z FORWARD
    #===========================================================================
    def import_m_xu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-X up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-X up -Z forward] format:
        
        # Export option     :[ -X up -Z forward                     ]
        # Convert formula   :[ X * -1, Z * -1, Y <-> Z, X <-> Z    ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        z = z * -1
        temp = y
        y = z
        z = temp
        temp = x
        x = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # Y UP X FORWARD
    #===========================================================================
    def import_yu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Y up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up X forward] format:
        
        # Export option     :[ Y up X forward      ]
        # Convert formula   :[ X <-> Z, Y <-> Z    ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # Y UP -X FORWARD
    #===========================================================================
    def import_yu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Y up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up -X forward] format:
        
        # Export option     :[ Y up -X forward                       ]
        # Convert formula   :[ X * -1, Z * -1, X <-> Z, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        z = z * -1
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # Y UP Z FORWARD
    #===========================================================================
    def import_yu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Y up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up Z forward] format:
        
        # Export option     :[ Y up Z forward      ]
        # Convert formula   :[ X * -1, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # Y UP -Z FORWARD
    #===========================================================================
    def import_yu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Y up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Y up -Z forward] format:
        
        # Export option     :[ Y up -Z forward      ]
        # Convert formula   :[ Z * -1, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        z = z * -1
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -Y UP X FORWARD
    #===========================================================================
    def import_m_yu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Y up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up X forward] format:
        
        # Export option     :[ -Y up X forward                      ]
        # Convert formula   :[ Y * -1, Z * -1, X <-> Z, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        y = y * -1
        z = z * -1
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -Y UP -X FORWARD
    #===========================================================================
    def import_m_yu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Y up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up -X forward] format:
        
        # Export option     :[ -Y up -X forward                     ]
        # Convert formula   :[ Y * -1, X * -1, X <-> Z, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        y = y * -1
        x = x * -1
        temp = x
        x = z
        z = temp
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -Y UP Z FORWARD
    #===========================================================================
    def import_m_yu_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Y up Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up Z forward] format:
        
        # Export option     :[ -Y up Z forward     ]
        # Convert formula   :[ Y * -1, Y <-> Z     ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        y = y * -1
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # -Y UP -Z FORWARD
    #===========================================================================
    def import_m_yu_m_zf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Y up -Z forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Y up -Z forward] format:
        
        # Export option     :[ -Y up -Z forward                     ]
        # Convert formula   :[ X * -1, Y * -1, Z * -1, Y <-> Z      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        y = y * -1
        z = z * -1
        temp = y
        y = z
        z = temp
        return (x,y,z)
    #===========================================================================
    # Z UP X FORWARD
    #===========================================================================
    def import_zu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Z up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up X forward] format:
        
        # Export option     :[ Z up X forward       ]
        # Convert formula   :[ Y * -1, Y <-> X      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        y = y * -1
        temp = y
        y = x
        x = temp
        return (x,y,z)
    #===========================================================================
    # Z UP -X FORWARD
    #===========================================================================
    def import_zu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Z up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up -X forward] format:
        
        # Export option     :[ Z up -X forward       ]
        # Convert formula   :[ X * -1, Y <-> X      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        temp = y
        y = x
        x = temp
        return (x,y,z)
    #===========================================================================
    # Z UP Y FORWARD
    #===========================================================================
    def import_zu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Z up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up Y forward] format:
        
        # Export option     :[ Z up Y forward       ]
        # Convert formula   :[ DEFAULT VALUE        ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        
        return (x,y,z)
    #===========================================================================
    # Z UP -Y FORWARD
    #===========================================================================
    def import_zu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [Z up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [Z up -Y forward] format:
        
        # Export option     :[ Z up -Y forward       ]
        # Convert formula   :[ Y * -1, Y <-> X      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        y = y * -1
        return (x,y,z)
    #===========================================================================
    # -Z UP X FORWARD
    #===========================================================================
    def import_m_zu_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Z up X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up X forward] format:
        
        # Export option     :[ -Z up X forward       ]
        # Convert formula   :[ Z * -1, Y <-> X      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        z = z * -1
        temp = y
        y = x
        x = temp
        return (x,y,z)
    #===========================================================================
    # -Z UP -X FORWARD
    #===========================================================================
    def import_m_zu_m_xf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Z up -X forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up -X forward] format:
        
        # Export option     :[ -Z up -X forward                     ]
        # Convert formula   :[ X * -1, Y * -1, Z * -1, Y <-> X      ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        y = y * -1
        z = z * -1
        temp = y
        y = x
        x = temp
        return (x,y,z)
    #===========================================================================
    # -Z UP Y FORWARD
    #===========================================================================
    def import_m_zu_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Z up Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up Y forward] format:
        
        # Export option     :[ -Z up Y forward      ]
        # Convert formula   :[ X * -1, Z * -1       ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        x = x * -1
        z = z * -1
        return (x,y,z)
    #===========================================================================
    # -Z UP -Y FORWARD
    #===========================================================================
    def import_m_zu_m_yf(self, x, y, z):
        '''
        ------------------------------------------------------------------------
        Title:
        ------------------------------------------------------------------------
        Sub coordinate system conversion function 
            - Importing as coordinate system format: [-Z up -Y forward]
        ------------------------------------------------------------------------
        Description:
        ------------------------------------------------------------------------
        Converting (X,Y,Z) vector value into [-Z up -Y forward] format:
        
        # Export option     :[ -Z up -Y forward     ]
        # Convert formula   :[ Y * -1, Z * -1       ]
        ------------------------------------------------------------------------
        Parameters:
        ------------------------------------------------------------------------
        :param x: Converting coordinate vector X value.
        :type  x: float
        :param y: Converting coordinate vector Y value.
        :type  z: float
        :param y: Converting coordinate vector Z value.
        :type  z: float

        ------------------------------------------------------------------------
        Returns:
        ------------------------------------------------------------------------
        :return: Returns the coordinate vector value converted into import 
                 format using current WYCoordsys data values intialized when
                 read from the mesh file.
        :rtype : (X,Y,Z)
        '''
        if (x >= int(sys.maxsize) or 
            y >= int(sys.maxsize) or 
            z >= int(sys.maxsize)):
            return None
            
        if (x <= int(-sys.maxsize) or 
            y <= int(-sys.maxsize) or 
            z <= int(-sys.maxsize)):
            return None
        y = y * -1
        z = z * -1
        return (x,y,z)
