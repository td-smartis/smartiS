from AUserInterface import *
from ipycanvas import MultiCanvas, Canvas, hold_canvas
from math import pi, sin, cos, atan, sqrt
from Colors import Color
 
class Chart(AUserInterface):
        
    def resize(self,scale):
        for i in self.canvas:
            print(i)
            i.scale(scale)
            print(i)
        for i in self.tmpCanvas:
            display(i)
            i.scale(scale)
            display(i)
        
                
    def __init__(self, layers, width, height):
        
        """ Initialisiert die smartiS-Instanz.
        
        layers <list (string)>: Liste mit Bezeichnungen der Canvas/Ebenen
                     width <int>: Breite des Canvas
                    height <int>: Höhe des Canvas
        """
        
        self.canvas = MultiCanvas(len(layers), width=width, height=height)
        self.tmpCanvas = MultiCanvas(len(layers), width=width, height=height)
        self.canvasDict = {}
        self.tmpCanvasDict = {}
        for i in range(len(layers)):
            self.canvasDict[layers[i]] = self.canvas[i]
            self.tmpCanvasDict[layers[i]] = self.tmpCanvas[i]
        #self.resize()

        
    
    def getChart(self):
        return self.canvas
     
    
    def clearLayer(self, layer):
        self.tmpCanvasDict[layer].clear()
        
                            
    def update(self,*args):
        
        with hold_canvas(self.canvas): 
            for layer in args:
                self.canvasDict[layer].clear()
                self.canvasDict[layer].draw_image(self.tmpCanvasDict[layer])
                #self.canvasDict[layer] = self.tmpCanvasDict[layer].copy()     
            
        
            
            
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
        elif str(function) == "transparency" :    
            currentCanvas.global_alpha = parameter
        else:
            print("changeLayerLook: no such funktion available")
    
    def drawRectangle(self,layer, x, y, width, height,fill = True):
        
        currentCanvas = self.tmpCanvasDict[layer]
        if fill:
            currentCanvas.fill_rect(x, y, width, height)
        currentCanvas.stroke_rect(x, y, width, height)
        
    def drawCircle(self,layer, x, y, radius,fill = True):
        
        currentCanvas = self.tmpCanvasDict[layer]
        if fill:            
            currentCanvas.fill_circle(x, y, radius)
        currentCanvas.stroke_circle(x, y, radius)    

            
    def drawLine(self, layer, x_start, y_start, x_end, y_end):
        
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.stroke_line(x_start, y_start, x_end, y_end)
    #new    
    def drawLines(self, layer, points):
        
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.stroke_lines(points)
    
    def drawArrow(self, layer, x_start, y_start, x_end, y_end, arrowLength, arrowWidth):
        
        currentCanvas = self.tmpCanvasDict[layer]
        
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
        
        x_line_end = x_end - arrowLength*cos_lineAngle
        y_line_end = y_end - arrowLength*sin_lineAngle
        
        currentCanvas.stroke_line(x_start, y_start, x_line_end, y_line_end)

        currentCanvas.fill_polygon([(x_end, y_end), (p1_x, p1_y), (p2_x, p2_y)])
        #currentCanvas.stroke_polygon([(x_end, y_end), (p1_x, p1_y), (p2_x, p2_y)])
        
    
 

            
    def drawParallelLines(self,layer, x_start, y_start, width, height, number, alignment): 
         
        currentCanvas = self.tmpCanvasDict[layer]        
        
        for i in range(abs(number)):
            if alignment == "vertical":
                x = x_start+width/(number*2)  + i * width/number
                currentCanvas.stroke_line(x,y_start,x,y_start+height)

            elif alignment == "horizontal":
                y = y_start +  height/(number*2) +i * height/number  
                currentCanvas.stroke_line(x_start,y,x_start+width,y)
                
            elif alignment == "diagonal":
                distance = (width+height)/number
                x = x_start+distance/2+i*distance           
                
                if x <= x_start + width:
                    y = y_start
                    x_end = x-height
                    if x_end>x_start:
                        y_end = y_start+height
                    else:
                        x_end = x_start
                        y_end = y_start+distance/2+i*distance
                    
                else:
                    x_oversized = x_start+distance/2+i*distance  
                    x = x_start+width
                    y = (x_oversized-x_start-width)+y_start
                    x_end = x_oversized-height
                    if x_end>x_start:
                        y_end = y_start+height
                    else:
                        x_end = x_start
                        y_end = y_start+distance/2+i*distance
                        
                currentCanvas.stroke_line(x,y,x_end,y_end)
                
    def drawParallelArrows(self,layer, x_start, y_start, width, height, number, alignment, arrowLength, arrowWidth): 
         
        currentCanvas = self.tmpCanvasDict[layer]
        #currentCanvas.clear()   
        
        for i in range(abs(number)):
            if alignment == "vertical":
                x = x_start+width/(number*2)  + i * width/number 
                self.drawArrow(layer, x,y_start,x,y_start+height,arrowLength, arrowWidth)

            elif alignment == "horizontal":
                y = y_start +  height/(number*2) +i * height/number 
                self.drawArrow(layer, x_start,y,x_start+width,y,arrowLength, arrowWidth)

    def drawElectron(self, layer,x, y, radius):
    
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.fill_style = Color.ELECTRON.value
        currentCanvas.stroke_style = Color.ELECTRON.value
        currentCanvas.line_width = abs(radius/3)
        currentCanvas.fill_circle(x, y, radius)
        #currentCanvas.stroke_circle(x, y, radius)  
        currentCanvas.stroke_style = Color.BACKGND.value
        currentCanvas.stroke_line(x-abs(radius/2), y, x+abs(radius/2), y)
        
    def drawProton(self,layer, x, y, radius):
    
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.fill_style = Color.PROTON.value
        currentCanvas.stroke_style = Color.PROTON.value
        currentCanvas.line_width = abs(radius/3)
        currentCanvas.fill_circle(x, y, radius)
        #currentCanvas.stroke_circle(x, y, radius)  
        currentCanvas.stroke_style = Color.BACKGND.value
        currentCanvas.stroke_line(x-abs(radius/2), y, x+abs(radius/2), y)
        currentCanvas.stroke_line(x, y-abs(radius/2), x, y+abs(radius/2))
    
    def drawText(self,layer,x,y,font,text,align = "start"):
        
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.font = str(font)
        currentCanvas.text_align = align
        currentCanvas.fill_text(text, x, y)  
            
    def drawPolygon(self, layer, *args):
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.fill_polygon([list(args)])
        currentCanvas.stroke_polygon([list(args)])

            
    def getImage(self,layer):
        image = self.canvasDict[layer]
        return image
            
    def drawImage(self,layer,image,x,y):
        currentCanvas = self.tmpCanvasDict[layer]
        currentCanvas.draw_image(image, x, y)
    
    #ohne Update (notwendig bei bildern nicht aus canvas
    def drawImageDirect(self,layer,image,x,y):
        currentCanvas = self.canvasDict[layer]
        currentCanvas.draw_image(image, x, y)
            
            
    def enableInteraction(self,function):
        from ipywidgets import Output
        out = Output()
        
        @out.capture()        
        def handle_interaction(x, y):
            function(x, y)

        self.canvas[-1].on_mouse_down(handle_interaction)
        display(out)
            
            
            
            
            
            
        
        