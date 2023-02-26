import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState<any>("");

  const submitImage = async (e: any) => {
    e.preventDefault();
    try {
      const image = await axios.post("http://localhost:5000/image", {
        file,
      });

      console.log(image);

      console.log(file);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="App">
      <img src="" alt="" width={200} height={200} />

      <br />

      <form onSubmit={submitImage}>
        <input
          type="file"
          name="file"
          onChange={(e) => {
            setFile(e.target.value);
          }}
        />

        <button typeof="submit">Sumbit </button>
      </form>
    </div>
  );
}

export default App;
