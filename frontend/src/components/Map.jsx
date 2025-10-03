"use client";

import { useState, useCallback } from "react";
//import { RedPin, BluePin, GrnPin, YelPin } from "./Pins";
import { RedPoints, BluePoints, YelPoints, GrnPoints, OrgPoints } from "./Points";
import config from "../data/config.json";
import "./GeolocationMarker";

import {
  APIProvider,
  Map,
  useMap,
  AdvancedMarker,
  InfoWindow,
  MapCameraChangedEvent,
} from "@vis.gl/react-google-maps";
  //MapCameraProps,

const INITIAL_CAMERA = {
    center: { lat: 50.52088296701928, lng: -110.21465690222468 },
    zoom: 18
};

//export function Intro() {
export const MapComp = () => {

  const [zoom, setZoom] = useState(18);

  const [cameraProps, setCameraProps] =
    useState(INITIAL_CAMERA);

  const handleCameraChange = useCallback(
    (ev: MapCameraChangedEvent) =>
    {
      setCameraProps(ev.detail);
      console.log('ev',ev.detail);
      console.log('ev',ev.detail.zoom);
      setZoom(ev.detail.zoom);
      console.log('zoom',zoom);
    }
  );


//  const center = { lat: 50.52088296701928, lng: -110.21465690222468 };
//  const zoom = 18;

  const MapTypeId = {
    HYBRID: 'hybrid',
    ROADMAP: 'roadmap',
    SATELLITE: 'satellite',
    TERRAIN: 'terrain'
  };

  const mapConf = {
    id: 'satellite',
    label: 'Satellite ("light" mapId)',
    mapId: '49ae42fed52588c3',
    mapTypeId: MapTypeId.SATELLITE
  };

  const onZoomChanged = () => {
    console.log('zoom',this.googleMap.current.getZoom())
  };

//          defaultZoom={zoom}
//          defaultCenter={center}

  return (
    <>
    <h3>
      Canola 2025
    </h3>
    <APIProvider
      apiKey={config.MAP_API_KEY}
      onLoad={() => console.log('Intro API has loaded.')}
    >
      <div style={{ height: "95vh", width: "95%", overflow:"visible" }}>
        <Map 
          mapId={'ADE'}
          styling={'overflow: visible'}
          mapTypeId={mapConf.mapTypeId}
          {...cameraProps} onCameraChanged={handleCameraChange}
         >
          <RedPoints zoom={zoom} />
          <BluePoints zoom={zoom} />
          <YelPoints zoom={zoom} />
          <GrnPoints zoom={zoom} />
          <OrgPoints zoom={zoom} />
        </Map>
      </div>
    </APIProvider>
    </>
  );
}
