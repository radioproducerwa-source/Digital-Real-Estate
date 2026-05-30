-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Habits
create table if not exists habits (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade not null,
  name text not null,
  type text not null check (type in ('checkbox', 'number', 'rating', 'text')),
  target numeric,
  "order" integer not null default 0,
  active boolean not null default true,
  created_at timestamptz not null default now()
);
alter table habits enable row level security;
create policy "habits: owner only" on habits for all using (auth.uid() = user_id);

-- Habit logs
create table if not exists habit_logs (
  id uuid primary key default uuid_generate_v4(),
  habit_id uuid references habits(id) on delete cascade not null,
  date date not null,
  value jsonb,
  completed boolean not null default false,
  unique(habit_id, date)
);
alter table habit_logs enable row level security;
create policy "habit_logs: owner only" on habit_logs for all
  using (habit_id in (select id from habits where user_id = auth.uid()));

-- Tasks
create table if not exists tasks (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade not null,
  title text not null,
  date date not null,
  completed boolean not null default false,
  rolled_over boolean not null default false,
  created_at timestamptz not null default now()
);
alter table tasks enable row level security;
create policy "tasks: owner only" on tasks for all using (auth.uid() = user_id);

-- Goals
create table if not exists goals (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade not null,
  title text not null,
  description text,
  target_date date,
  archived boolean not null default false,
  created_at timestamptz not null default now()
);
alter table goals enable row level security;
create policy "goals: owner only" on goals for all using (auth.uid() = user_id);

-- Milestones
create table if not exists milestones (
  id uuid primary key default uuid_generate_v4(),
  goal_id uuid references goals(id) on delete cascade not null,
  title text not null,
  horizon text not null check (horizon in ('daily', 'weekly', 'monthly', 'yearly')),
  completed boolean not null default false,
  created_at timestamptz not null default now()
);
alter table milestones enable row level security;
create policy "milestones: owner only" on milestones for all
  using (goal_id in (select id from goals where user_id = auth.uid()));

-- Chat messages
create table if not exists chat_messages (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade not null,
  role text not null check (role in ('user', 'assistant')),
  content text not null,
  context_snapshot jsonb,
  created_at timestamptz not null default now()
);
alter table chat_messages enable row level security;
create policy "chat_messages: owner only" on chat_messages for all using (auth.uid() = user_id);

-- User settings
create table if not exists user_settings (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade not null unique,
  visible_cards text[] not null default array['calendar','bitcoin','quote','content'],
  currency text not null default 'AUD' check (currency in ('AUD', 'USD')),
  ms_refresh_token text,
  updated_at timestamptz not null default now()
);
alter table user_settings enable row level security;
create policy "user_settings: owner only" on user_settings for all using (auth.uid() = user_id);
