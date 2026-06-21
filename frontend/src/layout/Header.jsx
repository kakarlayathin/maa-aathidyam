import { Search, Bell, User } from 'lucide-react';

export default function Header() {
  return (
    <header className="flex h-16 items-center justify-between border-b border-gray-200 bg-white px-8 shadow-sm">
      <div className="flex w-96 items-center rounded-md bg-gray-100 px-3 py-2">
        <Search className="h-5 w-5 text-gray-400" />
        <input
          type="text"
          placeholder="Search..."
          className="ml-2 w-full bg-transparent text-sm outline-none placeholder:text-gray-500"
        />
      </div>
      <div className="flex items-center space-x-4">
        <button className="rounded-full p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-500 transition-colors">
          <Bell className="h-6 w-6" />
        </button>
        <div className="h-8 w-px bg-gray-200" />
        <div className="flex items-center space-x-3">
          <div className="flex flex-col text-right">
            <span className="text-sm font-medium text-gray-900">John Doe</span>
            <span className="text-xs text-gray-500">Admin</span>
          </div>
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 text-indigo-600">
            <User className="h-6 w-6" />
          </div>
        </div>
      </div>
    </header>
  );
}
