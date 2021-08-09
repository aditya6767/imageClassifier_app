import React,{useState, useEffect} from 'react'
import './App.css';

function App() {
    const [image,setImage] = useState("")
    const [url,setUrl] = useState(undefined)
    const [response ,setResponse] = useState(null)
    const [loading ,setLoading] = useState(false)
    useEffect(()=>{
        if(url)
        {
            uploadFields()
        }
    },[url])

    const uploadPic = ()=>{
        const data = new FormData()
        data.append("file",image)
        data.append("upload_preset","classifier_image_upload")
        data.append("cloud_name","duxnhitdq")

        // for pic upload
        fetch("https://api.cloudinary.com/v1_1/duxnhitdq/image/upload",{
            method:"post",
            body:data
            })
            .then(res=>res.json())
            .then(data=>{
                 console.log(data)
                setUrl(data.url)
            })
            .catch(err=>{
                setLoading(false)
                console.log(err)
            })
    }
    const handleUploadpic = (e)=>{
        setResponse(null)
        setImage(e.target.files[0])
    }
    const uploadFields=()=>{

        fetch("http://0.0.0.0:8181/my_api/classify",{
            method:"post",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                imageUrl:url
            })
        }).then(res=>res.json()).then(data=>{
            console.log(data)
            setResponse(data?.output_result)
            setLoading(false)
        }).catch(err=>{
            setLoading(false)
            console.log(err)
        })
    }

    const PostData = ()=>{
        setLoading(true)
        uploadPic()
    }
  return (
    <div className="main-div">
            <h1>Image Classifier</h1>
            <div className="App">
                <div className="file-field input-field">
                    <div className="input-section">
                        <p id="select">select image</p>
                        <input type="file" onChange={(e) => handleUploadpic(e)} />
                    </div>
                </div>
                <button className="btn waves-effect waves-light .#6a1b9a purple darken-3" onClick={() => PostData()}>
                    Predict
                </button>
                {
                    response ? (
                        <div id="results">
                            <h3>Results</h3>
                            <div id="classname">
                                classname = {response.classname}
                            </div>
                            <div id="probab">
                                probability =  {response.probability}
                            </div>
                        </div>
                    ) : loading ? (
                        <div>
                            loading....
                        </div>
                    ) : null
                }
            </div>

        </div>
  );
}

export default App;
