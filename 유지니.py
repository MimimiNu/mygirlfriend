import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="짱구미 + 표독미 분석기",
    page_icon="🐶"
)

st.title("🐶 짱구미 + 😈 표독미 분석기")

st.write(
    """
    사진을 업로드하면 AI가 짱구미와 표독미를 분석합니다.
    """
)

uploaded_file = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="업로드한 사진",
        use_container_width=True
    )

    # 예시용 랜덤 점수
    jjanggu = random.randint(70, 100)
    pyodok = random.randint(70, 100)

    st.markdown("## 📊 분석 결과")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🐶 짱구미",
            f"{jjanggu}점"
        )

    with col2:
        st.metric(
            "😈 표독미",
            f"{pyodok}점"
        )

    if jjanggu >= 90 and pyodok >= 90:
        comment = """
        너무 이쁜데 짱구미 + 표독미가 넘침

        순둥한 분위기와 강렬한 눈빛이 동시에 존재하는 타입입니다.
        """
    elif pyodok > jjanggu:
        comment = """
        표독미 우세

        정면 응시와 분위기 때문에 강렬한 인상이 느껴집니다.
        """
    else:
        comment = """
        짱구미 우세

        전체적으로 귀엽고 보호본능을 자극하는 분위기입니다.
        """

    st.success(comment)

    # 게이지 느낌 차트
    st.markdown("### 짱구미 vs 표독미")

    chart_data = {
        "특성": ["짱구미", "표독미"],
        "점수": [jjanggu, pyodok]
    }

    st.bar_chart(
        data=chart_data,
        x="특성",
        y="점수"
    )