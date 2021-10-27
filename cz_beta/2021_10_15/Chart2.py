from IUserInterface import *
from ipycanvas import MultiCanvas, Canvas, hold_canvas
from math import pi, sin, cos, atan, sqrt
 
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
        self.tmpCanvas = MultiCanvas(len(layers), width=width, height=height)
        self.cdict = {}
        self.tmpCanvasDict = {}
        for i in range(len(layers)):
            self.cdict[layers[i]] = self.canvas[i]
            self.tmpCanvasDict[layers[i]] = self.tmpCanvas[i]
        #self.resize()
        
    def __del__(self): 
        del self.canvas
        del self.tmpCanvas
    
    def getChart(self):
        return self.canvas
    
    def getTmpChart(self):
        return self.tmpCanvas
    
    
    # wird vermutlich nicht gebraucht
    def getChartLayers(self):
        
        """ Gibt das Canvas mit angegebenem Namen zurück.
        
        key <string>: Bezeichnung der Ebene (durch __init__ bei Klassenaufruf definiert)
        """
        
        return self.cdict
    
    
    def clearLayer(self, layer):
        self.cdict[layer].clear()
        self.tmpCanvasDict[layer].clear()
    
    def drawRectangle(self,layer, x, y, width, height, savePath):
        
        currentCanvas = self.tmpCanvasDict[layer]

        if not savePath:
            currentCanvas.clear()
        currentCanvas.fill_rect(x, y, width, height)
        currentCanvas.stroke_rect(x, y, width, height)

            
    def drawLine(self, layer, x_start, y_start, x_end, y_end, savePath):
        
        currentCanvas = self.tmpCanvasDict[layer]
        if not savePath:
            currentCanvas.clear()
        currentCanvas.stroke_line(x_start, y_start, x_end, y_end)
    
    def drawArrow(self, layer, x_start, y_start, x_end, y_end,arrowLength, arrowWidth):
        
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.stroke_line(x_start, y_start, x_end, y_end)
        
        x_diff = x_end - x_start
        y_diff = y_end - y_start

        hyp = sqrt(x_diff*x_diff+y_diff*y_diff)

        cos_lineAngle = x_diff/hyp
        sin_lineAngle = y_diff/hyp

        #perpendicular vector
        x_perp = -sin_lineAngle
        y_perp = cos_lineAngle
        
        p1_x = x_end - arrowLength*cos_lineAngle+(arrowWidth/2)*x_perp
        p1_y = y_end - arrowLength*sin_lineAngle+(arrowWidth/2)*y_perp
        
        p2_x = x_end - arrowLength*cos_lineAngle-(arrowWidth/2)*x_perp
        p2_y = y_end - arrowLength*sin_lineAngle-(arrowWidth/2)*y_perp

        currentCanvas.fill_polygon([(x_end, y_end), (p1_x, p1_y), (p2_x, p2_y)])
        currentCanvas.stroke_polygon([(x_end, y_end), (p1_x, p1_y), (p2_x, p2_y)])
        
    
    def drawCircle(self,layer, x, y, radius, savePath):
        
        currentCanvas = self.tmpCanvasDict[layer]
        
        if not savePath:
            currentCanvas.clear()
        currentCanvas.fill_circle(x, y, radius)
        currentCanvas.stroke_circle(x, y, radius)     

            
    def drawParralelLines(self,layer, x_start, y_start, width, height, number, alignment): 
         
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.clear()
        
        
        for i in range(abs(number)):
            if alignment == "vertical":
                x = x_start + i * width/number 
                currentCanvas.stroke_line(x,y_start,x,y_start+height)

            elif alignment == "horizontal":
                y = y_start + i * height/number 
                currentCanvas.stroke_line(x_start,y,x_start+width,y)
                
    def drawParralelArrows(self,layer, x_start, y_start, width, height, number, alignment,arrowLength, arrowWidth): 
         
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.clear()   
        
        for i in range(abs(number)):
            if alignment == "vertical":
                x = x_start+width/(number*2)  + i * width/number 
                self.drawArrow(layer, x,y_start,x,y_start+height,arrowLength, arrowWidth)

            elif alignment == "horizontal":
                y = y_start +  height/(number*2) +i * height/number 
                self.drawArrow(layer, x_start,y,x_start+width,y,arrowLength, arrowWidth)
                    
    def update(self,*args):
        
        with hold_canvas(self.canvas): 
            for layer in args:
                self.cdict[layer].clear()
                self.cdict[layer].draw_image(self.tmpCanvasDict[layer])
                #self.cdict[layer] = self.tmpCanvasDict[layer].copy()
            
            
        
            
            
    def changeLayerLook(self, layer, function, parameter):
        
        currentCanvas = self.tmpCanvasDict[layer]
        
        
        if str(function) == "fillingColor" :
            currentCanvas.fill_style = parameter
        elif str(function) == "lineColor" :
            currentCanvas.stroke_style = parameter
        elif str(function) == "lineWidth" :
            currentCanvas.line_width = parameter
        elif str(function) == "lineDash" :
            currentCanvas.set_line_dash(parameter)
            
        else:
            print("changeLayerLook: no such funktion available")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        