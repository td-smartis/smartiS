from IUserInterface import *
import ipywidgets as widgets
 
class Buttons(IUserInterface):
    
    def __init__(self, creator):
        print("Konstruktor")
        self.eventListener = creator
        self.buttonsDict = {}
        self.statesDict = {}
        
    def resize(self):
        print("resize")
        
    def methode(self):
        print("methode")    
    
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
        
        
    def newIntSlider(self,name, minValue, maxValue, currentValue):
        
        slider = widgets.IntSlider(min = minValue,max = maxValue, value = currentValue, description = str(name))
        self.buttonsDict[name] = slider
        self.statesDict[name] = slider.value
        slider.observe(self.event, "value")
        
    def newFloatSlider(self,name, minValue, maxValue, currentValue):
        slider = widgets.FloatSlider(min = minValue,max = maxValue, value = currentValue, description = str(name))
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
        
        
    def getButtons(self):
        return self.buttonsDict
    
    def getStates(self):
        return self.statesDict
    
    def changeStates(self,name,value):
        self.buttonsDict[name].value = value  
        
    def changeOptions(self,name,newOptions):
        self.buttonsDict[name].unobserve(self.event, "value")
        self.buttonsDict[name].options = newOptions
        
        self.statesDict[name] = self.buttonsDict[name].value
        self.buttonsDict[name].observe(self.event, "value")
        
    def playPauseEvent(self,value):
        if value["new"]:
            value.owner.icon = "pause"
        else:
            value.owner.icon = "play"
        self.event(value)
        
        
    def event(self, value):
        
        for key, val in self.buttonsDict.items():
            if val == value.owner:
                 break

        self.eventListener.handleButtonEvents(key, value["new"])
        
    def disabled(self,name, state):
        self.buttonsDict[name].disabled = state
        