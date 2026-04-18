import { SectorHeatmap } from "@/components/dashboard/sector-heatmap";
import { getDashboardData } from "@/lib/api";

export default async function SectorsPage() {
  const { predictions, reactions } = await getDashboardData();
  return (
    <main className="min-h-screen px-6 py-8 md:px-10">
      <div className="mx-auto max-w-6xl">
        <SectorHeatmap predictions={predictions} reactions={reactions} />
      </div>
    </main>
  );
}

