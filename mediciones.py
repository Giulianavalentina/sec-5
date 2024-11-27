import sqlite3
from serial import Serial


bd = sqlite3.connect(
           "sensor.sqlite",
           detect_types=sqlite3.PARSE_DECLTYPES
       )
bd.row_factory = sqlite3.Row
with open("sensor.sql") as f:
   bd.executescript(f.read())



puerto = Serial("/dev/ttyUSB0", 9600)
puerto.readline() # descartar primer renglon


try:
   while True:
       lineaRenglon = puerto.readline()
       lineaRenglon = lineaRenglon.decode()
       lineaRenglon.strip()
       valorStr = lineaRenglon.split(" ")[1]
       valor = int(valorStr)


       print(valor)
       bd.execute(
           "INSERT INTO valores (valor_sensor) VALUES (?)",
           (valor, ),
       )
       bd.commit()


except KeyboardInterrupt:
   print('fin')
   bd.close()