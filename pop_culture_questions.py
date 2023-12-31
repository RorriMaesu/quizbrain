#pop_culture_questions.py
question_data = [
    {"question": "Beyoncé was a member of the group Destiny's Child.", "correct_answer": "True"},
    {"question": "The Beatles were formed in Manchester.", "correct_answer": "False"},
    {"question": "'Despacito' is a hit song by Ed Sheeran.", "correct_answer": "False"},
    {"question": "Lady Gaga's real name is Stefani Joanne Angelina Germanotta.", "correct_answer": "True"},
    {"question": "Ariana Grande began her career on the TV show 'Victorious'.", "correct_answer": "True"},
    {"question": "The TV show 'Keeping Up with the Kardashians' began airing in 2010.", "correct_answer": "False"},
    {"question": "Rihanna is originally from Barbados.", "correct_answer": "True"},
    {"question": "The 'Mona Lisa' is housed in the Louvre Museum in Paris.", "correct_answer": "True"},
    {"question": "Marilyn Monroe starred in the movie 'Gone with the Wind'.", "correct_answer": "False"},
    {"question": "Billie Eilish's debut album is titled 'Bad Guy'.", "correct_answer": "False"},
    {"question": "The character Jack Dawson, from the movie 'Titanic', is played by Brad Pitt.", "correct_answer": "False"},
    {"question": "The song 'Shape of You' is sung by Justin Bieber.", "correct_answer": "False"},
    {"question": "Taylor Swift's album '1989' was released in the year 1989.", "correct_answer": "False"},
    {"question": "The character 'Spider-Man' was first introduced by Marvel Comics in the 1960s.", "correct_answer": "True"},
    {"question": "The novel 'Fifty Shades of Grey' was written by J.K. Rowling.", "correct_answer": "False"},
    {"question": "'WAP' is a hit song by Megan Thee Stallion and Cardi B.", "correct_answer": "True"},
    {"question": "The 'Floss' dance move became popular because of the video game Fortnite.", "correct_answer": "True"},
    {"question": "Kanye West's album 'Graduation' was released after 'My Beautiful Dark Twisted Fantasy'.", "correct_answer": "False"},
    {"question": "The movie 'The Social Network' is based on the creation of Twitter.", "correct_answer": "False"},
    {"question": "Elon Musk is the founder of Amazon.", "correct_answer": "False"},
    {"question": "Oprah Winfrey ran for the U.S. presidency in 2016.", "correct_answer": "False"},
    {"question": "'Stranger Things' is set in the fictional town of Hawkins.", "correct_answer": "True"},
    {"question": "The character 'Wonder Woman' hails from the island of Themyscira.", "correct_answer": "True"},
    {"question": "The 'Macarena' dance originated in the 2010s.", "correct_answer": "False"},
    {"question": "Michael Jackson is known as the 'King of Rock'.", "correct_answer": "False"},
    {"question": "The 2020s viral dance trend 'Renegade' originated on TikTok.", "correct_answer": "True"},
    {"question": "Dua Lipa's song 'Don't Start Now' is from her debut album.", "correct_answer": "False"},
    {"question": "'Baby Yoda' is the official name of the character from 'The Mandalorian'.", "correct_answer": "False"},
    {"question": "The TV show 'Game of Thrones' is based on the book series 'A Song of Ice and Fire'.", "correct_answer": "True"},
    {"question": "The 'Dab' dance move was popularized by the singer Rihanna.", "correct_answer": "False"},
    {"question": "The character 'Iron Man' is also known as Steve Rogers.", "correct_answer": "False"},
    {"question": "The artist who sang 'Rolling in the Deep' is Adele.", "correct_answer": "True"},
    {"question": "The TV show 'Breaking Bad' is set in the city of Albuquerque.", "correct_answer": "True"},
    {"question": "Jennifer Aniston played the character of Monica in the TV show 'F.R.I.E.N.D.S'.", "correct_answer": "False"},
    {"question": "The song 'Old Town Road' is by Lil Nas X.", "correct_answer": "True"},
    {"question": "The 'Ice Bucket Challenge' was a viral trend in 2019.", "correct_answer": "False"},
    {"question": "The first iPhone was released in 2005.", "correct_answer": "False"},
    {"question": "Billie Eilish's brother, Finneas, is also her musical collaborator.", "correct_answer": "True"},
    {"question": "Kendall Jenner is the eldest of the Jenner/Kardashian siblings.", "correct_answer": "False"},
    {"question": "The movie 'La La Land' stars Emma Stone and Ryan Reynolds.", "correct_answer": "False"},
    {"question": "Britney Spears' debut single was 'Oops!... I Did It Again'.", "correct_answer": "False"},
    {"question": "The video game 'Among Us' was released in 2020.", "correct_answer": "False"},
    {"question": "The novel 'The Great Gatsby' was written by Ernest Hemingway.", "correct_answer": "False"},
    {"question": "Kobe Bryant played for the Los Angeles Lakers.", "correct_answer": "True"},
    {"question": "The song 'Hotline Bling' is by Kendrick Lamar.", "correct_answer": "False"},
    {"question": "The 2010s dance trend 'Gangnam Style' originated in China.", "correct_answer": "False"},
    {"question": "Tom Holland has portrayed the character 'Spider-Man' in the Marvel Cinematic Universe.", "correct_answer": "True"},
    {"question": "The animated film 'Shrek' was released in the 1990s.", "correct_answer": "False"},
    {"question": "The singer known as the 'Material Girl' is Madonna.", "correct_answer": "True"},
    {"question": "The 2020 Netflix documentary 'Tiger King' focuses on the life of Joe Biden.", "correct_answer": "False"},
    {"question": "The TV show 'Friends' aired its last episode in 2004.", "correct_answer": "True"},
    {"question": "'The Fresh Prince of Bel-Air' is a sitcom that starred Will Smith.", "correct_answer": "True"},
    {"question": "The song 'Uptown Funk' is by Bruno Mars and Mark Ronson.", "correct_answer": "True"},
    {"question": "The character 'Lara Croft' is associated with the video game series 'Tomb Raider'.", "correct_answer": "True"},
    {"question": "The Beatles released an album called 'Abbey Road'.", "correct_answer": "True"},
    {"question": "'The Hunger Games' is a series of novels written by Suzanne Collins.", "correct_answer": "True"},
    {"question": "Michael Jordan played the majority of his NBA career with the Chicago Bulls.", "correct_answer": "True"},
    {"question": "'The Witcher' series of books was written by Andrzej Sapkowski.", "correct_answer": "True"},
    {"question": "Elvis Presley was known as the 'King of Jazz'.", "correct_answer": "False"},
    {"question": "The 2010s dance trend 'Harlem Shake' became a viral sensation due to YouTube.", "correct_answer": "True"},
    {"question": "The song 'Believer' is by Imagine Dragons.", "correct_answer": "True"},
    {"question": "Kurt Cobain was the lead singer of the band Nirvana.", "correct_answer": "True"},
    {"question": "The animated film 'Frozen' features the song 'Let It Go'.", "correct_answer": "True"},
    {"question": "The 'Twilight' series of books was written by J.K. Rowling.", "correct_answer": "False"},
    {"question": "The TV series 'Parks and Recreation' is set in the fictional town of Pawnee, Indiana.", "correct_answer": "True"},
    {"question": "The song 'Smooth' is a collaboration between Santana and Rob Thomas.", "correct_answer": "True"},
    {"question": "The movie 'Black Panther' is set in the fictional African country of Wakanda.", "correct_answer": "True"},
    {"question": "The 'K-pop' genre originates from Japan.", "correct_answer": "False"},
    {"question": "The 'MacBook' is a line of laptops produced by Microsoft.", "correct_answer": "False"},
    {"question": "The social media platform 'TikTok' originated in the United States.", "correct_answer": "False"},
    {"question": "The TV series 'Sherlock', starring Benedict Cumberbatch, is set in modern-day London.", "correct_answer": "True"},
    {"question": "The video game 'The Legend of Zelda' primarily features a protagonist named Zelda.", "correct_answer": "False"},
    {"question": "The artist known for the hit 'Purple Rain' is Prince.", "correct_answer": "True"},
    {"question": "The 'PlayStation' gaming console is produced by Nintendo.", "correct_answer": "False"},
    {"question": "The song 'Bad Guy' is by Billie Eilish.", "correct_answer": "True"},
    {"question": "The TV series 'The Office (US)' was originally based on a UK series of the same name.", "correct_answer": "True"},
    {"question": "In the TV show 'Breaking Bad', the blue crystal sold is actual methamphetamine.", "correct_answer": "False"},
    {"question": "The 'MCU' stands for 'Marvel Cinematic Universe'.", "correct_answer": "True"},
    {"question": "The movie 'The Devil Wears Prada' stars Meryl Streep and Anne Hathaway.", "correct_answer": "True"},
    {"question": "The 'Xbox' gaming console is produced by Sony.", "correct_answer": "False"},
    {"question": "The song 'Thinking Out Loud' is by Ed Sheeran.", "correct_answer": "True"},
    {"question": "'The Last of Us' is a popular video game series developed by Naughty Dog.", "correct_answer": "True"},
    {"question": "'Netflix and Chill' became a popular internet slang term in the 2010s.", "correct_answer": "True"},
    {"question": "The song 'Livin' on a Prayer' is by Aerosmith.", "correct_answer": "False"},
    {"question": "The movie 'The Godfather' was directed by Francis Ford Coppola.", "correct_answer": "True"},
    {"question": "Stan Lee made cameo appearances in Marvel Cinematic Universe movies.", "correct_answer": "True"},
    {"question": "The TV show 'How I Met Your Mother' aired for 12 seasons.", "correct_answer": "False"},
    {"question": "Michael Scott is a character from the TV show 'Parks and Recreation'.", "correct_answer": "False"},
    {"question": "'Wonderwall' is a song by the band Oasis.", "correct_answer": "True"},
    {"question": "'A Song of Ice and Fire' series was written by George R. R. Martin.", "correct_answer": "True"},
    {"question": "BTS is a famous pop band from South Korea.", "correct_answer": "True"},
    {"question": "The movie 'A Star Is Born' starring Lady Gaga and Bradley Cooper was released in 2018.", "correct_answer": "True"},
    {"question": "The 'Wii' gaming console is produced by Microsoft.", "correct_answer": "False"},
    {"question": "The movie 'Avatar' directed by James Cameron was released in 2009.", "correct_answer": "True"},
    {"question": "The 'DC' in 'DC Comics' stands for 'Detective Comics'.", "correct_answer": "True"},
    {"question": "The Mona Lisa painting was created by Leonardo da Vinci.", "correct_answer": "True"},
    {"question": "Mickey Mouse was created by Walt Disney.", "correct_answer": "True"},
    {"question": "The 'Harry Potter' series consists of 7 books.", "correct_answer": "True"},
    {"question": "'TikTok' is a social media platform primarily known for short-form video content.", "correct_answer": "True"},
    {"question": "'Game of Thrones' TV series has a total of 8 seasons.", "correct_answer": "True"},
    {"question": "In the TV show 'The Mandalorian', the character Grogu is commonly referred to as 'Baby Yoda'.", "correct_answer": "True"},
    {"question": "The song 'Blinding Lights' is by The Weeknd.", "correct_answer": "True"},
    {"question": "'The Simpsons' TV show first aired in the 1980s.", "correct_answer": "True"},
    {"question": "'Black Panther' was the first Marvel film to win an Oscar.", "correct_answer": "True"},
    {"question": "Ariana Grande's song '7 Rings' was inspired by 'The Sound of Music'.", "correct_answer": "True"},
    {"question": "'Super Mario Bros.' is a video game series developed by Sega.", "correct_answer": "False"},
    {"question": "The main character in the 'Indiana Jones' film series is played by Harrison Ford.", "correct_answer": "True"},
    {"question": "The song 'Single Ladies' is by Rihanna.", "correct_answer": "False"},
    {"question": "The TV series 'Mindhunter' is based on real-life events and characters.", "correct_answer": "True"},
    {"question": "'The Umbrella Academy' TV series is based on a comic book series of the same name.", "correct_answer": "True"},
    {"question": "The character 'Wolverine' is portrayed by Hugh Jackman in the X-Men movies.", "correct_answer": "True"},
    {"question": "'Friends' TV show was set in the city of Los Angeles.", "correct_answer": "False"},
    {"question": "The movie 'Casablanca' features the famous line 'Play it again, Sam'.", "correct_answer": "False"},
    {"question": "'Spotify' is a music streaming platform founded in Sweden.", "correct_answer": "True"},
    {"question": "'Stranger Things' TV series is produced by HBO.", "correct_answer": "False"},
    {"question": "The character 'Loki' from the Marvel Cinematic Universe is played by Tom Hiddleston.", "correct_answer": "True"},
    {"question": "'Instagram' is a photo-sharing social media platform that was launched in 2010.", "correct_answer": "True"},
]