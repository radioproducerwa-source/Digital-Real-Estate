import { createClient } from '@/lib/supabase/server';
import { NextResponse } from 'next/server';

const MS_GRAPH_BASE = 'https://graph.microsoft.com/v1.0';

async function refreshAccessToken(refreshToken: string): Promise<string> {
  const res = await fetch('https://login.microsoftonline.com/common/oauth2/v2.0/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: process.env.MICROSOFT_CLIENT_ID!,
      client_secret: process.env.MICROSOFT_CLIENT_SECRET!,
      refresh_token: refreshToken,
      grant_type: 'refresh_token',
      scope: 'Calendars.Read offline_access',
    }),
  });
  const data = await res.json();
  return data.access_token;
}

export async function GET() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

  const { data: settings } = await supabase
    .from('user_settings')
    .select('ms_refresh_token')
    .eq('user_id', user.id)
    .single();

  if (!settings?.ms_refresh_token) {
    return NextResponse.json({ events: [] });
  }

  const accessToken = await refreshAccessToken(settings.ms_refresh_token);

  const now = new Date();
  const startOfDay = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString();
  const endOfDay = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59).toISOString();

  const res = await fetch(
    `${MS_GRAPH_BASE}/me/calendarView?startDateTime=${startOfDay}&endDateTime=${endOfDay}&$select=subject,start,end,isOnlineMeeting&$orderby=start/dateTime&$top=20`,
    { headers: { Authorization: `Bearer ${accessToken}` } }
  );

  const data = await res.json();
  const events = (data.value ?? []).map((e: any) => ({
    id: e.id,
    subject: e.subject,
    start: e.start.dateTime,
    end: e.end.dateTime,
    isOnlineMeeting: e.isOnlineMeeting,
  }));

  return NextResponse.json({ events });
}
