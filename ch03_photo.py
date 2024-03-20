import streamlit as st

st.set_page_config(
    page_title="사진첩",
    page_icon="📷"
)

st.title("나만의 사진첩")
st.markdown("**사진**을 하나씩 추가해서 사진첩을 채워보세요")

css_style = """
<style>
img {
    max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)

# 나머지 코드

type_list = ["동물", "풍경", "여행","음식"]

initial_photos = [
    {
        "name": "고양이",
        "type": "동물",
        "year": "2024",
        "image_url": "https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg"
    },
    {
        "name": "들판",
        "type": "풍경",
        "year": "2024",
        "image_url": "https://cdn.pixabay.com/photo/2023/06/13/11/45/landscape-8060760_1280.jpg"
    },
    {
    "name": "숲",
    "type": "풍경",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2024/02/19/22/58/forest-8584311_1280.jpg"
    },
    {
    "name": "강아지 2마리",
    "type": "동물",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2024/03/04/20/22/dogs-8613175_1280.jpg"
    },
    {
    "name": "로마 거리",
    "type": "여행",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2018/12/08/00/30/rome-3862643_1280.jpg"
    },
        {
    "name": "크로아티아 거리",
    "type": "여행",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2019/02/09/18/45/dubrovnik-3985715_1280.jpg"
    },
        {
    "name": "베트남 거리",
    "type": "여행",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2019/02/11/09/42/pham-ngu-lao-3989110_1280.jpg"
    },
        {
    "name": "미국 거리",
    "type": "여행",
    "year": "2024",
    "image_url": "https://cdn.pixabay.com/photo/2016/10/28/13/09/usa-1777986_1280.jpg"
    },
]
example_photo={
    "name":"나는 맹고",
    "type":"음식",
    "year":"2024",
    "image_url": "https://cdn.pixabay.com/photo/2015/02/20/07/57/mango-642957_1280.jpg"
    }





if "photos" not in st.session_state:
    st.session_state.photos=initial_photos

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete",auto_complete)




with st.form(key="form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input(label="사진 이름", value=example_photo["name"])
    with col2:  
        type = st.multiselect(
            label="사진 종류",
            options=type_list,
            max_selections=2,
            default=example_photo["type"] if auto_complete else []
        )
    with col3:
       year = st.text_input(label="촬영 연도", value=example_photo["year"] if auto_complete else "")
    
    image_url = st.text_input(label="사진 URL", value=example_photo["image_url"] if auto_complete else "")
    
    # 폼이 제출되었을 때만 사진을 추가
    if st.form_submit_button(label="Submit"):
        if not name:
            st.error("사진의 이름을 입력해주세요.")
        elif len(type) == 0:
            st.error("사진의 종류를 적어도 한 개는 선택해주세요.")
        elif len(year) == 0:
            st.error("촬영 연도를 입력해주세요.")
        else:
            st.success("사진을 추가할 수 있습니다.")
            st.session_state.photos.append({
                "name": name,
                "type": ''.join(type) if len(type) == 1 else ' '.join(type),
                "year": year,
                "image_url": image_url if image_url else "https://cdn.pixabay.com/photo/2015/02/20/07/57/mango-642957_1280.jpg"
            })



for i in range(0, len(st.session_state.photos), 4):
    row_photos = st.session_state.photos[i:i + 4]
    cols = st.columns(4)
    for j in range(len(row_photos)):
        with cols[j]:
            photo = row_photos[j]
            with st.expander(label="**{}**".format(photo["name"]), expanded=True):
                st.image(photo["image_url"])
                st.text(photo["year"])
                st.text(photo["type"])
                delete_button = st.button(label="삭제", key=(i, j), use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    st.session_state.photos.remove(photo)
                    st.rerun()





