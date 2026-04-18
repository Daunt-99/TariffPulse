import { EventTimeline } from "@/components/dashboard/event-timeline";
import { getDashboardData } from "@/lib/api";

export default async function EventsPage() {
  const { events } = await getDashboardData();
  return (
    <main className="min-h-screen px-6 py-8 md:px-10">
      <div className="mx-auto max-w-6xl">
        <EventTimeline events={events} />
      </div>
    </main>
  );
}

