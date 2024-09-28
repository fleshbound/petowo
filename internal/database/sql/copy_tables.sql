COPY "user"(email, hashed_password, role, name) from '/app/database/data/user.csv' delimiter ';' csv header;
-- home/sheglar/bmstu/petowo/ppo/internal
-- /app/database/data/user.csv
COPY "group" (name) from '/app/database/data/group.csv' delimiter ';' csv header;

COPY Species (name, group_id) from '/app/database/data/species.csv' delimiter ';' csv header;

COPY Breed (name, species_id) from '/app/database/data/breed.csv' delimiter ';' csv header;

COPY animal(user_id, breed_id, name, birth_dt, sex, weight, height, length, has_defects, is_multicolor) from '/app/database/data/animal.csv' delimiter ';' csv header;

COPY Standard (breed_id, country, weight, height, length, has_defects, is_multicolor, weight_delta_percent,
               height_delta_percent, length_delta_percent) from '/app/database/data/standard.csv' delimiter ';' csv header;

COPY Show (species_id, breed_id, standard_id, status, country, show_class, name, is_multi_breed) from '/app/database/data/show.csv' delimiter ';' csv header;

COPY UserShow (show_id, user_id, is_archived) from '/app/database/data/usershow.csv' delimiter ';' csv header;

-- COPY Certificate (animalshow_id, rank)
--     from '/app/database/data/species.csv'
--     delimiter ';'
--     csv header;

COPY AnimalShow (show_id, animal_id, is_archived) from '/app/database/data/animalshow.csv' delimiter ';' csv header;

-- Score
