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
        if "widgets" in str(type(self.buttonsDict[name])):
            self.buttonsDict[name].disabled = state   
        elif "canvas" in str(type(self.buttonsDict[name])):
            pass 
        else:
            print("Kein Objekt aus der Bibliothek ipywidgets oder ipycanvas")
        
    def disable_all(self,state):
        for key in self.buttonsDict:
            #print(self.currentButtons[key])
            self.buttonsDict[key].disabled = state
        
    def getButtons(self):
        return self.buttonsDict
    
    def getStates(self):
        return self.statesDict
    
    def changeState(self,name,value): 
        if "widgets" in str(type(self.buttonsDict[name])):
            self.buttonsDict[name].value = value  
        elif "canvas" in str(type(self.buttonsDict[name])):
            self.eventListener.handleButtonEvents(name, value)
        else:
            print("Kein Objekt aus der Bibliothek ipywidgets oder ipycanvas")
        
    def changeOptions(self,name,newOptions):
        self.buttonsDict[name].unobserve(self.event, "value")
        self.buttonsDict[name].options = newOptions
        
        self.statesDict[name] = self.buttonsDict[name].value
        self.buttonsDict[name].observe(self.event, "value")   
        
    def changeDescription(self,name,newDescription):
        self.buttonsDict[name].description = newDescription   
     #New   
    def changeLayout(self,name, **kwargs):
        self.buttonsDict[name].layout = widgets.Layout(**kwargs)  

        

        
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
        slider = widgets.FloatSlider(min = minValue,max = maxValue,step=0.01, value = currentValue, description = currentDescription,
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
        
        floatText = widgets.FloatText(value = currentValue, description = currentDescription, disabled=False)
        self.buttonsDict[name] = floatText
        self.statesDict[name] = floatText.value
        floatText.observe(self.event, "value")
        
    def newCheckBox(self,name,currentDescription):
        checkBox = widgets.Checkbox(value=False, description=currentDescription, disabled=False, indent=False)
        self.buttonsDict[name] = checkBox
        self.statesDict[name] = checkBox.value
        checkBox.observe(self.event, "value")
   
    def linkingButtons(self,*args):
        for i in range(len(args)-1):            
            widgets.jslink((self.buttonsDict[args[i]], 'value'), (self.buttonsDict[args[i+1]], 'value'))
            self.buttonsDict[args[i+1]].unobserve_all()

    
    def canvasInteraction(self,name,canvas):
        out = widgets.Output()
        
        self.buttonsDict[name] = canvas
        self.statesDict[name] = [0,0]
        
        @out.capture()        
        def handle_interaction(x, y):
            point = [x,y]
            #print(point)
            self.eventListener.handleButtonEvents(name, point)

        canvas[-1].on_mouse_down(handle_interaction)
        #display(out)
    