-- write your tables in here. 

--  child
DROP TABLE IF EXISTS albums;
-- parent
DROP TABLE IF EXISTS artists;

-- album (child) inherits artists (parent)
-- or the child has no genes to inherit

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id)
);

