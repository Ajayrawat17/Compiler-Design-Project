export default function Login() {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#1e1e1e] text-white">
        <div className="bg-gray-800 p-8 rounded-xl w-96 space-y-4">
          <h2 className="text-2xl font-bold">Login</h2>
          <input
            type="text"
            placeholder="Email"
            className="w-full p-2 rounded bg-gray-700 outline-none"
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-2 rounded bg-gray-700 outline-none"
          />
          <button className="bg-blue-600 px-4 py-2 rounded w-full hover:bg-blue-500">
            Login
          </button>
        </div>
      </div>
    );
  }
  