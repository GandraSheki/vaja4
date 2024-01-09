# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:18:47 2024

@author: dragan
"""

import pandas as pd
import pymysql  # predpostavljamo, da uporabljate MySQL, vendar lahko prilagodite glede na vašo podatkovno bazo

# Povezava s podatkovno bazo
connection = pymysql.connect(host='localhost', user='root', password='Sheki976!', database='vaja_3_tpb')
query = """
    SELECT
        dtd.ime_sportnika,
        YEAR(dtd.start_time) AS leto,
        MONTH(dtd.start_time) AS mesec,
        SUM(dtd.distance_metar / 1000) AS Skupaj_kilometri,
        SUM(dtd.total_time_seconds) AS skupaj_trajanje_aktivnosti_sek,
        SUM(dod.calories) AS poraba_kalorij
    FROM
        dimtimedistance dtd
    JOIN
        dimotherdata dod ON dtd.IdDimTimeDistance = dod.idDimOtherData
    GROUP BY
        dtd.ime_sportnika, YEAR(dtd.start_time), MONTH(dtd.start_time)
    ORDER BY
        dtd.ime_sportnika, YEAR(dtd.start_time), MONTH(dtd.start_time);
"""

# Izvedba poizvedbe in shranjevanje rezultatov v pandas DataFrame
df = pd.read_sql_query(query, connection)

# Zapiranje povezave
connection.close()

# Shranjevanje rezultatov v CSV datoteko
df.to_csv('factactivity.csv', index=False)
