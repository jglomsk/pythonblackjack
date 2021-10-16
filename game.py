#imports
import tkinter
from tkinter import messagebox
import random
from PIL import Image, ImageTk

#client class for multitime variable usage
class Client:
    #start it up with this
    def __init__(self, master):
        self.master = master
        master.title("Blackjack")
        #card value totals
        self.dealertext = tkinter.StringVar()
        self.playertext = tkinter.StringVar()
        #image placement
        self.dealerx = 0
        self.dealery = 0
        self.playerx = 0
        self.playery = 0
        #hands for each
        self.playerhand = []
        self.dealerhand = []
        #integer values for each
        self.dealer = 0
        self.player = 0
        #determines where we are in deck
        self.drawn = 0
        #boring images won't stay or leave unless I do this
        self.img1 = None
        self.reimg1 = None
        self.newimg1 = None
        self.img2 = None
        self.reimg2 = None
        self.newimg2 = None
        self.img3 = None
        self.reimg3 = None
        self.newimg3 = None
        self.img4 = None
        self.reimg4 = None
        self.newimg4 = None
        self.img5 = None
        self.reimg5 = None
        self.newimg5 = None
        self.img6 = None
        self.reimg6 = None
        self.newimg6 = None
        self.img7 = None
        self.reimg7 = None
        self.newimg7 = None
        self.img8 = None
        self.reimg8 = None
        self.newimg8 = None
        self.img9 = None
        self.reimg9 = None
        self.newimg9 = None
        self.img10 = None
        self.reimg10 = None
        self.newimg10 = None
        self.img11 = None
        self.reimg11 = None
        self.newimg11 = None
        self.img12 = None
        self.reimg12 = None
        self.newimg12 = None
        self.img13 = None
        self.reimg13 = None
        self.newimg13 = None
        self.img14 = None
        self.reimg14 = None
        self.newimg14 = None
        self.img15 = None
        self.reimg15 = None
        self.newimg15 = None
        self.img16 = None
        self.reimg16 = None
        self.newimg16 = None
        self.img17 = None
        self.reimg17 = None
        self.newimg17 = None
        self.img18 = None
        self.reimg18 = None
        self.newimg18 = None
        self.img19 = None
        self.reimg19 = None
        self.newimg19 = None
        self.img20 = None
        self.reimg20 = None
        self.newimg20 = None
        self.img21 = None
        self.reimg21 = None
        self.newimg21 = None
        self.img22 = None
        self.reimg22 = None
        self.newimg22 = None
        #canvasi
        self.dealercanvas = tkinter.Canvas(master, width = 160, height = 150, bg='blue')
        self.playercanvas = tkinter.Canvas(master, width = 160, height = 150, bg='green')
        #each card is a list
        self.a_club = [11, "Faces/Playing_card_club_A.png"]
        self.a_diamond = [11, "Faces/Playing_card_diamond_A.png"]
        self.a_heart = [11, "Faces/Playing_card_heart_A.png"]
        self.a_spade = [11, "Faces/Playing_card_spade_A.png"]
        self.two_club = [2, "Faces/Playing_card_club_2.png"]
        self.two_diamond = [2, "Faces/Playing_card_diamond_2.png"]
        self.two_heart = [2, "Faces/Playing_card_heart_2.png"]
        self.two_spade = [2, "Faces/Playing_card_spade_2.png"]
        self.three_club = [3, "Faces/Playing_card_club_3.png"]
        self.three_diamond = [3, "Faces/Playing_card_diamond_3.png"]
        self.three_heart = [3, "Faces/Playing_card_heart_3.png"]
        self.three_spade = [3, "Faces/Playing_card_spade_3.png"]
        self.four_club = [4, "Faces/Playing_card_club_4.png"]
        self.four_diamond = [4, "Faces/Playing_card_diamond_4.png"]
        self.four_heart = [4, "Faces/Playing_card_heart_4.png"]
        self.four_spade = [4, "Faces/Playing_card_spade_4.png"]
        self.five_club = [5, "Faces/Playing_card_club_5.png"]
        self.five_diamond = [5, "Faces/Playing_card_club_5.png"]
        self.five_heart = [5, "Faces/Playing_card_heart_5.png"]
        self.five_spade = [5, "Faces/Playing_card_spade_5.png"]
        self.six_club = [6, "Faces/Playing_card_club_6.png"]
        self.six_diamond = [6, "Faces/Playing_card_diamond_6.png"]
        self.six_heart = [6, "Faces/Playing_card_heart_6.png"]
        self.six_spade = [6, "Faces/Playing_card_spade_6.png"]
        self.seven_club = [7, "Faces/Playing_card_club_7.png"]
        self.seven_diamond = [7, "Faces/Playing_card_diamond_7.png"]
        self.seven_heart = [7,  "Faces/Playing_card_heart_7.png"]
        self.seven_spade = [7, "Faces/Playing_card_spade_7.png"]
        self.eight_club = [8, "Faces/Playing_card_club_8.png"]
        self.eight_diamond = [8, "Faces/Playing_card_diamond_8.png"]
        self.eight_heart = [8, "Faces/Playing_card_heart_8.png"]
        self.eight_spade = [8, "Faces/Playing_card_spade_8.png"]
        self.nine_club = [9, "Faces/Playing_card_club_9.png"]
        self.nine_diamond = [9, "Faces/Playing_card_diamond_9.png"]
        self.nine_heart = [9, "Faces/Playing_card_heart_9.png"]
        self.nine_spade = [9, "Faces/Playing_card_spade_9.png"]
        self.ten_club = [10, "Faces/Playing_card_club_10.png"]
        self.ten_diamond = [10, "Faces/Playing_card_diamond_10.png"]
        self.ten_heart = [10, "Faces/Playing_card_heart_10.png"]
        self.ten_spade = [10, "Faces/Playing_card_spade_10.png"]
        self.j_club = [10, "Faces/Playing_card_club_J.png"]
        self.j_diamond = [10, "Faces/Playing_card_diamond_J.png"]
        self.j_heart = [10, "Faces/Playing_card_heart_J.png"]
        self.j_spade = [10, "Faces/Playing_card_spade_J.png"]
        self.q_club = [10, "Faces/Playing_card_club_Q.png"]
        self.q_diamond = [10, "Faces/Playing_card_diamond_Q.png"]
        self.q_heart = [10, "Faces/Playing_card_heart_Q.png"]
        self.q_spade = [10, "Faces/Playing_card_spade_Q.png"]
        self.k_club = [10, "Faces/Playing_card_club_K.png"]
        self.k_diamond = [10, "Faces/Playing_card_diamond_K.png"]
        self.k_heart = [10, "Faces/Playing_card_heart_K.png"]
        self.k_spade = [10, "Faces/Playing_card_spade_K.png"]
        #deck is a list of all the lists
        self.deck = [
            self.a_club, self.a_diamond, self.a_heart, self.a_spade, self.two_club, self.two_diamond, self.two_heart, self.three_spade, self.three_club,
            self.three_diamond, self.three_heart, self.three_spade, self.four_club, self.four_diamond, self.four_heart, self.four_spade, self.five_club,
            self.five_diamond, self.five_heart, self.five_spade, self.six_club, self.six_diamond, self.six_heart, self.six_spade, self.seven_club,
            self.seven_diamond, self.seven_heart, self.seven_spade, self.eight_club, self.eight_diamond, self.eight_heart, self.eight_spade, self.nine_club,
            self.nine_diamond, self.nine_heart, self.nine_spade, self.ten_club, self.ten_diamond, self.ten_heart, self.ten_spade, self.j_club, self.j_diamond,
            self.j_heart, self.j_spade, self.q_club, self.q_diamond, self.q_heart, self.q_spade, self.k_club, self.k_diamond, self.k_heart, self.k_spade]
        #labels, buttons, etc.
        self.dealerlabel = tkinter.Label(master, text = "Dealer:")
        self.dealercurrent = tkinter.Label(master, textvariable = self.dealertext)
        self.yourlabel = tkinter.Label(master, text = "You:")
        self.yourcurrent = tkinter.Label(master, textvariable = self.playertext)
        self.playbutton = tkinter.Button(master, text = "Play game!", command = self.playgame)
        self.hitmebutton = tkinter.Button(master, text = "Hit me baby~!", command = self.hitme)
        self.imdonebutton = tkinter.Button(master, text = "I stand my ground", command = self.dealerhit)
        #packing
        self.dealerlabel.pack()
        self.dealercanvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.dealercurrent.pack()
        self.yourlabel.pack()
        self.playercanvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.yourcurrent.pack()
        self.playbutton.pack()
        self.hitmebutton.pack()
        self.imdonebutton.pack()

    #add up the player to update for ace values
    def sumplayer(self):
        self.player = 0
        for k in range(len(self.playerhand)):
            self.player = self.player + self.playerhand[k][0]

    #same for dealer and aces
    def sumdealer(self):
        self.dealer = 0
        for k in range(len(self.dealerhand)):
            self.dealer = self.dealer + self.dealerhand[k][0]

    #winner winner chicken dinner
    def victory(self):
        messagebox.showinfo("Victory!", "YOU WIN!")

    #loser loser grandma refuser
    def loss(self):
        messagebox.showinfo("Defeat", "You lose :(")

    #double twenty one's!
    def tie(self):
        messagebox.showinfo("TIE!", "You tied :/")

    #for the play game button
    def playgame(self):
        #reset images, placements, variables, etc.
        self.img1 = None
        self.reimg1 = None
        self.newimg1 = None
        self.img2 = None
        self.reimg2 = None
        self.newimg2 = None
        self.img3 = None
        self.reimg3 = None
        self.newimg3 = None
        self.img4 = None
        self.reimg4 = None
        self.newimg4 = None
        self.img5 = None
        self.reimg5 = None
        self.newimg5 = None
        self.img6 = None
        self.reimg6 = None
        self.newimg6 = None
        self.img7 = None
        self.reimg7 = None
        self.newimg7 = None
        self.img8 = None
        self.reimg8 = None
        self.newimg8 = None
        self.img9 = None
        self.reimg9 = None
        self.newimg9 = None
        self.img10 = None
        self.reimg10 = None
        self.newimg10 = None
        self.img11 = None
        self.reimg11 = None
        self.newimg11 = None
        self.img12 = None
        self.reimg12 = None
        self.newimg12 = None
        self.img13 = None
        self.reimg13 = None
        self.newimg13 = None
        self.img14 = None
        self.reimg14 = None
        self.newimg14 = None
        self.img15 = None
        self.reimg15 = None
        self.newimg15 = None
        self.img16 = None
        self.reimg16 = None
        self.newimg16 = None
        self.img17 = None
        self.reimg17 = None
        self.newimg17 = None
        self.img18 = None
        self.reimg18 = None
        self.newimg18 = None
        self.img19 = None
        self.reimg19 = None
        self.newimg19 = None
        self.img20 = None
        self.reimg20 = None
        self.newimg20 = None
        self.img21 = None
        self.reimg21 = None
        self.newimg21 = None
        self.img22 = None
        self.reimg22 = None
        self.newimg22 = None
        self.dealerx = 0
        self.dealery = 0
        self.playerx = 0
        self.playery = 0
        self.playerhand = []
        self.dealerhand = []
        self.dealer = 0
        self.player = 0
        self.drawn = 0
        #shuffle the deck
        random.shuffle(self.deck)
        #add the first 2 cards to the dealers hand
        self.dealer = self.deck[0][0] + self.deck[1][0]
        self.dealerhand.append(self.deck[0])
        self.dealerhand.append(self.deck[1])
        #in the slight off chance that the dealer pulls two aces, this is here
        if self.dealer > 21 and (self.a_club in self.playerhand or self.a_diamond in self.playerhand or
                                     self.a_heart in self.playerhand or self.a_spade in self.playerhand):
                self.a_club[0] = self.a_diamond[0] = self.a_heart[0] = self.a_spade[0] = 1
                self.sumdealer()
        #image time
        self.img1 = Image.open(self.dealerhand[0][1])
        self.img2 = Image.open(self.dealerhand[1][1])
        self.reimg1 = self.img1.resize((40, 50), Image.ANTIALIAS)
        self.reimg2 = self.img2.resize((40, 50), Image.ANTIALIAS)
        self.newimg1 = ImageTk.PhotoImage(self.reimg1)
        self.newimg2 = ImageTk.PhotoImage(self.reimg2)
        self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg1, anchor=tkinter.NW)
        self.dealerx = self.dealerx + 40
        self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg2, anchor=tkinter.NW)
        self.x = self.dealerx + 40
        #if the dealer is still over 21, you win (which is impossible with a starting hand, but for debugs)
        if self.dealer > 21:
            self.victory()
        else:
            self.player = self.deck[2][0] + self.deck[3][0]
            self.playerhand.append(self.deck[2])
            self.playerhand.append(self.deck[3])
            #in the scenario where the PLAYER pulls two aces, this is here
            if self.player > 21 and (self.a_club in self.playerhand or self.a_diamond in self.playerhand or
                                 self.a_heart in self.playerhand or self.a_spade in self.playerhand):
                self.a_club[0] = self.a_diamond[0] = self.a_heart[0] = self.a_spade[0] = 1
                self.sumplayer()
            #more images :)
            self.img3 = Image.open(self.playerhand[0][1])
            self.img4 = Image.open(self.playerhand[1][1])
            self.reimg3 = self.img3.resize((40, 50), Image.ANTIALIAS)
            self.reimg4 = self.img4.resize((40, 50), Image.ANTIALIAS)
            self.newimg3 = ImageTk.PhotoImage(self.reimg3)
            self.newimg4 = ImageTk.PhotoImage(self.reimg4)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg3, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg4, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
            #also impossible, but in case of bugs
            if self.player > 21:
                self.loss()
            else:
                self.drawn = 3
        #set the text variables to the new values
        self.dealertext.set(str(self.dealer))
        int(self.dealer)
        self.playertext.set(str(self.player))
        int(self.player)

    #for the hitting button
    def hitme(self):
        self.drawn = self.drawn + 1
        self.player = self.player + self.deck[self.drawn][0]
        self.playerhand.append(self.deck[self.drawn])
        #set aces to lower value for bust
        if self.player > 21 and (self.a_club in self.playerhand or self.a_diamond in self.playerhand or
                                 self.a_heart in self.playerhand or self.a_spade in self.playerhand):
                self.a_club[0] = self.a_diamond[0] = self.a_heart[0] = self.a_spade[0] = 1
                self.sumplayer()
        #haha bad
        if self.player > 21:
            self.loss()
        self.playertext.set(str(self.player))
        int(self.player)
        #this is for typewriter style of grid
        if self.playerx == 160:
            self.playerx = 0
            self.playery = self.playery + 50
        #yeehaw images
        if self.drawn == 4:
            self.img5 = Image.open(self.deck[self.drawn][1])
            self.reimg5 = self.img5.resize((40, 50), Image.ANTIALIAS)
            self.newimg5 = ImageTk.PhotoImage(self.reimg5)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg5, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 5:
            self.img6 = Image.open(self.deck[self.drawn][1])
            self.reimg6 = self.img6.resize((40, 50), Image.ANTIALIAS)
            self.newimg6 = ImageTk.PhotoImage(self.reimg6)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg6, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 6:
            self.img7 = Image.open(self.deck[self.drawn][1])
            self.reimg7 = self.img7.resize((40, 50), Image.ANTIALIAS)
            self.newimg7 = ImageTk.PhotoImage(self.reimg7)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg7, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 7:
            self.img8 = Image.open(self.deck[self.drawn][1])
            self.reimg8 = self.img8.resize((40, 50), Image.ANTIALIAS)
            self.newimg8 = ImageTk.PhotoImage(self.reimg8)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg8, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 8:
            self.img9 = Image.open(self.deck[self.drawn][1])
            self.reimg9 = self.img9.resize((40, 50), Image.ANTIALIAS)
            self.newimg9 = ImageTk.PhotoImage(self.reimg9)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg9, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 9:
            self.img10 = Image.open(self.deck[self.drawn][1])
            self.reimg10 = self.img10.resize((40, 50), Image.ANTIALIAS)
            self.newimg10 = ImageTk.PhotoImage(self.reimg10)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg10, anchor=tkinter.NW)
            self.playerx = self.playerx + 40
        elif self.drawn == 10:
            self.img11 = Image.open(self.deck[self.drawn][1])
            self.reimg11 = self.img11.resize((40, 50), Image.ANTIALIAS)
            self.newimg11 = ImageTk.PhotoImage(self.reimg11)
            self.playercanvas.create_image(self.playerx, self.playery, image=self.newimg11, anchor=tkinter.NW)
            self.playerx = self.playerx + 40

    #for the dealers pesky images in the while loop he has (the button is pressed once, unlike player)
    def dealerimg(self):
        if self.dealerx == 160:
            self.dealerx = 0
            self.dealery = self.dealery + 50
        else:
            self.dealerx = self.dealerx + 40
        if self.drawn == 4:
            self.img5 = Image.open(self.deck[self.drawn][1])
            self.reimg5 = self.img5.resize((40, 50), Image.ANTIALIAS)
            self.newimg5 = ImageTk.PhotoImage(self.reimg5)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg5, anchor=tkinter.NW)
        elif self.drawn == 5:
            self.img6 = Image.open(self.deck[self.drawn][1])
            self.reimg6 = self.img6.resize((40, 50), Image.ANTIALIAS)
            self.newimg6 = ImageTk.PhotoImage(self.reimg6)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg6, anchor=tkinter.NW)
        elif self.drawn == 6:
            self.img7 = Image.open(self.deck[self.drawn][1])
            self.reimg7 = self.img7.resize((40, 50), Image.ANTIALIAS)
            self.newimg7 = ImageTk.PhotoImage(self.reimg7)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg7, anchor=tkinter.NW)
        elif self.drawn == 7:
            self.img8 = Image.open(self.deck[self.drawn][1])
            self.reimg8 = self.img8.resize((40, 50), Image.ANTIALIAS)
            self.newimg8 = ImageTk.PhotoImage(self.reimg8)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg8, anchor=tkinter.NW)
        elif self.drawn == 8:
            self.img9 = Image.open(self.deck[self.drawn][1])
            self.reimg9 = self.img9.resize((40, 50), Image.ANTIALIAS)
            self.newimg9 = ImageTk.PhotoImage(self.reimg9)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg9, anchor=tkinter.NW)
        elif self.drawn == 9:
            self.img10 = Image.open(self.deck[self.drawn][1])
            self.reimg10 = self.img10.resize((40, 50), Image.ANTIALIAS)
            self.newimg10 = ImageTk.PhotoImage(self.reimg10)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg10, anchor=tkinter.NW)
        elif self.drawn == 10:
            self.img11 = Image.open(self.deck[self.drawn][1])
            self.reimg11 = self.img11.resize((40, 50), Image.ANTIALIAS)
            self.newimg11 = ImageTk.PhotoImage(self.reimg11)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg11, anchor=tkinter.NW)
        elif self.drawn == 11:
            self.img12 = Image.open(self.deck[self.drawn][1])
            self.reimg12 = self.img12.resize((40, 50), Image.ANTIALIAS)
            self.newimg12 = ImageTk.PhotoImage(self.reimg12)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg12, anchor=tkinter.NW)
        elif self.drawn == 12:
            self.img13 = Image.open(self.deck[self.drawn][1])
            self.reimg13 = self.img13.resize((40, 50), Image.ANTIALIAS)
            self.newimg13 = ImageTk.PhotoImage(self.reimg13)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg13, anchor=tkinter.NW)
        elif self.drawn == 13:
            self.img14 = Image.open(self.deck[self.drawn][1])
            self.reimg14 = self.img14.resize((40, 50), Image.ANTIALIAS)
            self.newimg14 = ImageTk.PhotoImage(self.reimg14)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg14, anchor=tkinter.NW)
        elif self.drawn == 14:
            self.img15 = Image.open(self.deck[self.drawn][1])
            self.reimg15 = self.img15.resize((40, 50), Image.ANTIALIAS)
            self.newimg15 = ImageTk.PhotoImage(self.reimg15)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg15, anchor=tkinter.NW)
        elif self.drawn == 15:
            self.img16 = Image.open(self.deck[self.drawn][1])
            self.reimg16 = self.img16.resize((40, 50), Image.ANTIALIAS)
            self.newimg16 = ImageTk.PhotoImage(self.reimg16)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg16, anchor=tkinter.NW)
        elif self.drawn == 16:
            self.img17 = Image.open(self.deck[self.drawn][1])
            self.reimg17 = self.img17.resize((40, 50), Image.ANTIALIAS)
            self.newimg17 = ImageTk.PhotoImage(self.reimg17)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg17, anchor=tkinter.NW)
        elif self.drawn == 17:
            self.img18 = Image.open(self.deck[self.drawn][1])
            self.reimg18 = self.img18.resize((40, 50), Image.ANTIALIAS)
            self.newimg18 = ImageTk.PhotoImage(self.reimg18)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg18, anchor=tkinter.NW)
        elif self.drawn == 18:
            self.img19 = Image.open(self.deck[self.drawn][1])
            self.reimg19 = self.img19.resize((40, 50), Image.ANTIALIAS)
            self.newimg15 = ImageTk.PhotoImage(self.reimg19)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg19, anchor=tkinter.NW)
        elif self.drawn == 19:
            self.img20 = Image.open(self.deck[self.drawn][1])
            self.reimg20 = self.img20.resize((40, 50), Image.ANTIALIAS)
            self.newimg20 = ImageTk.PhotoImage(self.reimg20)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg20, anchor=tkinter.NW)
        elif self.drawn == 20:
            self.img21 = Image.open(self.deck[self.drawn][1])
            self.reimg21 = self.img21.resize((40, 50), Image.ANTIALIAS)
            self.newimg21 = ImageTk.PhotoImage(self.reimg21)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg21, anchor=tkinter.NW)
        elif self.drawn == 21:
            self.img22 = Image.open(self.deck[self.drawn][1])
            self.reimg22 = self.img22.resize((40, 50), Image.ANTIALIAS)
            self.newimg22 = ImageTk.PhotoImage(self.reimg22)
            self.dealercanvas.create_image(self.dealerx, self.dealery, image=self.newimg22, anchor=tkinter.NW)
            
    #for the dealers fate
    def dealerhit(self):
        #set a while loop so the dealer HAS to be higher or equal to the player
        while self.dealer <= self.player:
            #if statement for the double 21 that a while loop can't (?) cover
            if self.player == 21 and self.dealer == 21:
                break
            self.drawn = self.drawn + 1
            self.dealer = self.dealer + self.deck[self.drawn][0]
            self.dealerhand.append(self.deck[self.drawn])
            #set aces to lower value if bust
            if self.dealer > 21 and (self.a_club in self.playerhand or self.a_diamond in self.playerhand or
                                     self.a_heart in self.playerhand or self.a_spade in self.playerhand):
                self.a_club[0] = self.a_diamond[0] = self.a_heart[0] = self.a_spade[0] = 1
                self.sumdealer()
            self.dealertext.set(str(self.dealer))
            int(self.dealer)
            #call this for those image updates
            self.dealerimg()
        #win, loss, tie (duh)
        if self.dealer > self.player and self.dealer <= 21:
            self.loss()
        elif self.dealer == 21 and self.player == 21:
            self.tie()
        elif self.dealer > 21 and self.player <= 21:
            self.victory()

#finally
root = tkinter.Tk()
client = Client(root)
root.mainloop()
