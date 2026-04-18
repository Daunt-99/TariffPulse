export function DashboardHeader() {
  return (
    <header className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
      <div>
        <p className="eyebrow">Tariff Shock Intelligence System</p>
        <h1 className="mt-3 text-4xl font-semibold tracking-tight text-white">
          Trade policy shocks, sector stress, and reaction timing in one view
        </h1>
      </div>
      <div className="dashboard-panel max-w-sm p-5">
        <p className="eyebrow">System Status</p>
        <div className="mt-3 flex items-center justify-between">
          <div>
            <p className="text-sm text-slate-300">Pipeline posture</p>
            <p className="text-lg font-medium text-accent">Mock-ready and bootable</p>
          </div>
          <div className="h-3 w-3 rounded-full bg-accent shadow-[0_0_18px_rgba(124,247,212,0.9)]" />
        </div>
      </div>
    </header>
  );
}

