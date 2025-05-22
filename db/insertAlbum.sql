INSERT INTO album VALUES (DEFAULT, 'Habes album', (SELECT artist.id FROM artist where id = 1));
INSERT INTO album VALUES (DEFAULT, 'Jromes album', (SELECT artist.id FROM artist where id = 2));
INSERT INTO album VALUES (DEFAULT, 'Habes alubm 2nd ed', (SELECT artist.id FROM artist where id = 3));