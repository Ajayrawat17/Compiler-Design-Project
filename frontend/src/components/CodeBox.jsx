import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

export default function CodeBox() {
  const [code, setCode] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [language, setLanguage] = useState("");

  const navigate = useNavigate();

  const handleRun = async () => {
  setOutput(`Running ${language} code...`);

  try {
    // Step 1: Send POST request
    const postResponse = await fetch("http://localhost:8000/compiler/compile/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, language }),
    });

    const postData = await postResponse.json();

    // If no placeholders, directly show output
    if (postData.output) {
      setOutput(postData.output);
    } else if (postData.code_id) {
      // Step 2: Prepare inputs from textarea
      let inputObj = {};
      try {
        // Assume input is a JSON object like: { "input1": "5", "input2": "hello" }
        inputObj = JSON.parse(input);
      } catch (e) {
        setOutput("Invalid input format. Use JSON like {\"input1\": \"5\"}");
        return;
      }

      // Step 3: Send PUT request
      const putResponse = await fetch("http://localhost:8000/compiler/compile/", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code_id: postData.code_id, inputs: inputObj }),
      });

      const putData = await putResponse.json();
      setOutput(putData.output || "No output returned.");
    } else {
      setOutput("Unexpected server response.");
    }
  } catch (err) {
    console.error(err);
    setOutput("An error occurred while compiling the code.");
  }
};


  const handleConvert = () => {
    setOutput(`Converting ${language} code...`);
  };

  return (
    <div className="min-h-screen bg-[#1e1e1e] text-white">
      {/* Top Nav */}
      <div className="flex justify-between items-center p-4 border-b border-gray-700">
        <motion.h1
          initial={{ x: -200, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ type: "spring", stiffness: 60 }}
          className="text-3xl font-bold text-blue-400"
        >
          CodeBox
        </motion.h1>

        <div className="space-x-4">
          <button
            onClick={() => navigate("/login")}
            className="bg-gray-700 px-4 py-2 rounded hover:bg-gray-600"
          >
            Login
          </button>
          <button
            onClick={() => navigate("/signup")}
            className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-500"
          >
            Sign Up
          </button>
        </div>
      </div>

      {/* Main Split Layout */}
      <div className="grid grid-cols-2 gap-4 p-6">
        {/* Left: Code Editor */}
        <div className="flex flex-col space-y-4">
        <select
     value={language}
     onChange={(e) => setLanguage(e.target.value)}
      className="bg-gray-800 p-2 rounded text-white w-fit"
       >
    <option value="c">C</option>
    <option value="python">Python</option>
    </select>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="# write your code here..."
            className="h-[400px] p-4 bg-[#2d2d2d] rounded resize-none outline-none"
          />
        </div>

        {/* Right: Input/Output */}
        <div className="flex flex-col space-y-4">
          <div className="flex flex-row space-x-5">
          <button
            onClick={handleRun}
            className="bg-blue-500 hover:bg-blue-600 w-fit px-4 py-2 rounded"
          >
            Run
          </button>
          <button
            onClick={handleConvert}
            className="bg-green-500 hover:bg-green-600 w-fit px-4 py-2 rounded"
          >
            Convert
          </button>

          </div>
          
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter input here..."
            className="h-24 p-2 bg-[#2d2d2d] rounded resize-none outline-none"
          />
          <div className="bg-[#2d2d2d] p-4 rounded h-40 overflow-auto">
            <h2 className="font-semibold mb-2">Output:</h2>
            <pre>{output || "No output yet."}</pre>
          </div>
        </div>
      </div>
    </div>
  );
}
