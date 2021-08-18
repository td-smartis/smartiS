from IUserInterface import *
from ipycanvas import MultiCanvas, Canvas, hold_canvas
 
class Chart(IUserInterface):
        
    def resize(self):
        print(self.canvas)
        #self.canvas[1].scale(0.5)
        for i in self.canvas:
            i.scale(1)
        
                
    def __init__(self, layers, width, height):
        
        """ Initialisiert die smartiS-Instanz.
        
        layers <list (string)>: Liste mit Bezeichnungen der Canvas/Ebenen
                     width <int>: Breite des Canvas
                    height <int>: Höhe des Canvas
        """
        
        self.canvas = MultiCanvas(len(layers), width=width, height=height)
        self.cdict = {}
        for i in range(len(layers)):
            self.cdict[layers[i]] = self.canvas[i]
        self.resize()
        
        
    
    def getChart(self):
        return self.canvas
    
    
    # wird vermutlich nicht gebraucht
    def getChartLayers(self):
        
        """ Gibt das Canvas mit angegebenem Namen zurück.
        
        key <string>: Bezeichnung der Ebene (durch __init__ bei Klassenaufruf definiert)
        """
        
        return self.cdict
    
    
    def clearLayer(self, layer):
        currentCanvas = self.cdict[layer]
        currentCanvas.clear()
    
    def drawRectangle(self,layer, x, y, width, height, savePath):
        
        currentCanvas = self.cdict[layer]
        with hold_canvas(currentCanvas):
            if not savePath:
                currentCanvas.clear()
            currentCanvas.fill_rect(x, y, width, height)
            currentCanvas.stroke_rect(x, y, width, height)

            
    def drawLine(self, layer, x_start, y_start, x_end, y_end, savePath):
        
        currentCanvas = self.cdict[layer]
        with hold_canvas(currentCanvas):
            if not savePath:
                currentCanvas.clear()
            currentCanvas.stroke_line(x_start, y_start, x_end, y_end)
    
    def drawArrow(self, layer, x_start, y_start, x_end, y_end, savePath):
        
        currentCanvas = self.cdict[layer]
        with hold_canvas(currentCanvas):
            if not savePath:
                currentCanvas.clear()
            currentCanvas.stroke_line(x_start, y_start, x_end, y_end)
            #currentCanvas.fill_polygon([(x_end+10, y_end+10), (x_end-10, y_end-10), (x_end, y_end)])
            #currentCanvas.stroke_polygon([(x_end+10, y_end+10), (x_end-10, y_end-10), (x_end, y_end)])
    
    def drawCircle(self,layer, x, y, radius, savePath):
        
        currentCanvas = self.cdict[layer]
        with hold_canvas(currentCanvas):
            if not savePath:
                currentCanvas.clear()
            currentCanvas.fill_circle(x, y, radius)
            currentCanvas.stroke_circle(x, y, radius)      

            
    def drawParralelLines(self,layer, x_start, y_start, width, height, number, alignment): 
         
        currentCanvas = self.cdict[layer]
        with hold_canvas(currentCanvas):    
            
            for i in range(abs(number)):
                if alignment == "vertical":
                    x = x_start + i * width/number 
                    currentCanvas.stroke_line(x,y_start,x,y_start+height)

                elif alignment == "horizontal":
                    y = y_start + i * height/number 
                    currentCanvas.stroke_line(x_start,y,x_start+width,y)
                    
    
            
            
    def changeLayerLook(self, layer, funktion, parameter):
        
        currentCanvas = self.cdict[layer]
        
        if str(funktion) == "fillingColor" :
            currentCanvas.fill_style = parameter
        elif str(funktion) == "lineColor" :
            currentCanvas.stroke_style = parameter
        elif str(funktion) == "lineWidth" :
            currentCanvas.line_width = parameter
        elif str(funktion) == "lineDash" :
            currentCanvas.set_line_dash(parameter)
            
        else:
            print("no such funktion available")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        