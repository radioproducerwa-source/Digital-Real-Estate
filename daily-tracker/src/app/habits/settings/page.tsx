import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';
import HabitsSettingsClient from './HabitsSettingsClient';

export default async function HabitsSettingsPage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/login');

  const { data: habits } = await supabase
    .from('habits')
    .select('*')
    .order('order');

  return <HabitsSettingsClient habits={habits ?? []} />;
}
