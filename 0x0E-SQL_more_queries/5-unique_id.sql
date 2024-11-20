-- creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS unique_id  (
   id INT DEFAULT 1,
   name VARCHAR(256) NOT NULL,

   CONSTRAINT unique_table_id UNIQUE(id)
)
