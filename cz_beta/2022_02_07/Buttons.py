from AUserInterface import *
import ipywidgets as widgets
 
class Buttons(AUserInterface):
    
    def __init__(self, creator):
        self.eventListener = creator
        self.buttonsDict = {}
        self.statesDict = {}
        
    def resize(self):
        print("resize")
        
    def event(self, eventButton):
        
        for key, val in self.buttonsDict.items():
            if val == eventButton.owner:
                 break
        self.eventListener.handleButtonEvents(key, eventButton["new"])
        
    def disabled(self,name, state):
        self.buttonsDict[name].disabled = state    
        
    def getButtons(self):
        return self.buttonsDict
    
    def getStates(self):
        return self.statesDict
    
    def changeState(self,name,value):
        self.buttonsDict[name].value = value  
        
    def changeOptions(self,name,newOptions):
        self.buttonsDict[name].unobserve(self.event, "value")
        self.buttonsDict[name].options = newOptions
        
        self.statesDict[name] = self.buttonsDict[name].value
        self.buttonsDict[name].observe(self.event, "value")   
        
    def changeDescription(self,name,newDescription):
        self.buttonsDict[name].description = newDescription
        

        

        
    def playPauseEvent(self,eventButton):
        if eventButton["new"]:
            eventButton.owner.icon = "pause"
        else:
            eventButton.owner.icon = "play"
        self.event(eventButton)
        
        
    
    def newTogglePlayPause(self, name, width, height):       

        unit = "px"

        width = str(width)+unit
        height = str(height)+unit
        
        
        playPause = widgets.ToggleButton(value=False,description='',disabled=False,button_style='', 
            tooltip='play/pause',icon='play', layout=widgets.Layout(width=width, height=height))
        
        
        
        
        self.buttonsDict[name] = playPause
        self.statesDict[name] = playPause.value
        
        playPause.observe(self.playPauseEvent, "value")
        
    def newReset(self, name, width, height):
        unit = "px"

        width = str(width)+unit
        height = str(height)+unit
        
        
        reset = widgets.ToggleButton(value=False,description='',disabled=False,button_style='', 
            tooltip='reset',icon='undo', layout=widgets.Layout(width=width, height=height))
        
        self.buttonsDict[name] = reset
        self.statesDict[name] = reset.value
        
        reset.observe(self.event, "value")        
        
        #Slider Change in description
    def newIntSlider(self,name, minValue, maxValue, currentValue, currentDescription, newOrientation='horizontal',newReadout=True):        
        slider = widgets.IntSlider(min = minValue,max = maxValue, value = currentValue, description = currentDescription, 
               orientation=newOrientation,readout=newReadout)
        self.buttonsDict[name] = slider
        self.statesDict[name] = slider.value
        slider.observe(self.event, "value")
        
    def newFloatSlider(self,name, minValue, maxValue, currentValue, currentDescription,newOrientation='horizontal',newReadout=True):
        slider = widgets.FloatSlider(min = minValue,max = maxValue, value = currentValue, description = currentDescription,
                orientation=newOrientation,readout=newReadout)
        self.buttonsDict[name] = slider
        self.statesDict[name] = slider.value
        slider.observe(self.event, "value")
        
    def newRadioButtons(self, name, currentOptions, currentDescription):             
                        
        radioButtons = widgets.RadioButtons(options = currentOptions,description = currentDescription, disabled=False)        
        self.buttonsDict[name] = radioButtons
        self.statesDict[name] = radioButtons.value
        radioButtons.observe(self.event, "value")
        
    def newDropdown(self, name, currentOptions, currentDescription):
        
        dropdown = widgets.Dropdown(options = currentOptions,description = currentDescription, disabled=False)
        self.buttonsDict[name] = dropdown
        self.statesDict[name] = dropdown.value
        dropdown.observe(self.event, "value")
    
    #NEW
    def newFloatTextbox(self,name, currentValue, currentDescription):
        
        floatText = widgets.BoundedFloatText(value = currentValue, description = currentDescription, disabled=True)
        self.buttonsDict[name] = floatText
        self.statesDict[name] = floatText.value
        floatText.observe(self.event, "value")
        

        
        

        