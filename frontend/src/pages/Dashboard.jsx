export default function Dashboard() {
  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
      <p className="mt-2 text-gray-600">Welcome to Maa Aathidyam SaaS Client Dashboard.</p>
      
      <div className="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {[
          { label: 'Total Users', value: '1,234', change: '+12%' },
          { label: 'Active Projects', value: '45', change: '+5%' },
          { label: 'Revenue', value: '$12,450', change: '+18%' },
          { label: 'Support Tickets', value: '3', change: '-2%' },
        ].map((stat) => (
          <div key={stat.label} className="rounded-lg bg-white p-6 shadow-sm ring-1 ring-gray-200">
            <p className="text-sm font-medium text-gray-500">{stat.label}</p>
            <div className="mt-2 flex items-baseline justify-between">
              <p className="text-2xl font-semibold text-gray-900">{stat.value}</p>
              <p className={stat.change.startsWith('+') ? 'text-sm font-medium text-green-600' : 'text-sm font-medium text-red-600'}>
                {stat.change}
              </p>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8 rounded-lg bg-white p-6 shadow-sm ring-1 ring-gray-200">
        <h2 className="text-lg font-medium text-gray-900">Recent Activity</h2>
        <div className="mt-4 h-64 flex items-center justify-center border-2 border-dashed border-gray-200 rounded-lg">
          <p className="text-gray-400">Activity chart will be here</p>
        </div>
      </div>
    </div>
  );
}
