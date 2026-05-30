'use client';

import { useEffect, useState } from 'react';

interface CalendarEvent {
  id: string;
  subject: string;
  start: string;
  end: string;
  isOnlineMeeting: boolean;
}

export default function CalendarCard({ msConnected }: { msConnected: boolean }) {
  const [events, setEvents] = useState<CalendarEvent[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!msConnected) { setLoading(false); return; }
    fetch('/api/calendar/events')
      .then(r => r.json())
      .then(d => { setEvents(d.events ?? []); setLoading(false); })
      .catch(() => { setError('Failed to load events'); setLoading(false); });
  }, [msConnected]);

  function formatTime(iso: string) {
    return new Date(iso).toLocaleTimeString('en-AU', { hour: '2-digit', minute: '2-digit', hour12: true });
  }

  function duration(start: string, end: string) {
    const mins = Math.round((new Date(end).getTime() - new Date(start).getTime()) / 60000);
    return mins >= 60 ? `${Math.floor(mins / 60)}h${mins % 60 ? ` ${mins % 60}m` : ''}` : `${mins}m`;
  }

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-blue-500" />
          <h2 className="card-title">Calendar</h2>
        </div>
        {!msConnected && (
          <a href="/settings" className="text-xs text-blue-400 hover:underline">Connect Outlook</a>
        )}
      </div>

      {!msConnected ? (
        <div className="text-center py-6">
          <p className="text-slate-400 text-sm">Connect your Outlook account in settings to see today's meetings.</p>
        </div>
      ) : loading ? (
        <div className="space-y-2">
          {[1,2,3].map(i => <div key={i} className="h-10 bg-slate-700 rounded-lg animate-pulse" />)}
        </div>
      ) : error ? (
        <p className="text-red-400 text-sm">{error}</p>
      ) : events.length === 0 ? (
        <p className="text-slate-400 text-sm">No events today. Enjoy the focus time!</p>
      ) : (
        <ul className="space-y-2">
          {events.map(event => (
            <li key={event.id} className="flex items-start gap-3 py-2 px-3 bg-slate-700 rounded-lg">
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-white truncate">{event.subject}</p>
                <p className="text-xs text-slate-400">{formatTime(event.start)} – {formatTime(event.end)} · {duration(event.start, event.end)}</p>
              </div>
              {event.isOnlineMeeting && (
                <span className="text-xs bg-blue-900 text-blue-300 px-1.5 py-0.5 rounded flex-shrink-0">Online</span>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
