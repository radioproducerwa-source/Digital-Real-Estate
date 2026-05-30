import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';
import GoalsClient from './GoalsClient';

export default async function GoalsPage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/login');

  const [{ data: goals }, { data: milestones }] = await Promise.all([
    supabase.from('goals').select('*').order('created_at', { ascending: false }),
    supabase.from('milestones').select('*').order('created_at'),
  ]);

  return <GoalsClient goals={goals ?? []} milestones={milestones ?? []} />;
}
