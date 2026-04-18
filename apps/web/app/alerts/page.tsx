import { AlertPanel } from "@/components/dashboard/alert-panel";
import { getDashboardData } from "@/lib/api";

export default async function AlertsPage() {
  const { alerts } = await getDashboardData();
  return (
    <main className="min-h-screen px-6 py-8 md:px-10">
      <div className="mx-auto max-w-4xl">
        <AlertPanel alerts={alerts} />
      </div>
    </main>
  );
}
