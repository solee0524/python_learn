#!/usr/bin/python
__author__ = 'oracle'


#
#    sg_welcome.py
#
#

"""
This builds something similar to the CodeSkulptor welcome screen at
  http://www.codeskulptor.org/  except I added a second button to toggle
  between the two messages

Key things to learn: our first use of the Canvas widget, and note how awkward it
  is to render text to the canvas.
"""

# import simplegui

from Tkinter import *   # works in V2.7.3 with change to Tkinter
root = Tk()

root.title("Welcome")
root.geometry("500x300")  # 500 x 300 pixel window with no offset

helv30 = ('Helvetica', 30)  #  font for printing text to canvas.  Helvetica
                            #   is supposedly a 'safe' font ... see the next
                            #   few lines

"""
   'Tk 8.0 automatically maps Courier, Helvetica, and Times to their
   corresponding native family names on all platforms. In addition, a font
   specification can never fail under Tk 8.0; if Tk cannot come up with an
   exact match, it tries to find a similar font. If that fails, Tk falls
   back to a platform-specific default font. Tk's idea of what is
   "similar enough" probably doesn't correspond to your own view, so you
   shouldn't rely too much on this feature.'  ... from
   http://www.pythonware.com/library/tkinter/introduction/x444-fonts.htm
"""
message = "Welcome!"
message2 = "Good Job!"

frame1 = Frame(root)
frame1.grid(row = 0, column = 0)

"""
 OK, a new widget of type Canvas, named 'first_canvas' by me (usually you'll
   see it called 'canvas' but I thought it might be confusing to give the
   variable the same name as the widget Canvas, so I changed it(.  So the
   Frame (frame1) and the Canvas (first_canvas) are two separate areas inside
   the window 'root'.  We can draw, display images and print on the Canvas.

"""
first_canvas = Canvas(root,width=300, height=200, bg='black')
first_canvas.grid(row = 0, column = 1)   # change to column = 0 and it will cover
                                   #  frame1 and the buttons.
                                   # change to row = 1, column = 0 and it is
                                   #   placed under the buttons in the same col
                                   #
                                   #  put this in column 0 and frame1 in
                                   #   column 1 and see what happens


# Handler for mouse click on a button
#
def click():
    global t_message
    """
    this is how we hide or display the messages, by
    changing their states
    """
    first_canvas.itemconfig(t_message, state = 'hidden')
    t_message = first_canvas.create_text(150,100, text = message2, fill = 'blue', font = helv30 )

#  I added this 2nd button so you could toggle the text
#
def reset():
    global t_message
    """ reverses the states and hence the display """
    first_canvas.itemconfig(t_message, state = 'hidden')
    t_message = first_canvas.create_text(150,100, text = message, fill = 'red', font = helv30)


# Handler to draw on canvas
#def draw(canvas):
#    canvas.draw_text(message, [50,112], 48, "Red")

"""
tkinter doesn't let you change text on the canvas by changing a variable,
  like simplegui did.  At least as far as I understood it (maybe I missed
  something, because their method seems very awkward).

Instead, you create a text object with first_canvas.create_text and then you change
  its state from 'normal' (the default) to 'hidden'.

So I had to make a message 'hidden' and then rewrite the create_text object to
   get this to work like the simplegui welcome screen.

So here's a detailed explaination of the line of code defining the text:

t_message = first_canvas.create_text(150,100, text = message, fill = 'red', font = helv30 )

  t_message is the variable name I used for this text message
  first_canvas is the name of the Canvas widget, create_text is the command
    to create text (tricky, huh?)
  150,100 is where it is placed, centered at this location.  Simplegui aligns
    lower-left, note.
  text = message defines the text (here, the variable 'message')
  fill is the color of the text, font is obvious
  activefill is the color the text changes to on a mouse-over (try it)

  there's a 'anchor' option that aligns the text to the assigned x-y coordinates.
    for example, adding anchor = 'sw' aligns the lower-left of the text at
    150,100 in this example

Only 14 options for this command instead of the usual 36 :)
  http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_text-method

"""
t_message = first_canvas.create_text(150, 100, text = message, fill = 'red', font = helv30)

#t_message = first_canvas.create_text(150,100, text = message, fill = 'red', \
# font = helv30, activefill = "green", anchor = 'sw' )


# Create a frame and assign callbacks to event handlers
#frame = simplegui.create_frame("Home", 300, 200)
#frame.add_button("Click me", click)

click_button = Button(frame1, text = "Click me", command = click, width=20)
click_button.grid(row = 0, column = 0, padx = 15, pady = 2)

reset_button = Button(frame1, text = "Reset Text", command = reset, width=20)
reset_button.grid(row = 2, column = 0, padx = 15, pady = 2)

#frame.set_draw_handler(draw)

# Start the frame animation
# frame.start()

mainloop()