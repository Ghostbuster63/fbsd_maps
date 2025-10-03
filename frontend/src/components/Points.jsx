
import {
  AdvancedMarker,
} from "@vis.gl/react-google-maps";

import { RedPin, BluePin, GrnPin, YelPin, OrgPin } from "./Pins";

import RPoints from "../data/B3020_Canola.json";
import BPoints from "../data/L340PC_Canola.json";
import GPoints from "../data/L333PC_Canola.json";
import OPoints from "../data/L330PC_A4.2TSW_Canola.json";
import YPoints from "../data/L330PC_B_4.8TSW_Canola.json";


export const RedPoints = (props) => {
  const zoom = props.zoom 
  return (
    <>
      {RPoints.map((point) => (
        <AdvancedMarker
          key={point.key}
          position={{lat: point.lat , lng: point.lon }}
        >
          <RedPin zoom={zoom} />
        </AdvancedMarker>
      ))}
    </>
  )
}

export const BluePoints = (props) => {
  const zoom = props.zoom 
  return (
    <>
      {BPoints.map((point) => (
        <AdvancedMarker
          key={point.key}
          position={{lat: point.lat , lng: point.lon }}
        >
          <BluePin zoom={zoom} />
        </AdvancedMarker>
      ))}
    </>
  )
}

export const YelPoints = (props) => {
  const zoom = props.zoom 
  return (
    <>
      {YPoints.map((point) => (
        <AdvancedMarker
          key={point.key}
          position={{lat: point.lat , lng: point.lon }}
        >
          <YelPin zoom={zoom} />
        </AdvancedMarker>
      ))}
    </>
  )
}

export const GrnPoints = (props) => {
  const zoom = props.zoom 
  return (
    <>
      {GPoints.map((point) => (
        <AdvancedMarker
          key={point.key}
          position={{lat: point.lat , lng: point.lon }}
        >
          <GrnPin zoom={zoom} />
        </AdvancedMarker>
      ))}
    </>
  )
}


export const OrgPoints = (props) => {
  const zoom = props.zoom 
  return (
    <>
      {OPoints.map((point) => (
        <AdvancedMarker
          key={point.key}
          position={{lat: point.lat , lng: point.lon }}
        >
          <OrgPin zoom={zoom} />
        </AdvancedMarker>
      ))}
    </>
  )
}

