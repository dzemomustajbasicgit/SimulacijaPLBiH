lista_klubova = ["FK Sarajevo", "FK Željezničar", "FK Borac Banja Luka", "HŠK Zrinjski Mostar", "FK Velež Mostar", "NK GOŠK Gabela", "FK Igman Konjic", "FK Tuzla City", "FK Zvijezda 09", "HNK Posušje", "NK Široki Brijeg", "FK Sloga Doboj"]
lista_stadiona = ["Asim Ferhatović Hase", "Grbavica", "GS Banja Luka", "Pod Bijelim Brijegom", "Rođeni", "Perica Pero Pavlović", "GS Konjic", "Tušanj", "GS Ugljevik", "Mokri Dolac", "Pecara", "Luke"]
dict_igraci = {
    'Muhamed Sahinovic': (20, 'GK', 'FK Sarajevo'), 
    'Miomir Djurickovic': (26, 'CB', 'FK Sarajevo'), 
    'Marin Anicic': (34, 'CB', 'FK Sarajevo'), 
    'Elvir Durakovic': (23, 'LB', 'FK Sarajevo'), 
    'Amar Beganovic': (24, 'RB', 'FK Sarajevo'), 
    'Muhamed Buljubasic': (19, 'DMF', 'FK Sarajevo'), 
    'Edin Julardzija': (22, 'CMF', 'FK Sarajevo'), 
    'Daniel Avramovski': (28, 'AMF', 'FK Sarajevo'), 
    'Adalberto Penaranda': (26, 'LW', 'FK Sarajevo'), 
    'Ajdin Hasic': (22, 'RW', 'FK Sarajevo'), 
    'Renan Oliveira': (26, 'CF', 'FK Sarajevo'), 
    'Vedad Muftic': (22, 'GK', 'FK Željezničar'), 
    'Edin Cocalic': (35, 'CB', 'FK Željezničar'), 
    'Amar Drina': (21, 'CB', 'FK Željezničar'), 
    'Irfan Jasarevic': (28, 'LB', 'FK Željezničar'), 
    'Mehmed Cosic': (26, 'RB', 'FK Željezničar'), 
    'Edin Rustemovic': (30, 'DMF', 'FK Željezničar'), 
    'Nedim Mekic': (28, 'CMF', 'FK Željezničar'), 
    'Semir Stilic': (36, 'AMF', 'FK Željezničar'), 
    'Joseph Amoah': (21, 'LW', 'FK Željezničar'), 
    'Aleksandar Boljevic': (27, 'RW', 'FK Željezničar'), 
    'Sulejman Krpic': (32, 'CF', 'FK Željezničar'), 
    'Milan Mijatovic': (36, 'GK', 'FK Borac Banja Luka'), 
    'Ranko Jokic': (24, 'CB', 'FK Borac Banja Luka'), 
    'Maks Celic': (27, 'CB', 'FK Borac Banja Luka'), 
    'Sebastian Herrera': (28, 'LB', 'FK Borac Banja Luka'), 
    'Zoran Kvrzic': (35, 'RB', 'FK Borac Banja Luka'), 
    'Srdjan Grahovac': (31, 'DMF', 'FK Borac Banja Luka'), 
    'Stefan Ficovic': (25, 'CMF', 'FK Borac Banja Luka'), 
    'Vasilije Terzic': (24, 'AMF', 'FK Borac Banja Luka'), 
    'Jakov Blagaic': (23, 'LW', 'FK Borac Banja Luka'), 
    'Enver Kulasin': (20, 'RW', 'FK Borac Banja Luka'), 
    'Milan Makaric': (28, 'CF', 'FK Borac Banja Luka'),
    'Marko Maric': (27, 'GK', 'HŠK Zrinjski Mostar'),
    'Stipe Radic': (23, 'CB', 'HŠK Zrinjski Mostar'),
    'Slobodan Jakovljevic': (34, 'CB', 'HŠK Zrinjski Mostar'),
    'Luka Marin': (25, 'LB', 'HŠK Zrinjski Mostar'),
    'Josip Corluka': (28, 'RB', 'HŠK Zrinjski Mostar'),
    'Filip Bradarac': (31, 'DMF', 'HŠK Zrinjski Mostar'),
    'Zvonimir Kozulj': (30, 'CMF', 'HŠK Zrinjski Mostar'),
    'Tomislav Kis': (29, 'AMF', 'HŠK Zrinjski Mostar'),
    'Matija Malekinusic': (24, 'RW', 'HŠK Zrinjski Mostar'),
    'Mario Cuze': (23, 'LW', 'HŠK Zrinjski Mostar'),
    'Nemanja Bilbija': (33, 'CF', 'HŠK Zrinjski Mostar'),
    'Osman Hadzikic': (27, 'GK', 'FK Velež Mostar'),
    'Bruno Oliveira': (27, 'CB', 'FK Velež Mostar'),
    'Ante Hrkac': (31, 'CB', 'FK Velež Mostar'),
    'Klemen Sturm': (29, 'LB', 'FK Velež Mostar'),
    'Ante Orec': (22, 'RB', 'FK Velež Mostar'),
    'Dino Halilovic': (25, 'DMF', 'FK Velež Mostar'),
    'Omar Prses': (28, 'CMF', 'FK Velež Mostar'),
    'Mihael Mlinaric': (23, 'AMF', 'FK Velež Mostar'),
    'Asmir Suljic': (27, 'LW', 'FK Velež Mostar'),
    'Giorgi Guliashvili': (27, 'RW', 'FK Velež Mostar'),
    'Nermin Haskic': (27, 'CF', 'FK Velež Mostar'),
    'Adnan Bobic': (36, 'GK', 'NK GOŠK Gabela'),
    'Vasilije Radenovic': (29, 'CB', 'NK GOŠK Gabela'),
    'Jure Obsivac': (33, 'CB', 'NK GOŠK Gabela'),
    'Mateo Ramljak': (22, 'LB', 'NK GOŠK Gabela'),
    'Tino Bradara': (25, 'RB', 'NK GOŠK Gabela'),
    'Faruk Gogic': (24, 'DMF', 'NK GOŠK Gabela'),
    'Aldin Cajic': (31, 'CMF', 'NK GOŠK Gabela'),
    'Marko Musulin': (24, 'AMF', 'NK GOŠK Gabela'),
    'Stanisa Mandic': (28, 'LW', 'NK GOŠK Gabela'),
    'Leo Jankovic': (23, 'RW', 'NK GOŠK Gabela'),
    'Esmir Hasukic': (22, 'CF', 'NK GOŠK Gabela'),
    'Aldin Ceman': (28, 'GK', 'FK Igman Konjic'),
    'Amer Dupovac': (32, 'CB', 'FK Igman Konjic'),
    'Enes Sipovic': (33, 'CB', 'FK Igman Konjic'),
    'Marko Cubrilo': (25, 'LB', 'FK Igman Konjic'),
    'Mirko Oremus': (35, 'RB', 'FK Igman Konjic'),
    'Armin Besagic': (25, 'DMF', 'FK Igman Konjic'),
    'Petar Bojo': (25, 'CMF', 'FK Igman Konjic'),
    'Darko Bodul': (34, 'AMF', 'FK Igman Konjic'),
    'Stefan Denkovic': (32, 'LW', 'FK Igman Konjic'),
    'Anel Hebibovic': (33, 'RW', 'FK Igman Konjic'),
    'Mirsad Ramic': (30, 'CF', 'FK Igman Konjic'),
    'Nevres Fejzic': (33, 'GK', 'FK Tuzla City'),
    'Mustafa Sukilovic': (20, 'CB', 'FK Tuzla City'),
    'Faruk Bihorac': (27, 'CB', 'FK Tuzla City'),
    'Dusan Hodzic': (30, 'LB', 'FK Tuzla City'),
    'Benjamin Colic': (32, 'RB', 'FK Tuzla City'),
    'Huso Karjasevic': (26, 'DMF', 'FK Tuzla City'),
    'Amer Ordagic': (30, 'CMF', 'FK Tuzla City'),
    'Mirzad Mehanovic': (30, 'AMF', 'FK Tuzla City'),
    'Alen Masovic': (29, 'LW', 'FK Tuzla City'),
    'Djordje Pantelic': (23, 'RW', 'FK Tuzla City'),
    'Irfan Hadzic': (30, 'CF', 'FK Tuzla City'),
    'Milan Jelovac': (30, 'GK', 'FK Zvijezda 09'),
    'Stefan Sapic': (26, 'CB', 'FK Zvijezda 09'),
    'Predrag Ristanovic': (22, 'CB', 'FK Zvijezda 09'),
    'Marko Jevremovic': (27, 'LB', 'FK Zvijezda 09'),
    'Luka Jankovic': (21, 'RB', 'FK Zvijezda 09'),
    'Sasa Tomanovic': (34, 'DMF', 'FK Zvijezda 09'),
    'Nebojsa Gavric': (32, 'CMF', 'FK Zvijezda 09'),
    'Sedad Subasic': (22, 'AMF', 'FK Zvijezda 09'),
    'Petar Karaklajic': (23, 'LW', 'FK Zvijezda 09'),
    'Milan Savic': (23, 'RW', 'FK Zvijezda 09'),
    'Kayode Saliman': (20, 'CF', 'FK Zvijezda 09'),
    'Franko Kolic': (20, 'GK', 'HNK Posušje'),
    'Jovan Pavlovic': (23, 'CB', 'HNK Posušje'),
    'Branko Vrgoc': (33, 'CB', 'HNK Posušje'),
    'Ante Bekavac': (23, 'LB', 'HNK Posušje'),
    'Frane Maglica': (26, 'RB', 'HNK Posušje'),
    'Zvonimir Begic': (33, 'DMF', 'HNK Posušje'),
    'Karlo Kamenar': (29, 'CMF', 'HNK Posušje'),
    'Arijan Brkovic': (22, 'AMF', 'HNK Posušje'),
    'Gabrijel Boban': (34, 'LW', 'HNK Posušje'),
    'Vinko Rozic': (20, 'RW', 'HNK Posušje'),
    'Nikola Mandic': (28, 'CF', 'HNK Posušje'),
    'Josip Bender': (28, 'GK', 'NK Široki Brijeg'),
    'Ivan Saravanja': (27, 'CB', 'NK Široki Brijeg'),
    'Mate Suto': (27, 'CB', 'NK Široki Brijeg'),
    'Mihael Kupresak': (22, 'LB', 'NK Široki Brijeg'),
    'Adam Benic': (23, 'RB', 'NK Široki Brijeg'),
    'Marko Capan': (19, 'DMF', 'NK Široki Brijeg'),
    'Marijan Cavar': (25, 'CMF', 'NK Široki Brijeg'),
    'Simun Mikolcic': (19, 'AMF', 'NK Široki Brijeg'),
    'Luka Mamic': (21, 'LW', 'NK Široki Brijeg'),
    'Cyrille Kpan': (25, 'RW', 'NK Široki Brijeg'),
    'Stephen Chinedu': (23, 'CF', 'NK Široki Brijeg'),
    'Nemanja Scekic': (31, 'GK', 'FK Sloga Doboj'),
    'Milos Nikolic': (29, 'CB', 'FK Sloga Doboj'),
    'Albin Omic': (19, 'CB', 'FK Sloga Doboj'),
    'Srdjan Grabez': (32, 'LB', 'FK Sloga Doboj'),
    'Sinisa Dujakovic': (32, 'RB', 'FK Sloga Doboj'),
    'Dejan Popara': (20, 'DMF', 'FK Sloga Doboj'),
    'Stasa Bastic': (21, 'CMF', 'FK Sloga Doboj'),
    'Ajdin Redzic': (26, 'AMF', 'FK Sloga Doboj'),
    'Danilo Sipovac': (23, 'LW', 'FK Sloga Doboj'),
    'Toni Jovic': (31, 'RW', 'FK Sloga Doboj'),
    'Dejan Vidic': (30, 'CF', 'FK Sloga Doboj')
    }
