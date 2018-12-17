import xml.etree.ElementTree as ET
from db import *



# Ange vad filen heter som du vill importera till databasen. Se till att de ligger i samma mapp som denna filen.
tree = ET.ElementTree(file='hej.xml')

# Ange program_id för det programmet du vill lägga till. Kolla i databasen vilket ID du skall ange.
program_id = 1


for elem in tree.iterfind('schemaPost'):
    boknings_id = elem.find('bokningsId').text
    date = elem.find('bokadeDatum/bokatDatum').get("datum")
    start = elem.find('bokadeDatum/bokatDatum').get("startTid")
    stop = elem.find('bokadeDatum/bokatDatum').get("slutTid")
    week_day = elem.find('bokadeDatum/bokatDatum').get("dagNamn")
    week_nr = elem.find('bokadeDatum/bokatDatum').get("veckoNummer")
    moment = elem.find('moment').text.strip()
    course_code = elem.find('resursTrad/resursNod[@resursTypId="UTB_KURSINSTANS_GRUPPER"]/resursId').text.strip()[:6]
    

    sql = "INSERT INTO lectures (bokning_id, program_id, datum, start_tid, slut_tid, dagnamn, veckonummer, moment, kurskod)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, (boknings_id, program_id, date, start, stop, week_day, week_nr, moment, course_code))
        db.commit()
        print("Sucess!")

    except:
        # Om det blir fel i importen av filen så ta kommentera bort denna raden för att se felet.
        print("Något gick fel...")
