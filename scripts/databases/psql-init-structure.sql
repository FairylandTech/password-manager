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

--------------------------------------------------------------
-------------------------- 测试表 -----------------------------
--------------------------------------------------------------

create schema public_dev_test authorization austin;

create table public_dev_test.pubilsh
(
    id         serial primary key,
    name       varchar(255) not null unique,
    area       varchar(255) not null,
    exist      boolean      not null default true,
    created_at timestamp    not null default current_timestamp,
    updated_at timestamp    not null default current_timestamp
);

comment on table public_dev_test.pubilsh is '出版社表';
comment on column public_dev_test.pubilsh.id is '主键ID';
comment on column public_dev_test.pubilsh.name is '出版社名字';
comment on column public_dev_test.pubilsh.area is '出版社地区';
comment on column public_dev_test.pubilsh.exist is '数据状态';
comment on column public_dev_test.pubilsh.created_at is '创建时间';
comment on column public_dev_test.pubilsh.updated_at is '修改时间';

create table public_dev_test.author
(
    id          serial primary key,
    name        varchar(255) not null,
    gender      boolean      not null,
    birthday    date         not null default current_date,
    description text,
    exist       boolean      not null default true,
    created_at  timestamp    not null default current_timestamp,
    updated_at  timestamp    not null default current_timestamp
);

comment on table public_dev_test.author is '作者表';
comment on column public_dev_test.author.id is '主键ID';
comment on column public_dev_test.author.name is '作者名字';
comment on column public_dev_test.author.gender is '性别: true=1=男, false=0=女';
comment on column public_dev_test.author.birthday is '出生日期';
comment on column public_dev_test.author.description is '描述';
comment on column public_dev_test.author.exist is '数据状态';
comment on column public_dev_test.author.created_at is '创建时间';
comment on column public_dev_test.author.updated_at is '修改时间';

insert into public_dev_test.pubilsh (name, area)
values ('香梨出版社', '北京'),
       ('雪梨出版社', '广州');

insert into public_dev_test.author (name, gender, birthday)
values ('姜添池', true, '1998-01-24'),
       ('陈欣宜', false, '2001-3-9');
