import random
import time
import math
import configparser
import sys

#To-do list
    #sus4#5
    #impliment #11 chords
    # 11 chords
    ##slash chords
    ###Chord rotations?
    ###Add GUI and setting page

###Things to test###
    #In the second alternative scale, I have made the diminished chords major

print("Welcome to ChordFinder 0.3.5\n")

#------------------------------------------------------#
'''                    The Kitchen                   '''
zest_max = 10 #How often it changes key: 1/zest_max chance. Normally 10

zest =  3#How many alternative chords are used(7,sus2), max is zest_max. Normally 3

spice = 25#How many really spicey chords are used. Normally between 25-75 (9,sus4)

sour = 120#The lower this number the more often the first chord is not I. Normally 100

salt = 3 #Control how closely key changes adhere to parallel keys (min is 1) normally 3

#savory

#------------------------------------------------------#

progression = []

keys = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","Cmin","C#min","Dmin","D#min","Emin","Fmin","F#min","Gmin","G#min","Amin","A#min","Bmin"]

yes = ['yes','y','yep','yesh','yeah','i guess','']

TEST_N = ["test"]
TESTmin_N = ["testmin"]

A_N = ['A','A major','a','a major','Amaj','amaj','A maj','a maj']
AS_N = ['A#','a#','A #','a #','A sharp','a sharp','A Sharp','a Sharp',]
AF_N = ['Ab','ab','A b','a b','A flat','a flat','A Flat','a Flat',]
Amin_N = ['Am','am','A minor','a minor','Amin','amin','A min','a min']
ASmin_N = ['A#min','a#min','A#m','a#m''A#minor','a#minor','A# min','a# min']
AFmin_N = ['Abmin','abmin','Abm','abm','Abminor','abminor','Ab min','ab min']
B_N = ['B','B major','b','b major','Bmaj','bmaj','B maj','b maj']
BS_N = ['B#','b#','B #','b #','B sharp','b sharp','B Sharp','b Sharp',]
BF_N = ['Bb','bb','B b','b b','B flat','b flat','B Flat','b Flat',]
Bmin_N = ['Bm','bm','B minor','b minor','Bmin','bmin','B min','b min']
BSmin_N = ['B#min','b#min','B#m','b#m','B#minor','b#minor','B# min','b# min']
BFmin_N = ['Bbmin','bbmin','Bbm','bbm','Bbminor','bbminor','Bb min','bb min']
C_N = ['C','C major','c','c major','Cmaj','cmaj','C maj','c maj']
CS_N = ['C#','c#','C #','c #','C sharp','c sharp','C Sharp','c Sharp',]
CF_N = ['Cb','cb','C b','c b','C flat','c flat','C Flat','c Flat',]
Cmin_N = ['Cm','cm','C minor','c minor','Cmin','cmin','C min','c min']
CSmin_N = ['C#min','c#min','C#m','c#m','C#minor','c#minor','C# min','c# min']
CFmin_N = ['Cbmin','cbmin','Cbm','cbm','Cbminor','cbminor','Cb min','cb min']
D_N = ['D','D major','d','d major','Dmaj','dmaj','D maj','d maj']
DS_N = ['D#','d#','D #','d #','D sharp','d sharp','D Sharp','d Sharp',]
DF_N = ['Db','db','D b','d b','D flat','d flat','D Flat','d Flat',]
Dmin_N = ['Dm','dm','D minor','d minor','Dmin','dmin','D min','d min']
DSmin_N = ['D#min','d#min','D#m','d#m','D#minor','d#minor','D# min','d# min']
DFmin_N = ['Dbmin','dbmin','Dbm','dbm','Dbminor','dbminor','Db min','db min']
E_N = ['E','E major','e','e major','Emaj','emaj','E maj','e maj']
EF_N = ['Eb','eb','E b','e b','E flat','e flat','E Flat','e Flat',]
ES_N = ['E#','e#','E #','e #','E sharp','e sharp','E Sharp','e Sharp',]
Emin_N = ['Em','em','E minor','e minor','Emin','emin','E min','e min']
EFmin_N = ['Ebmin','ebmin','Ebm','ebm','Ebminor','ebminor','Eb min','eb min']
ESmin_N = ['E#min','e#min','E#m','e#m','E#minor','e#minor','E# min','e# min']
F_N = ['F','F major','f','f major','Fmaj','fmaj','F maj','f maj']
FS_N = ['F#','f#','F #','f #','F sharp','f sharp','F Sharp','f Sharp',]
FF_N = ['Fb','fb','F b','f b','F flat','f flat','F Flat','f Flat',]
Fmin_N = ['Fm','fm','F minor','f minor','Fmin','fmin','F min','f min']
FSmin_N = ['F#min','f#min','F#m','f#m','F#minor','f#minor','F# min','f# min']
FFmin_N = ['Fbmin','fbmin','Fbm','fbm','Fbminor','fbminor','Fb min','fb min']
G_N = ['G','G major','g','g major','Gmaj','gmaj','G maj','g maj']
GS_N = ['G#','g#','G #','g #','G sharp','g sharp','G Sharp','g Sharp',]
GF_N = ['Gb','gb','G b','g b','G flat','g flat','G Flat','g Flat',]
Gmin_N = ['Gm','gm','G minor','g minor','Gmin','gmin','G min','g min']
GSmin_N = ['G#min','g#min','G#m','g#m','G#minor','g#minor','G# min','g# min']
GFmin_N = ['Gbmin','gbmin','Gbm','gbm','Gbminor','gbminor','Gb min','gb min']

#############################################################################

TEST = ["I","II","III","IV","V","VI","VII",0],["I7","II7","III7","IV7","V7","VI7","VII7",0],["Isus2","II7","III7","IVsus2","Vsus2","VI7","VIIsus2",0],["I9","II9","III9","IV9","V9","VI9","VII9",0],["Isus4","II9","III9","IVsus4","Vsus4","VI9","VIIsus4",0],["I#11","II#11","III#11","IV#11","V#11","VI#11","VII#11",0]
TESTmin = ["Im","IIm","IIIm","IVm","Vm","VIm","VIIm",12],["Im7","IIm7","IIIm7","IVm7","Vm7","VIm7","VIIm7",12],["Im7","IImsus2","IIImsus2","IVm7","Vm7","VImsus2","VIImsus2",12],["Im9","IIm9","IIIm9","IVm9","Vm9","VIm9","VIIm9",12],["Im9","IImsus4","IIImsus4","IVm9","Vm9","VImsus4","VIImsus4",12],["Im#11","IIm#11","IIIm#11","IVm#11","Vm#11","VIm#11","VIIm#11",12]

#In the second alternative scale, I have made the diminished chords major

C =["C","Dm","Em","F","G","Am","Bdim",0],["Cmaj7","Dmin7","Emin7","Fmaj7","G7","Amin7","B7",0],["Csus2","Dmin7","Emin7","Fsus2","Gsus2","Amin7","Bsus2",0],["Cmaj9","Dmin9","Emin9","Fmaj9","G9","Amin9","B9",0],["Csus4","Dmin9","Emin9","Fsus4","Gsus4","Amin9","Bsus4",0],["Cmaj#11","Dmin#11","Emin#11","Fmaj#11","G#11","Amin#11","B#11",0]
CS =["C#","D#m","E#m","F#","G#","A#m","B#dim",1],["C#maj7","D#min7","E#min7","F#maj7","G#7","A#min7","B#7",1],["C#sus2","D#min7","E#min7","F#sus2","G#sus2","A#sus2","B#sus2",1],["C#maj9","D#min9","E#min9","F#maj9","G#9","A#min9","B#9",1],["C#sus4","D#min9","E#min9","F#sus4","G#sus4","A#min9","B#sus4",1],["C#maj#11","D#min#11","E#min#11","F#maj#11","G#add#11","A#min#11","B#maj#11",1]
D =["D","Em","F#m","G","A","Bm","C#dim",2],["Dmaj7","Emin7","F#min7","Gmaj7","A7","Bmin7","C#7",2],["Dsus2","Emin7","F#min7","Gsus2","Asus2","Bmin7","C#sus2",2],["Dmaj9","Emin9","F#min9","Gmaj9","A9","Bmin9","C#9",2],["Dsus4","Emin9","F#min9","Gsus4","Asus4","Bmin9","C#sus4",2],["Dmaj#11","Emin#11","F#min#11","Gmaj#11","A#11","Bmin#11","C#add#11",2]
DS =["Eb","Fm","Gm","Ab","Bb","Cm","Ddim",3],["Ebmaj7","Fmin7","Gmin7","Abmaj7","Bb7","Cmin7","D7",3],["Ebsus2","Fmin7","Gmin7","Absus2","Bbsus2","Cmin7","Dsus2",3],["Ebmaj9","Fmin9","Gmin9","Abmaj9","Bb9","Cmin9","D9",3],["Ebsus4","Fmin9","Gmin9","Absus4","Bbsus4","Cmin9","Dsus4",3],["Ebmaj#11","Fmin#11","Gmin#11","Abmaj#11","Bb#11","Cmin#11","D#11",3]
E =["E","F#m","G#m","A","B","C#m","D#dim",4],["Emaj7","F#min7","G#min7","Amaj7","B7","C#min7","D#7",4],["Esus2","F#min7","G#min7","Asus2","Bsus2","C#min7","D#sus2",4],["Emaj9","F#min9","G#min9","Amaj9","B9","C#min9","D#9",4],["Esus4","F#min9","G#min9","Asus4","Bsus4","C#min9","D#sus4",4],["Emaj#11","F#min#11","G#min#11","Amaj#11","B#11","C#min#11","D#add#11",4]
F =["F","Gm","Am","Bb","C","Dm","Edim",5],["Fmaj7","Gmin7","Amin7","Bbmaj7","C7","Dmin7","E7",5],["Fsus2","Gmin","Amin7","Bbsus2","Csus2","Dmin7","Esus2",5],["Fmaj9","Gmin9","Amin9","Bbmaj9","C9","Dmin9","E9",5],["Fsus4","Gmin9","Amin9","Bbsus4","Csus4","Dmin9","Esus4",5],["Fmaj#11","Gmin#11","Amin#11","Bbmaj#11","C#11","Dmin#11","E#11",5]
FS =["F#","G#m","A#m","B","C#","D#m","E#dim",6],["F#maj7","G#min7","A#min7","Bmaj7","C#7","D#min7","E#7",6],["F#sus2","G#min7","A#min7","Bsus2","C#sus2","D#min7","E#sus2",6],["F#maj9","G#min9","A#min9","Bmaj9","C#9","D#min9","E#9",6],["F#sus4","G#min9","A#min9","Bsus4","C#sus4","D#min9","E#sus4",6],["F#maj#11","G#min#11","A#min#11","Bmaj#11","C#add#11","D#min#11","E#add#11",6]
G =["G","Am","Bm","C","D","Em","F#dim",7],["Gmaj7","Amin7","Bmin7","Cmaj7","D7","Emin7","F#7",7],["Gsus2","Amin7","Bmin7","Csus2","Dsus2","Emin7","F#sus2",7],["Gmaj9","Amin9","Bmin9","Cmaj9","D9","Emin9","F#9",7],["Gsus4","Amin9","Bmin9","Csus4","Dsus4","Emin9","F#sus4",7],["Gmaj#11","Amin#11","Bmin#11","Cmaj#11","D#11","Emin#11","F#add#11",7]
GS =["Ab","Bbm","Cm","Db","Eb","Fm","Gdim",8],["Abmaj7","Bbmin7","Cmin7","Dbmaj7","Eb7","Fmin7","G7",8],["Absus2","Bbmin7","Cmin7","Dbsus2","Ebsus2","Fmin7","Gsus2",8],["Abmaj9","Bbmin9","Cmin9","Dbmaj9","Eb9","Fmin9","G9",8],["Absus4","Bbmin9","Cmin9","Dbsus4","Ebsus4","Fmin9","Gsus4",8],["Abmaj#11","Bbmin#11","Cmin#11","Dbmaj#11","Eb#11","Fmin#11","G#11",8]
A =["A","Bm","C#m","D","E","F#m","G#dim",9],["Amaj7","Bmin7","C#min7","Dmaj7","E7","F#min7","G#7",9],["Asus2","Bmin7","C#min7","Dsus2","Esus2","F#min7","G#sus2",9],["Amaj9","Bmin9","C#min9","Dmaj9","E9","F#min9","G#9",9],["Asus4","Bmin9","C#min9","Dsus4","Esus4","F#min9","G#sus4",9],["Amaj#11","Bmin#11","C#min#11","Dmaj#11","E#11","F#min#11","G#add#11",9]
AS =["Bb","Cm","Dm","Eb","F","Gm","Adim",10],["Bbmaj7","Cmin7","Dmin7","Ebmaj7","F7","Gmin7","A7",10],["Bbsus2","Cmin7","Dmin7","Ebsus2","Fsus2","Gmin7","Asus2",10],["Bbmaj9","Cmin9","Dmin9","Ebmaj9","F9","Gmin9","A9",10],["Bbsus4","Cmin9","Dmin9","Ebsus4","Fsus4","Gmin9","Asus4",10],["Bbmaj#11","Cmin#11","Dmin#11","Ebmaj#11","F#11","Gmin#11","A#11",10]
B =["B","C#m","D#m","E","F#","G#m","A#dim",11],["Bmaj7","C#min7","D#min7","Emaj7","F#7","G#min7","A#7",11],["Bsus2","C#min7","D#min7","Esus2","F#sus2","G#min7","A#sus2",11],["Bmaj9","C#min9","D#min9","Emaj9","F#9","G#min9","A#9",11],["Bsus4","C#min9","D#min9","Esus4","F#sus4","G#min9","A#sus4",11],["Bmaj#11","C#min#11","D#min#11","Emaj#11","F#add#11","G#min#11","A#add#11",11]

Cmin =["Cm","Ddim","Eb","Fm","Gm","Ab","Bb",12],["Cmin7","D7","Ebmaj7","Fmin7","Gmin7","Abmaj7","Bb7",12],["Cmin7","Dsus2","Ebsus2","Fmin7","Gmin7","Absus2","Bbsus2",12],["Cmin9","D9","Ebmaj9","Fmin9","Gmin9","Abmaj9","Bb9",12],["Cmin9","Dsus4","Ebsus4","Fmin9","Gmin9","Absus4","Bbsus4",12],["Cmin#11","D#11","Ebmaj#11","Fmin#11","Gmin#11","Abmaj#11","Bb#11",12]
CSmin =["C#m","D#dim","E","F#m","G#m","A","B",13],["C#min7","D#7","Emaj7","F#min7","G#min7","Amaj7","B7",13],["C#min7","D#sus2","Esus2","F#min7","G#min7","Asus2","Bsus2",13],["C#min9","D#9","Emaj9","F#min9","G#min9","Amaj9","B9",13],["C#min9","D#sus4","Esus4","F#min9","G#min9","Asus4","Bsus4",13],["C#min#11","D#add#11","Emaj#11","F#min#11","G#min#11","Amaj#11","B#11",13]
Dmin =["Dm","Edim","F","Gm","Am","Bb","C",14],["Dmin7","E7","Fmaj7","Gmin7","Amin7","Bbmaj7","C7",14],["Dmin7","Esus2","Fsus2","Gmin7","Amin7","Bbsus2","Csus2",14],["Dmin9","E9","Fmaj9","Gmin9","Amin9","Bbmaj9","C9",14],["Dmin9","Esus4","Fsus4","Gmin9","Amin9","Bbsus4","Csus4",14],["Dmin#11","E#11","Fmaj#11","Gmin#11","Amin#11","Bbmaj#11","C#11",14]
DSmin =["Ebm","Fdim","Gb","Abm","Bbm","Cb","Db",15],["Ebmin7","F7","Gbmaj7","Abmin7","Bbmin7","Cbmaj7","Db7",15],["Ebmin7","Fsus2","Gbsus2","Abmin7","Bbmin7","Cbsus2","Dbsus2",15],["Ebmin9","F9","Gbmaj9","Abmin9","Bbmin9","Cbmaj9","Db9",15],["Ebmin9","Fsus4","Gbsus4","Abmin9","Bbmin9","Cbsus4","Dbsus4",15],["Ebmin#11","F#11","Gbmaj#11","Abmin#11","Bbmin#11","Cbmaj#11","Db#11",15]
Emin =["Em","F#dim","G","Am","Bm","C","D",16],["Emin7","F#7","Gmaj7","Amin7","Bmin7","Cmaj7","D7",16],["Emin7","F#sus2","Gsus2","Amin7","Bmin7","Csus2","Dsus2",16],["Emin9","F#9","Gmaj9","Amin9","Bmin9","Cmaj9","D9",16],["Emin9","F#sus4","Gsus4","Amin9","Bmin9","Csus4","Dsus4",16],["Emin#11","F#add#11","Gmaj#11","Amin#11","Bmin#11","Cmaj#11","D#11",16]
Fmin =["Fm","Gdim","Ab","Bbm","Cm","Db","Eb",17],["Fmin7","G7","Abmaj7","Bbmin7","Cmin7","Dbmaj7","Eb7",17],["Fmin7","Gsus2","Absus2","Bbmin7","Cmin7","Dbsus2","Ebsus2",17],["Fmin9","G9","Abmaj9","Bbmin9","Cmin9","Dbmaj9","Eb9",17],["Fmin9","Gsus4","Absus4","Bbmin9","Cmin9","Dbsus4","Ebsus4",17],["Fmin#11","G#11","Abmaj#11","Bbmin#11","Cmin#11","Dbmaj#11","Eb#11",17]
FSmin =["F#m","G#dim","A","Bm","C#m","D","E",18],["F#min7","G#7","Amaj7","Bmin7","C#min7","Dmaj7","E7",18],["F#min7","G#sus2","Asus2","Bmin7","C#min7","Dsus2","Esus2",18],["F#min9","G#9","Amaj9","Bmin9","C#min9","Dmaj9","E9",18],["F#min9","G#sus4","Asus4","Bmin9","C#min9","Dsus4","Esus4",18],["F#min#11","G#add#11","Amaj#11","Bmin#11","C#min#11","Dmaj#11","E#11",18]
Gmin =["Gm","Adim","Bb","Cm","Dm","Eb","F",19],["Gmin7","A7","Bbmaj7","Cmin7","Dmin7","Ebmaj7","F7",19],["Gmin7","Asus2","Bbsus2","Cmin7","Dmin7","Ebsus2","Fsus2",19],["Gmin9","A9","Bbmaj9","Cmin9","Dmin9","Ebmaj9","F9",19],["Gmin9","Asus4","Bbsus4","Cmin9","Dmin9","Ebsus4","Fsus4",19],["Gmin#11","A#11","Bbmaj#11","Cmin#11","Dmin#11","Ebmaj#11","F#11",19]
GSmin =["Abm","Bbdim","Cb","Dbm","Ebm","Fb","Gb",20],["Abmin7","Bb7","Cbmaj7","Dbmin7","Ebmin7","Fbmaj7","Gb7",20],["Abmin7","Bbsus2","Cbsus2","Dbmin7","Ebmin7","Fbsus2","Gbsus2",20],["Abmin9","Bb9","Cbmaj9","Dbmin9","Ebmin9","Fbmaj9","Gb9",20],["Abmin9","Bbsus4","Cbsus4","Dbmin9","Ebmin9","Fbsus4","Gbsus4",20],["Abmin#11","Bb#11","Cbmaj#11","Dbmin#11","Ebmin#11","Fbmaj#11","Gb#11",20]
Amin =["Am","Bdim","C","Dm","Em","F","G",21],["Amin7","B7","Cmaj7","Dmin7","Emin7","Fmaj7","G7",21],["Amin7","Bsus2","Csus2","Dmin7","Emin7","Fsus2","Gsus2",21],["Amin9","B9","Cmaj9","Dmin9","Emin9","Fmaj9","G9",21],["Amin9","Bsus4","Csus4","Dmin9","Emin9","Fsus4","Gsus4",21],["Amin#11","B#11","Cmaj#11","Dmin#11","Emin#11","Fmaj#11","G#11",21]
ASmin =["Bbm","Cdim","Db","Ebm","Fm","Gb","Ab",22],["Bbmin7","C7","Dbmaj7","Ebmin7","Fmin7","Gbmaj7","Ab7",22],["Bbmin7","Csus2","Dbsus2","Ebmin7","Fmin7","Gbsus2","Absus2",22],["Bbmin9","C9","Dbmaj9","Ebmin9","Fmin9","Gbmaj9","Ab9",22],["Bbmin9","Csus4","Dbsus4","Ebmin9","Fmin9","Gbsus4","Absus4",22],["Bbmin#11","C#11","Dbmaj#11","Ebmin#11","Fmin#11","Gbmaj#11","Ab#11",22]
Bmin =["Bm","C#dim","D","Em","F#m","G","A",23],["Bmin7","C#7","Dmaj7","Emin7","F#min7","Gmaj7","A7",23],["Bmin7","C#sus2","Dsus2","Emin7","F#min7","Gsus2","Asus2",23],["Bmin9","C#9","Dmaj9","Emin9","F#min9","Gmaj9","A9",23],["Bmin9","C#sus4","Dsus4","Emin9","F#min9","Gsus4","Asus4",23],["Bmin#11","C#add#11","Dmaj#11","Emin#11","F#min#11","Gmaj#11","A#11",23]

key_list = [C[0],CS[0],D[0],DS[0],E[0],F[0],FS[0],G[0],GS[0],A[0],AS[0],B[0],Cmin[0],CSmin[0],Dmin[0],DSmin[0],Emin[0],Fmin[0],FSmin[0],Gmin[0],GSmin[0],Amin[0],ASmin[0],Bmin[0],C[1],CS[1],D[1],DS[1],E[1],F[1],FS[1],G[1],GS[1],A[1],AS[1],B[1],Cmin[1],CSmin[1],Dmin[1],DSmin[1],Emin[1],Fmin[1],FSmin[1],Gmin[1],GSmin[1],Amin[1],ASmin[1],Bmin[1],C[0],CS[0],D[0],DS[0],E[0],F[0],FS[0],G[0],GS[0],A[0],AS[0],B[0],Cmin[0],CSmin[0],Dmin[0],DSmin[0],Emin[0],Fmin[0],FSmin[0],Gmin[0],GSmin[0],Amin[0],ASmin[0],Bmin[0],C[1],CS[1],D[1],DS[1],E[1],F[1],FS[1],G[1],GS[1],A[1],AS[1],B[1],Cmin[1],CSmin[1],Dmin[1],DSmin[1],Emin[1],Fmin[1],FSmin[1],Gmin[1],GSmin[1],Amin[1],ASmin[1],Bmin[1]]

key_list_resolvers = [C[0],CS[0],D[0],DS[0],E[0],F[0],FS[0],G[0],GS[0],A[0],AS[0],B[0],Cmin[0],CSmin[0],Dmin[0],DSmin[0],Emin[0],Fmin[0],FSmin[0],Gmin[0],GSmin[0],Amin[0],ASmin[0],Bmin[0],C[1],CS[1],D[1],DS[1],E[1],F[1],FS[1],G[1],GS[1],A[1],AS[1],B[1],Cmin[1],CSmin[1],Dmin[1],DSmin[1],Emin[1],Fmin[1],FSmin[1],Gmin[1],GSmin[1],Amin[1],ASmin[1],Bmin[1],C[3],CS[3],D[3],DS[3],E[3],F[3],FS[3],G[3],GS[3],A[3],AS[3],B[3],Cmin[3],CSmin[3],Dmin[3],DSmin[3],Emin[3],Fmin[3],FSmin[3],Gmin[3],GSmin[3],Amin[3],ASmin[3],Bmin[3],C[0],CS[0],D[0],DS[0],E[0],F[0],FS[0],G[0],GS[0],A[0],AS[0],B[0],Cmin[0],CSmin[0],Dmin[0],DSmin[0],Emin[0],Fmin[0],FSmin[0],Gmin[0],GSmin[0],Amin[0],ASmin[0],Bmin[0],C[1],CS[1],D[1],DS[1],E[1],F[1],FS[1],G[1],GS[1],A[1],AS[1],B[1],Cmin[1],CSmin[1],Dmin[1],DSmin[1],Emin[1],Fmin[1],FSmin[1],Gmin[1],GSmin[1],Amin[1],ASmin[1],Bmin[1],C[3],CS[3],D[3],DS[3],E[3],F[3],FS[3],G[3],GS[3],A[3],AS[3],B[3],Cmin[3],CSmin[3],Dmin[3],DSmin[3],Emin[3],Fmin[3],FSmin[3],Gmin[3],GSmin[3],Amin[3],ASmin[3],Bmin[3]]

################
def questions():
    global key_response
    global iterations
    global chorus
    
    auto = input("Do you want to decide the key and length? ")
    auto = auto.lower()

    if auto in yes:
        key_response = input("What key do you want the song in? ")
        key_response = key_response.lower()

        iterations = input("How many chords do you want in the progression? ")
        iterations = int(iterations)

    else:
        key_response = random.choice(keys)
        iterations = random.randint(2,8)

    if iterations > 20:
        print("20 chords is the maximum value allowed.")
        iterations = 20

    chorus = input("Do you want a verse, bridge, and chorus? ")
    chorus = chorus.lower()

    if chorus in yes:
        iterations = (3 * iterations) + 2

def basic():

    global key_response
    global key
    
    walker_spice = random.randint(1,zest_max+1)#WalkerSpice decides if it changes key, and then which scale is used
    original_key = key_response

    changer = 0

    if walker_spice == zest_max:#****
        if random.randint(0,1)==1:#***
            if random.randint(0,salt)==0:#***
                key_response = random.choice(keys)#****
            else:
                changer = 1#***
                

    if key_response in TEST_N:
        if walker_spice >= (zest+1): #70% of the time
            key = TEST[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = TEST[random.randint(1,2)]#30% of the time
            else:
                key = TEST[random.randint(3,4)]#10% of the time
    elif key_response in TESTmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = TESTmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = TESTmin[random.randint(1,2)]#30% of the time
            else:
                key = TESTmin[random.randint(3,4)]#10% of the time


                
    elif key_response in C_N:
        if walker_spice >= (zest+1): #60% of the time
            key = C[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = C[random.randint(1,2)]#30% of the time
            else:
                key = C[random.randint(3,4)]
    elif key_response in CS_N or key_response in DF_N:
        if walker_spice >= (zest+1): #60% of the time
            key = CS[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = CS[random.randint(1,2)]#30% of the time
            else:
                key = CS[random.randint(3,4)]
    elif key_response in D_N:
        if walker_spice >= (zest+1): #60% of the time
            key = D[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = D[random.randint(1,2)]#30% of the time
            else:
                key = D[random.randint(3,4)]
    elif key_response in DS_N or key_response in EF_N:
        if walker_spice >= (zest+1): #60% of the time
            key = D[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = D[random.randint(1,2)]#30% of the time
            else:
                key = D[random.randint(3,4)]
    elif key_response in E_N:
        if walker_spice >= (zest+1): #60% of the time
            key = E[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = E[random.randint(1,2)]#30% of the time
            else:
                key = E[random.randint(3,4)]
    elif key_response in F_N:
        if walker_spice >= (zest+1): #60% of the time
            key = F[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = F[random.randint(1,2)]#30% of the time
            else:
                key = F[random.randint(3,4)]
    elif key_response in FS_N or key_response in GF_N:
        if walker_spice >= (zest+1): #60% of the time
            key = FS[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = FS[random.randint(1,2)]#30% of the time
            else:
                key = FS[random.randint(3,4)]
    elif key_response in G_N:
        if walker_spice >= (zest+1): #60% of the time
            key = G[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = G[random.randint(1,2)]#30% of the time
            else:
                key = G[random.randint(3,4)]
    elif key_response in GS_N or key_response in AF_N:
        if walker_spice >= (zest+1): #60% of the time
            key = GS[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = GS[random.randint(1,2)]#30% of the time
            else:
                key = GS[random.randint(3,4)]
    elif key_response in A_N:
        if walker_spice >= (zest+1): #60% of the time
            key = A[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = A[random.randint(1,2)]#30% of the time
            else:
                key = A[random.randint(3,4)]
    elif key_response in AS_N or key_response in BF_N:
        if walker_spice >= (zest+1): #60% of the time
            key = AS[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = AS[random.randint(1,2)]#30% of the time
            else:
                key = AS[random.randint(3,4)]
    elif key_response in B_N:
        if walker_spice >= (zest+1): #60% of the time
            key = B[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = B[random.randint(1,2)]#30% of the time
            else:
                key = B[random.randint(3,4)]
    elif key_response in Cmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Cmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Cmin[random.randint(1,2)]#30% of the time
            else:
                key = Cmin[random.randint(3,4)]
    elif key_response in CSmin_N or key_response in DFmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = CSmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = CSmin[random.randint(1,2)]#30% of the time
            else:
                key = CSmin[random.randint(3,4)]
    elif key_response in Dmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Dmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Dmin[random.randint(1,2)]#30% of the time
            else:
                key = Dmin[random.randint(3,4)]
    elif key_response in DSmin_N or key_response in EFmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = DSmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = DSmin[random.randint(1,2)]#30% of the time
            else:
                key = DSmin[random.randint(3,4)]
    elif key_response in Emin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Emin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Emin[random.randint(1,2)]#30% of the time
            else:
                key = Emin[random.randint(3,4)]
    elif key_response in Fmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Fmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Fmin[random.randint(1,2)]#30% of the time
            else:
                key = Fmin[random.randint(3,4)]
    elif key_response in FSmin_N or key_response in GFmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = FSmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = FSmin[random.randint(1,2)]#30% of the time
            else:
                key = FSmin[random.randint(3,4)]
    elif key_response in Gmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Gmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Gmin[random.randint(1,2)]#30% of the time
            else:
                key = Gmin[random.randint(3,4)]
    elif key_response in GSmin_N or key_response in AFmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = GSmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = GSmin[random.randint(1,2)]#30% of the time
            else:
                key = GSmin[random.randint(3,4)]
    elif key_response in Amin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Amin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Amin[random.randint(1,2)]#30% of the time
            else:
                key = Amin[random.randint(3,4)]
    elif key_response in ASmin_N or key_response in BFmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = ASmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = ASmin[random.randint(1,2)]#30% of the time
            else:
                key = ASmin[random.randint(3,4)]
    elif key_response in Bmin_N:
        if walker_spice >= (zest+1): #60% of the time
            key = Bmin[0]
        elif walker_spice <= zest:
            if random.randint(0,100)>=spice:
                key = Bmin[random.randint(1,2)]#30% of the time
            else:
                key = Bmin[random.randint(3,4)]
    else:
        print ('\nSorry, I did not understand that, I can only write in minor and major keys. I may know the key you are trying to write in by another name.\n')
        questions()
        basic()

    if changer == 1:#***
        key = key_list[int(key[7])+12]#***

    ################################################################

    if random.randint(0,sour) < second_starter: #Controls how often the first chord is II
        first_chord = 1
    elif random.randint(0,sour) <= 15:
        first_chord = 5
    else:
        first_chord = 0
    
    if first_chord == 0:
        progression.append(key[0])
    elif first_chord == 1:
        progression.append(key[1])
    elif first_chord == 2:
        progression.append(key[2])
    elif first_chord == 3:
        progression.append(key[3])
    elif first_chord == 4:
        progression.append(key[4])
    elif first_chord == 5:
        progression.append(key[5])
    elif first_chord == 6:
        progression.append(key[6])
    else:
        print("An unexpected error occurred. Error 001\n")

    if random.randint(0,100) >= 50:#****
        key_response = original_key#****

    changer = 0

    #-------------------------------------------------#
    for i in range (iterations-2):

        walker_spice = random.randint(1,zest_max+1)

        if walker_spice == zest_max:#****
            if random.randint(0,salt) == 0:#***
                key_response = random.choice(keys)#****
            else:
                changer = 1#***
        
        if key_response in TEST_N:
            if walker_spice >= (zest+1): #60% of the time
                key = TEST[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = TEST[random.randint(1,2)]#30% of the time
                else:
                    key = TEST[random.randint(3,4)]
        elif key_response in TESTmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = TESTmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = TESTmin[random.randint(1,2)]#30% of the time
                else:
                    key = TESTmin[random.randint(3,4)]
        elif key_response in C_N:
            if walker_spice >= (zest+1): #60% of the time
                key = C[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = C[random.randint(1,2)]#30% of the time
                else:
                    key = C[random.randint(3,4)]
        elif key_response in CS_N or key_response in DF_N:
            if walker_spice >= (zest+1): #60% of the time
                key = CS[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = CS[random.randint(1,2)]#30% of the time
                else:
                    key = CS[random.randint(3,4)]
        elif key_response in D_N:
            if walker_spice >= (zest+1): #60% of the time
                key = D[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = D[random.randint(1,2)]#30% of the time
                else:
                    key = D[random.randint(3,4)]
        elif key_response in DS_N or key_response in EF_N:
            if walker_spice >= (zest+1): #60% of the time
                key = D[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = D[random.randint(1,2)]#30% of the time
                else:
                    key = D[random.randint(3,4)]
        elif key_response in E_N:
            if walker_spice >= (zest+1): #60% of the time
                key = E[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = E[random.randint(1,2)]#30% of the time
                else:
                    key = E[random.randint(3,4)]
        elif key_response in F_N:
            if walker_spice >= (zest+1): #60% of the time
                key = F[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = F[random.randint(1,2)]#30% of the time
                else:
                    key = F[random.randint(3,4)]
        elif key_response in FS_N or key_response in GF_N:
            if walker_spice >= (zest+1): #60% of the time
                key = FS[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = FS[random.randint(1,2)]#30% of the time
                else:
                    key = FS[random.randint(3,4)]
        elif key_response in G_N:
            if walker_spice >= (zest+1): #60% of the time
                key = G[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = G[random.randint(1,2)]#30% of the time
                else:
                    key = G[random.randint(3,4)]
        elif key_response in GS_N or key_response in AF_N:
            if walker_spice >= (zest+1): #60% of the time
                key = GS[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = GS[random.randint(1,2)]#30% of the time
                else:
                    key = GS[random.randint(3,4)]
        elif key_response in A_N:
            if walker_spice >= (zest+1): #60% of the time
                key = A[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = A[random.randint(1,2)]#30% of the time
                else:
                    key = A[random.randint(3,4)]
        elif key_response in AS_N or key_response in BF_N:
            if walker_spice >= (zest+1): #60% of the time
                key = AS[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = AS[random.randint(1,2)]#30% of the time
                else:
                    key = AS[random.randint(3,4)]
        elif key_response in B_N:
            if walker_spice >= (zest+1): #60% of the time
                key = B[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = B[random.randint(1,2)]#30% of the time
                else:
                    key = B[random.randint(3,4)]
        elif key_response in Cmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Cmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Cmin[random.randint(1,2)]#30% of the time
                else:
                    key = Cmin[random.randint(3,4)]
        elif key_response in CSmin_N or key_response in DFmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = CSmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = CSmin[random.randint(1,2)]#30% of the time
                else:
                    key = CSmin[random.randint(3,4)]
        elif key_response in Dmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Dmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Dmin[random.randint(1,2)]#30% of the time
                else:
                    key = Dmin[random.randint(3,4)]
        elif key_response in DSmin_N or key_response in EFmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = DSmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = DSmin[random.randint(1,2)]#30% of the time
                else:
                    key = DSmin[random.randint(3,4)]
        elif key_response in Emin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Emin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Emin[random.randint(1,2)]#30% of the time
                else:
                    key = Emin[random.randint(3,4)]
        elif key_response in Fmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Fmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Fmin[random.randint(1,2)]#30% of the time
                else:
                    key = Fmin[random.randint(3,4)]
        elif key_response in FSmin_N or key_response in GFmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = FSmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = FSmin[random.randint(1,2)]#30% of the time
                else:
                    key = FSmin[random.randint(3,4)]
        elif key_response in Gmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Gmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Gmin[random.randint(1,2)]#30% of the time
                else:
                    key = Gmin[random.randint(3,4)]
        elif key_response in GSmin_N or key_response in AFmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = GSmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = GSmin[random.randint(1,2)]#30% of the time
                else:
                    key = GSmin[random.randint(3,4)]
        elif key_response in Amin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Amin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Amin[random.randint(1,2)]#30% of the time
                else:
                    key = Amin[random.randint(3,4)]
        elif key_response in ASmin_N or key_response in BFmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = ASmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = ASmin[random.randint(1,2)]#30% of the time
                else:
                    key = ASmin[random.randint(3,4)]
        elif key_response in Bmin_N:
            if walker_spice >= (zest+1): #60% of the time
                key = Bmin[0]
            elif walker_spice <= zest:
                if random.randint(0,100)>=spice:
                    key = Bmin[random.randint(1,2)]#30% of the time
                else:
                    key = Bmin[random.randint(3,4)]

        if changer == 1:#***
            key = key_list[int(key[7])+12]#***
    
        if first_chord ==0:
            second_chord = random.randint(0,6)#THIS DECIDES FIRST CHORD DAUGHTERS
        elif first_chord ==1:
            second_chord = first_chord + random.choice(II_daughters)
        elif first_chord == 2:
            second_chord = first_chord + random.choice(III_daughters)
        elif first_chord == 3:
            second_chord = first_chord + random.choice(IV_daughters)
        elif first_chord == 4:
            second_chord = first_chord + random.choice(V_daughters)
        elif first_chord == 5:
            second_chord = first_chord + random.choice(VI_daughters)
        elif first_chord == 6:
            second_chord = first_chord + random.choice(VII_daughters)
        else:
            print("An unexpected error occurred. Error 002\n")

        if second_chord == 0:
            progression.append(key[0])
        elif second_chord == 1:
            progression.append(key[1])
        elif second_chord == 2:
            progression.append(key[2])
        elif second_chord == 3:
            progression.append(key[3])
        elif second_chord == 4:
            progression.append(key[4])
        elif second_chord == 5:
            progression.append(key[5])
        elif second_chord == 6:
            progression.append(key[6])
        else:
            print("An unexpected error occurred. Error 003\n")
            
        first_chord = second_chord
        
        if random.randint(0,100) >= 50:#****
            key_response = original_key#****

        changer = 0
        
    #-------------------------------------------------#

    missing_ingredient = random.randint(0,100) #decides which versions of the key it will resolve with

    if missing_ingredient <= 60:
        resolvers = 0
    elif missing_ingredient <= 90:
        resolvers = 24
    elif missing_ingredient <= 100:
        resolvers = 48
    
    key = key_list[int(key[7])+resolvers]

    second_chord = first_chord
    
    if second_chord == 0:
        final_chord = random.choice(finishers_not1)
    elif second_chord == 3:
        final_chord = random.choice(finishers_not4)
    elif second_chord == 4:
        final_chord = random.choice(finishers_not5)
    elif second_chord == 6:
        final_chord = random.choice(finishers_not7)
    else:
        final_chord = random.choice(finishers)
          
    if final_chord == 3:
        progression.append(key[3])
    elif final_chord == 4:
        progression.append(key[4])
    elif final_chord == 0:
        progression.append(key[0])
    elif final_chord == 6:
        progression.append(key[6])
    else:
        print("An unexpected error occurred. Error 004\n")

    ella = int(iterations)/3
    aidan = (int(iterations)/3)+1
    walker = ((int(iterations)/3)*2)
    mika = ((int(iterations)/3)*2)+1
    don = int(iterations)

    if chorus in yes:
        print ("Verse:")
        print ("    ", progression[0:int(ella)])
        print ("Bridge:")
        print ("    ", progression[int(aidan):int(walker)])
        print ("Chorus:")
        print ("    ", progression[int(mika):int(don)])
    else:
        print (progression)
        
    progression[:] = []

    key_response = original_key #****

    regenerate = input("Regenerate? ")
    regenerate = regenerate.lower()

    if regenerate in yes:
        basic()
    ending()

######################################################################

def ending():
    again = input("Do you want another progression? ")
    again = again.lower()

    if again in yes:
        questions()
        basic()
    else:
        print("\nThank you for using chord finder 0.3.5")
        time.sleep(2.5)
        sys.exit()

questions()

if key_response in TEST_N or key_response in A_N or key_response in AS_N or key_response in AF_N or key_response in B_N or key_response in BS_N or key_response in BF_N or key_response in C_N or key_response in CS_N or key_response in CF_N or key_response in D_N or key_response in DS_N or key_response in DF_N or key_response in E_N or key_response in ES_N or key_response in EF_N or key_response in F_N or key_response in FS_N or key_response in FF_N or key_response in G_N or key_response in GS_N or key_response in GF_N:
    
    #Below is for major
    II_daughters = [0,1,1,3,3]
    III_daughters = [0,1,1,3,3]
    IV_daughters = [0,-3,-3,-2,-2,1,1]
    V_daughters = [0,-4,-4,-2,-2,1,1]
    VI_daughters = [0,-4,-4,-3,-3,-2,-2]
    VII_daughters = [0,-4,-4,-4,-6,-6,-6]
    
    finishers_not1 = [3,4] 
    finishers_not4 = [0,4]
    finishers_not5 = [0,3]
    finishers_not7 = [0,3,4]
    finishers = [0,3,4]

    second_starter = 15
    
else:
    #below is for minor
    II_daughters = [0,1,1,3,3]
    III_daughters = [0,1,1,3,3,4,4]
    IV_daughters = [0,-3,-3,-2,-2,1,1,3]
    V_daughters = [0,-4,-4,-2,-2,1,1]
    VI_daughters = [0,-4,-4,-3,-3,-2,-2,1]
    VII_daughters = [0,-6,-6,-6]

    finishers_not1 = [3,4,6,6] #why there has to be two 6's? I dont know, but without it it is not even
    finishers_not4 = [0,4,6,6]
    finishers_not5 = [0,3,6,6]
    finishers_not7 = [0,3,4]
    finishers = [0,3,4,6]

    second_starter = 0

basic()

