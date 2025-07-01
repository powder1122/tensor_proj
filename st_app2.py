import streamlit as st
import tensorflow as tf
from PIL import Image, UnidentifiedImageError
import numpy as np

# 모델 로드
def load_model():
    try:
        st.success('모델을 로드했습니다.')
        return tf.keras.models.load_model('cat_dog_classifier.keras')
    except:
        st.error('모델을 로드할 수 없습니다. 경로를 확인해주세요!')

model = load_model()

# 전처리 --> 사용자가 업로드한 이미지를 전처리한다.
def preprocess_image(image):
    try:
        image = image.resize((150, 150))  #150 by 150 크기로 모델을 학습시킴
        image = np.array(image) /255.0  #정규화

        if image.shape[-1]  != 3: #배열의 마지막 차원의 크기!.
            raise ValueError('이미지는 RGB 형식의 컬러 이미지만 처리가 가능합니다.')
        image = np.expand_dims(image, axis=0)   #(1, 150, 150, 3)
        return image
    except Exception as e:
        st.error(f'이미지 전처리중 문제가 발생했습니다.: {e}')
        return None



#UI
st.title('Cat/Dog 분류기')
st.write('이미지를 업로드 하면 개 또는 고양이를 판별합니다.')

uploadfile = st.file_uploader('이미지를 업로드하세요.', type=['jpg', 'png', 'jpeg'])

if uploadfile is not None:
    try:
        #이미지 로드 --> 이미지 파일을 이미지 객체로 변환
        image = Image.open(uploadfile)
        st.image(image, caption='업로드 한 이미지', use_column_width=True)

        preprocessed_image = preprocess_image(image)#이미지 전처리

        if preprocessed_image is not None:
            prediction = model.predict(preprocessed_image)
            print(prediction)

            #결과 표시
            if prediction [0][0] > 0.5 :
                st.success('이 이미지는 개로 분류되었습니다.')
            else:
                st.success('이 이미지는 고양이로 분류되었습니다.')
    except UnidentifiedImageError : #이미지 형식이 아닌 경우 발생
        st.error('이미지를 로드할 수 없습니다. 지원되지 않는 파일 형식입니다.')
    except Exception as e:
        st.error(f'예측 처리 중 오류 발생: {e}')


    







