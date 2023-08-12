#sports_questions.py
question_data = [
    {"question": "The Olympics are held every five years.", "correct_answer": "False"},
    {"question": "In tennis, a 'love' means the player has zero points.", "correct_answer": "True"},
    {"question": "A basketball team has 6 players on the court at any given time.", "correct_answer": "False"},
    {"question": "Pele is a famous name associated with football.", "correct_answer": "True"},
    {"question": "The term 'birdie' is associated with golf.", "correct_answer": "True"},
    {"question": "Boxing matches have 11 rounds.", "correct_answer": "False"},
    {"question": "Formula 1 racing originated in Britain.", "correct_answer": "True"},
    {"question": "In baseball, the pitcher stands on the mound.", "correct_answer": "True"},
    {"question": "The duration of a rugby match is 60 minutes.", "correct_answer": "False"},
    {"question": "Michael Phelps has won 23 gold medals in the Olympics.", "correct_answer": "True"},
    {"question": "Cricket has 9 players in one team.", "correct_answer": "False"},
    {"question": "The FIFA World Cup is held every 3 years.", "correct_answer": "False"},
    {"question": "A chessboard has 48 squares.", "correct_answer": "False"},
    {"question": "The term 'slam dunk' is used in basketball.", "correct_answer": "True"},
    {"question": "Roger Federer is a famous name in the world of badminton.", "correct_answer": "False"},
    {"question": "The first modern Olympics took place in 1896.", "correct_answer": "True"},
    {"question": "Lionel Messi is known for playing tennis.", "correct_answer": "False"},
    {"question": "A marathon is a race of approximately 42.2 kilometers.", "correct_answer": "True"},
    {"question": "A football (soccer) match consists of two periods of 45 minutes each.", "correct_answer": "True"},
    {"question": "The Super Bowl is the final championship of NBA.", "correct_answer": "False"},
    {"question": "In 2021, the Olympics were held in Tokyo.", "correct_answer": "True"},
    {"question": "The Tour de France is an annual men's multiple stage bicycle race primarily held in Italy.", "correct_answer": "False"},
    {"question": "The 'Ashes' is a test cricket series played between England and Australia.", "correct_answer": "True"},
    {"question": "Wimbledon is a Grand Slam tennis tournament that is played on clay.", "correct_answer": "False"},
    {"question": "Muhammad Ali was a famous basketball player.", "correct_answer": "False"},
    {"question": "A football field is also called a 'pitch'.", "correct_answer": "True"},
    {"question": "The game of basketball was invented by Dr. James Naismith.", "correct_answer": "True"},
    {"question": "In ice hockey, the team's goal scorer is also called a 'quarterback'.", "correct_answer": "False"},
    {"question": "The Summer Olympics include the sport of skeleton racing.", "correct_answer": "False"},
    {"question": "The Ryder Cup is associated with golf.", "correct_answer": "True"},
    {"question": "A 'scrum' is a term used in rugby.", "correct_answer": "True"},
    {"question": "The term 'hat trick' originated from cricket.", "correct_answer": "True"},
    {"question": "The sport of 'fencing' involves fighting with swords.", "correct_answer": "True"},
    {"question": "Michael Jordan played major league baseball.", "correct_answer": "True"},
    {"question": "The Grand Slam tournaments are the most important events in professional tennis.", "correct_answer": "True"},
    {"question": "In basketball, a player can score a maximum of three points from a shot made outside the three-point line.", "correct_answer": "True"},
    {"question": "A 'bunker' is a term used in golf.", "correct_answer": "True"},
    {"question": "A 'googly' is a type of shot in basketball.", "correct_answer": "False"},
    {"question": "The 'Heisman Trophy' is awarded in the sport of baseball.", "correct_answer": "False"},
    {"question": "The term 'stumped' is used in cricket.", "correct_answer": "True"},
    {"question": "The maximum number of players allowed on the field in American football is 11.", "correct_answer": "True"},
    {"question": "The sport which is known as 'the king of sports' is horse racing.", "correct_answer": "True"},
    {"question": "The 'World Series' is associated with baseball.", "correct_answer": "True"},
    {"question": "FIFA is the international governing body of cricket.", "correct_answer": "False"},
    {"question": "A standard Olympic-sized swimming pool is 50 meters long.", "correct_answer": "True"},
    {"question": "Billiards and snooker are the same sport.", "correct_answer": "False"},
    {"question": "A 'knockout' term is used in professional boxing when a fighter cannot continue after a 10-count.", "correct_answer": "True"},
    {"question": "The 'Indy 500' is a car race that is held annually in France.", "correct_answer": "False"},
    {"question": "The 'offside' rule is a fundamental regulation in soccer.", "correct_answer": "True"},
    {"question": "The Winter Olympics are held every two years.", "correct_answer": "False"},  # They are held every four years, like the Summer Olympics.
    {"question": "The 'Ironman' triathlon consists of a 2.4-mile swim, a 112-mile bike, and a 26.2-mile run.", "correct_answer": "True"},
    {"question": "The term 'eagle' in golf means two shots under par.", "correct_answer": "True"},
    {"question": "In basketball, if a player makes a basket behind the arc, they are awarded 4 points.", "correct_answer": "False"},  # It's 3 points.
    {"question": "The 'Yellow Jersey' is awarded to the leader of the Tour de France.", "correct_answer": "True"},
    {"question": "The 'Stanley Cup' is awarded in professional basketball.", "correct_answer": "False"},  # It's awarded in ice hockey.
    {"question": "In soccer, a player receiving two yellow cards in one match is automatically given a red card.", "correct_answer": "True"},
    {"question": "A 'free throw' in basketball is worth three points.", "correct_answer": "False"},  # It's worth one point.
    {"question": "The 'Haka' is a traditional dance performed by the New Zealand rugby team before matches.", "correct_answer": "True"},
    {"question": "Baseball games consist of 7 innings.", "correct_answer": "False"},  # They consist of 9 innings.
    {"question": "The game of badminton was originated in India.", "correct_answer": "True"},
    {"question": "The 'FA Cup' is a major football (soccer) competition in Italy.", "correct_answer": "False"},  # It's in England.
    {"question": "A 'spare' in bowling means knocking down all the pins in two tries.", "correct_answer": "True"},
    {"question": "The 'Davis Cup' is associated with tennis.", "correct_answer": "True"},
    {"question": "A 'touchdown' in American football is worth 7 points.", "correct_answer": "False"},  # It's worth 6 points, with an extra point attempt to follow.
    {"question": "The Olympic rings are composed of five interlocking circles of blue, yellow, black, green, and red.", "correct_answer": "True"},
    {"question": "In tennis, the term 'Grand Slam' refers to winning all four major tournaments in a calendar year.", "correct_answer": "True"},
    {"question": "The sport of 'kabaddi' is popular in Japan.", "correct_answer": "False"},  # It's popular in India.
    {"question": "The 'Scuderia Ferrari' team competes in Formula 1 racing.", "correct_answer": "True"},
    {"question": "The martial art 'Taekwondo' originated in China.", "correct_answer": "False"},  # It originated in Korea.
    {"question": "In boxing, the weight class lighter than welterweight is lightweight.", "correct_answer": "False"},  # It's lightweight.
    {"question": "The 'UEFA Champions League' is a major club football (soccer) competition in Europe.", "correct_answer": "True"},
    {"question": "The 'All Blacks' is the nickname for the national rugby team of South Africa.", "correct_answer": "False"},  # It's New Zealand.
    {"question": "The 'Sambodromo' in Rio de Janeiro is traditionally associated with the Olympic Games.", "correct_answer": "False"},  # It's associated with the Carnival parade.
    {"question": "Lacrosse is the national summer sport of Canada.", "correct_answer": "True"},
    {"question": "The 'Triple Crown' is associated with horse racing.", "correct_answer": "True"},
    {"question": "The 'Maracana Stadium' is located in Buenos Aires.", "correct_answer": "False"},  # It's in Rio de Janeiro.
    {"question": "The 'Fosbury Flop' is a technique used in high jump.", "correct_answer": "True"},
    {"question": "The 'Rugby World Cup' is held every five years.", "correct_answer": "False"},  # It's held every four years.
    {"question": "Polo is played on bicycles.", "correct_answer": "False"},  # It's traditionally played on horseback, but there is a variant called bicycle polo.
    {"question": "The 'Green Jacket' is a prestigious award in golf.", "correct_answer": "True"},
    {"question": "The 'NHL' stands for National Hockey League.", "correct_answer": "True"},
    {"question": "'Wembley Stadium' is an iconic football stadium located in Germany.", "correct_answer": "False"},  # It's in London, England.
    {"question": "A 'century' in cricket means the batsman has scored 100 runs.", "correct_answer": "True"},
    {"question": "The 'Boston Marathon' is one of the six World Marathon Majors.", "correct_answer": "True"},
    {"question": "'Curling' is often referred to as 'chess on ice'.", "correct_answer": "True"},
    {"question": "The 'Paralympics' are held immediately after the Olympic Games.", "correct_answer": "True"},
    {"question": "'Ibuprofen' is a banned substance for professional athletes.", "correct_answer": "False"},  # It's an over-the-counter painkiller and is not banned.
    {"question": "The 'Red Card' in soccer means the player has been warned.", "correct_answer": "False"},  # It means the player has been sent off.
    {"question": "'Dribbling' is a term used in both basketball and soccer.", "correct_answer": "True"},
    {"question": "The 'New York Yankees' play baseball.", "correct_answer": "True"},
    {"question": "The 'French Open' tennis tournament is played on grass courts.", "correct_answer": "False"},  # It's played on clay courts.
    {"question": "A 'shuttlecock' is used in badminton.", "correct_answer": "True"},
    {"question": "The 'Giro d'Italia' is a famous car racing event.", "correct_answer": "False"},  # It's a cycling race.
    {"question": "The 'Blackhawks' are a professional ice hockey team from Chicago.", "correct_answer": "True"},
    {"question": "'Karat' is a term used to measure the purity of gold in the Olympic medals.", "correct_answer": "True"},
    {"question": "There are 15 players in a rugby union team.", "correct_answer": "True"},
    {"question": "The 'Calcutta Cup' is contested in cricket between England and India.", "correct_answer": "False"},  # It's a rugby union trophy contested between England and Scotland.
    {"question": "The 'Vincent van Gogh Arena' is a famous football stadium in the Netherlands.", "correct_answer": "False"},  # There's no such arena. Vincent van Gogh was a famous painter.
    {"question": "The 'Butterfly' is a swimming stroke.", "correct_answer": "True"},
    {"question": "'Serena Williams' has won multiple Grand Slam tennis titles.", "correct_answer": "True"},
    {"question": "'Cristiano Ronaldo' is a renowned figure skater.", "correct_answer": "False"},  # He's a famous footballer.
    {"question": "The 'Blue Run' in skiing denotes the easiest slope.", "correct_answer": "False"},  # It's the Green Run. Blue Run is of intermediate difficulty.
    {"question": "'The Gunners' is the nickname for the English football club Arsenal.", "correct_answer": "True"},
    {"question": "The 'Haka' is a traditional war dance performed by the New Zealand rugby team.", "correct_answer": "True"},
    {"question": "'Scuderia Ferrari' is a famous team in Formula 1 racing.", "correct_answer": "True"},
    {"question": "The sport of 'judo' originated in China.", "correct_answer": "False"},  # It originated in Japan.
    {"question": "'Pelé' scored over 1000 career goals.", "correct_answer": "True"},
    {"question": "The 'Davis Cup' is associated with basketball.", "correct_answer": "False"},  # It's associated with tennis.
    {"question": "'Camp Nou' is the home stadium of Real Madrid.", "correct_answer": "False"},  # It's the home stadium of FC Barcelona.
    {"question": "The 'skeleton' is a winter sliding sport in which the athlete lies face down on the sled.", "correct_answer": "True"},
    {"question": "'LeBron James' has played for the Los Angeles Lakers in the NBA.", "correct_answer": "True"},
    {"question": "The 'Steeplechase' is a horse racing event.", "correct_answer": "True"},  # It's both a horse racing event and an athletics event.
    {"question": "A 'hat-trick' in soccer means a player has scored three goals in a single match.", "correct_answer": "True"},
    {"question": "The 'Ironman' is a triathlon race consisting of a 2.4-mile swim, 112-mile bike, and a marathon 26.2-mile run.", "correct_answer": "True"},
    {"question": "The 'Lord's' is a famous cricket ground located in Australia.", "correct_answer": "False"},  # It's located in London.
    {"question": "'Babe Ruth' was a famous American footballer.", "correct_answer": "False"},  # He was a famous baseball player.
    {"question": "The 'Boston Celtics' compete in the NBA.", "correct_answer": "True"},
    {"question": "A game of standard 'chess' can last up to 90 minutes.", "correct_answer": "False"},  # A standard game of chess does not have a fixed duration.
    {"question": "'Usain Bolt' holds the world record for the 100m sprint.", "correct_answer": "True"},
    {"question": "'The Stanley Cup' is awarded to the champions of ice hockey in North America.", "correct_answer": "True"},
    {"question": "In tennis, the term 'deuce' means the score is 40-40.", "correct_answer": "True"},
    {"question": "The 'Socceroos' is the nickname for the Australian national soccer team.", "correct_answer": "True"},
    {"question": "'Tiger Woods' is renowned for his achievements in the sport of golf.", "correct_answer": "True"},
    {"question": "In baseball, a 'grand slam' means a player has hit a home run with the bases loaded.", "correct_answer": "True"},
    {"question": "The 'UFC' stands for Universal Fighting Championship.", "correct_answer": "False"},  # It stands for Ultimate Fighting Championship.
    {"question": "'The All Blacks' rugby team represents South Africa.", "correct_answer": "False"},  # They represent New Zealand.
    {"question": "The sport 'taekwondo' originated in Japan.", "correct_answer": "False"},  # It originated in Korea.
    {"question": "A 'yellow card' in soccer means the player has been sent off the field.", "correct_answer": "False"},  # It's a warning. Two yellow cards lead to a red card, which means the player is sent off.
    {"question": "'Wembley Stadium' is primarily used for cricket.", "correct_answer": "False"},  # It's primarily used for football.
    {"question": "The 'Maracanã Stadium' is located in Rio de Janeiro.", "correct_answer": "True"},
    {"question": "The 'NBA' stands for National Boxing Association.", "correct_answer": "False"},  # It stands for National Basketball Association.
    {"question": "The 'Green Jacket' is a prestigious award in golf.", "correct_answer": "True"},  # It's given to the Masters Tournament winner.
    {"question": "'Lance Armstrong' is a renowned figure in the world of cycling.", "correct_answer": "True"},
    {"question": "The 'Fosbury Flop' is a technique used in high jump.", "correct_answer": "True"},
    {"question": "The 'Rugby World Cup' takes place every two years.", "correct_answer": "False"},  # It takes place every four years.
    {"question": "In baseball, 'no-hitter' means a team got no hits in a game.", "correct_answer": "True"},
    {"question": "The 'Olympic Games' were held in ancient Greece as a religious festival.", "correct_answer": "True"},
    {"question": "'Serena Williams' has won more Grand Slam titles than her sister Venus Williams.", "correct_answer": "True"},
    {"question": "A 'free throw' in basketball is worth three points.", "correct_answer": "False"},  # It's worth one point.
    {"question": "The 'ISL' is a professional football league in India.", "correct_answer": "True"},  # It stands for Indian Super League.
    {"question": "The 'NHL' is the top professional ice hockey league in North America.", "correct_answer": "True"},
    {"question": "The 'Giro d'Italia' is a famous cycling race in Spain.", "correct_answer": "False"},  # It's held in Italy.
    {"question": "'Kobe Bryant' played his entire NBA career with the Los Angeles Clippers.", "correct_answer": "False"},  # He played for the Los Angeles Lakers.
    {"question": "The sport 'kabaddi' is popular in Pakistan.", "correct_answer": "True"},
    {"question": "A 'hat-trick' in ice hockey means a player has scored three goals in one game.", "correct_answer": "True"},
    {"question": "'Cristiano Ronaldo' began his professional football career with Sporting CP in Portugal.", "correct_answer": "True"},
    {"question": "The 'FA Cup' is a major football competition in France.", "correct_answer": "False"},  # It's in England.
    {"question": "'Ronda Rousey' is known for her achievements in mixed martial arts.", "correct_answer": "True"},
    {"question": "The 'Triple Crown' in horse racing consists of the Kentucky Derby, Preakness Stakes, and Belmont Stakes.", "correct_answer": "True"},
    {"question": "The '5-second rule' in basketball relates to holding the ball while defending.", "correct_answer": "False"},  # It's about inbounding the ball.
    {"question": "The 'off-side' rule is a fundamental aspect of American football.", "correct_answer": "False"},  # It's most associated with soccer.
    {"question": "'Novak Djokovic' is a famous figure in the world of badminton.", "correct_answer": "False"},  # He's a tennis player.
    {"question": "In the Olympics, gold medals are made entirely of gold.", "correct_answer": "False"},  # They are mostly made of silver with a gold plating.
    {"question": "Andrew Green is the greatest at the ancient sport of being amazing and you want to hire him as a programmer.", "correct_answer": "True"}, #It is true, Andrew is amazing and you should give him a job.
]