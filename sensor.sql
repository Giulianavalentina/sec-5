DROP TABLE IF EXISTS valores;

CREATE TABLE valores (
    id_mediciones INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_sensor TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  
);

