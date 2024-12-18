create type country as enum(
    'Afghanistan',
        'Albania',
        'Algeria',
        'Andorra',
        'Angola',
        'Antigua & Deps',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bermuda',
        'Bhutan',
        'Bolivia',
        'Bosnia Herzegovina',
        'Botswana',
        'Brazil',
        'Brunei',
        'Bulgaria',
        'Burkina',
        'Burundi',
        'Cambodia',
        'Cameroon',
        'Canada',
        'Cape Verde',
        'Central African Rep',
        'Chad',
        'Chile',
        'China',
        'Colombia',
        'Comoros',
        'Congo',
        'Congo (Democratic Rep)',
        'Costa Rica',
        'Croatia',
        'Cuba',
        'Cyprus',
        'Czech Republic',
        'Denmark',
        'Djibouti',
        'Dominica',
        'Dominican Republic',
        'East Timor',
        'Ecuador',
        'Egypt',
        'El Salvador',
        'Equatorial Guinea',
        'Eritrea',
        'Estonia',
        'Eswatini',
        'Ethiopia',
        'Fiji',
        'Finland',
        'France',
        'Gabon',
        'Gambia',
        'Georgia',
        'Germany',
        'Ghana',
        'Greece',
        'Grenada',
        'Guatemala',
        'Guinea',
        'Guinea-Bissau',
        'Guyana',
        'Haiti',
        'Honduras',
        'Hungary',
        'Iceland',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ireland (Republic)',
        'Israel',
        'Italy',
        'Ivory Coast',
        'Jamaica',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Kenya',
        'Kiribati',
        'Korea North',
        'Korea South',
        'Kosovo',
        'Kuwait',
        'Kyrgyzstan',
        'Laos',
        'Latvia',
        'Lebanon',
        'Lesotho',
        'Liberia',
        'Libya',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Macedonia',
        'Madagascar',
        'Malawi',
        'Malaysia',
        'Maldives',
        'Mali',
        'Malta',
        'Marshall Islands',
        'Mauritania',
        'Mauritius',
        'Mexico',
        'Micronesia',
        'Moldova',
        'Monaco',
        'Mongolia',
        'Montenegro',
        'Morocco',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Nepal',
        'Netherlands',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigeria',
        'Norway',
        'Oman',
        'Pakistan',
        'Palau',
        'Palestine',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Philippines',
        'Poland',
        'Portugal',
        'Qatar',
        'Romania',
        'Russian Federation',
        'Rwanda',
        'St Kitts & Nevis',
        'St Lucia',
        'Saint Vincent & the Grenadines',
        'Samoa',
        'San Marino',
        'Sao Tome & Principe',
        'Saudi Arabia',
        'Senegal',
        'Serbia',
        'Seychelles',
        'Sierra Leone',
        'Singapore',
        'Slovakia',
        'Slovenia',
        'Solomon Islands',
        'Somalia',
        'South Africa',
        'South Sudan',
        'Spain',
        'Sri Lanka',
        'Sudan',
        'Suriname',
        'Sweden',
        'Switzerland',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Tanzania',
        'Thailand',
        'Togo',
        'Tonga',
        'Trinidad & Tobago',
        'Tunisia',
        'Turkey',
        'Turkmenistan',
        'Tuvalu',
        'Uganda',
        'Ukraine',
        'United Arab Emirates',
        'United Kingdom',
        'United States',
        'Uruguay',
        'Uzbekistan',
        'Vanuatu',
        'Vatican City',
        'Venezuela',
        'Vietnam',
        'Yemen',
        'Zambia',
        'Zimbabwe'
    );
CREATE TYPE show_status AS ENUM ('created', 'started', 'stopped');
CREATE TYPE sex AS ENUM ('female', 'male');
create type user_role as enum ('admin', 'guest', 'breeder', 'judge');

create table if not exists Animal (
    id int,
    user_id int,
    breed_id int,
    "name" text,
    birth_dt date,
    sex sex,
    weight float,
    height float,
    "length" float,
    has_defects bool,
    is_multicolor bool,
    photo bytea
);

create table if not exists "user" (
    id int,
    email text,
    hashed_password text,
    "role" user_role,
    "name" text
);

create table if not exists UserShow (
    id int,
    show_id int,
    user_id int,
    is_archived bool
);

create table if not exists AnimalShow (
    id int,
    show_id int,
    animal_id int,
    is_archived bool
);

create table if not exists Standard (
    id int,
    breed_id int,
    country country,
    weight float,
    height float,
    length float,
    has_defects bool,
    is_multicolor bool,
    weight_delta_percent float,
    height_delta_percent float,
    length_delta_percent float
);

create table if not exists Species (
    id int,
    name text,
    group_id int
);

create table if not exists Breed (
    id int,
    name text,
    species_id int
);

create table if not exists "group" (
    id int,
    name text
);

create table if not exists Score (
    id int,
    usershow_id int,
    animalshow_id int,
    value int,
    is_archived bool,
    dt_created timestamp
);

create table if not exists Certificate (
    id int,
    animalshow_id int,
    rank int
);

create table if not exists Show (
    id int,
    species_id int,
    breed_id int,
    standard_id int,
    status show_status,
    country country,
    show_class text,
    name text,
    is_multi_breed bool
);

