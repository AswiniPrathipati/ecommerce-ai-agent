# -*- coding: utf-8 -*-
"""main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QB_0UPFVhGUKqqhwv72-zA1fXgtwVtvv
"""

from fastapi import FastAPI, Query
from gemini_query import convert_question_to_sql
import sqlite3

app = FastAPI()

@app.get("/ask/")
def ask(question: str = Query(..., description="Your question about sales data")):
    try:
        sql_query = convert_question_to_sql(question)

        conn = sqlite3.connect("ecommerce.db")
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()

        return {
            "question": question,
            "generated_sql": sql_query,
            "result": result
        }

    except Exception as e:
        return {"error": str(e)}