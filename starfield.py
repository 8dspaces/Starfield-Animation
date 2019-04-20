#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:00:15 2019

@author: bikash
"""

import numpy as np

class StarField():
    def __init__(self, canvas, width, height, nstar=60, message=None):
        self.STAR_SIZE = 2
        self.N_STAR = 100
        self.DEPTH = [0.1, 0.3, 0.6, 0.9] #how far we are from the screen
        self.WIDTH = width
        self.HEIGHT = height
        self.COLORS = ["white", "yellow", "red", "grey"]
        self.canvas = canvas
     
    @staticmethod    
    def create_circle(canvasName, x, y, r, color): #center coordinates, radius 
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=color)

    def init_stars(self):
        """ Create the starfield """
        self.stars = []
        for i in range(self.N_STAR):
            # A star is represented as a list with this format: [X,Y,Z]
            star = [np.random.randint(0, self.WIDTH), \
                    np.random.randint(0, self.HEIGHT), \
                    np.random.choice(self.DEPTH)]
            self.stars.append(star)

    
    def draw_stars(self):
        for i, star in enumerate(self.stars):
            starColor = self.COLORS[self.DEPTH.index(star[2])] #pick color wrto distance 
            StarField.create_circle(self.canvas, star[0], star[1], \
                                    self.STAR_SIZE, starColor)
            
    def animate_stars(self, color=None):
        for i, star in enumerate(self.stars):
            starColor = self.COLORS[self.DEPTH.index(star[2])]
            star_size = self.STAR_SIZE*(1-star[2]) #reduce size with distance
            StarField.create_circle(self.canvas, star[0], star[1], \
                                    star_size, starColor)
            #motion of star increasing with depth to simulate parallax effect
            self.stars[i][1] += self.stars[i][2]
            
            if self.stars[i][1] >= self.HEIGHT:
            #reset coordinates if we exceed height
                self.stars[i][1] = 0
                self.stars[i][0] = np.random.randint(0, self.HEIGHT)
                self.stars[i][2] = np.random.choice(self.DEPTH)

    def run_all(self, canvas=None):
        np.random.seed()
        StarField.init_stars(self)
        while True:
            StarField.animate_stars(self, color='black')
            self.canvas.update()
        
        

import tkinter as tk
from tkinter import *

root = Tk()
background = Canvas(root, width=300, height=300, background='black')
background.pack()
star_begin = StarField(canvas=background, width=300, height=300)
star_begin.run_all()

root.mainloop()
        
