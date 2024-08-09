import pygame
from .gamui_exception import *
import time
import threading

#? --- START CLASS BUTTON --- ?#
class Button():
    """
    !<>---| Button class arguments |---<>
    The class Button as 20 arguments:

    !1) screen
    It's the variable that the user must pass to the constructor for 
    display the button on the screen.
    
    !2) x : int
    It's used for place the button on the axies x.
    
    !3) y : int
    It's used for place the button on the axies x.
    
    !4) height : int
    It's used for specify the height of the button.
    
    !5) width : int
    It's used for specify the width of the button.
    
    !6) text : str
    It's used for specify the text of the button.
    
    !7) bold : bool
    It's used for specify the boldness of the text button.
    
    !8) fonttype : str | None
    It's used for specify the font type of the text button.
    The font type that you can use are the font that are downloaded 
    locally on your machine. 
    Use the method my_font_type() to see what font type you have 
    installed on your machine
    
    !9) fontsize : int
    It's used for specify the size of the text button.
    
    !10) backgroundcolor : tuple
    It's used for specify the background color of the button.
    
    !11) color : tuple
    It's used for specify the text color of the button.
    
    !12) justifycontent : string
    In input recive a string that must be "start", "center" or "end".
    With justifycontent = "center" the item gonna be placed on the center
    of the screen on the x axies.

    !13) alignitems : string
    In input recive a string that must be "start", "center" or "end".
    With alignitems = "center" the item gonna be placed on the center
    of the screen on the y axies.
    
    !14) border_radius_top_left : int
    Used for make the border left top of the button radius.
    
    !15) border_radius_top_right : int
    Used for make the border right top of the button radius.
       
    !16) border_radius_bottom_left : int
    Used for make the border left bottom of the button radius.
    
    !17) border_radius_bottom_right : int
    Used for make the border right bottom of the button radius.

    !18) border_radius : int | None
    Used for make all the border of the button radius.
    
    !19) border_width : int | None
    Used for make the border with custom width.
    
    !20) border_color : tuple
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
                background_color : tuple = (255, 0, 0),
                color : tuple = (255, 255, 255),
                justify_content : str = "",
                align_items : str = "",
                border_radius_top_left : int = 0,
                border_radius_top_right : int = 0,
                border_radius_bottom_left : int = 0,
                border_radius_bottom_right : int = 0,
                border_radius : int | None = None,
                border_width : int | None = None,
                border_color : tuple = (0, 0, 0)
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
        self.display()
    #! --- END CONSTRUCTOR --- !#


    #! --- START SETTER --- !#
    def set_screen(self, scr : pygame.surface) -> None:
        self.__screen = scr

    def set_pos_x(self, px : int) -> None:
        self.__posx = px
    
    def set_pos_y(self, py : int) -> None:
        self.__posy = py

    def set_height(self, h : int) -> None:
        self.__height = h
    
    def set_width(self, w : int) -> None:
        self.__width = w
    
    def set_text(self, t : str) -> None:
        self.__text = t

    def set_bold(self, b : bool) -> None:
        self.__bold = b

    def set_fonttype(self, ft : str | None) -> None:
        self.__fonttype = ft

    def set_fontsize(self, fs : int) -> None:
        self.__fontsize = fs

    def set_backgroundcolor(self, bg : tuple) -> None:
        self.__backgroundcolor = bg
    
    def set_color(self, c : tuple) -> None:
        self.__color = c

    def set_justifycontent(self, jc : str) -> None:
        self.__justifycontent = jc.lower()
    
    def set_alignitems(self, ai : str) -> None:
        self.__alignitems = ai.lower()
    
    def set_border_radius_top_left(self, brtp : int) -> None:
        self.__border_radius_top_left = brtp
    
    def set_border_radius_top_right(self, brtr : int) -> None:
        self.__border_radius_top_right = brtr
    
    def set_border_radius_bottom_left(self, brbl : int) -> None:
        self.__border_radius_bottom_left = brbl
    
    def set_border_radius_bottom_right(self, brbr : int) -> None:
        self.__border_radius_bottom_right = brbr
    
    def set_border_radius(self, br : int) -> None:
        self.__border_radius = br
    
    def set_border_width(self, bw : int) -> None:
        self.__border_width = bw
    
    def set_border_color(self, bc : tuple) -> None:
        self.__border_color = bc
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

    def get_backgroundcolor(self) -> tuple:
        return self.__backgroundcolor

    def get_color(self) -> tuple:
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
    
    def get_border_color(self) -> tuple:
        return self.__border_color
    #! --- END GETTER --- !#

    
    #! --- START PRIVATE METHOD --- !#
    #Method used for checking if the not custom position is setted
    def check_if_not_custom_pos(self, placing : str) -> bool:
        position = ["start", "center", "end"]

        if(placing not in position):
            return False
        else:
            return True
    
    #Placing the items in the not custom position that the user want to display in the screen
    def set_not_custom_position(self, item : str, axies : str) -> None:
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
    #Method used for see the font type installed on your machine
    def my_font_type(self) -> None:
        system_fonts = pygame.font.get_fonts()

        for font in system_fonts:
            print("Font name: " + font)
    
    #Method used for create the shape of the button
    def display(self) -> None:
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
    
    #Method used for checking if the button was cliccked
    def is_clicked(self, event : pygame.event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                return True
            
        return False
    
    #Method used for checking if the cursor is hover the button
    def is_hover(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        if self.rectangle.collidepoint(mouse_pos):
            return True
        
        return False

    #Method used for start the animation
    def start_animation(self, what_animate : str, time : float, max_reach : int, operation : str) -> None:
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

    !1) screen
    It's the variable that the user must pass to the constructor for 
    display the image on the screen.
    
    !2) path : string
    It's the path where you have the image that you want to display on the
    screen.
    
    !3) x : int
    It's used for place the image on the axies x.
    
    !4) y : int
    It's used for place the image on the axies y.
    
    !5) height : int
    It's used for specify the height of the image.
    
    !6) width : int
    It's used for specify the width of the image.
    
    !7) justifycontent : string
    In input recive a string that must be "start", "center" or "end".
    With justifycontent = "center" the item gonna be placed on the center
    of the screen on the x axies.
    
    !8) alignitems : string
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
        self.__image = pygame.image.load(pth)
    #! --- END SETTER --- !#


    #! --- START GETTER --- !#
    def get_image(self) -> pygame.image:
        return self.__image
    #! --- END GETTER --- !#


    #! --- START PUBLIC METHOD --- !#
    #Method used for display the image on the screen
    def display_image(self) -> None:
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
    
    #Method used for detect collision on the image
    def get_collision_image(self, x : int, y : int) -> bool:
        start_x, end_x = super().get_pos_x(), super().get_pos_x() + super().get_width()
        start_y, end_y = super().get_pos_y(), super().get_pos_y() + super().get_height()

        if start_x <= x <= end_x and start_y <= y <= end_y:
            return True
        
        return False
    
    #Method used for checking if the image was clicked
    def is_clicked(self, event : pygame.event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if self.get_collision_image(x, y):
                return True
            
        return False
    
    #Method used for checking if the image is hover the button
    def is_hover(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        if self.get_collision_image(mouse_pos[0], mouse_pos[1]):
            return True
        
        return False
    #! --- END PUBLIC METHOD --- !#
#? --- END CLASS IMAGE --- ?#
