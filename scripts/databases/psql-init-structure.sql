create schema if not exists public_dev_password_manager authorization austin;
alter schema public_dev_password_manager owner to austin;

set search_path = public_dev_password_manager;

create table public_dev_password_manager.test_using
(
    id          serial primary key,
    name        varchar(255) not null,
    age         integer      not null,
    email       varchar(255) not null,
    description text,
    created_at  timestamp    not null default current_timestamp,
    updated_at  timestamp    not null default current_timestamp
);

comment on table public_dev_password_manager.test_using is 'This is a test table';
comment on column public_dev_password_manager.test_using.id is 'id';
comment on column public_dev_password_manager.test_using.name is 'name';
comment on column public_dev_password_manager.test_using.email is 'email';
comment on column public_dev_password_manager.test_using.description is 'descriptsion';
comment on column public_dev_password_manager.test_using.created_at is 'create time';
comment on column public_dev_password_manager.test_using.updated_at is 'update time';

insert into public_dev_password_manager.test_using (name, age, email)
values ('Jack', 18, 'jack@example.com');

create table public_dev_password_manager.test_using_temp as
select id,
       name,
       age,
       email,
       description,
       false as exist, -- 默认值为 FALSE
       created_at,
       updated_at
from public_dev_password_manager.test_using
where false;

insert into public_dev_password_manager.test_using_temp (id, name, age, email, description, exist, created_at, updated_at)
select id,
       name,
       age,
       email,
       description,
       true as exist, -- 设置 exist 的默认值为 true
       created_at,
       updated_at
from public_dev_password_manager.test_using;

drop table public_dev_password_manager.test_using;

create table public_dev_password_manager.test_using
(
    id          serial primary key,
    name        varchar(255) not null,
    age         integer      not null,
    email       varchar(255) not null,
    description text,
    exist       boolean      not null default true,
    created_at  timestamp    not null default current_timestamp,
    updated_at  timestamp    not null default current_timestamp
);

comment on table public_dev_password_manager.test_using is 'This is a test table';
comment on column public_dev_password_manager.test_using.id is 'id';
comment on column public_dev_password_manager.test_using.name is 'name';
comment on column public_dev_password_manager.test_using.email is 'email';
comment on column public_dev_password_manager.test_using.description is 'descriptsion';
comment on column public_dev_password_manager.test_using.exist is 'state';
comment on column public_dev_password_manager.test_using.created_at is 'create time';
comment on column public_dev_password_manager.test_using.updated_at is 'update time';

insert into public_dev_password_manager.test_using (id, name, age, email, description, exist, created_at, updated_at)
select id,
       name,
       age,
       email,
       description,
       true as exist, -- 设置 exist 的默认值为 true
       created_at,
       updated_at
from public_dev_password_manager.test_using_temp;

drop table public_dev_password_manager.test_using_temp;


SELECT "public_dev_password_manager"."test_using"."id",
       "public_dev_password_manager"."test_using"."name",
       "public_dev_password_manager"."test_using"."age",
       "public_dev_password_manager"."test_using"."email",
       "public_dev_password_manager"."test_using"."description",
       "public_dev_password_manager"."test_using"."exist",
       "public_dev_password_manager"."test_using"."created_at",
       "public_dev_password_manager"."test_using"."updated_at"
FROM "public_dev_password_manager"."test_using"
WHERE ("public_dev_password_manager"."test_using"."exist" AND "public_dev_password_manager"."test_using"."id" = 1);
