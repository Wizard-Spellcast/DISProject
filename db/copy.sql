COPY books(bookID, authors, 
average_rating, isbn, isbn13, 
language_code, num_pages, 
ratings_count, text_review_count, 
publication_date, publisher)

FROM 'C:\Users\asbjornvm\Downloads\archive\books.csv'
DELIMITER ','
CSV HEADER;
