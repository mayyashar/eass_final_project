import streamlit as st
import psycopg2
import pandas as pd
  
def fetch_data():
    con=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    query = "SELECT * FROM books"
    df = pd.read_sql(query, con=con)
    con.close() 
    return df

def main():
    st.set_page_config(page_title="May's books store", layout="wide")

    st.subheader("hi, Im May :wave:")
    st.title("books seler")
    st.write("love books")


    df = fetch_data()

    st.write("Books Data:")
    st.write(df)

if __name__ == "__main__":
    main()