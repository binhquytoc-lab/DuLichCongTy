import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Quản trị", page_icon="📋")

st.title("📋 Danh sách đăng ký du lịch")

conn = get_connection()

sql = "SELECT * FROM dangky_dulich ORDER BY id DESC"

df = pd.read_sql(sql, conn)

conn.close()

st.dataframe(df, use_container_width=True)
