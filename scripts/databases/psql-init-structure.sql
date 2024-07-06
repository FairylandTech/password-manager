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

SELECT "public_dev_password_manager"."test_using"."id",
       "public_dev_password_manager"."test_using"."name",
       "public_dev_password_manager"."test_using"."age",
       "public_dev_password_manager"."test_using"."email",
       "public_dev_password_manager"."test_using"."description",
       "public_dev_password_manager"."test_using"."created_at",
       "public_dev_password_manager"."test_using"."updated_at"
FROM "public_dev_password_manager"."test_using";
