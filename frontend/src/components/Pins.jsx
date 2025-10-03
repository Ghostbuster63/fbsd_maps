import {
  Pin,
} from "@vis.gl/react-google-maps";

export const RedPin = (props) => {
  const zoom = props.zoom
  return (
    <>
      <Pin
        background={"red"}
        borderColor={"red"}
        glyphColor={"red"}
        scale={zoom * 0.25 - 3.5}
      />
    </>
  )
}
export const BluePin = (props) => {
  const zoom = props.zoom
  return (
    <>
      <Pin
        background={"blue"}
        borderColor={"blue"}
        glyphColor={"blue"}
        scale={zoom * 0.25 - 3.5}
      />
    </>
  )
}
export const GrnPin = (props) => {
  const zoom = props.zoom
  return (
    <>
      <Pin
        background={"green"}
        borderColor={"green"}
        glyphColor={"green"}
        scale={zoom * 0.25 - 3.5}
      />
    </>
  )
}
export const YelPin = (props) => {
  const zoom = props.zoom
  return (
    <>
      <Pin
        background={"yellow"}
        borderColor={"yellow"}
        glyphColor={"yellow"}
        scale={zoom * 0.25 - 3.5}
      />
    </>
  )
}
export const OrgPin = (props) => {
  const zoom = props.zoom
  return (
    <>
      <Pin
        background={"orange"}
        borderColor={"orange"}
        glyphColor={"orange"}
        scale={zoom * 0.25 - 3.5}
      />
    </>
  )
}
