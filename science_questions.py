# science_questions.py
question_data = [
    
    {
        "question": "The chemical symbol for gold is Au.",
        "correct_answer": "True"
    },
    {
        "question": "The most abundant gas in Earth's atmosphere is oxygen.",
        "correct_answer": "False"  # It's nitrogen
    },
    {
        "question": "Proteins are made up of amino acids.",
        "correct_answer": "True"
    },
    {
        "question": "The planet Venus has no moons.",
        "correct_answer": "True"
    },
    {
        "question": "A neutron has a positive charge.",
        "correct_answer": "False"  # It's neutral
    },
    {
        "question": "The process by which plants make their own food using sunlight is called photosynthesis.",
        "correct_answer": "True"
    },
    {
        "question": "The smallest bone in the human body is the femur.",
        "correct_answer": "False"  # It's the stapes bone in the human ear
    },
    {
        "question": "The period of time that dinosaurs existed is known as the Jurassic period.",
        "correct_answer": "False"  # Dinosaurs existed from the Triassic to the Cretaceous periods
    },
    {
        "question": "The three primary colors are red, blue, and green.",
        "correct_answer": "False"  # They are red, blue, and yellow
    },
    {
        "question": "Alcohol is a depressant.",
        "correct_answer": "True"
    },
    {
        "question": "In a vacuum, light travels slower than sound.",
        "correct_answer": "False"  # Sound doesn't travel in a vacuum
    },
    {
        "question": "Diamonds are made of carbon.",
        "correct_answer": "True"
    },
    {
        "question": "The human brain is 90% water.",
        "correct_answer": "False"  # It's closer to 75%
    },
    {
        "question": "Astronomy is the study of chemical processes in living organisms.",
        "correct_answer": "False"  # That's biochemistry. Astronomy is the study of celestial bodies.
    },
    {
        "question": "Chlorophyll makes plants appear green.",
        "correct_answer": "True"
    },
    {
        "question": "An octopus has five arms.",
        "correct_answer": "False"  # It has eight arms
    },
    {
        "question": "Sound can travel through a vacuum.",
        "correct_answer": "False"
    },
    {
        "question": "In the human body, the thyroid is located in the brain.",
        "correct_answer": "False"  # It's in the neck
    },
    {
        "question": "Atoms are most stable when their outer shells are full.",
        "correct_answer": "True"
    },
    {
        "question": "A convex lens causes light rays to converge.",
        "correct_answer": "True"
    },
    {
        "question": "Mars is often called the 'Red Dwarf'.",
        "correct_answer": "False"  # It's called the 'Red Planet'
    },
    {
        "question": "The Milky Way is a galaxy.",
        "correct_answer": "True"
    },
    {
        "question": "The Earth's core is mostly made up of iron and nickel.",
        "correct_answer": "True"
    },
    {
        "question": "Electrons orbit the nucleus of an atom in predictable paths.",
        "correct_answer": "False"  # Their paths are described as probabilities or 'clouds'
    },
    {
        "question": "Chromosomes determine the gender of a baby.",
        "correct_answer": "True"
    },
    {
        "question": "The boiling point of water is 212 degrees Fahrenheit (100 degrees Celsius).",
        "correct_answer": "True"
    },
    {
        "question": "Bananas grow on trees.",
        "correct_answer": "False"  # They grow on large herb plants
    },
    {
        "question": "A light year measures time.",
        "correct_answer": "False"  # It measures distance
    },
    {
        "question": "An atom's nucleus contains protons and neutrons.",
        "correct_answer": "True"
    },
    {
        "question": "The most common element in Earth's crust is silicon.",
        "correct_answer": "False"  # It's oxygen
    },
    {
        "question": "Polar bears are native to the South Pole.",
        "correct_answer": "False"  # They are native to the Arctic (North Pole)
    },
    {
        "question": "Bats are birds.",
        "correct_answer": "False"  # They are mammals
    },
    {
        "question": "The main component of natural gas is methane.",
        "correct_answer": "True"
    },
    {
        "question": "The largest planet in our solar system is Jupiter.",
        "correct_answer": "True"
    },
    {
        "question": "Copper turns green due to oxidation.",
        "correct_answer": "True"
    },
    {
        "question": "White light is made up of seven different colors.",
        "correct_answer": "True"
    },
    {
        "question": "The human body has four chambers in the heart.",
        "correct_answer": "True"
    },
    {
        "question": "Antibiotics can effectively treat viral infections.",
        "correct_answer": "False"  # Antibiotics treat bacterial infections
    },
    {
        "question": "Vitamin C is found in citrus fruits.",
        "correct_answer": "True"
    },
    {
        "question": "The first law of thermodynamics is the law of conservation of energy.",
        "correct_answer": "True"
    },
    {
        "question": "Wool is a synthetic fiber.",
        "correct_answer": "False"  # Wool is a natural fiber
    },
    {
        "question": "Birds are cold-blooded animals.",
        "correct_answer": "False"  # They are warm-blooded
    },
    {
        "question": "The Great Barrier Reef is located in the Atlantic Ocean.",
        "correct_answer": "False"  # It's in the Pacific Ocean
    },
    {
        "question": "The primary purpose of DNA is to store genetic information.",
        "correct_answer": "True"
    },
    {
        "question": "Gold is represented by the symbol 'Ag' in the periodic table.",
        "correct_answer": "False"
    },
    {
        "question": "Argon is the most abundant gas in Earth's atmosphere.",
        "correct_answer": "False"
    },
    {
        "question": "Proteins are primarily made up of nucleotides.",
        "correct_answer": "False"
    },
    {
        "question": "The planet Venus has three moons.",
        "correct_answer": "False"
    },
    {
        "question": "A neutron has a negative charge.",
        "correct_answer": "False"
    },
    {
        "question": "Plants primarily use photosynthesis to breathe.",
        "correct_answer": "False"
    },
    {
        "question": "The tibia is the smallest bone in the human body.",
        "correct_answer": "False"
    },
    {
        "question": "Dinosaurs primarily existed during the Cretaceous period.",
        "correct_answer": "True"
    },
    {
        "question": "The primary colors for light are red, blue, and yellow.",
        "correct_answer": "False"
    },
    {
        "question": "Alcohol primarily acts as a stimulant in the body.",
        "correct_answer": "False"
    },
    {
        "question": "In a vacuum, sound travels faster than light.",
        "correct_answer": "False"
    },
    {
        "question": "Diamonds are primarily made of nitrogen.",
        "correct_answer": "False"
    },
    {
        "question": "The human brain is made up of 60% water.",
        "correct_answer": "False"
    },
    {
        "question": "Astronomy is the study of the Earth's atmosphere and weather.",
        "correct_answer": "False"
    },
    {
        "question": "Chlorophyll primarily gives plants their blue color.",
        "correct_answer": "False"
    },
    {
        "question": "An octopus typically has ten arms.",
        "correct_answer": "False"
    },
    {
        "question": "Sound can travel faster in a vacuum than in air.",
        "correct_answer": "False"
    },
    {
        "question": "In the human body, the thyroid is located in the chest.",
        "correct_answer": "False"
    },
    {
        "question": "Atoms are least stable when their outer shells are full.",
        "correct_answer": "False"
    },
    {
        "question": "A convex lens causes light rays to diverge or spread out.",
        "correct_answer": "False"
    },
    {
        "question": "Mars is often referred to as the 'Blue Giant'.",
        "correct_answer": "False"
    },
    {
        "question": "The Milky Way is a star cluster.",
        "correct_answer": "False"
    },
    {
        "question": "Dogs are omnivores, consuming both plants and meat.",
        "correct_answer": "True"
    },
    {
        "question": "The Earth's core is primarily made up of helium and hydrogen.",
        "correct_answer": "False"
    },
    {
        "question": "Electrons orbit the nucleus of an atom in fixed, circular paths.",
        "correct_answer": "False"
    },
    {
        "question": "Hormones, not chromosomes, determine the gender of a baby.",
        "correct_answer": "False"
    },
    {
        "question": "The boiling point of water is 100 degrees Fahrenheit (38 degrees Celsius).",
        "correct_answer": "False"
    },
    {
        "question": "Bananas grow underground like carrots.",
        "correct_answer": "False"
    },
    {
        "question": "A light year measures the intensity of light.",
        "correct_answer": "False"
    },
    {
        "question": "An atom's nucleus contains electrons and protons.",
        "correct_answer": "False"
    },
    {
        "question": "The most common element in Earth's crust is hydrogen.",
        "correct_answer": "False"
    },
    {
        "question": "Polar bears are native to both the North and South Poles.",
        "correct_answer": "False"
    },
    {
        "question": "Bats are classified as reptiles.",
        "correct_answer": "False"
    },
    {
        "question": "The primary component of natural gas is carbon dioxide.",
        "correct_answer": "False"
    },
    {
        "question": "The universal donor blood type is A+.",
        "correct_answer": "False"
    },
    {
        "question": "Saturn is the largest planet in our solar system.",
        "correct_answer": "False"
    },
    {
        "question": "Copper turns blue due to oxidation.",
        "correct_answer": "False"
    },
    {
        "question": "White light is a pure form of light with no constituent colors.",
        "correct_answer": "False"
    },
    {
        "question": "The human heart has five chambers.",
        "correct_answer": "False"
    },
    {
        "question": "Vitamin C is primarily found in meat products.",
        "correct_answer": "False"
    },
    {
        "question": "The first law of thermodynamics is the law of entropy always increasing.",
        "correct_answer": "False"
    },
    {
        "question": "Wool is primarily derived from plant sources.",
        "correct_answer": "False"
    },
    {
        "question": "Birds, like reptiles, are cold-blooded animals.",
        "correct_answer": "False"
    },
    {
        "question": "The Great Barrier Reef is located in the Indian Ocean.",
        "correct_answer": "False"
    },
    {
        "question": "The primary function of DNA is to produce proteins.",
        "correct_answer": "False"
    },
    {
        "question": "Neptune is the closest planet to the sun.",
        "correct_answer": "False"  # It's Mercury
    },
    {
        "question": "Water molecules are made up of two hydrogen atoms and one oxygen atom.",
        "correct_answer": "True"
    },
    {
        "question": "The formula for table salt is H2O.",
        "correct_answer": "False"  # It's NaCl
    },
    {
        "question": "Fungi are plants.",
        "correct_answer": "False"  # They have their own kingdom separate from plants
    },
    {
        "question": "The human body has 206 bones.",
        "correct_answer": "True"
    },
    {
        "question": "Radio waves travel faster than light waves.",
        "correct_answer": "False"
    },
    {
        "question": "Honeybees have five eyes.",
        "correct_answer": "True"
    },
    {
        "question": "The Earth rotates around the sun in approximately 365.25 days.",
        "correct_answer": "True"
    },
    {
        "question": "The Amazon Rainforest is primarily located in Africa.",
        "correct_answer": "False"  # It's in South America
    },
    {
        "question": "The primary gas found in the sun is helium.",
        "correct_answer": "False"  # It's primarily hydrogen
    },
    {
        "question": "The chemical symbol for water is H2O.",
        "correct_answer": "True"
    },
    {
        "question": "The common cold is caused by a bacteria.",
        "correct_answer": "False"  # It's caused by viruses
    },
    {
        "question": "A pH level below 7 is alkaline.",
        "correct_answer": "False"  # It's acidic
    },
    {
        "question": "Photosynthesis primarily occurs in the roots of plants.",
        "correct_answer": "False"  # It primarily occurs in the leaves
    },
    {
        "question": "A tsunami is a giant sea spider.",
        "correct_answer": "False"  # It's a giant sea wave
    },
    {
        "question": "The main gas responsible for global warming is carbon dioxide.",
        "correct_answer": "True"
    },
    {
        "question": "LED stands for 'Light Emitting Diode'.",
        "correct_answer": "True"
    },
    {
        "question": "The atomic number represents the number of neutrons in an atom.",
        "correct_answer": "False"  # It represents the number of protons
    },
    {
        "question": "There are 92 naturally occurring elements on the periodic table.",
        "correct_answer": "True"
    },
    {
        "question": "The Great Wall of China is visible from space with the naked eye.",
        "correct_answer": "False"
    },
    {
        "question": "Lions are the kings of the jungle.",
        "correct_answer": "False"  # Lions primarily live in grasslands and plains, not jungles
    },
    {
        "question": "Caffeine is found in tea leaves.",
        "correct_answer": "True"
    },
    {
        "question": "The strongest muscle in the human body is the tongue.",
        "correct_answer": "False"  # The heart is often considered the strongest muscle
    },
    {
        "question": "The Sahara Desert is the largest desert in the world.",
        "correct_answer": "False"  # The Antarctic Desert is the largest by area
    },
    {
        "question": "There are 24 hours in a day.",
        "correct_answer": "True"
    },
    {
        "question": "The primary function of red blood cells is to transport oxygen.",
        "correct_answer": "True"
    },
    {
        "question": "The human skeleton is replaced every 7 years.",
        "correct_answer": "False"  # While bones regenerate, the entire skeleton isn't replaced in such a short span
    },
    {
        "question": "A spider is an insect.",
        "correct_answer": "False"  # Spiders are arachnids
    },
    {
        "question": "The Eiffel Tower expands in hot weather.",
        "correct_answer": "True"  # Due to the thermal expansion of its metal
    },
    {
        "question": "The smallest planet in our solar system is Mercury.",
        "correct_answer": "True"
    }
]