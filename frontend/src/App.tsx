import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState<any>(null);
  const [fileName, setfileName] = useState<any>("");
  const [imageAdded, setImageAdded] = useState<boolean>(false);
  const formData = new FormData();

  const submitImage = async (e: any) => {
    e.preventDefault();

    formData.append("files", file[0]);

    try {
      await axios.post("http://localhost:5000/upload", formData, {
        headers: {
          Accept: "*/*",
          "Content-Type": "multipart/form-data",
        },
      });

      setImageAdded(true);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    if (file) {
      setfileName("/images/");
    }
  }, [file, formData]);

  //frontend/src/images/ai_app.png
  return (
    <div className="App">
      <br />

      <form onSubmit={submitImage}>
        <input
          type="file"
          name="file"
          onChange={(e) => {
            console.log(e.target.files);
            setFile(e.target.files);
          }}
        />

        <button typeof="submit">Sumbit</button>
      </form>

      {imageAdded && <AddedImage />}
    </div>
  );
}

const AddedImage = () => {
  return (
    <img
      src={require(`./images/ai_app.png`).default}
      height={200}
      width={200}
    />
  );
};

export default App;
