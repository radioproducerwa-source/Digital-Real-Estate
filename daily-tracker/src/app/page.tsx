import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';
import Dashboard from '@/components/Dashboard';

export default async function HomePage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();

  if (!user) redirect('/login');

  const [habitsRes, tasksRes, goalsRes, milestonesRes, settingsRes] = await Promise.all([
    supabase.from('habits').select('*').eq('active', true).order('order'),
    supabase.from('tasks').select('*').eq('date', new Date().toISOString().split('T')[0]).order('created_at'),
    supabase.from('goals').select('*').eq('archived', false).order('created_at'),
    supabase.from('milestones').select('*').eq('completed', false),
    supabase.from('user_settings').select('*').eq('user_id', user.id).single(),
  ]);

  const today = new Date().toISOString().split('T')[0];
  const habitIds = (habitsRes.data ?? []).map((h) => h.id);
  const logsRes = habitIds.length
    ? await supabase.from('habit_logs').select('*').eq('date', today).in('habit_id', habitIds)
    : { data: [] };

  const settings = settingsRes.data ?? {
    visible_cards: ['calendar', 'bitcoin', 'quote', 'content'],
    currency: 'AUD',
    ms_refresh_token: null,
  };

  return (
    <Dashboard
      user={user}
      habits={habitsRes.data ?? []}
      habitLogs={logsRes.data ?? []}
      tasks={tasksRes.data ?? []}
      goals={goalsRes.data ?? []}
      milestones={milestonesRes.data ?? []}
      settings={settings}
    />
  );
}
