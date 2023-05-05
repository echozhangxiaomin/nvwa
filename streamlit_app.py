
import streamlit as st

def main():
  st.title("欢迎使用 Streamlit")
  st.header("这是一个简单的示例程序")

  if st.button("点击这里"):
    st.write("你好，世界！")

if __name__ == "__main__":
  main()
