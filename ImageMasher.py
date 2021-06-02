import streamlit as st
from PIL import Image
st.title('IMAGE MASHER')
st.markdown('<h1><u><b><i>MERGE/DIFFUSE  TWO  IMAGE  AND  CREATE  NEW  IMAGE</i></b></u></h1><br><br>',unsafe_allow_html=True)


img_file1=st.file_uploader("upload image1",['JPEG','PNG','JPG','JFIF'])
img_file2=st.file_uploader("upLoad image2",['JPEG','PNG','JPG','JFIF'])
if  img_file1 and img_file2:
  im1=Image.open(img_file1)
  resize=im1.resize((555,555))
  st.write(resize)
  st.write(resize.size)
  st.image(resize)
  im2=Image.open(img_file2)
  re=im2.resize((555,555))
  st.write(re)
  st.write(re.size)
  st.image(re)
  st.markdown('<h2>DIFFUSING IMAGES</h2>',unsafe_allow_html=True)

  btn=st.button("diffuse")
  sv=st.checkbox("save")
  if btn:
    resize.paste(re,(222,222))
    st.image(resize)
    if sv:
      resize.save('diff_maker.png',format='png')
      st.success('save suceessfully')
  st.markdown('---------')
  
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
           dst.save('merge_left_side.png','PNG')
           st.success('safe sucessfully')
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

  