
import './App.css';
import axios from 'axios';
import img from './Images/upload.png'
import { Loader } from './Components/Loader';
import { useState } from 'react';

function App() {
  const [loader,setLoader]=useState(false);
  const [fileData,setFileData]=useState();
  const submitFile=(e)=>{
    const data=new FormData();
    console.log(e.target.files[0]);
    console.log(e);
    setLoader(true);
    data.append("file",e.target.files[0]);
    axios.post("http://localhost:8000/model",data).then((res)=>{
      console.log(res);
      setFileData(res.data.data);
      setLoader(false);
    }).catch((err)=>{
      console.log(err);
      setLoader(false);
    })
  }

  return (
      <>{
        !loader ?
    <div className="App container">
      <h1>
        <center>
          50 - Neural Not works
        </center>
      </h1>
      <div className="h-100 w-100 pt-5">
        <div className=''>
        <div className="mb-4">
        <h1>
        Automated Detection of Cardiac Diseases
        </h1>
      <p>
        <ul>
    <li>
      What is the use of this portal?
      <ol>
 ●
 We aim to reduce the incidence of sudden cardiac arrest, particularly among younger
 populations by automated detection of ECGs.
 </ol>
    </li>
    <li>
      What user has to do?
      <ol>● Upload a resting <b>
  12-lead </b>ECG recordings in standard formats.
      </ol>
    </li>
    <li>
      What we provide?
      <ol>● Alerts indicating the presence or risk of cardiac diseases,
 accompanied by confidence scores
      </ol>
    </li>
        </ul>
        </p>
        </div>
        </div>

      </div>
      <div className="m-auto text-align-center form">
          <form action="" encType="multipart/form-data" className="">
          <p className="d-flex gap-5 align-items-center">
          Upload your .hdf5 file
        <label htmlFor="file" style={{cursor:"pointer"}}>
        <img src={img} alt="Uplaod Img" height="50px" width="50px" />
        </label>
          </p>
          <p>
        <input type="file"  name="file" id="file" 
        onChange={submitFile}
        style={{display:"None"}}
         />          </p>
          </form>
          </div>

             <table className='table table-hover table-dark'>
              <thead><tr className='sticky-top'>
                <th>Patient Number</th>
                <th>1dAVb</th>
                  <th>RBBB</th>
                  <th>LBBB</th>

                <th>SB</th>
                <th>AF</th>
                <th>ST</th>
                </tr>
              </thead>
              <tbody>
          {fileData && fileData?.map((e,id)=>{
            console.log(e);
            return <tr>
              <td>{id+1}</td>
                {e?.map((j)=>{
                  return <td className={`${j==1 ? 'bg-danger' :''}`}>{j}</td>
                })}
              </tr>
          })}
          </tbody>
        </table>
          </div> : <Loader/>}
          </>
  );
}

export default App;
