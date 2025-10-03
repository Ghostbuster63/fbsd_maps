import { useState } from 'react'
import './App.css'

import { MapComp } from './components/Map'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
         <MapComp />
      </div>
    </>
  )
}

export default App
