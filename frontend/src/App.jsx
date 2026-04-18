import { useState } from "react"
import "./App.css"

function App() {
  const [brand, setBrand] = useState("")
  const [niche, setNiche] = useState("")
  const [audience, setAudience] = useState("")
  const [platform, setPlatform] = useState("")
  const [goal, setGoal] = useState("")
  const [submittedData, setSubmittedData] = useState(null)
  const [ideas, setIdeas] = useState(null)

  const handleSubmit = async () => {
    const data = {
      brand,
      niche,
      audience,
      platform,
      goal,
    }

    setSubmittedData(data)

    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })

      const result = await response.json()

      setIdeas({
        contentIdea: result.message,
        caption: `${brand} helps ${audience} achieve better ${niche} results`,
        hashtags: `#${niche} #${brand.replace(/\s/g, "")} #ContentStrategy`,
        bestTime: "7 PM - 9 PM",
        pillar1: "Educational Content",
        pillar2: "Customer Testimonials",
        pillar3: "Product Benefits",
        monday: "Post skincare tips reel",
        wednesday: "Share customer review post",
        friday: "Post product demo video",
      })
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <div
      style={{
        padding: "40px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        fontFamily: "Arial",
      }}
    >
      <h1>Content Strategy Agent</h1>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          width: "400px",
        }}
      >
        <input
          type="text"
          placeholder="Enter Brand"
          value={brand}
          onChange={(e) => setBrand(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter Niche"
          value={niche}
          onChange={(e) => setNiche(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter Audience"
          value={audience}
          onChange={(e) => setAudience(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter Platform"
          value={platform}
          onChange={(e) => setPlatform(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter Goal"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
        />

        <button onClick={handleSubmit}>Submit</button>
      </div>

      {submittedData && (
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid gray",
            borderRadius: "10px",
            width: "400px",
          }}
        >
          <h2>Submitted Details</h2>
          <p><b>Brand:</b> {submittedData.brand}</p>
          <p><b>Niche:</b> {submittedData.niche}</p>
          <p><b>Audience:</b> {submittedData.audience}</p>
          <p><b>Platform:</b> {submittedData.platform}</p>
          <p><b>Goal:</b> {submittedData.goal}</p>
        </div>
      )}

      {ideas && (
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid green",
            borderRadius: "10px",
            width: "500px",
          }}
        >
          <h2>Generated Content Ideas</h2>
          <p><b>Content Idea:</b> {ideas.contentIdea}</p>
          <p><b>Caption:</b> {ideas.caption}</p>
          <p><b>Hashtags:</b> {ideas.hashtags}</p>
          <p><b>Best Time:</b> {ideas.bestTime}</p>

          <h3>Content Pillars</h3>
          <ul>
            <li>{ideas.pillar1}</li>
            <li>{ideas.pillar2}</li>
            <li>{ideas.pillar3}</li>
          </ul>

          <h3>Weekly Plan</h3>
          <p><b>Monday:</b> {ideas.monday}</p>
          <p><b>Wednesday:</b> {ideas.wednesday}</p>
          <p><b>Friday:</b> {ideas.friday}</p>
        </div>
      )}
    </div>
  )
}

export default App