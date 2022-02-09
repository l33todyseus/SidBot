#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# Creando Database

conn = sqlite3.connect('sid.db')
print("Base abierta exitosamente")

def generatedb():
    conn.execute('''CREATE TABLE PRETRACKER
        (HORA   TEXT NOT NULL,
        PRECIO  REAL   NOT NULL  )
    ''')
