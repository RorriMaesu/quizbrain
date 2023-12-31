#history_questions.py
question_data = [
    {"question": "The Great Wall of China was built to fend off Viking invaders.", "correct_answer": "False"},
    {"question": "Napoleon Bonaparte was a prominent general during the French Revolution.", "correct_answer": "True"},
    {"question": "The Aztecs were a civilization that lived in what is now Mexico.", "correct_answer": "True"},
    {"question": "The first modern Olympic Games were held in Greece in 1896.", "correct_answer": "True"},
    {"question": "The first person to fly solo across the Atlantic Ocean was Charles Lindbergh.", "correct_answer": "True"},
    {"question": "The Wright brothers were the first people to fly a plane.", "correct_answer": "True"},
    {"question": "The first person to vote in a U.S. presidential election was Susan B. Anthony.", "correct_answer": "False"},
    {"question": "The first person to climb Mount Everest was Sir Edmund Hillary.", "correct_answer": "True"},
    {"question": "The first person to walk on the moon was Neil Armstrong.", "correct_answer": "True"},
    {"question": "The first person to swim the English Channel was Gertrude Ederle.", "correct_answer": "True"},
    {"question": "The first person to win the Nobel Prize in Literature was a woman.", "correct_answer": "False"},
    {"question": "Christopher Columbus was the first person to discover the Americas.", "correct_answer": "False"},
    {"question": "Alexander Graham Bell invented the telephone.", "correct_answer": "True"},
    {"question": "Thomas Edison invented the light bulb.", "correct_answer": "True"},
    {"question": "The Wright brothers invented the airplane.", "correct_answer": "False"},
    {"question": "Henry Ford invented the car.", "correct_answer": "False"},
    {"question": "The first computer was invented by a woman.", "correct_answer": "False"},
    {"question": "The internet was invented by a woman.", "correct_answer": "False"},
    {"question": "Johannes Gutenberg invented the printing press.", "correct_answer": "True"},
    {"question": "The compass was invented by a Chinese man.", "correct_answer": "True"},
    {"question": "The wheel was invented by the Mesopotamians.", "correct_answer": "True"},
    {"question": "The alphabet was invented by the Phoenicians.", "correct_answer": "True"},
    {"question": "The number zero was invented by an Indian.", "correct_answer": "True"},
    {"question": "The decimal system was invented by the Greeks.", "correct_answer": "False"},
    {"question": "The steam engine was invented by a British man.", "correct_answer": "True"},
    {"question": "The light bulb was invented by a British man.", "correct_answer": "False"},
    {"question": "The Magna Carta was signed by King John of England in 1215.", "correct_answer": "True"},
    {"question": "The Punic Wars were fought between Rome and Carthage.", "correct_answer": "True"},
    {"question": "Queen Elizabeth II became queen of England in 1952.", "correct_answer": "True"},
    {"question": "The 'Scramble for Africa' occurred in the 18th century.", "correct_answer": "False"},
    {"question": "The Sistine Chapel's ceiling was painted by Leonardo da Vinci.", "correct_answer": "False"},
    {"question": "The Rosetta Stone helped scholars understand and translate Egyptian hieroglyphs.", "correct_answer": "True"},
    {"question": "Galileo was tried and executed for his scientific beliefs.", "correct_answer": "False"},
    {"question": "The Opium Wars took place between China and France.", "correct_answer": "False"},
    {"question": "The Khmer Rouge was a regime that ruled in Vietnam.", "correct_answer": "False"},
    {"question": "The Treaty of Versailles ended World War II.", "correct_answer": "False"},
    {"question": "The city of Constantinople was renamed to Istanbul in the 20th century.", "correct_answer": "True"},
    {"question": "The Eiffel Tower was constructed as the entrance arch for the 1889 World's Fair.", "correct_answer": "True"},
    {"question": "The Peloponnesian War was fought between Athens and Sparta.", "correct_answer": "True"},
    {"question": "The Incan Empire was conquered by Hernán Cortés.", "correct_answer": "False"},
    {"question": "The 'Reign of Terror' is associated with the Russian Revolution.", "correct_answer": "False"},
    {"question": "The ancient Olympic Games were held in honor of the god Apollo.", "correct_answer": "False"},
    {"question": "The 'Doomsday Book' was a record of a survey conducted in England in the 11th century.", "correct_answer": "True"},
    {"question": "The Code of Hammurabi is one of the oldest deciphered writings of significant length in the world.", "correct_answer": "True"},
    {"question": "The Battle of Thermopylae was fought between the Greeks and Persians.", "correct_answer": "True"},
    {"question": "The Colossus of Rhodes was one of the Seven Wonders of the Ancient World.", "correct_answer": "True"},
    {"question": "The Spanish Inquisition was established in the 15th century.", "correct_answer": "True"},
    {"question": "The Hundred Years' War was primarily fought between France and Spain.", "correct_answer": "False"},
    {"question": "The art movement known as 'Cubism' was pioneered by Pablo Picasso and Georges Braque.", "correct_answer": "True"},
    {"question": "The 'Meiji Restoration' in Japan occurred in the 17th century.", "correct_answer": "False"},
    {"question": "The Battle of Trafalgar was won by the British against the French and Spanish navies.", "correct_answer": "True"},
    {"question": "King Henry VIII of England had six wives.", "correct_answer": "True"},
    {"question": "The guillotine was used for the last time in France in the 19th century.", "correct_answer": "False"},
    {"question": "The American Revolutionary War started in 1775.", "correct_answer": "True"},
    {"question": "The first country to grant women the right to vote was the United States.", "correct_answer": "False"},
    {"question": "The Great Fire of London occurred in 1666.", "correct_answer": "True"},
    {"question": "The sinking of the Lusitania directly led to the U.S. entering World War I.", "correct_answer": "False"},
    {"question": "The Dead Sea Scrolls were found in the 1940s.", "correct_answer": "True"},
    {"question": "The Silk Road was a trade route primarily between ancient China and Rome.", "correct_answer": "True"},
    {"question": "The Battle of Little Bighorn is also known as Custer's Last Stand.", "correct_answer": "True"},
    {"question": "Leonardo da Vinci painted the Mona Lisa.", "correct_answer": "True"},
    {"question": "The French Revolution ended in 1799 with the rise of Napoleon Bonaparte.", "correct_answer": "True"},
    {"question": "The Berlin Conference in the late 19th century was about the division of African territories.", "correct_answer": "True"},
    {"question": "The U.S. Declaration of Independence was signed on July 4, 1776.", "correct_answer": "True"},
    {"question": "The Hagia Sophia was originally constructed as a mosque.", "correct_answer": "False"},
    {"question": "The Council of Nicaea in 325 AD established the Nicene Creed.", "correct_answer": "True"},
    {"question": "The Roman Empire was officially declared as a Christian state in 380 AD.", "correct_answer": "True"},
    {"question": "The Treaty of Tordesillas divided the New World between Spain and Portugal.", "correct_answer": "True"},
    {"question": "The Kievan Rus was a medieval state that existed in what is now Ukraine.", "correct_answer": "True"},
    {"question": "The first successful circumnavigation of the Earth was led by Ferdinand Magellan.", "correct_answer": "True"},
    {"question": "The Spanish Civil War took place in the 1920s.", "correct_answer": "False"},
    {"question": "The Battle of Marathon was a conflict between Athens and Persia.", "correct_answer": "True"},
    {"question": "The Gutenberg Bible was the first book printed using movable type.", "correct_answer": "True"},
    {"question": "The Magna Carta limited the power of the English monarchy.", "correct_answer": "True"},
    {"question": "The Bubonic Plague in the 14th century is also referred to as the Spanish Flu.", "correct_answer": "False"},
    {"question": "The Renaissance is often considered to have begun in the city of Florence.", "correct_answer": "True"},
    {"question": "The famous explorer Marco Polo hailed from Spain.", "correct_answer": "False"},
    {"question": "The Seven Years' War was a global conflict that lasted from 1756 to 1763.", "correct_answer": "True"},
    {"question": "The Rosetta Stone is key to understanding ancient Greek scripts.", "correct_answer": "False"},
    {"question": "The Spanish Armada's attempt to invade England was successful.", "correct_answer": "False"},
    {"question": "The Pyramids of Egypt were built by slaves.", "correct_answer": "False"},
    {"question": "Socrates, Plato, and Aristotle are three renowned philosophers from ancient Greece.", "correct_answer": "True"},
    {"question": "The ancient city of Carthage is located in modern-day Tunisia.", "correct_answer": "True"},
    {"question": "The 'Long March' is associated with the history of Russia.", "correct_answer": "False"},
    {"question": "The 'Pax Romana' was a period of relative peace in the Roman Empire lasting around 200 years.", "correct_answer": "True"},
    {"question": "The Vikings originated from modern-day Germany.", "correct_answer": "False"},
    {"question": "The discovery of the Rosetta Stone was instrumental in deciphering Egyptian hieroglyphs.", "correct_answer": "True"},
    {"question": "The ancient Olympic Games were a religious festival dedicated to the god Zeus.", "correct_answer": "True"},
    {"question": "The Colosseum in Rome was primarily used for gladiatorial combat.", "correct_answer": "True"},
    {"question": "The Han Dynasty in China followed the Qin Dynasty.", "correct_answer": "True"},
    {"question": "The Battle of Stalingrad is considered the turning point of World War II in Europe.", "correct_answer": "True"},
    {"question": "The ancient civilization of Mesopotamia was located between the Tigris and Euphrates rivers.", "correct_answer": "True"},
    {"question": "The city of Timbuktu was an ancient center of learning in India.", "correct_answer": "False"},
    {"question": "The 'Black Death' plague in the 14th century is believed to have originated in China.", "correct_answer": "True"},
    {"question": "The city of Petra is located in modern-day Jordan.", "correct_answer": "True"},
    {"question": "The 'Domesday Book' was a record commissioned by William the Conqueror.", "correct_answer": "True"},
    {"question": "Joan of Arc led the French resistance against English occupation during the Hundred Years' War.", "correct_answer": "True"},
    {"question": "The 'Hundred Days' refers to Napoleon's period of return to power after his exile.", "correct_answer": "True"},
    {"question": "The 'Trail of Tears' was a forced relocation of Native Americans in the 19th century.", "correct_answer": "True"},
    {"question": "The 'Boston Tea Party' was a protest against the British government's tax on coffee.", "correct_answer": "False"},
    {"question": "The 'Edict of Milan' in 313 AD proclaimed religious tolerance in the Roman Empire.", "correct_answer": "True"},
    {"question": "The 'Renaissance' period followed the Middle Ages in Europe.", "correct_answer": "True"},
    {"question": "The 'Spanish Inquisition' was primarily concerned with the persecution of Protestants in Spain.", "correct_answer": "False"},
    {"question": "The 'Punic Wars' were fought between Rome and Carthage.", "correct_answer": "True"},
    {"question": "The 'Great Schism' in 1054 split the Christian church into the Roman Catholic and Eastern Orthodox churches.", "correct_answer": "True"},
    {"question": "The Roman Empire was established in 27 BC.", "correct_answer": "True"},
    {"question": "The First Crusade was launched in 1099 AD.", "correct_answer": "True"},
    {"question": "The 'October Revolution' in Russia took place in November according to the Gregorian calendar.", "correct_answer": "True"},
    {"question": "Queen Victoria ruled England for over 60 years.", "correct_answer": "True"},
    {"question": "The Battle of Hastings took place in 1066 AD.", "correct_answer": "True"},
    {"question": "Marco Polo traveled to India and wrote about his adventures.", "correct_answer": "False"},
    {"question": "The Dutch East India Company was established in the 17th century.", "correct_answer": "True"},
    {"question": "The Salem Witch Trials took place in the 18th century.", "correct_answer": "False"},
    {"question": "Archduke Franz Ferdinand's assassination was a significant event leading up to World War I.", "correct_answer": "True"},
    {"question": "The 'Hundred Days of Napoleon' refers to the period after his escape from Elba and before his final defeat at Waterloo.", "correct_answer": "True"},
    {"question": "The 'Wars of the Roses' were fought between the houses of Lancaster and York.", "correct_answer": "True"},
    {"question": "The 'Golden Age of Piracy' was primarily during the 15th century.", "correct_answer": "False"},
    {"question": "The Industrial Revolution began in Britain in the late 18th century.", "correct_answer": "True"},
    {"question": "The 'Protestant Reformation' was initiated by Martin Luther in the 16th century.", "correct_answer": "True"},
    {"question": "The 'Charge of the Light Brigade' took place during the Crimean War.", "correct_answer": "True"},
    {"question": "The 'Boxer Rebellion' was an uprising in India against British rule.", "correct_answer": "False"},
    {"question": "The 'Zulu War' was fought between the British and the Zulu Kingdom in the 19th century.", "correct_answer": "True"},
    {"question": "The 'Waterloo Campaign' was the final action of the Napoleonic Wars.", "correct_answer": "True"},
    {"question": "The city of Venice was known for its powerful navy in the Middle Ages.", "correct_answer": "True"},
    {"question": "The 'Habeas Corpus Act' was passed by the British Parliament in 1679.", "correct_answer": "True"},
    {"question": "The 'East India Company' was founded by the Dutch.", "correct_answer": "False"},
    {"question": "The 'Thirty Years War' took place in the 17th century.", "correct_answer": "True"},
    {"question": "The 'Spanish Reconquista' was completed in 1492.", "correct_answer": "True"},
    {"question": "The 'Berlin Wall' fell in 1989.", "correct_answer": "True"},
    {"question": "The 'Seven Wonders of the Ancient World' include the Great Wall of China.", "correct_answer": "False"},
    {"question": "The 'Athenian democracy' was established in the 5th century BC.", "correct_answer": "True"},
    {"question": "The 'Peace of Westphalia' treaties in 1648 ended the Eighty Years' War.", "correct_answer": "True"},
    {"question": "The 'California Gold Rush' began in 1849.", "correct_answer": "True"},
    {"question": "The 'Apollo 11' mission in 1969 was the first manned mission to land on the Moon.", "correct_answer": "True"},
    {"question": "The 'Anglo-Zanzibar War', fought between Britain and the Zanzibar Sultanate in 1896, is the shortest war in history.", "correct_answer": "True"},
    {"question": "The 'Chernobyl disaster' occurred in 1986.", "correct_answer": "True"},
    {"question": "The 'Vietnam War' ended in 1973.", "correct_answer": "False"},
    {"question": "The 'Mona Lisa' is housed at the Louvre Museum in Paris.", "correct_answer": "True"},
    {"question": "The 'Panama Canal' was opened in 1914.", "correct_answer": "True"},
    {"question": "The 'RMS Titanic' sank on its maiden voyage in 1912.", "correct_answer": "True"}
]
