import { AlertPanel } from "@/components/dashboard/alert-panel";
import { DashboardHeader } from "@/components/dashboard/header";
import { EventTimeline } from "@/components/dashboard/event-timeline";
import { SectorHeatmap } from "@/components/dashboard/sector-heatmap";
import { ShockProfile } from "@/components/dashboard/shock-profile";
import { getDashboardData } from "@/lib/api";

export default async function HomePage() {
  const data = await getDashboardData();
  const heroEvent = data.events[0];

  return (
    <main className="min-h-screen bg-radial-grid px-6 py-8 md:px-10">
      <div className="mx-auto flex max-w-7xl flex-col gap-8">
        <DashboardHeader />
        <div className="grid gap-8 xl:grid-cols-[1.2fr_0.8fr]">
          <EventTimeline events={data.events} />
          <AlertPanel alerts={data.alerts} />
        </div>
        <div className="grid gap-8 xl:grid-cols-[0.95fr_1.05fr]">
          <ShockProfile event={heroEvent} predictions={data.predictions} />
          <SectorHeatmap reactions={data.reactions} predictions={data.predictions} />
        </div>
      </div>
    </main>
  );
}

