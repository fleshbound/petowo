\copy "user"(email, hashed_password, role, name) from '/home/sheglar/bmstu/petowo/db/internal/database/data/user.csv' delimiter ';' csv header;
-- home/sheglar/bmstu/petowo/db/internal
\copy "group" (name) from '/home/sheglar/bmstu/petowo/db/internal/database/data/group.csv' delimiter ';' csv header;

\copy Species (name, group_id) from '/home/sheglar/bmstu/petowo/db/internal/database/data/species.csv' delimiter ';' csv header;

\copy Breed (name, species_id) from '/home/sheglar/bmstu/petowo/db/internal/database/data/breed.csv' delimiter ';' csv header;

\copy animal(user_id, breed_id, name, birth_dt, sex, weight, height, length, has_defects, is_multicolor) from '/home/sheglar/bmstu/petowo/db/internal/database/data/animal.csv' delimiter ';' csv header;

-- \copy UserShow (show_id, user_id, is_archived)
--     from '/home/sheglar/bmstu/petowo/db/internal/database/data/usershow.csv'
--     delimiter ';'
--     csv header;
--
-- \copy AnimalShow (show_id, animal_id, is_archived)
--     from '/home/sheglar/bmstu/petowo/db/internal/database/data/animalshow.csv'
--     delimiter ';'
--     csv header;

\copy Standard (breed_id, country, weight, height, length, has_defects, is_multicolor, weight_delta_percent,
               height_delta_percent, length_delta_percent) from '/home/sheglar/bmstu/petowo/db/internal/database/data/standard.csv' delimiter ';' csv header;

-- \copy Certificate (animalshow_id, rank)
--     from '/home/sheglar/bmstu/petowo/db/internal/database/data/species.csv'
--     delimiter ';'
--     csv header;

\copy Show (species_id, breed_id, standard_id, status, country, show_class, name, is_multi_breed) from '/home/sheglar/bmstu/petowo/db/internal/database/data/show.csv' delimiter ';' csv header;

-- Score
