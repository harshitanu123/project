import streamlit as st
from PIL import Image,ImageFilter,ImageFont,ImageDraw,ImageColor,ImageEnhance
st.title("IMAGE EDITOR")
sidebar=st.sidebar
sidebar.title('image processing method')
option=['image croping','image marging','image font','Image Blend','image resizeing','image filtering','image masking','image rotation','image split','image diffusing','image fliping','image drawing',]
ch=sidebar.selectbox('layout',option)
if ch=='image croping':
    st.markdown('<h2> CROP IMAGE </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload image')
    if im:
        img=Image.open(im)
        st.image(img)
        st.write(img.size)
        st.write(img.format)
        x=st.number_input('x-axis')
        y=st.number_input('y-axis')
        width=st.number_input('width')
        hieght=st.number_input('hight')
        btn=st.button('submit')
        if btn:
            im1=img.crop((x,y,width,hieght))
            st.image(im1)
if ch=='image marging':
   st.markdown('<h2> MARGING TWO IMAGES </h2',unsafe_allow_html=True)
   im1=st.file_uploader('Image 1')
   im2=st.file_uploader('Image 2')
   if im1 and im2:
      img1=Image.open(im1)
      resize=img1.resize((555,555))
      st.write(resize)
      st.write(resize.size)
      st.image(resize)
      img2=Image.open(im2)
      re=img2.resize((555,555))
      st.write(re)
      st.write(re.size)
      st.image(re)
      st.markdown("<h2>MERGING IMAGE FROM LEFT,RIGHT,TOP,BOTTOM</h2>",unsafe_allow_html=True)
      option=['left_side','right_side','top','bottom']
      ch=st.selectbox('label',option)
      if ch=='left_side':
        bu=st.button("submit")
        sv=st.checkbox('save1')
        if bu:
            dst=Image.new('RGB',(555+555,555))
            dst.paste(resize,(0,0))
            dst.paste(re,(resize.width,0))
            st.image(dst)
            if sv:
                dst.save('merge_lift_side.png','PNG')
      if ch=='right_side':
           bu=st.button('submit')
           sv=st.checkbox('save2')
           if bu:
             dst=Image.new('RGB',(555+555,555))
             dst.paste(re,(0,0))
             dst.paste(resize,(re.width,0))
             st.image(dst)
             if sv:
                dst.save('merge_right_side.png','PNG')
      if ch=='top':
            bu=st.button('submit')
            sv=st.checkbox('save3')
            if bu:
                dst=Image.new('RGB',(555,555+555))
                dst.paste(re,(0,0))
                dst.paste(resize,(0,re.height))
                st.image(dst)
                if sv:
                    dst.save('merge_top.png','PNG')
      if ch=='bottom':
            bu=st.button("submit")
            sv=st.checkbox('save4')
            if bu:
               dst=Image.new('RGB',(555,555+555))
               dst.paste(resize,(0,0))
               dst.paste(re,(0,resize.height))
               st.image(dst)
               if sv:
                dst.save('merge_bottom.png','PNG')
                st.markdown("------------")
if ch=='image filtering':
    st.markdown('<h2> FILTERING IMAGES </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload Image')
    if im:
        im1=Image.open(im)
        st.write(im1)
        st.image(im1)
        filter_option=['EDGE_ENHANCE','EMBOSS','BOXBLUR','CONOUR','BLUR','FIND_EDGES']
        st.header('---------filter_option---------')
        ch=st.selectbox('layout',filter_option)
        if ch=='EDGE_ENHANCE':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.EDGE_ENHANCE)
                st.image(img1)
        if ch=='EMBOSS':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.EMBOSS)
                st.image(img1)
        if ch=='BOXBLUR':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.BoxBlur(7))
                st.image(img1) 
        if ch=='CONOUR':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.CONTOUR)
                st.image(img1)
        if ch=='BLUR':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.BLUR)
                st.image(img1)
        if ch=='FIND_EDGES':
            btn=st.button('submit')
            if btn:
                img1=im1.filter(ImageFilter.FIND_EDGES)
                st.image(img1)
if ch=='image font':
        st.markdown('<h2> SET IMAGE WITH FONT </h2',unsafe_allow_html=True)
        im=st.file_uploader('upload image------')
        text=st.text_input('Enter Text Here----')
        if im and text:
            img=Image.open(im)
            st.write(img.size)
            st.image(img)
            st.title('Selecting font features')
            option=['Shelter_PersonalUseOnly.ttf','Vazeelia.ttf','Girassol-Regular.ttf','Bernadette.ttf','ChocoladineDemo.ttf']
            font_web_text=st.selectbox('font style',option)
            font_size=st.slider('font size')
            font_color=st.color_picker('enter color')
            btn=st.button("submit")
            if btn:
              
              font=ImageFont.truetype(font_web_text,font_size)
              writer=ImageDraw.Draw(img)
              writer.text((100,111),text,font=font,fill=font_color)
              st.image(img)
if ch=='Image Blend':
    st.markdown('<h2> BLEND TWO IMAGES </h2',unsafe_allow_html=True)
    im1=st.file_uploader('Image 1')
    im2=st.file_uploader('Image 2')
    if im1 and im2:
      img1=Image.open(im1)
      st.write(img1.size)
      st.write(img1.mode)
      st.image(img1)
      img2=Image.open(im2)
      st.write(img2.size)
      st.write(img2.mode)
      st.image(img2)
      if img1.size==img2.size and img1.mode==img2.mode:
         btn=st.button('submit')
         if btn:
          img3=Image.blend(img1,img2,0.4)
          st.image(img3)
      if img1.size==img2.size and img1.mode!=img2.mode:
         btn=st.button('submit')
         if btn:
            img4=img1.convert(img2.mode)
            img3=Image.blend(img4,img2,0.4)
            st.image(img3)
      if img1.size!=img2.size and img1.mode==img2.mode:
         btn=st.button('submit')
         if btn:
                img3=img1.resize(img2.size)
                img4=Image.blend(img2,img3,0.4)
                st.image(img4)
      if img1.size!=img2.size and img1.mode!=img2.mode:
         btn=st.button('submit')
         if btn:
            img4=img1.convert(img2.mode).resize(img2.size)
            
            #img3=img1.resize(img2.size)
            img5=Image.blend(img4,img2,0.4)
            st.image(img5)
if ch=='image resizeing':
    st.markdown('<h2> CHANGE  SIZE  </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload file')
    if im:
        img1=Image.open(im)
        st.image(img1)
        width=st.slider('width',min_value=0,max_value=1000)
        heigth=st.slider('heigth',min_value=0,max_value=1000)
        btn=st.button('submit')
        if btn:
           img=img1.resize((width,heigth))
           st.image(img)
if ch=='image split':
    st.markdown('<h2> SPLITING IMAGES </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload image')
    if im:
        img=Image.open(im)
        st.image(img)
        btn=st.button('submit')
        if btn:
           im1=[]
           im1=img.split()
           for i in im1:
               st.image(i)
if ch=='image fliping':
    st.markdown('<h2> FLIP THE IMAGES </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload image')
    if im:
        img=Image.open(im)
        st.image(img)
        st.title('FLIPING OPTIONS')
        option=['FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','ROTATE_90','ROTATE_180','ROTATE_270']
        ch=st.selectbox('layout',option)
        if ch=='FLIP_LEFT_RIGHT':
           btn=st.button('submit')
           if btn:
              img2=img.transpose(Image.FLIP_LEFT_RIGHT)
              st.image(img2)
        if ch=='FLIP_TOP_BOTTOM':
           btn=st.button('submit')
           if btn:
              img2=img.transpose(Image.FLIP_TOP_BOTTOM)
              st.image(img2)
        if ch=='ROTATE_90':
           btn=st.button('submit')
           if btn:
              img2=img.transpose(Image.ROTATE_90)
              st.image(img2)
        if ch=='ROTATE_180':
           btn=st.button('submit')
           if btn:
              img2=img.transpose(Image.ROTATE_180)
              st.image(img2)
        if ch=='ROTATE_270':
           btn=st.button('submit')
           if btn:
              img2=img.transpose(Image.ROTATE_270)
              st.image(img2)
if ch=='image rotation':
    st.markdown('<h2> ROTATE IMAGES </h2',unsafe_allow_html=True)
    im=st.file_uploader('upload image')
    if im:
        img=Image.open(im)
        st.image(img)
        deg=st.slider('degrees',min_value=0,max_value=360)
        color=st.color_picker('color')
        btn=st.button('submit')
        if btn:
            rot_img=img.rotate(deg,fillcolor=color)
            st.image(rot_img)
if ch=='image diffusing':
    im1=st.file_uploader('upload image1')
    im2=st.file_uploader('upload image2')

    if im1 and im2 :
        img1=Image.open(im1)
        st.image(img1)
        img2=Image.open(im2)
        st.image(img2)
        if img1.size>img2.size:
            btn=st.button('submit')
            if btn:
              img1.paste(img2)
              st.image(img1)
        if img2.size>img1.size:
            btn=st.button('submit')
            if btn:
                img2.paste(img1)
                st.image(img2)
if ch=='image drawing':
     st.markdown('<h2> DRAW ELLIPSE </h2',unsafe_allow_html=True)
     w,h=220,190
     shape=[(40,40),(w-10,h-10)]
     img=Image.new('RGB',(w,h))
     st.image(img)
     fill=st.text_input('Enter color')
     outline=st.text_input("enter  boderline  color")
     btn=st.button('submit')
     if btn and img:
        
         drawer=ImageDraw.Draw(img)
         drawer.ellipse(shape,fill=fill,outline=outline) 
         st.image(img)
if ch=='image masking':
    st.markdown('<h2> MASKING IN IMAGE </h2',unsafe_allow_html=True)
    im=Image.open('mask_pic.png')
    st.image(im)
    img3=Image.new('RGB',(1200, 1496))
    btn=st.button('submit')
    if btn and img3 and im:
        im1=im.resize((1200, 1496))
        mask=Image.open('mask.png')
        mask1=mask.convert('L')
          
        #mask=Image.new('L',(1200,1496))
        #drawer=ImageDraw.Draw(mask)
        #drawer.ellipse((900,900,0,1150),fill=255)
        im2=Image.composite(im1,img3,mask1)
        st.image(im2)
    
    
