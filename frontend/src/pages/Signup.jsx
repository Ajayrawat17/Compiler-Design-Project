import { Link } from "react-router-dom";

export default function Signup() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-[#1e1e1e] text-white">
      <div className="bg-gray-800 p-8 rounded-xl w-96 space-y-4">
        <h2 className="text-2xl font-bold">Sign Up</h2>
        <input
          type="text"
          placeholder="Username"
          className="w-full p-2 rounded bg-gray-700 outline-none"
        />
        <input
          type="email"
          placeholder="Email"
          className="w-full p-2 rounded bg-gray-700 outline-none"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full p-2 rounded bg-gray-700 outline-none"
        />
        <button className="bg-green-600 px-4 py-2 rounded w-full hover:bg-green-500">
          Sign Up
        </button>

        <p className="text-sm text-center text-gray-400">
          Already signed up?{" "}
          <Link to="/login" className="text-blue-400 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
