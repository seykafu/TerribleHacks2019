
# coding: utf-8

# In[2]:


from sklearn import linear_model
import pandas as pd
import numpy as np
import base64
from PIL import Image
from io import BytesIO
from IPython.display import HTML

# In[57]:



def matching_function(gender, age_range, hair_color, ethnicity):
    global image
    if gender == 'masculine':
        if age_range == 'under 18':
            if hair_color == 'black':
                if ethnicity == 'asian':
                    image = Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_asian_black.jpg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg') #find some black dude
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')#switch this to white
                    return image.show()
                
            elif hair_color == 'blonde':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                    return image.show()
                
        elif age_range == '18 - 30':
            if hair_color == 'black':
                if ethnicity == 'asian':
                    image = Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_asian_black.jpg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg') #find some black dude
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg') #switch this to white
                    return image.show()
                
            elif hair_color == 'blonde':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_blonde.jpg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\black_anime_blonde.jpg')
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_blonde_guy.jpg')
                    return image.show()            
            
            
            
        elif age_range == '30 - 50':
            if hair_color == 'black':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #find some black dude
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #switch this to white
                    return image.show()
                
            elif hair_color == 'blonde':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_white_old_blonde.jpg')
                    return image.show()  
                
        else:
            if hair_color == 'black':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #find some black dude
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #switch this to white
                    return image.show()
                
            elif hair_color == 'blonde':
                if ethnicity == 'asian':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                elif ethnicity == 'black':
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()
                else:
                    image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                    return image.show()  
    else:
        while gender == 'feminine':
            if age_range == 'under 18':
                if hair_color == 'black':
                    if ethnicity == 'asian':
                        image = Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #find some black dude
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')#switch this to white
                        return image.show()
                
                elif hair_color == 'blonde':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()

            elif age_range == '18 - 30':
                if hair_color == 'black':
                    if ethnicity == 'asian':
                        image = Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg') #find some black dude
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg') #switch this to white
                        return image.show()
                
                elif hair_color == 'blonde':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpg')
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_blonde_girl.jpeg')
                        return image.show()            
            
            
            
            elif age_range == '30 - 50':
                if hair_color == 'black':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #find some black dude
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #switch this to white
                        return image.show()

                elif hair_color == 'blonde':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()  

            else:
                if hair_color == 'black':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #find some black dude
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg') #switch this to white
                        return image.show()

                elif hair_color == 'blonde':
                    if ethnicity == 'asian':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    elif ethnicity == 'black':
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_black.jpeg')
                        return image.show()
                    else:
                        image == Image.open(r'C:\Users\Kasey Fu\Desktop\terrible\input\anime_blonde_girl.jpeg')
                        return image.show()  

    


# In[34]:


terrible_df


# In[59]:


gender = 'masculine'
age_range = '18 - 30'
ethnicity = 'asian'
hair_color = 'black'
matching_function(gender, age_range, hair_color, ethnicity)

