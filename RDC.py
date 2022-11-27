# RDC.py - Python Script

# DESCRIPTION: Rendering Duration Calculator(RDC)
# REQUIRE: Python3
# AUTHOR: BulinThira - Github

import maya.cmds as mc
import math

def RDC():
    if mc.window('RDC_window', q=True, ex=True):
        mc.deleteUI('RDC_window', window=True)
    mc.window('RDC_window', title='Rendering Duration Calculator')
    mc.columnLayout(adj=True)
    
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='Start Frame: ')
    mc.intField('start_TF', w=80)
    mc.setParent('..')
    
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='End Frame:  ')
    mc.intField('end_TF', w=80)
    mc.setParent('..')
    
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='render/min: ')
    mc.floatField('RDM', w=80)
    mc.setParent('..')
    
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='Total Frame >> ')
    mc.text('resultframe_text', label='')
    mc.setParent('..')
    
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='Total Duration (hr) >> ')
    mc.text('result_text', label='')
    mc.setParent('..')
    
    mc.button(label='Calculate', h=30, c=rdCal)
    
    mc.showWindow('RDC_window')
    mc.window('RDC_window', e=True, wh=(350,130))
    
def rdCal(*args):
    SF = mc.intField('start_TF', q=True, v=True)
    EF = mc.intField('end_TF', q=True, v=True)
    RF = mc.floatField('RDM', q=True, v=True)
    
    totalFrame = (EF - SF) + 1
    result = (((EF - SF) + 1) * RF)/60
    res = math.modf(result)
    hrRes = ('%d' % res[1])
    minRes = ('%.d' % (res[0]*60))
    
    print(hrRes)
    print(minRes)

    totalResult = (f'{hrRes} hr {minRes} min')
    
    
    if totalResult:
        mc.text('resultframe_text', e=True, label=totalFrame)
        mc.text('result_text', e=True, label=totalResult)
    else:
        mc.text('result_text', e=True, label='INVALID')
    
RDC()