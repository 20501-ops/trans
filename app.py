import streamlit as st
from deep_translator import GoogleTranslator

# 페이지 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="centered")

st.title("🌐 한국어 다국어 번역기")
st.write("한국어를 영어, 중국어(간체), 일본어로 동시에 번역해 줍니다.")

# 텍스트 입력 창
text_to_translate = st.text_area("번역할 한국어 텍스트를 입력하세요:", height=150)

# 번역 버튼
if st.button("번역하기"):
    if text_to_translate.strip():
        with st.spinner("번역 중입니다... 잠시만 기다려주세요."):
            try:
                # 각 언어로 번역 수행
                en_translation = GoogleTranslator(source='ko', target='en').translate(text_to_translate)
                zh_translation = GoogleTranslator(source='ko', target='zh-CN').translate(text_to_translate)
                ja_translation = GoogleTranslator(source='ko', target='ja').translate(text_to_translate)

                # 번역 결과 출력
                st.subheader("🇺🇸 영어 (English)")
                st.info(en_translation)

                st.subheader("🇨🇳 중국어 (Chinese - Simplified)")
                st.success(zh_translation)

                st.subheader("🇯🇵 일본어 (Japanese)")
                st.warning(ja_translation)
                
            except Exception as e:
                st.error(f"번역 중 오류가 발생했습니다: {e}")
    else:
        st.error("번역할 텍스트를 먼저 입력해 주세요.")
