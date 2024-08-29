import pygame
from .gamui_exception import *
from .gamui_functions import *
import time
import threading

#? --- START CLASS BUTTON --- ?#
class Button():
    """
    !<>---| Button class arguments |---<>
    The class Button as 20 arguments:

    
    !1) screen : pygame.surface - [REQUIRED]
    It's the variable that the user must pass to the constructor for 
    display the button on the screen.
    
    !2) x : int - [DEFAULT VALUE]
    It's used for place the button on the axies x.
    
    !3) y : int - [DEFAULT VALUE]
    It's used for place the button on the axies y.
    
    !4) height : int - [DEFAULT VALUE]
    It's used for specify the height of the button.
    
    !5) width : int - [DEFAULT VALUE]
    It's used for specify the width of the button.
    
    !6) text : str - [DEFAULT VALUE]
    It's used for specify the text of the button.
    
    !7) bold : bool - [DEFAULT VALUE]
    It's used for specify the boldness of the text button.
    
    !8) fonttype : str | None - [DEFAULT VALUE]
    It's used for specify the font type of the text button.
    The font type that you can use are the font that are downloaded 
    locally on your machine. 
    Use the method my_font_type() to see what font type you have 
    installed on your machine
    
    !9) fontsize : int - [DEFAULT VALUE]
    It's used for specify the size of the text button.
    
    !10) backgroundcolor : tuple[int, int, int] - [DEFAULT VALUE]
    It's used for specify the background color of the button.
    
    !11) color : tuple[int, int, int] - [DEFAULT VALUE]
    It's used for specify the text color of the button.
    
    !12) justifycontent : string - [DEFAULT VALUE]
    In input recive a string that must be "start", "center" or "end".
    With justifycontent = "center" the item gonna be placed on the center
    of the screen on the x axies.

    !13) alignitems : string - [DEFAULT VALUE]
    In input recive a string that must be "start", "center" or "end".
    With alignitems = "center" the item gonna be placed on the center
    of the screen on the y axies.
    
    !14) border_radius_top_left : int - [DEFAULT VALUE]
    Used for make the border left top of the button radius.
    
    !15) border_radius_top_right : int - [DEFAULT VALUE]
    Used for make the border right top of the button radius.
       
    !16) border_radius_bottom_left : int - [DEFAULT VALUE]
    Used for make the border left bottom of the button radius.
    
    !17) border_radius_bottom_right : int - [DEFAULT VALUE]
    Used for make the border right bottom of the button radius.

    !18) border_radius : int | None - [DEFAULT VALUE]
    Used for make all the border of the button radius.
    
    !19) border_width : int | None - [DEFAULT VALUE]
    Used for make the border with custom width.
    
    !20) border_color : tuple[int, int, int] - [DEFAULT VALUE]
    Used for put a color on the border.
    """
    
    #! --- START CONSTRUCTOR --- !#
    def __init__(self, 
                screen : pygame.surface,
                x : int = 100, 
                y : int = 100,
                height : int = 75, 
                width : int = 150, 
                text : str = 'Press me!',
                bold : bool = False,
                font_type : str | None = None,
                font_size : int = 22,
                background_color : tuple[int, int, int] = (255, 0, 0),
                color : tuple[int, int, int] = (255, 255, 255),
                justify_content : str = "",
                align_items : str = "",
                border_radius_top_left : int = 0,
                border_radius_top_right : int = 0,
                border_radius_bottom_left : int = 0,
                border_radius_bottom_right : int = 0,
                border_radius : int | None = None,
                border_width : int | None = None,
                border_color : tuple[int, int, int] = (0, 0, 0)
                ) -> None:
        #Methods used to set the value that are passed to the constructor
        self.set_screen(screen)
        self.set_pos_x(x)
        self.set_pos_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_text(text)
        self.set_bold(bold)
        self.set_fonttype(font_type)
        self.set_fontsize(font_size)
        self.set_backgroundcolor(background_color)
        self.set_color(color)
        self.set_justifycontent(justify_content)
        self.set_alignitems(align_items)
        self.set_border_radius_top_left(border_radius_top_left)
        self.set_border_radius_top_right(border_radius_top_right)
        self.set_border_radius_bottom_left(border_radius_bottom_left)
        self.set_border_radius_bottom_right(border_radius_bottom_right)
        self.set_border_radius(border_radius)
        self.set_border_width(border_width)
        self.set_border_color(border_color)

        #Other inizialization
        self.animation_height = False
        self.animation_width = False
        self.animation_x = False
        self.animation_y = False

        #Method used to create and display the button on the screen
        self.display_button()
    #! --- END CONSTRUCTOR --- !#


    #! --- START SETTER --- !#
    def set_screen(self, scr : pygame.surface) -> None:
        self.__screen = scr

    def set_pos_x(self, px : int) -> None:
        if type(px) is int or type(px) is float:
            if is_negative_number(px) == False:
                self.__posx = px
            else:
                raise NegativeNumberError("The position on the axies x must be a positive number")
        else:
            raise TypeError("The position on the axies x must be an integer or float")
    
    def set_pos_y(self, py : int) -> None:
        if type(py) is int or type(py) is float:
            if is_negative_number(py) == False:
                self.__posy = py
            else:
                raise NegativeNumberError("The position on the axies x must be a positive number")
        else:
            raise TypeError("The position on the axies y must be an integer or float")

    def set_height(self, h : int) -> None:
        if type(h) is int or type(h) is float:
            if is_negative_number(h) == False:
                self.__height = h
            else:
                raise NegativeNumberError("The height must be a positive number")
        else:
            raise TypeError("The height must be an integer or float")
    
    def set_width(self, w : int) -> None:
        if type(w) is int or type(w) is float:
            if is_negative_number(w) == False:
                self.__width = w
            else:
                raise NegativeNumberError("The width must be a positive number")
        else:
            raise TypeError("The width must be an integer or float")
    
    def set_text(self, t : str) -> None:
        if type(t) is str:
            self.__text = t
        else:
            raise TypeError("The text must be a string")

    def set_bold(self, b : bool) -> None:
        if type(b) is bool:
            self.__bold = b
        else:
            raise TypeError("The boldness must be a boolean")

    def set_fonttype(self, ft : str | None) -> None:
        if type(ft) is str or ft is None:
            self.__fonttype = ft
        else:
            raise TypeError("The font type must be a string or a None type")

    def set_fontsize(self, fs : int) -> None:
        if type(fs) is int or type(fs) is float:
            if is_negative_number(fs) == False:
                self.__fontsize = fs
            else:
                raise NegativeNumberError("The font size must be a positive number")
        else:
            raise TypeError("The font size must be an integer or float")

    def set_backgroundcolor(self, bg : tuple[int, int, int]) -> None:
        if type(bg) is tuple:
            self.__backgroundcolor = bg
        else:
            raise TypeError("The background color must be a tuple of 3 integers from 0 to 255")
    
    def set_color(self, c : tuple[int, int, int]) -> None:
        if type(c) is tuple:
            self.__color = c
        else:
            raise TypeError("The color must be a tuple of 3 integers from 0 to 255")
        
    def set_justifycontent(self, jc : str) -> None:
        if type(jc) is str:
            ljc = jc.lower()

            if ljc == "" or self.check_if_not_custom_pos(ljc) == True:
                self.__justifycontent = ljc
            else:
                raise TypeError("The justify content parameter must be: an empty string, 'start', 'center' or 'end'")
        else:
            raise TypeError("The justify content parameter must be a string")
    
    def set_alignitems(self, ai : str) -> None:
        if type(ai) is str:
            lai = ai.lower()

            if lai == "" or self.check_if_not_custom_pos(lai) == True:
                self.__alignitems = lai
            else:
                raise TypeError("The align items parameter must be: an empty string, 'start', 'center' or 'end'")
        else:
            raise TypeError("The align items parameter must be a string")
    
    def set_border_radius_top_left(self, brtp : int) -> None:
        if type(brtp) is int or type(brtp) is float:
            if is_negative_number(brtp) == False:
                self.__border_radius_top_left = brtp
            else:
                raise NegativeNumberError("The border radius top left must be a positive number")
        else:
            raise TypeError("The border radius top left must be an integer or float")
    
    def set_border_radius_top_right(self, brtr : int) -> None:
        if type(brtr) is int or type(brtr) is float:
            if is_negative_number(brtr) == False:
                self.__border_radius_top_right = brtr
            else:
                raise NegativeNumberError("The border radius top right must be a positive number")
        else:
            raise TypeError("The border radius top right must be an integer or float")
    
    def set_border_radius_bottom_left(self, brbl : int) -> None:
        if type(brbl) is int or type(brbl) is float:
            if is_negative_number(brbl) == False:
                self.__border_radius_bottom_left = brbl
            else:
                raise NegativeNumberError("The border radius bottom left must be a positive number")
        else:
            raise TypeError("The border radius bottom left must be an integer or float")
    
    def set_border_radius_bottom_right(self, brbr : int) -> None:
        if type(brbr) is int or type(brbr) is float:
            if is_negative_number(brbr) == False:
                self.__border_radius_bottom_right = brbr
            else:
                raise NegativeNumberError("The border radius bottom right must be a positive number")
        else:
            raise TypeError("The border radius bottom right must be an integer or float")
    
    def set_border_radius(self, br : int | None) -> None:
        if type(br) is int or type(br) is float or br is None:
            if is_negative_number(br) == False:
                self.__border_radius = br
            else:
                raise NegativeNumberError("The border radius must be a positive number")
        else:
            raise TypeError("The border radius must be an integer, float or None type")
    
    def set_border_width(self, bw : int | None) -> None:
        if type(bw) is int or type(bw) is float or bw is None:
            if is_negative_number(bw) == False:
                self.__border_width = bw
            else:
                raise NegativeNumberError("The border width must be a positive number")
        else:
            raise TypeError("The border width must be an integer, float or None type")
    
    def set_border_color(self, bc : tuple[int, int, int]) -> None:
        if type(bc) is tuple:
            self.__border_color = bc
        else:
            raise TypeError("The border color must be a tuple of 3 integers from 0 to 255")
    #! --- END SETTER --- !#

    
    #! --- START GETTER --- !#
    def get_screen(self) -> pygame.surface:
        return self.__screen
    
    def get_pos_x(self) -> int:
        return self.__posx

    def get_pos_y(self) -> int:
        return self.__posy

    def get_height(self) -> int:
        return self.__height
    
    def get_width(self) -> int:
        return self.__width

    def get_text(self) -> str:
        return self.__text

    def get_bold(self) -> bool:
        return self.__bold

    def get_fonttype(self) -> str | None:
        return self.__fonttype

    def get_fontsize(self) -> int:
        return self.__fontsize

    def get_backgroundcolor(self) -> tuple[int, int, int]:
        return self.__backgroundcolor

    def get_color(self) -> tuple[int, int, int]:
        return self.__color

    def get_justifycontent(self) -> str:
        return self.__justifycontent
    
    def get_alignitems(self) -> str:
        return self.__alignitems
    
    def get_border_radius_top_left(self) -> int:
        return self.__border_radius_top_left
    
    def get_border_radius_top_right(self) -> int:
        return self.__border_radius_top_right
    
    def get_border_radius_bottom_left(self) -> int:
        return self.__border_radius_bottom_left
    
    def get_border_radius_bottom_right(self) -> int:
        return self.__border_radius_bottom_right

    def get_border_radius(self) -> int | None:
        return self.__border_radius

    def get_border_width(self) -> int | None:
        return self.__border_width
    
    def get_border_color(self) -> tuple[int, int, int]:
        return self.__border_color
    #! --- END GETTER --- !#

    
    #! --- START PRIVATE METHOD --- !#    
    #Method used for drawing the rectangle
    def ___draw_rectangle(self, rec : pygame.Rect, bg : tuple, mr : int = 0) -> None:
        try:
            if self.___border_is_radius() == True and self.get_border_width() >= 3:
                more_radius = mr
            else:
                more_radius = 0
        except TypeError:
            more_radius = 0

        #Before drawing the button we check if the user wanna a specific border radius to specific angle or to all angle
        if self.get_border_radius() == None or self.get_border_radius() <= 0:
            #Drawing the button with specified border radius
            pygame.draw.rect(self.get_screen(), 
                            bg,
                            rec,
                            border_top_left_radius = self.get_border_radius_top_left() + more_radius,
                            border_top_right_radius = self.get_border_radius_top_right() + more_radius,
                            border_bottom_left_radius = self.get_border_radius_bottom_left() + more_radius,
                            border_bottom_right_radius = self.get_border_radius_bottom_right() + more_radius
                            )
        else:
            #Drawing the button with all the border radius
            pygame.draw.rect(self.get_screen(), 
                            bg, 
                            rec,
                            border_radius = self.get_border_radius() + more_radius
                            )
    
    #Method for check if there is a need of a border
    def ___check_border_need(self) -> bool:
        if self.get_border_width() != None and self.get_border_width() > 0:
            return True
        else:
            return False
    
    #Method for check if there is a border radius
    def ___border_is_radius(self) -> bool:
        if self.get_border_radius() > 0 or self.get_border_radius_top_left() > 0 or self.get_border_radius_top_right() > 0 or self.get_border_radius_bottom_left() > 0 or self.get_border_radius_top_right() > 0:
            return True
        else:
            return False
    
    #Method used for animate the height of a object
    def __animate_height(self, t : float, ea : int, o : str) -> None:
        #Setting default time for do not decrease the performace of the game
        if t > 0.02:
            t = 0.02

        while self.get_height() != ea:
            self.animation_height = True
            time.sleep(t)
            self.set_height(eval(f"{self.get_height()} {o} {1}"))

        self.animation_height = False

    #Method used for animate the height of a object
    def __animate_width(self, t : float, ea : int, o : str) -> None:
        #Setting default time for do not decrease the performace of the game
        if t > 0.02:
            t = 0.02

        while self.get_width() != ea:
            self.animation_width = True
            time.sleep(t)
            self.set_width(eval(f"{self.get_width()} {o} {1}"))

        self.animation_width = False

    #Method used for animate the axies x of a object
    def __animate_x(self, t : float, ea : int, o : str) -> None:
        #Setting default time for do not decrease the performace of the game
        if t > 0.02:
            t = 0.02

        while self.get_pos_x() != ea:
            self.animation_x = True
            time.sleep(t)
            self.set_pos_x(eval(f"{self.get_pos_x()} {o} {1}"))

        self.animation_x = False

    #Method used for animate the axies y of a object
    def __animate_y(self, t : float, ea : int, o : str) -> None:
        #Setting default time for do not decrease the performace of the game
        if t > 0.02:
            t = 0.02

        while self.get_pos_y() != ea:
            self.animation_y = True
            time.sleep(t)
            self.set_pos_y(eval(f"{self.get_pos_y()} {o} {1}"))

        self.animation_y = False
    
    #Method used for see if the use insert wrong data for animation
    def __error_check_animation(self, rd : int, op: str, d : int) -> bool:
        if rd > d and op == "-":
            return True
        elif rd < d and op == "+":
            return True
        
        return False
    #! --- END PRIVATE METHOD --- !#

    
    #! --- START PUBLIC METHOD --- !#
    def check_if_not_custom_pos(self, placing : str) -> bool:
        """
        Method used for checking if the not custom position is setted.

        The parameters that the method need are:
        1) placing = 'start', 'center' or 'end'

        The method is gonna return True if 'start', 'center' or 'end' are
        setted and False if is passed an empty string or basically if the 
        parameters justify_content or align_items are not setted.
        """
        
        position = ["start", "center", "end"]

        if(placing not in position):
            return False
        else:
            return True
    
    def set_not_custom_position(self, item : str, axies : str) -> None:
        """
        Method used for placing the items in a not custom position that the user want to display in the screen.

        The parameters that the method need are:
        1) item = 'start', 'center' or 'end'
        2) axies = 'x' or 'y'

        Basically the method gonna set on the axies x or y the correct number for place the object
        on the start, center or end of the screen in base of the axies that has been passed to the
        method.
        """
        SCREEN_WIDTH = self.get_screen().get_width()
        SCREEN_HEIGHT = self.get_screen().get_height()
        #After the plus if the conditions return true the coordinate gonna be calculated in base of the border
        ITEM_WIDTH = self.get_width() + ((self.get_border_width() * 2) if self.___check_border_need() == True else 0)
        ITEM_HEIGHT = self.get_height() + ((self.get_border_width() * 2) if self.___check_border_need() == True else 0)
        pos_x = 0
        pos_y = 0

        #Setting the coordinate to the x axies
        if(item == "start" and axies == "x"):
            pos_x = 0
            self.set_pos_x(pos_x)

        if(item == "center" and axies == "x"):
            pos_x = (SCREEN_WIDTH / 2) - (ITEM_WIDTH / 2)
            self.set_pos_x(pos_x)
        
        if(item == "end" and axies == "x"):
            pos_x = SCREEN_WIDTH - ITEM_WIDTH
            self.set_pos_x(pos_x)
        
        #Setting the coordinate to the y axies
        if(item == "start" and axies == "y"):
            pos_y = 0
            self.set_pos_y(pos_y)

        if(item == "center" and axies == "y"):
            pos_y = (SCREEN_HEIGHT / 2) - (ITEM_HEIGHT / 2)
            self.set_pos_y(pos_y)
        
        if(item == "end" and axies == "y"):
            pos_y = SCREEN_HEIGHT - ITEM_HEIGHT
            self.set_pos_y(pos_y)

    def my_font_type(self) -> None:
        """
        Method used for see the font type installed on your machine.
        """
        system_fonts = pygame.font.get_fonts()

        for font in system_fonts:
            print("Font name: " + font)
    
    def display_button(self) -> None:
        """
        Method used for create the shape of the button and display it on the screen.
        """
        #Checking if the items have a custom placing or no
        if(self.check_if_not_custom_pos(self.get_justifycontent()) == True):
            self.set_not_custom_position(self.get_justifycontent(), "x")

        if(self.check_if_not_custom_pos(self.get_alignitems()) == True):
            self.set_not_custom_position(self.get_alignitems(), "y")

        #Check if we need a border, if we need we gonna place the rectangle at the center
        #in base at the border width
        if self.___check_border_need() == True:
            px_rectangle = self.get_pos_x() + self.get_border_width()
            py_rectangle = self.get_pos_y() + self.get_border_width()
        else:
            px_rectangle = self.get_pos_x()
            py_rectangle = self.get_pos_y()

        #Creation of the rectangle
        self.rectangle = pygame.Rect(px_rectangle, py_rectangle, self.get_width(), self.get_height())

        #Creating a custom border if we need
        if self.___check_border_need() == True:
            self.custom_border = pygame.Rect(self.get_pos_x(), 
                                            self.get_pos_y(), 
                                            self.get_width() + (self.get_border_width() * 2), 
                                            self.get_height() + (self.get_border_width() * 2)
                                            )
        
        #Definition of the font button
        font = pygame.font.SysFont(self.get_fonttype(), self.get_fontsize(), self.get_bold())

        #Creation of the text button
        self.text_surface = font.render(self.get_text(), True, self.get_color())

        #Placing the text on the center of the button
        self.text_rectangle = self.text_surface.get_rect(center = self.rectangle.center)

        #Drawing the border if we need
        if self.___check_border_need() == True:
            self.___draw_rectangle(self.custom_border, self.get_border_color(), 3)

        #Drawing the button
        self.___draw_rectangle(self.rectangle, self.get_backgroundcolor())

        #Displaying the button
        self.get_screen().blit(self.text_surface, self.text_rectangle)
    
    def is_clicked(self, event : pygame.event) -> bool:
        """
        Method used for checking if the button was cliccked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                return True
            
        return False
    
    def is_hover(self) -> bool:
        """
        Method used for checking if the cursor of the mouse is hover the button.
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.rectangle.collidepoint(mouse_pos):
            return True
        
        return False

    def start_animation(self, what_animate : str, time : float, max_reach : int, operation : str) -> None:
        """
        Method used for start an animation for animate the:
        1) axies x
        2) axies y
        3) width
        4) height

        The parameters that the method need are:
        1) what_animate = a string that has to be 'x', 'y', 'height' or 'width' (used for specify what we wanna animate of the object)
        2) time = below or equal to 0.02 (in how may seconds the animation have to finish)
        3) max_reach = an integer (the final number that we wanna reach for the animation)
        4) operation = a string that has to be '+' or '-' (if is set with the string '+' the animation gonna increase otherwise with the string '-' the animation gonna decrease)
        """
        #Height animation
        if what_animate.lower() == "height" and not self.animation_height:
            if self.__error_check_animation(max_reach, operation, self.get_height()) == False:
                animation = threading.Thread(target = self.__animate_height, args = (time, max_reach, operation))
                animation.start()
            else:
                raise ConstraintHeightError("The height that you wanna try to animate is lower or higer than the original height that you put on your object, please insert valid parameters")

        #Width animation
        if what_animate.lower() == "width" and not self.animation_width:
            if self.__error_check_animation(max_reach, operation, self.get_width()) == False:
                animation = threading.Thread(target = self.__animate_width, args = (time, max_reach, operation))
                animation.start()
            else:
                raise ConstraintWidthError("The width that you wanna try to animate is lower or higer than the original width that you put on your object, please insert valid parameters")
        
        #X animation
        if what_animate.lower() == "x" and not self.animation_x:
            if self.__error_check_animation(max_reach, operation, self.get_pos_x()) == False:
                animation = threading.Thread(target = self.__animate_x, args = (time, max_reach, operation))
                animation.start()
            else:
                raise ConstraintAxiesXError("The axies x that you wanna try to animate is lower or higer than the original axies x that you put on your object, please insert valid parameters")

        #Y animation
        if what_animate.lower() == "y" and not self.animation_y:
            if self.__error_check_animation(max_reach, operation, self.get_pos_y()) == False:
                animation = threading.Thread(target = self.__animate_y, args = (time, max_reach, operation))
                animation.start()
            else:
                raise ConstraintAxiesYError("The axies y that you wanna try to animate is lower or higer than the original axies y that you put on your object, please insert valid parameters")

    #! --- END PUBLIC METHOD --- !#
#? --- END CLASS BUTTON --- ?#


#? --- START CLASS IMAGE -- ?#
class Image(Button):
    """
    !<>---| Image class arguments |---<>
    The class Image as 8 arguments:

    !1) screen - [REQUIRED]
    It's the variable that the user must pass to the constructor for 
    display the image on the screen.
    
    !2) path : string - [REQUIRED]
    It's the path where you have the image that you want to display on the
    screen.
    
    !3) x : int - [DEFAULT VALUE]
    It's used for place the image on the axies x.
    
    !4) y : int - [DEFAULT VALUE]
    It's used for place the image on the axies y.
    
    !5) height : int - [DEFAULT VALUE]
    It's used for specify the height of the image.
    
    !6) width : int - [DEFAULT VALUE]
    It's used for specify the width of the image.
    
    !7) justifycontent : string - [DEFAULT VALUE]
    In input recive a string that must be "start", "center" or "end".
    With justifycontent = "center" the item gonna be placed on the center
    of the screen on the x axies.
    
    !8) alignitems : string - [DEFAULT VALUE]
    In input recive a string that must be "start", "center" or "end".
    With alignitems = "center" the item gonna be placed on the center
    of the screen on the y axies.
    """

    #! --- START CONSTRUCTOR --- !#
    def __init__(self, 
                screen : pygame.surface,
                path : str,
                x : int = 100, 
                y : int = 100,
                height : int = 0, 
                width : int = 0,
                justify_content : str = "",
                align_items : str = ""
                ):
        #Passing to the father the parameters that we can use by the ereditation
        super().__init__(screen = screen,
                        x = x,
                        y = y,
                        height = height,
                        width = width,
                        justify_content = justify_content,
                        align_items = align_items
                        )
        
        #Methods used to set the value that are passed to the constructor
        self.set_image(path)

        #Method used to create and display the image on the screen
        self.display_image()
    #! --- END CONSTRUCTOR --- !#


    #! --- START SETTER --- !#
    def set_image(self, pth : str) -> None:
        if type(pth) is str:
            self.__image = pygame.image.load(pth)
        else:
            raise TypeError("The image path parameter must be a string")
    #! --- END SETTER --- !#


    #! --- START GETTER --- !#
    def get_image(self) -> pygame.image:
        return self.__image
    #! --- END GETTER --- !#


    #! --- START PUBLIC METHOD --- !#
    def display_image(self) -> None:
        """
        Method used for display the image on the screen.
        """
        #Checking if the items have a custom placing or no
        if(super().check_if_not_custom_pos(super().get_justifycontent()) == True):
            super().set_not_custom_position(super().get_justifycontent(), "x")

        if(super().check_if_not_custom_pos(super().get_alignitems()) == True):
            super().set_not_custom_position(super().get_alignitems(), "y")

        #Resizing the image
        if(super().get_width() != 0 and super().get_height() != 0):
            self.res_img = pygame.transform.scale(self.get_image(), (super().get_width(), super().get_height()))
        else:
            self.res_img = self.get_image()

            #Getting the height and the width of the image
            image_width, image_height = self.get_image().get_size()

            #Setting the height and the width of the image
            super().set_height(image_width)
            super().set_width(image_height)

        #Display the image on the screen
        super().get_screen().blit(self.res_img, (super().get_pos_x(), super().get_pos_y()))

        #Updating the screen for display the image
        pygame.display.update()
    
    def get_collision_image(self, x : int, y : int) -> bool:
        """
        Method used for detect collision on the image.
        """
        start_x, end_x = super().get_pos_x(), super().get_pos_x() + super().get_width()
        start_y, end_y = super().get_pos_y(), super().get_pos_y() + super().get_height()

        if start_x <= x <= end_x and start_y <= y <= end_y:
            return True
        
        return False
    
    def is_clicked(self, event : pygame.event) -> bool:
        """
        Method used for checking if the image was clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if self.get_collision_image(x, y):
                return True
            
        return False
    
    def is_hover(self) -> bool:
        """
        Method used for checking if the mouse cursor is hover the image.
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.get_collision_image(mouse_pos[0], mouse_pos[1]):
            return True
        
        return False
    #! --- END PUBLIC METHOD --- !#
#? --- END CLASS IMAGE --- ?#