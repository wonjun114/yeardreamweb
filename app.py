# app.py
import streamlit as st
import pandas as pd
import numpy as np

# 제목
st.title("스트림릿 기본 예제")

# 텍스트 입력
name = st.text_input("이름을 입력하세요:")
st.write(f"안녕하세요, {name}님!")

# 숫자 입력
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=25)
st.write(f"당신의 나이는 {age}살입니다.")

# 버튼
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# 체크박스
if st.checkbox("데이터 테이블 보기"):
    data = pd.DataFrame({
        "A": np.random.randn(5),
        "B": np.random.randn(5)
    })
    st.write(data)

# 라인 차트
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["X", "Y", "Z"]
)
st.line_chart(chart_data)
