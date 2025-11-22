import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

plt.style.use('dark_background')
pType = 'image'
cmap = ['green','orange','yellow','red','darkblue','blue']

images_list = ['kahire.png',
               'tunus.png',
               'fas.png',
               'girnata.png',
               'becaye.png',
               'misir.png']

bar_lbl_list = ['Kahirede konaklama süresi',
                'Tunusta konaklama süresi',
                'Fasta konaklama süresi',
                'Gırnatada konaklama süresi',
                'Becayede konaklama süresi',
                'Mısırda konaklama süresi']

dataset = [2,3,15,15,24,24]



def CreateTestData(gauss,n):
    pass

def CreateGlobalFigure(clr):
    global pType

    obj_index = 0
    axindex = 0

    fig,ax = plt.subplots(2,6)
    
    for obj in fig.axes:
        obj.axis(False)

        if True == True:     
            if pType == 'image':
                for img in images_list:
                    matrix = cv.imread(img,cv.COLOR_BGR2RGB)

                    if matrix is not None:
                        if axindex >= (len(fig.axes) // 2):
                            break

                        matrix = cv.cvtColor(matrix,cv.COLOR_BGR2RGB)

                        ax[1,axindex].imshow(matrix,cmap='gray')  

                    axindex += 1
                    
        obj_index += 1
    
    for qk in range(len(dataset)):
        ax[0,qk].axis(True)
        ax[0,qk].grid(False)
        ax[0,qk].set_title(bar_lbl_list[qk])

        ax[0,qk].ecdf(x=np.linspace(0,dataset[qk], dataset[qk]),c=cmap[qk],linewidth=2.5)
        ax[0,qk].set_xlabel(f'{dataset[qk]} Yıl kadar',c='red',size=15,font='Arial')

        ax[0,qk].set_title(bar_lbl_list[qk])

def CreateLocalFigure(clr):
    pass

selection = 'global'

if selection == 'global':
    CreateGlobalFigure(None)

else:
    if selection == 'local':
        CreateLocalFigure(None)

plt.show()
