'use client';

import { useState } from 'react';
import type { User } from '@supabase/supabase-js';
import HabitsCard from './cards/HabitsCard';
import TasksCard from './cards/TasksCard';
import GoalsCard from './cards/GoalsCard';
import SummaryCard from './cards/SummaryCard';
import ChatCard from './cards/ChatCard';
import CalendarCard from './cards/CalendarCard';
import BitcoinCard from './cards/BitcoinCard';
import QuoteCard from './cards/QuoteCard';
import ContentIdeasCard from './cards/ContentIdeasCard';
import TopBar from './TopBar';

interface DashboardProps {
  user: User;
  habits: any[];
  habitLogs: any[];
  tasks: any[];
  goals: any[];
  milestones: any[];
  settings: {
    visible_cards: string[];
    currency: string;
    ms_refresh_token: string | null;
  };
}

export default function Dashboard({ user, habits, habitLogs, tasks, goals, milestones, settings }: DashboardProps) {
  const [visibleCards, setVisibleCards] = useState<string[]>(settings.visible_cards);
  const [localTasks, setLocalTasks] = useState(tasks);
  const [localHabitLogs, setLocalHabitLogs] = useState(habitLogs);

  const completedHabits = habits.filter(h =>
    localHabitLogs.find(l => l.habit_id === h.id && l.completed)
  ).length;

  const completedTasks = localTasks.filter(t => t.completed).length;

  const isVisible = (card: string) => visibleCards.includes(card);

  return (
    <div className="min-h-screen bg-slate-900">
      <TopBar user={user} visibleCards={visibleCards} onToggleCard={setVisibleCards} />
      <main className="max-w-7xl mx-auto px-4 py-6 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {/* Core cards — always visible */}
        <HabitsCard
          habits={habits}
          logs={localHabitLogs}
          onLogsChange={setLocalHabitLogs}
        />
        <TasksCard
          tasks={localTasks}
          onTasksChange={setLocalTasks}
        />
        <GoalsCard goals={goals} milestones={milestones} />

        {/* Toggleable cards */}
        {isVisible('calendar') && <CalendarCard msConnected={!!settings.ms_refresh_token} />}
        {isVisible('bitcoin') && <BitcoinCard currency={settings.currency as 'AUD' | 'USD'} />}
        {isVisible('quote') && <QuoteCard />}
        {isVisible('content') && <ContentIdeasCard tasks={localTasks} />}

        {/* Full-width bottom cards */}
        <div className="md:col-span-2 xl:col-span-3">
          <SummaryCard
            habitTotal={habits.length}
            habitDone={completedHabits}
            taskTotal={localTasks.length}
            taskDone={completedTasks}
          />
        </div>
        <div className="md:col-span-2 xl:col-span-3">
          <ChatCard
            habits={habits}
            habitLogs={localHabitLogs}
            tasks={localTasks}
            goals={goals}
            milestones={milestones}
          />
        </div>
      </main>
    </div>
  );
}
