import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';
import SettingsClient from './SettingsClient';

export default async function SettingsPage({ searchParams }: { searchParams: Promise<{ ms?: string; error?: string }> }) {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/login');

  const { data: settings } = await supabase
    .from('user_settings')
    .select('*')
    .eq('user_id', user.id)
    .single();

  const params = await searchParams;

  return (
    <SettingsClient
      settings={settings ?? { visible_cards: [], currency: 'AUD', ms_refresh_token: null }}
      msStatus={params.ms === 'connected' ? 'connected' : params.error ? 'error' : null}
    />
  );
}
